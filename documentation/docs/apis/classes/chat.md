---
sidebar_position: 11
title: ✅ ChatUser
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
:::tip
 
This page contains documentation for the `ChatUser` class and its subclasses:  
-  [ChatBot](#chatbot)   

 
:::
# ChatUser
## Overview
Synology Chat API via DSM session (username + password).  
  
Wraps the SYNO.Chat.* APIs discovered on DSM 7.3.2+. 25 of 39
registered APIs confirmed working; see module docstring for details.

For token-based access (no DSM login), use :class:`ChatBot`.  
  
## Methods
### `channel_list`
List all chat channels.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_simple_** `bool`  
If True, return ``{channel_id: channel_name}``
instead of the full JSON response.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str or dict[int, str]`  
Full API response, or ``{channel_id: name}`` dict
when ``simple=True``.  
</div>
  



---


### `channel_create`
Create a new named chat channel and auto-join it.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel.Named`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
Channel name.  
  
**_members_** `list[str]`  
User IDs to invite after creation.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created channel with ``channel_id`` and ``auto_join`` flag.  
</div>
  



---


### `channel_close`
Close (delete) a chat channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Numeric channel ID to close.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_archive`
Archive a chat channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Numeric channel ID to archive.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_invite`
Invite users to a named channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel.Named`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Numeric channel ID.  
  
**_user_ids_** `list[int]`  
List of user IDs to invite.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_join`
Join a channel (must be public or the user must be invited).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel.Named`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Numeric channel ID to join.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_leave`
Leave a channel.  
.. warning::
   If you are the **only member**, the channel becomes orphaned
   (no one can rejoin or close it via API). Only leave channels
   that have other members.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel.Named`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Numeric channel ID to leave.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_view`
Mark a channel as read up to a given timestamp.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
**_last_view_at_** `int`  
Unix timestamp in **milliseconds** marking the last read
point. Defaults to current time.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `channel_preference_get`
Get channel preferences (notifications, etc.).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Channel.Preference`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_list`
List all chat users.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.User`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_get`
Get user details.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.User`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `str`  
User ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_status_get`
Get user online status.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.User.Status`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `str`  
User ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_avatar_get`
Get user avatar.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.User.Avatar`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `str`  
User ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `user_preference_get`
Get current user's Chat preferences.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.User.Preference`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `incoming_webhook_list`
List all incoming webhooks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Incoming`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `incoming_webhook_create`
Create an incoming webhook to post messages into a channel.  
Provides a token and webhook user_id. The webhook URL to POST
messages to must be constructed as::  
    ``https://{host}:{port}/webapi/entry.cgi?api=SYNO.Chat.Webhook.Incoming&version=1&method=incoming&token=***``  
with ``payload={"text": "..."}`` as form-encoded POST body.  
For direct posting without webhooks, prefer :meth:`post_create`.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Incoming`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
Webhook name.  
  
**_channel_id_** `str`  
Target channel ID.  
  
**_icon_url_** `str`  
URL for the webhook icon.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created webhook with token and user_id.  
</div>
  



---


### `incoming_webhook_delete`
Delete an incoming webhook.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Incoming`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_webhook_id_** `str`  
Webhook ID to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `outgoing_webhook_list`
List all outgoing webhooks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Outgoing`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `outgoing_webhook_create`
Create an outgoing webhook (Chat POSTs events to your URL).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Outgoing`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
Webhook name.  
  
**_channel_id_** `str`  
Channel ID.  
  
**_url_** `str`  
Target URL for events.  
  
**_events_** `list[str]`  
Event types (default ["message"]).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `outgoing_webhook_delete`
Delete an outgoing webhook.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Outgoing`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_webhook_id_** `str`  
Webhook ID to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `slash_command_list`
List all slash commands.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Slash`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `slash_command_create`
Create a slash command (/deploy, /alert, etc.).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Slash`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_name_** `str`  
Command display name.  
  
**_command_** `str`  
Command text (e.g. "deploy").  
  
**_url_** `str`  
Webhook URL to POST to.  
  
**_channel_id_** `str`  
Channel ID to restrict command to.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `slash_command_delete`
Delete a slash command.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Slash`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_command_id_** `str`  
Command ID to delete.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `builtin_webhook_list`
List built-in webhook integrations (e.g., GitHub, Jira).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.BuiltIn`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `broadcast_webhook_list`
List broadcast webhooks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Webhook.Broadcast`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `bot_set`
Add/update a bot in the chat user list.  
The ``user_id`` comes from a webhook or chatbot integration.
Call this after creating an incoming webhook or chatbot to
make the bot visible to users.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Bot`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `int`  
Bot user ID (from webhook/chatbot create response).  
  
**_nickname_** `str`  
Display name for the bot in chat.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `bot_delete`
Remove a bot from the chat user list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Bot`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `int`  
Bot user ID to remove.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `external_list`
List all external integrations (combined view).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.External`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_list`
List posts in a channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
**_limit_** `int`  
Max posts per page (default 50).  
  
**_offset_** `int`  
Pagination offset (default 0).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_search`
Search posts across one or more channels.  
Powerful search with filters for post type, attachments (pin/url/star),
author, time range, and sorting.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_ids_** `list[int]`  
Channel IDs to search in (e.g. ``[72]`` or ``[72, 73]``).  
  
**_keyword_** `str`  
Free-text search in message body.  
  
**_post_type_** `list[str]`  
Filter by post type: ``["file"]``, ``["normal"]``, or both
``["file", "normal"]``.  
  
**_has_** `list[str]`  
Filter by attachment type. Valid values:
``"pin"`` (pinned), ``"url"`` (contains link), ``"star"``
(starred). :::note
 
 ``"file"``/``"mention"`` are silently ignored
 
:::

by the API.  
  
**_creator_ids_** `list[int]`  
Filter by message author user IDs.  
  
**_after_** `int`  
Only posts created after this Unix timestamp (ms).  
  
**_before_** `int`  
Only posts created before this Unix timestamp (ms).  
  
**_sort_by_** `str`  
Sort field: ``"create_at"``, ``"update_at"``,
``"last_pin_at"``, or ``"last_comment_at"``.
Default: ``"create_at"``.  
  
**_sort_by_array_** `list[str]`  
Multi-field sort (e.g. ``["is_sticky", "last_pin_at"]``).
Overrides ``sort_by`` when provided.  
  
**_thread_id_** `int`  
Filter by thread ID. ``0`` = root posts only (no replies).  
  
**_offset_** `int`  
Pagination offset. Default: 0.  
  
**_limit_** `int`  
Max results per page. Default: 50.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"search_results": [...], "total": N, "offset": 0, "limit": 50}, "success": True}``.  
</div>
  



