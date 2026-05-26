"""
Synology Chat API wrapper for DSM 7.3.2.

Tested against DSM 7.3.2 (DS218+) with Synology Chat Server 2.4.5-22148.
39 Chat APIs registered; 35 confirmed working (+ bot/webhook token modes).

Two authentication modes
------------------------
1. **DSM session** (username + password) — full API access via WebAPI.
   Use ``ChatUser`` class.  Works for channel/user/post CRUD and webhook mgmt.
2. **Bot / Webhook token** (no DSM login) — lightweight, token-only.
   Use ``ChatBot`` class.  Token from Chat UI Integration page.

Working APIs (DSM session)
--------------------------
- SYNO.Chat.Channel.list              — List all channels
- SYNO.Chat.Channel.archive           — Archive a channel
- SYNO.Chat.Channel.close             — Close (delete) a channel
- SYNO.Chat.Channel.view              — Mark channel as read
- SYNO.Chat.Channel.Named.create      — Create a named channel
- SYNO.Chat.Channel.Named.join        — Join a channel after creation
- SYNO.Chat.Channel.Named.invite      — Invite users to a channel
- SYNO.Chat.Channel.Preference.get    — Read channel preferences
- SYNO.Chat.User.list / get           — List/get Chat users
- SYNO.Chat.User.Preference.get       — Read user preferences
- SYNO.Chat.Post.list / create        — Read/send channel messages
- SYNO.Chat.Post.search               — Search with filters (keyword, type, has, author, time)
- SYNO.Chat.Post.thread_list          — List threads (posts with replies)
- SYNO.Chat.Post.pin / unpin          — Pin/unpin posts
- SYNO.Chat.Post.Reaction.set         — Add sticker reactions to posts
- SYNO.Chat.Post.Reminder.*           — Get/set/list/delete post reminders
- SYNO.Chat.Post.Schedule.*           — List/create/delete scheduled posts
- SYNO.Chat.Webhook.Incoming.*        — Full CRUD incoming webhooks
- SYNO.Chat.Webhook.Outgoing.*        — Full CRUD outgoing webhooks
- SYNO.Chat.Webhook.Slash.*           — Full CRUD slash commands
- SYNO.Chat.Chatbot.list / set          — List/create chatbots
- SYNO.Chat.Bot.set / delete           — Add/remove bots from chat
- SYNO.Chat.Admin.Setting.get         — Read admin settings
- SYNO.Chat.Sticker.list              — List stickers
- SYNO.Chat.App.list                  — App info

Working APIs (Bot token — ``ChatBot``)
-------------------------------------------
- channel_list                        — Channels visible to bot
- user_list                           — Users visible to bot
- post_list                           — Messages in a channel (bot must be member)
- chatbot (send)                      — Send DM to users via user_ids
- post_file_get                       — Download file attachments

Working APIs (Webhook token — ``ChatBot``)
-----------------------------------------------
- incoming (send)                     — Post messages to channel

Important notes
---------------
- Chat APIs are in ``self.gen_list`` (full_api_list), NOT ``core_list``.
- ``post_create()`` uses ``message`` key (not ``text``).
- **Sending DMs:** Synology Chat has no direct "send DM" API. DMs are
  posts to anonymous/private channels with exactly 2 members.
  Find the channel via ``channel_list()``, then use ``post_create()``.
- Webhook tokens created via API are NOT usable for sending.
  Only UI-created webhook tokens work with ``SYNO.Chat.External``.
- Bot tokens from Chat UI give access to ``channel_list/user_list/post_list``.
"""

from __future__ import annotations

import json
from typing import Any

import requests

from synology_api.base_api import BaseApi