---


### `post_create`
Post a message to a channel (direct API, no webhook needed).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `str`  
Target channel ID.  
  
**_message_** `str`  
Message text. Supports newlines.  
  
**_file_id_** `str`  
File ID from :meth:`post_file_upload`.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created post with 'post_id' key.  
</div>
  



---


### `post_attachment_list`
List post attachments.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Attachment`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
**_limit_** `int`  
Max results (default 50).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_file_upload`
Upload a file to a chat channel.  
Sends a ``multipart/form-data`` POST to ``SYNO.Chat.Post``
(``method=create``, ``version=5``).  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `str`  
Target channel ID.  
  
**_file_path_** `str`  
Local path to the file to upload.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Success response with ``file_props`` including file name and size.  
</div>
  



---


### `post_reaction_add`
Add a reaction (sticker) to a post.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Reaction`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Target post ID.  
  
**_sticker_name_** `str`  
Sticker name, e.g. ``"grinning"``, ``"heart"``, ``"thumbsup"``.
See Synology Chat sticker picker for available names.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_pin`
Pin a post to the top of the channel.  
Pinned posts are visible via :meth:`post_search` with
``has=["pin"]``.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Target post ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_unpin`
Unpin a previously pinned post.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Target post ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_thread_list`
List threads (posts with replies) in a channel.  
Returns root posts that have replies, along with the reply
posts themselves.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID to list threads from.  
  
**_offset_** `int`  
Pagination offset. Default: 0.  
  
**_limit_** `int`  
Max threads per page. Default: 25.  
  
**_related_comment_count_** `int`  
Number of reply posts to include per thread. Default: 3.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"search_results": [...], "related_posts": [...], "total": N}, "success": True}``.
``search_results`` contains root posts (``thread_id`` == own
``post_id``). ``related_posts`` contains replies.  
</div>
  



---


### `post_reminder_list`
List post reminders in a channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Reminder`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"posts": [...]}, "success": True}``.  
</div>
  



---


### `post_reminder_delete`
Delete a post reminder.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Reminder`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
**_post_id_** `str`  
Post ID whose reminder should be deleted.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_reminder_get`
Get the reminder set on a post.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Reminder`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Post ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"remind_at": 0}, "success": True}`` —
``remind_at`` is 0 if no reminder is set, otherwise a Unix
timestamp in **milliseconds**.  
</div>
  



---


### `post_reminder_set`
Set or update a reminder on a post.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Reminder`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Post ID.  
  
**_remind_at_** `int`  
Unix timestamp in **milliseconds** when to trigger the
reminder.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `post_schedule_list`
List scheduled (delayed) posts in a channel.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Schedule`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Channel ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"schedule_posts": [{"cronjob_id": N, "message": "...", "send_at": ms_ts}]}, "success": True}``.  
</div>
  



---


### `post_schedule_create`
Schedule a post to be sent at a future time.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Schedule`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `int`  
Target channel ID.  
  
**_message_** `str`  
Message text.  
  
**_send_at_** `int`  
Unix timestamp in **milliseconds** when the message
should be sent.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Response with ``cronjob_id``.  
</div>
  



---


### `post_schedule_delete`
Delete a scheduled post before it's sent.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Post.Schedule`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cronjob_id_** `int`  
Cron job ID (from :meth:`post_schedule_list`).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `chatbot_list`
List chatbots.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Chatbot`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `chatbot_set`
Create/update a chatbot integration.  
Requires a ``user_id`` from an incoming webhook.
The chatbot will receive messages and can respond via the URL.  
.. note::
   This API requires admin privileges. Error 117 (permission
   denied) or 105 (missing parameter) may occur if the user
   lacks permission or the ``user_id`` is not a valid chatbot.  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Chatbot`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_user_id_** `int`  
Bot user ID (from incoming webhook create).  
  
**_url_** `str`  
Webhook URL the chatbot posts events to.  
  
**_purpose_** `str`  
Short description shown in the integration page.  
  
**_welcome_note_** `str`  
Welcome message shown when a user opens the bot chat.  
  
**_hide_from_user_** `bool`  
If True, bot is hidden from the "Add" list (default True).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `sticker_list`
List available stickers.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Sticker`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `admin_setting_get`
Get Chat Server admin settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Admin.Setting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `app_info`
Get Chat app information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.App`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `misc_info`
Get miscellaneous Chat info.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Chat.Misc`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
API response.  
</div>
  



---


### `build_webhook_url`
Build the incoming webhook URL from a UI-created token.  
Use a token from the Chat UI Integration → Incoming Webhook page
(64 characters).  API-created webhook tokens will NOT work —
only UI-created ones are valid for ``SYNO.Chat.External``.  
  
#### Parameters
<div class="padding-left--md">

**_token_** `str`  
The 64-char webhook token from Chat UI.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`str`  
``https://{ip}:{port}/webapi/entry.cgi?api=SYNO.Chat.External&version=2&method=incoming&token=***``.  
</div>
  



---


### `send_webhook`
Send a message via incoming webhook token (UI-created).  
No DSM session required — just the webhook token and NAS URL.  
  
#### Parameters
<div class="padding-left--md">

**_token_** `str`  
64-char webhook token from Chat UI Integration page.  
  
**_text_** `str`  
Message text. Supports \n and \<url|link\> syntax.  
  
**_nas_url_** `str`  
Base NAS URL, e.g. ``https://your-nas.local:5001``.  
  
**_verify_** `bool`  
Verify SSL certificate.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict`  
``{"success": True}`` or ``{"success": False, "error": ...}``.  
</div>
  



---


## ChatBot
## Overview
Synology Chat bot/webhook API — no DSM session required.  
  
Works with tokens created in the Chat UI Integration page.
Supports two token types:

* **Incoming Webhook token** — send messages to a channel via
  :meth:`send_incoming`.
* **Bot token** — list channels/users/messages, send DMs via
  :meth:`send_message`.  
  
### Parameters
<div class="padding-left--md">

**_nas_url_** `str`  
Base URL of the NAS, e.g. ``https://your-nas.local:5001``.  
  
**_token_** `str`  
64-character token from Chat UI Integration page.  
  
**_cert_verify_** `bool`  
Verify SSL certificate (default False).  
  
</div>
  
  
## Methods
### `channel_list`
List channels visible to the bot.  
Requires a **bot token**.  Webhook tokens return code 404.  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


### `user_list`
List users visible to the bot.  
Requires a **bot token**.  Webhook tokens return code 404.  
  
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


### `post_list`
List messages in a channel.  
Requires a **bot token** and the bot must be a member of
the channel (otherwise error 401).  
  
#### Parameters
<div class="padding-left--md">

**_channel_id_** `str`  
Channel ID.  
  
**_post_id_** `str`  
Anchor post — omit for newest.  
  
**_next_count_** `int`  
Messages after anchor.  
  
**_prev_count_** `int`  
Messages before anchor.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


### `post_file_get`
Download file attachment for a post (bot token).  
  
  
#### Parameters
<div class="padding-left--md">

**_post_id_** `str`  
Post ID with file attachment.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


### `send_incoming`
Send a message to a channel via **incoming webhook token**.  
  
  
#### Parameters
<div class="padding-left--md">

**_text_** `str`  
Message text. Supports \n and \<url|link\> syntax.  
  
**_file_url_** `str`  
Publicly accessible file URL to attach (max 32 MB).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


### `send_message`
Send a DM to specific users via **bot token**.  
  
  
#### Parameters
<div class="padding-left--md">

**_text_** `str`  
Message text.  
  
**_user_ids_** `list[int]`  
Target user IDs (e.g. ``[2]`` for user 2).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, Any]`  
API response.  
</div>
  



---