class ChatUser(BaseApi):
    """
    Synology Chat API via DSM session (username + password).

    Wraps the SYNO.Chat.* APIs discovered on DSM 7.3.2+. 25 of 39
    registered APIs confirmed working; see module docstring for details.

    For token-based access (no DSM login), use :class:`ChatBot`.

    Parameters
    ----------
    ip_address : str
    port : str
    username : str
    password : str
    secure : bool, optional (default False)
    cert_verify : bool, optional (default False)
    dsm_version : int, optional (default 7)
    debug : bool, optional (default True)
    otp_code : str, optional
    device_id : str, optional
    device_name : str, optional
    interactive_output : bool, optional (default False)

    Notes
    -----
    Most Chat APIs require admin permissions. Error code 119 means
    the authenticated user lacks access. Error code 103 means the
    API method doesn't exist (wrong method name or version).
    """

    # ═══════════════════════════════════════════════════════════════════════
    # Channel Management (SYNO.Chat.Channel — maxVersion 5)
    # ═══════════════════════════════════════════════════════════════════════

    def channel_list(
        self, simple: bool = False
    ) -> dict[str, object] | str | dict[int, str]:
        """List all chat channels.

        Args:
            simple: If True, return ``{channel_id: channel_name}``
                instead of the full JSON response.

        Example:
            >>> chat.channel_list(simple=True)
            {1: 'General', 27: '', 42: 'test'}
        """
        api_name = "SYNO.Chat.Channel"
        info = self.gen_list[api_name]
        result = self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )
        if simple and isinstance(result, dict) and result.get("success"):
            simple_dict = {}
            for ch in result["data"].get("channels", []):
                ch_id = ch["channel_id"]
                name = ch.get("name", "")
                if name:
                    simple_dict[ch_id] = name
                elif ch.get("members"):
                    # Empty name = DM/bot channel — show member IDs
                    members = ",".join(str(m) for m in ch["members"])
                    prefix = "BOT" if ch.get("type") == "chatbot" else "DM"
                    simple_dict[ch_id] = f"({prefix}:[{members}])"
                else:
                    simple_dict[ch_id] = ""
            return simple_dict
        return result

    def channel_create(
        self, name: str, members: list[str] | None = None
    ) -> dict[str, object] | str:
        """Create a new named chat channel and auto-join it.

        Parameters
        ----------
        name : str
            Channel name.
        members : list[str], optional
            User IDs to invite after creation.

        Example:
            >>> chat.channel_create("my_channel")
            >>> chat.channel_create("team", members=["2", "3"])
        """
        api_name = "SYNO.Chat.Channel.Named"
        info = self.gen_list[api_name]

        # Step 1: Create the channel
        req: dict[str, Any] = {
            "version": 1, "method": "create",
            "name": name, "type": "private",
        }
        create_result = self.request_data(api_name, info["path"], req)

        if not isinstance(create_result, dict) or not create_result.get("success"):
            return create_result

        ch_id = create_result["data"]["channel_id"]

        # Step 2: Auto-join (like the Synology Chat UI does)
        # Note: join may return error 117 if create already auto-joined the
        # caller — that is NOT a failure, the user is already a member.
        join_result = self.request_data(
            api_name, info["path"],
            {"version": 1, "method": "join", "channel_id": ch_id},
        )
        if isinstance(join_result, dict):
            if join_result.get("success"):
                create_result["data"]["auto_join"] = True
            else:
                err = join_result.get("error", {})
                # Error 117 = already joined (harmless)
                if isinstance(err, dict) and err.get("code") == 117:
                    create_result["data"]["auto_join"] = True
                else:
                    create_result["data"]["auto_join"] = False
                    create_result["data"]["auto_join_error"] = err

        # Step 3: Invite members if specified
        if members:
            self.channel_invite(ch_id, [int(m) for m in members])

        return create_result

    def channel_close(self, channel_id: int) -> dict[str, object] | str:
        """Close (delete) a chat channel.

        Args:
            channel_id: Numeric channel ID to close.

        Example:
            >>> chat.channel_close(40)
        """
        api_name = "SYNO.Chat.Channel"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": 4, "method": "close", "channel_id": channel_id},
        )

    def channel_archive(self, channel_id: int) -> dict[str, object] | str:
        """Archive a chat channel.

        Args:
            channel_id: Numeric channel ID to archive.

        Example:
            >>> chat.channel_archive(49)
        """
        api_name = "SYNO.Chat.Channel"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": 2, "method": "archive", "channel_id": channel_id},
        )

    def channel_invite(
        self, channel_id: int, user_ids: list[int],
    ) -> dict[str, object] | str:
        """Invite users to a named channel.

        Args:
            channel_id: Numeric channel ID.
            user_ids: List of user IDs to invite.

        Example:
            >>> chat.channel_invite(42, [3])
        """
        api_name = "SYNO.Chat.Channel.Named"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": 1,
                "method": "invite",
                "channel_id": channel_id,
                "user_ids": json.dumps(user_ids),
                "channel_key_encs": "[]",
            },
        )

    def channel_join(self, channel_id: int) -> dict[str, object] | str:
        """Join a channel (must be public or the user must be invited).

        Args:
            channel_id: Numeric channel ID to join.

        Example:
            >>> chat.channel_join(11)
        """
        api_name = "SYNO.Chat.Channel.Named"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": 1, "method": "join", "channel_id": channel_id},
        )

    def channel_leave(self, channel_id: int) -> dict[str, object] | str:
        """Leave a channel.

        .. warning::
           If you are the **only member**, the channel becomes orphaned
           (no one can rejoin or close it via API). Only leave channels
           that have other members.

        Args:
            channel_id: Numeric channel ID to leave.

        Example:
            >>> chat.channel_leave(11)
        """
        api_name = "SYNO.Chat.Channel.Named"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": 1, "method": "disjoin", "channel_id": channel_id},
        )

    def channel_view(
        self, channel_id: int, last_view_at: int | None = None
    ) -> dict[str, object] | str:
        """Mark a channel as read up to a given timestamp.

        Parameters
        ----------
        channel_id : int
            Channel ID.
        last_view_at : int, optional
            Unix timestamp in **milliseconds** marking the last read
            point. Defaults to current time.

        Example:
            >>> import time
            >>> chat.channel_view(72, int(time.time() * 1000))
        """
        import time as _time
        api_name = "SYNO.Chat.Channel"
        info = self.gen_list[api_name]
        ts = last_view_at if last_view_at is not None else int(_time.time() * 1000)
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "view",
                "channel_id": str(channel_id),
                "last_view_at": str(ts),
            },
        )

    def channel_preference_get(self, channel_id: int) -> dict[str, object] | str:
        """Get channel preferences (notifications, etc.)."""
        api_name = "SYNO.Chat.Channel.Preference"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get", "channel_id": channel_id},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # User Management (SYNO.Chat.User — maxVersion 3)
    # ═══════════════════════════════════════════════════════════════════════

    def user_list(self) -> dict[str, object] | str:
        """List all chat users."""
        api_name = "SYNO.Chat.User"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    def user_get(self, user_id: str) -> dict[str, object] | str:
        """Get user details."""
        api_name = "SYNO.Chat.User"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get", "user_id": user_id},
        )

    def user_status_get(self, user_id: str) -> dict[str, object] | str:
        """Get user online status."""
        api_name = "SYNO.Chat.User.Status"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get", "user_id": user_id},
        )

    def user_avatar_get(self, user_id: str) -> dict[str, object] | str:
        """Get user avatar."""
        api_name = "SYNO.Chat.User.Avatar"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get", "user_id": user_id},
        )

    def user_preference_get(self) -> dict[str, object] | str:
        """Get current user's Chat preferences."""
        api_name = "SYNO.Chat.User.Preference"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhooks — Incoming (SYNO.Chat.Webhook.Incoming — maxVersion 1)
    # ═══════════════════════════════════════════════════════════════════════

    def incoming_webhook_list(self) -> dict[str, object] | str:
        """List all incoming webhooks."""
        api_name = "SYNO.Chat.Webhook.Incoming"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    def incoming_webhook_create(
        self, name: str, channel_id: str, icon_url: str | None = None
    ) -> dict[str, object] | str:
        """Create an incoming webhook to post messages into a channel.

        Returns a token and webhook user_id. The webhook URL to POST
        messages to must be constructed as:
            https://{host}:{port}/webapi/entry.cgi?api=SYNO.Chat.Webhook.Incoming&version=1&method=incoming&token={token}
        with payload={\"text\": \"...\"} as form-encoded POST body.

        For direct posting without webhooks, prefer :meth:`post_create`.
        """
        api_name = "SYNO.Chat.Webhook.Incoming"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"], "method": "create",
            "name": name, "channel_id": channel_id,
        }
        if icon_url:
            req["icon_url"] = icon_url
        return self.request_data(api_name, info["path"], req)

    def incoming_webhook_delete(self, webhook_id: str) -> dict[str, object] | str:
        """Delete an incoming webhook."""
        api_name = "SYNO.Chat.Webhook.Incoming"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "delete", "id": webhook_id},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhooks — Outgoing (SYNO.Chat.Webhook.Outgoing — maxVersion 1)
    # ═══════════════════════════════════════════════════════════════════════

    def outgoing_webhook_list(self) -> dict[str, object] | str:
        """List all outgoing webhooks."""
        api_name = "SYNO.Chat.Webhook.Outgoing"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    def outgoing_webhook_create(
        self, name: str, channel_id: str, url: str, events: list[str] | None = None
    ) -> dict[str, object] | str:
        """Create an outgoing webhook (Chat POSTs events to your URL)."""
        if events is None:
            events = ["message"]
        api_name = "SYNO.Chat.Webhook.Outgoing"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"], "method": "create",
            "name": name, "channel_id": channel_id, "url": url,
            "events": json.dumps(events),
        }
        return self.request_data(api_name, info["path"], req)

    def outgoing_webhook_delete(self, webhook_id: str) -> dict[str, object] | str:
        """Delete an outgoing webhook."""
        api_name = "SYNO.Chat.Webhook.Outgoing"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "delete", "id": webhook_id},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhooks — Slash Commands (SYNO.Chat.Webhook.Slash — maxVersion 2)
    # ═══════════════════════════════════════════════════════════════════════

    def slash_command_list(self) -> dict[str, object] | str:
        """List all slash commands."""
        api_name = "SYNO.Chat.Webhook.Slash"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    def slash_command_create(
        self, name: str, command: str, url: str, channel_id: str | None = None
    ) -> dict[str, object] | str:
        """Create a slash command (/deploy, /alert, etc.)."""
        api_name = "SYNO.Chat.Webhook.Slash"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"], "method": "create",
            "name": name, "command": command.lstrip("/"), "url": url,
        }
        if channel_id:
            req["channel_id"] = channel_id
        return self.request_data(api_name, info["path"], req)

    def slash_command_delete(self, command_id: str) -> dict[str, object] | str:
        """Delete a slash command."""
        api_name = "SYNO.Chat.Webhook.Slash"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "delete", "id": command_id},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhooks — BuiltIn (SYNO.Chat.Webhook.BuiltIn — maxVersion 2)
    # ═══════════════════════════════════════════════════════════════════════

    def builtin_webhook_list(self) -> dict[str, object] | str:
        """List built-in webhook integrations (e.g., GitHub, Jira)."""
        api_name = "SYNO.Chat.Webhook.BuiltIn"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhooks — Broadcast (SYNO.Chat.Webhook.Broadcast — maxVersion 1)
    # ═══════════════════════════════════════════════════════════════════════

    def broadcast_webhook_list(self) -> dict[str, object] | str:
        """List broadcast webhooks."""
        api_name = "SYNO.Chat.Webhook.Broadcast"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Bots (SYNO.Chat.Bot — maxVersion 1)
    # ═══════════════════════════════════════════════════════════════════════

    def bot_set(
        self, user_id: int, nickname: str,
    ) -> dict[str, object] | str:
        """Add/update a bot in the chat user list.

        The ``user_id`` comes from a webhook or chatbot integration.
        Call this after creating an incoming webhook or chatbot to
        make the bot visible to users.

        Parameters
        ----------
        user_id : int
            Bot user ID (from webhook/chatbot create response).
        nickname : str
            Display name for the bot in chat.

        Example:
            >>> wh = chat.incoming_webhook_create("mybot", "1")
            >>> chat.bot_set(wh["data"]["user_id"], "My Bot")
        """
        api_name = "SYNO.Chat.Bot"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": 1, "method": "set",
                "user_id": str(user_id), "nickname": nickname,
            },
        )

    def bot_delete(self, user_id: int) -> dict[str, object] | str:
        """Remove a bot from the chat user list.

        Parameters
        ----------
        user_id : int
            Bot user ID to remove.

        Example:
            >>> chat.bot_delete(40)
        """
        api_name = "SYNO.Chat.Bot"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": 1, "method": "delete", "user_id": str(user_id)},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # External Integrations (SYNO.Chat.External — maxVersion 3)
    # ═══════════════════════════════════════════════════════════════════════

    def external_list(self) -> dict[str, object] | str:
        """List all external integrations (combined view)."""
        api_name = "SYNO.Chat.External"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Posts / Messages (SYNO.Chat.Post — maxVersion 8)
    # ═══════════════════════════════════════════════════════════════════════

    def post_list(
        self, channel_id: int, limit: int = 50, offset: int = 0
    ) -> dict[str, object] | str:
        """List posts in a channel."""
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "list",
                "channel_id": channel_id, "limit": str(limit),
                "offset": str(offset),
            },
        )

    def post_search(
        self,
        channel_ids: list[int],
        keyword: str | None = None,
        post_type: list[str] | None = None,
        has: list[str] | None = None,
        creator_ids: list[int] | None = None,
        after: int | None = None,
        before: int | None = None,
        sort_by: str = "create_at",
        sort_by_array: list[str] | None = None,
        thread_id: int | None = None,
        offset: int = 0,
        limit: int = 50,
    ) -> dict[str, object] | str:
        """Search posts across one or more channels.

        Powerful search with filters for post type, attachments (pin/url/star),
        author, time range, and sorting.

        Parameters
        ----------
        channel_ids : list[int]
            Channel IDs to search in (e.g. ``[72]`` or ``[72, 73]``).
        keyword : str, optional
            Free-text search in message body.
        post_type : list[str], optional
            Filter by post type: ``["file"]``, ``["normal"]``, or both
            ``["file", "normal"]``.
        has : list[str], optional
            Filter by attachment type. Valid values:
            ``"pin"`` (pinned), ``"url"`` (contains link), ``"star"``
            (starred). Note: ``"file"``/``"mention"`` are silently ignored
            by the API.
        creator_ids : list[int], optional
            Filter by message author user IDs.
        after : int, optional
            Only posts created after this Unix timestamp (ms).
        before : int, optional
            Only posts created before this Unix timestamp (ms).
        sort_by : str
            Sort field: ``"create_at"``, ``"update_at"``,
            ``"last_pin_at"``, or ``"last_comment_at"``.
            Default: ``"create_at"``.
        sort_by_array : list[str], optional
            Multi-field sort (e.g. ``["is_sticky", "last_pin_at"]``).
            Overrides ``sort_by`` when provided.
        thread_id : int, optional
            Filter by thread ID. ``0`` = root posts only (no replies).
        offset : int
            Pagination offset. Default: 0.
        limit : int
            Max results per page. Default: 50.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"search_results": [...], "total": N,
            "offset": 0, "limit": 50}, "success": True}``

        Examples
        --------
        >>> # Find all pinned posts
        >>> chat.post_search([72], has=["pin"], sort_by="last_pin_at")

        >>> # Find all file attachments
        >>> chat.post_search([72], post_type=["file"])

        >>> # Find messages with URLs
        >>> chat.post_search([72], has=["url"])

        >>> # Full-text search
        >>> chat.post_search([72], keyword="backup", creator_ids=[3])

        >>> # Search with time range
        >>> from datetime import datetime, timezone
        >>> after = int(datetime(2026,5,1, tzinfo=timezone.utc).timestamp() * 1000)
        >>> chat.post_search([72, 75], after=after, limit=100)
        """
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        params: dict[str, Any] = {
            "version": info["maxVersion"],
            "method": "search",
            "in": json.dumps(channel_ids),
            "offset": str(offset),
            "limit": str(limit),
        }
        if keyword:
            params["keyword"] = keyword
        if post_type:
            params["post_type"] = json.dumps(post_type)
        if has:
            params["has"] = json.dumps(has)
        if creator_ids:
            params["creator_ids"] = json.dumps(creator_ids)
        if after is not None:
            params["after"] = str(after)
        if before is not None:
            params["before"] = str(before)
        if sort_by_array:
            params["sort_by_array"] = json.dumps(sort_by_array)
        elif sort_by:
            params["sort_by"] = sort_by
        if thread_id is not None:
            params["thread_id"] = str(thread_id)
        return self.request_data(api_name, info["path"], params)

    def post_create(
        self, channel_id: int, message: str, file_id: str | None = None
    ) -> dict[str, object] | str:
        """Post a message to a channel (direct API, no webhook needed).

        Parameters
        ----------
        channel_id : str
            Target channel ID.
        message : str
            Message text. Supports newlines.
        file_id : str, optional
            File ID from :meth:`post_file_upload`.

        Returns
        -------
        dict[str, object] or str
            Created post with 'post_id' key.

        Notes
        -----
        The authenticated user must be a member of the channel.
        This is the simplest way to send messages programmatically.

        **Sending DMs:** Direct messages are posts to anonymous/private
        channels with exactly 2 members. Use :meth:`channel_list` to
        find the DM channel ID, then call :meth:`post_create` on it.
        """
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"], "method": "create",
            "channel_id": channel_id, "message": message,
        }
        if file_id:
            req["file_id"] = file_id
        return self.request_data(api_name, info["path"], req)

    def post_attachment_list(
        self, channel_id: int, limit: int = 50
    ) -> dict[str, object] | str:
        """List post attachments."""
        api_name = "SYNO.Chat.Post.Attachment"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "list",
                "channel_id": channel_id, "limit": str(limit),
            },
        )

    def post_file_upload(self, channel_id: int, file_path: str) -> dict[str, object] | str:
        """Upload a file to a chat channel.

        Sends a ``multipart/form-data`` POST to ``SYNO.Chat.Post``
        (``method=create``, ``version=5``).

        Parameters
        ----------
        channel_id : str
            Target channel ID.
        file_path : str
            Local path to the file to upload.

        Returns
        -------
        dict[str, object] or str
            Success response with ``file_props`` including file name and size.

        Example:
            >>> chat.post_file_upload("72", "/tmp/report.pdf")
        """
        import os
        import requests as _requests

        api_name = "SYNO.Chat.Post"
        url = f"{self.session.base_url}entry.cgi"
        file_name = os.path.basename(file_path)

        params: dict[str, Any] = {
            "api": api_name,
            "method": "create",
            "version": "5",
            "channel_id": str(channel_id),
        }
        headers: dict[str, str] = {
            "X-SYNO-TOKEN": self.session.syno_token,
        }
        data: dict[str, str] = {
            "type": "file",
            "message": "",
            "conn_id": "",
        }
        try:
            with open(file_path, "rb") as fh:
                files = {"file": (file_name, fh, "application/octet-stream")}
                resp = _requests.post(
                    url,
                    params=params,
                    data=data,
                    files=files,
                    headers=headers,
                    cookies={"id": self.session.sid or ""},
                    verify=self.session._verify,
                    timeout=60,
                )
            resp.raise_for_status()
            result = resp.json()
            if result.get("success"):
                return result
            return {"success": False, "error": result.get("error", resp.text)}
        except _requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}

    def post_reaction_add(
        self, post_id: str, sticker_name: str
    ) -> dict[str, object] | str:
        """Add a reaction (sticker) to a post.

        Parameters
        ----------
        post_id : str
            Target post ID.
        sticker_name : str
            Sticker name, e.g. ``"grinning"``, ``"heart"``, ``"thumbsup"``.
            See Synology Chat sticker picker for available names.

        Example:
            >>> chat.post_reaction_add("115964116996", "grinning")
        """
        api_name = "SYNO.Chat.Post.Reaction"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": 1, "method": "set",
                "post_id": post_id, "sticker_name": sticker_name,
            },
        )

    def post_pin(self, post_id: str) -> dict[str, object] | str:
        """Pin a post to the top of the channel.

        Pinned posts are visible via :meth:`post_search` with
        ``has=["pin"]``.

        Parameters
        ----------
        post_id : str
            Target post ID.

        Example:
            >>> chat.post_pin("309237645323")
        """
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "pin",
             "post_id": post_id},
        )

    def post_unpin(self, post_id: str) -> dict[str, object] | str:
        """Unpin a previously pinned post.

        Parameters
        ----------
        post_id : str
            Target post ID.
        """
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "unpin",
             "post_id": post_id},
        )

    def post_thread_list(
        self,
        channel_id: int,
        offset: int = 0,
        limit: int = 25,
        related_comment_count: int = 3,
    ) -> dict[str, object] | str:
        """List threads (posts with replies) in a channel.

        Returns root posts that have replies, along with the reply
        posts themselves.

        Parameters
        ----------
        channel_id : int
            Channel ID to list threads from.
        offset : int
            Pagination offset. Default: 0.
        limit : int
            Max threads per page. Default: 25.
        related_comment_count : int
            Number of reply posts to include per thread. Default: 3.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"search_results": [...], "related_posts": [...],
            "total": N}, "success": True}``

        ``search_results`` contains root posts (``thread_id`` == own
        ``post_id``). ``related_posts`` contains replies.

        Example:
            >>> threads = chat.post_thread_list(72)
            >>> for t in threads["data"]["search_results"]:
            ...     print(f"Thread: {t['message'][:50]} "
            ...           f"({t['comment_count']} replies)")
        """
        api_name = "SYNO.Chat.Post"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "thread_list",
                "channel_id": str(channel_id),
                "offset": str(offset), "limit": str(limit),
                "related_comment_count": str(related_comment_count),
            },
        )

    def post_reminder_list(
        self, channel_id: int
    ) -> dict[str, object] | str:
        """List post reminders in a channel.

        Parameters
        ----------
        channel_id : int
            Channel ID.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"posts": [...]}, "success": True}``
        """
        api_name = "SYNO.Chat.Post.Reminder"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "list",
                "channel_id": str(channel_id),
            },
        )

    def post_reminder_delete(
        self, channel_id: int, post_id: str
    ) -> dict[str, object] | str:
        """Delete a post reminder.

        Parameters
        ----------
        channel_id : int
            Channel ID.
        post_id : str
            Post ID whose reminder should be deleted.
        """
        api_name = "SYNO.Chat.Post.Reminder"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "delete",
                "channel_id": str(channel_id), "post_id": post_id,
            },
        )

    def post_reminder_get(
        self, post_id: str
    ) -> dict[str, object] | str:
        """Get the reminder set on a post.

        Parameters
        ----------
        post_id : str
            Post ID.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"remind_at": 0}, "success": True}`` —
            ``remind_at`` is 0 if no reminder is set, otherwise a Unix
            timestamp in **milliseconds**.
        """
        api_name = "SYNO.Chat.Post.Reminder"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "get",
                "post_id": post_id,
            },
        )

    def post_reminder_set(
        self, post_id: str, remind_at: int
    ) -> dict[str, object] | str:
        """Set or update a reminder on a post.

        Parameters
        ----------
        post_id : str
            Post ID.
        remind_at : int
            Unix timestamp in **milliseconds** when to trigger the
            reminder.

        Example:
            >>> import time
            >>> # Remind in 1 hour
            >>> remind_at = int((time.time() + 3600) * 1000)
            >>> chat.post_reminder_set("309237645323", remind_at)
        """
        api_name = "SYNO.Chat.Post.Reminder"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "set",
                "post_id": post_id, "remind_at": str(remind_at),
            },
        )

    def post_schedule_list(
        self, channel_id: int
    ) -> dict[str, object] | str:
        """List scheduled (delayed) posts in a channel.

        Parameters
        ----------
        channel_id : int
            Channel ID.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"schedule_posts": [
            {"cronjob_id": N, "message": "...", "send_at": ms_ts}
            ]}, "success": True}``
        """
        api_name = "SYNO.Chat.Post.Schedule"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "list",
                "channel_id": str(channel_id),
            },
        )

    def post_schedule_create(
        self, channel_id: int, message: str, send_at: int
    ) -> dict[str, object] | str:
        """Schedule a post to be sent at a future time.

        Parameters
        ----------
        channel_id : int
            Target channel ID.
        message : str
            Message text.
        send_at : int
            Unix timestamp in **milliseconds** when the message
            should be sent.

        Returns
        -------
        dict[str, object] or str
            Response with ``cronjob_id``.

        Example:
            >>> import time
            >>> # Schedule 1 hour from now
            >>> send_at = int((time.time() + 3600) * 1000)
            >>> chat.post_schedule_create(72, "Reminder!", send_at)
        """
        api_name = "SYNO.Chat.Post.Schedule"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "create",
                "channel_id": str(channel_id), "message": message,
                "send_at": str(send_at),
            },
        )

    def post_schedule_delete(
        self, cronjob_id: int
    ) -> dict[str, object] | str:
        """Delete a scheduled post before it's sent.

        Parameters
        ----------
        cronjob_id : int
            Cron job ID (from :meth:`post_schedule_list`).
        """
        api_name = "SYNO.Chat.Post.Schedule"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {
                "version": info["maxVersion"], "method": "delete",
                "cronjob_id": str(cronjob_id),
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Chatbot (SYNO.Chat.Chatbot — maxVersion 1)
    # ═══════════════════════════════════════════════════════════════════════

    def chatbot_list(self) -> dict[str, object] | str:
        """List chatbots."""
        api_name = "SYNO.Chat.Chatbot"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    def chatbot_set(
        self, user_id: int, url: str, purpose: str = "",
        welcome_note: str = "", hide_from_user: bool = True,
    ) -> dict[str, object] | str:
        """Create/update a chatbot integration.

        Requires a ``user_id`` from an incoming webhook.
        The chatbot will receive messages and can respond via the URL.

        .. note::
           This API requires admin privileges. Error 117 (permission
           denied) or 105 (missing parameter) may occur if the user
           lacks permission or the ``user_id`` is not a valid chatbot.

        Parameters
        ----------
        user_id : int
            Bot user ID (from incoming webhook create).
        url : str
            Webhook URL the chatbot posts events to.
        purpose : str
            Short description shown in the integration page.
        welcome_note : str
            Welcome message shown when a user opens the bot chat.
        hide_from_user : bool
            If True, bot is hidden from the "Add" list (default True).

        Example:
            >>> wh = chat.incoming_webhook_create("mybot", "1")
            >>> chat.chatbot_set(
            ...     wh["data"]["user_id"],
            ...     "https://myserver.com/hook",
            ...     purpose="Sends alerts",
            ...     welcome_note="Hello! I'll keep you posted.",
            ... )
        """
        api_name = "SYNO.Chat.Chatbot"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": 1, "method": "set",
            "user_id": str(user_id), "url": url,
            "purpose": purpose, "welcome_note": welcome_note,
            "hide_from_user": str(hide_from_user).lower(),
        }
        return self.request_data(api_name, info["path"], req)

    # ═══════════════════════════════════════════════════════════════════════
    # Stickers (SYNO.Chat.Sticker — maxVersion 2)
    # ═══════════════════════════════════════════════════════════════════════

    def sticker_list(self) -> dict[str, object] | str:
        """List available stickers."""
        api_name = "SYNO.Chat.Sticker"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Admin Settings (SYNO.Chat.Admin.Setting — maxVersion 5)
    # ═══════════════════════════════════════════════════════════════════════

    def admin_setting_get(self) -> dict[str, object] | str:
        """Get Chat Server admin settings."""
        api_name = "SYNO.Chat.Admin.Setting"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # App / Misc
    # ═══════════════════════════════════════════════════════════════════════

    def app_info(self) -> dict[str, object] | str:
        """Get Chat app information."""
        api_name = "SYNO.Chat.App"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    def misc_info(self) -> dict[str, object] | str:
        """Get miscellaneous Chat info."""
        api_name = "SYNO.Chat.Misc"
        info = self.gen_list[api_name]
        return self.request_data(
            api_name, info["path"],
            {"version": info["maxVersion"], "method": "get"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # Webhook URL Builder
    # ═══════════════════════════════════════════════════════════════════════

    def build_webhook_url(self, token: str) -> str:
        """Build the incoming webhook URL from a UI-created token.

        Use a token from the Chat UI Integration → Incoming Webhook page
        (64 characters).  API-created webhook tokens will NOT work —
        only UI-created ones are valid for ``SYNO.Chat.External``.

        Parameters
        ----------
        token : str
            The 64-char webhook token from Chat UI.

        Returns
        -------
        str
            ``https://{ip}:{port}/webapi/entry.cgi?api=SYNO.Chat.External&version=2&method=incoming&token={token}``
        """
        protocol = "https" if self.session._secure else "http"
        return (
            f"{protocol}://{self.session._ip_address}:{self.session._port}"
            f"/webapi/entry.cgi"
            f"?api=SYNO.Chat.External"
            f"&version=2"
            f"&method=incoming"
            f"&token={token}"
        )

    @staticmethod
    def send_webhook(token: str, text: str,
                     nas_url: str,
                     verify: bool = False) -> dict[str, Any]:
        """Send a message via incoming webhook token (UI-created).

        No DSM session required — just the webhook token and NAS URL.

        Parameters
        ----------
        token : str
            64-char webhook token from Chat UI Integration page.
        text : str
            Message text. Supports \\n and <url|link> syntax.
        nas_url : str
            Base NAS URL, e.g. ``https://your-nas.local:5001``.
        verify : bool
            Verify SSL certificate.

        Returns
        -------
        dict
            ``{"success": True}`` or ``{"success": False, "error": ...}``
        """
        payload = f"payload={json.dumps({'text': text})}"
        url = (
            f"{nas_url.rstrip('/')}/webapi/entry.cgi"
            f"?api=SYNO.Chat.External"
            f"&method=incoming"
            f"&version=2"
            f"&token={token}"
        )
        try:
            resp = requests.post(
                url,
                data=payload,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30,
                verify=verify,
            )
            resp.raise_for_status()
            data = resp.json()
            if data.get("success"):
                return {"success": True}
            return {"success": False, "error": data.get("error", resp.text)}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}


# ── Token-based external API (no DSM session required) ────────────────────────


class ChatBot:
    """Synology Chat bot/webhook API — no DSM session required.

    Works with tokens created in the Chat UI Integration page.
    Supports two token types:

    * **Incoming Webhook token** — send messages to a channel via
      :meth:`send_incoming`.
    * **Bot token** — list channels/users/messages, send DMs via
      :meth:`send_message`.

    Parameters
    ----------
    nas_url : str
        Base URL of the NAS, e.g. ``https://your-nas.local:5001``.
    token : str
        64-character token from Chat UI Integration page.
    cert_verify : bool
        Verify SSL certificate (default False).
    """

    def __init__(
        self, nas_url: str, token: str, cert_verify: bool = False
    ) -> None:
        self._base = nas_url.rstrip("/")
        self._token = token
        self._verify = cert_verify
        self._api_url = f"{self._base}/webapi/entry.cgi"

    def _get(self, method: str, **params: Any) -> dict[str, Any]:
        """GET request to SYNO.Chat.External."""
        url_params = {
            "api": "SYNO.Chat.External",
            "method": method,
            "version": "2",
            "token": self._token,
        }
        url_params.update(params)
        try:
            resp = requests.get(
                self._api_url, params=url_params,
                timeout=30, verify=self._verify,
            )
            resp.raise_for_status()
            data = resp.json()
            if data.get("success", False):
                return {"success": True, "data": data}
            return {"success": False, "error": data.get("error", {})}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}
        except json.JSONDecodeError:
            return {"success": False, "error": resp.text}

    def _post(self, method: str, payload: dict[str, Any],
              extra_params: dict[str, Any] | None = None) -> dict[str, Any]:
        """POST request to SYNO.Chat.External (form-encoded payload)."""
        url_params: dict[str, Any] = {
            "api": "SYNO.Chat.External",
            "method": method,
            "version": "2",
            "token": self._token,
        }
        if extra_params:
            url_params.update(extra_params)
        body = f"payload={json.dumps(payload)}"
        try:
            resp = requests.post(
                self._api_url,
                data=body,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                params=url_params,
                timeout=30,
                verify=self._verify,
            )
            resp.raise_for_status()
            data = resp.json()
            if data.get("success", False):
                return {"success": True, "data": data}
            return {"success": False, "error": data.get("error", {})}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": str(e)}
        except json.JSONDecodeError:
            return {"success": False, "error": resp.text}

    # ── Read methods (Bot token only) ────────────────────────────────────

    def channel_list(self) -> dict[str, Any]:
        """List channels visible to the bot.

        Requires a **bot token**.  Webhook tokens return code 404.
        """
        return self._get("channel_list")

    def user_list(self) -> dict[str, Any]:
        """List users visible to the bot.

        Requires a **bot token**.  Webhook tokens return code 404.
        """
        return self._get("user_list")

    def post_list(
        self,
        channel_id: str,
        post_id: str | None = None,
        next_count: int = 20,
        prev_count: int = 1,
    ) -> dict[str, Any]:
        """List messages in a channel.

        Requires a **bot token** and the bot must be a member of
        the channel (otherwise error 401).

        Parameters
        ----------
        channel_id : str
            Channel ID.
        post_id : str, optional
            Anchor post — omit for newest.
        next_count : int
            Messages after anchor.
        prev_count : int
            Messages before anchor.
        """
        params: dict[str, Any] = {
            "channel_id": channel_id,
            "next_count": str(next_count),
            "prev_count": str(prev_count),
        }
        if post_id:
            params["post_id"] = post_id
        return self._get("post_list", **params)

    def post_file_get(self, post_id: str) -> dict[str, Any]:
        """Download file attachment for a post (bot token)."""
        return self._get("post_file_get", post_id=post_id)

    # ── Send methods ─────────────────────────────────────────────────────

    def send_incoming(self, text: str, file_url: str | None = None) -> dict[str, Any]:
        """Send a message to a channel via **incoming webhook token**.

        Parameters
        ----------
        text : str
            Message text. Supports \\n and <url|link> syntax.
        file_url : str, optional
            Publicly accessible file URL to attach (max 32 MB).
        """
        payload: dict[str, Any] = {"text": text}
        if file_url:
            payload["file_url"] = file_url
        return self._post("incoming", payload)

    def send_message(self, text: str, user_ids: list[int]) -> dict[str, Any]:
        """Send a DM to specific users via **bot token**.

        Parameters
        ----------
        text : str
            Message text.
        user_ids : list[int]
            Target user IDs (e.g. ``[2]`` for user 2).

        Notes
        -----
        Uses ``method=chatbot`` which is the correct endpoint for
        bot-originated messages.  The ``incoming`` method only works
        with webhook tokens, not bot tokens.
        """
        payload: dict[str, Any] = {"text": text, "user_ids": user_ids}
        return self._post("chatbot", payload)
