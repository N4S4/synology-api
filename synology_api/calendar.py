"""
Synology Calendar API wrapper.

Wraps the SYNO.Cal.* APIs documented in the Synology Calendar API Guide.
Requires Synology Calendar 2.5.0+ installed and initialised on the target NAS.

Calendar must be opened at least once via the DSM UI before the APIs
will work — the database tables are created on first launch. Until then,
most endpoints return error 9006 (database operation error).

API endpoints
~~~~~~~~~~~~~
- SYNO.Cal.Cal       -- Calendar/task-list CRUD
- SYNO.Cal.Event     -- Event CRUD + recurrence + invitations
- SYNO.Cal.Todo      -- Task/to-do CRUD
- SYNO.Cal.Setting   -- User calendar settings
- SYNO.Cal.Timezone  -- Timezone listing (works without DB init)
- SYNO.Cal.Contact   -- Invitee/contact listing

Reference
~~~~~~~~~
https://kb.synology.com/en-us/DG/Calendar_API_Guide/4
"""

from __future__ import annotations

import json
from typing import Any

from synology_api.base_api import BaseApi


class Calendar(BaseApi):
    """
    Synology Calendar API client.

    Manages calendars, events, tasks, settings, and timezone information
    via the SYNO.Cal.* WebAPI endpoints.

    Requires Synology Calendar 2.5.0+ on the target NAS.
    """

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Cal — Calendar / Task List CRUD
    # ═══════════════════════════════════════════════════════════════════════

    def _cal_request(
        self, api_name: str, req: dict[str, Any]
    ) -> dict[str, object] | str:
        """
        Wrap Calendar API request with double-quoted string values.

        Calendar 3.x requires string parameter values to be wrapped in
        double quotes (e.g. ``"value"``) while booleans, integers, and
        JSON arrays/objects are sent as-is.  This helper applies the
        quoting convention and delegates to :meth:`request_data`.

        Parameters
        ----------
        api_name : str
            API key as registered in ``gen_list`` (e.g. ``"SYNO.Cal.Cal"``).
        req : dict[str, Any]
            Request payload dictionary.

        Returns
        -------
        dict[str, object] or str
            API response.
        """
        for key, value in req.items():
            if key in ("version", "method"):
                continue
            if isinstance(value, str):
                if value.startswith("[") or value.startswith("{"):
                    continue
                if not (value.startswith('"') and value.endswith('"')):
                    req[key] = f'"{value}"'
        info = self.gen_list[api_name]
        return self.request_data(api_name, info["path"], req)

    def cal_create(
        self,
        cal_type: str,
        cal_displayname: str,
        cal_description: str,
        cal_color: str,
        is_hidden_in_cal: bool = False,
        is_hidden_in_list: bool = False,
        notify_alarm_by_browser: bool = True,
        notify_alarm_by_mail: bool = True,
        notify_evt_by_browser: bool = True,
        notify_evt_by_mail: bool = False,
        notify_import_cal_by_browser: bool = True,
        notify_import_cal_by_mail: bool = True,
    ) -> dict[str, object] | str:
        """
        Create a calendar or task list.

        Parameters
        ----------
        cal_type : str
            ``"event"`` for calendar, ``"todo"`` for task list.
        cal_displayname : str
            Calendar display name.
        cal_description : str
            Calendar description.
        cal_color : str
            Calendar colour in RGB hex, e.g. ``"#FF8000"``.
        is_hidden_in_cal : bool, optional
            Hide events for this calendar (default False).
        is_hidden_in_list : bool, optional
            Hide calendar from list (default False).
        notify_alarm_by_browser : bool, optional
            Send reminder via browser (default True).
        notify_alarm_by_mail : bool, optional
            Send reminder via email (default True).
        notify_evt_by_browser : bool, optional
            Send event changes via browser (default True).
        notify_evt_by_mail : bool, optional
            Send event changes via email (default False).
        notify_import_cal_by_browser : bool, optional
            Send import results via browser (default True).
        notify_import_cal_by_mail : bool, optional
            Send import results via email (default True).

        Returns
        -------
        dict[str, object] or str
            Created calendar object with ``cal_id``.

        Examples
        --------
            >>> cal.cal_create("event", "Work Calendar", "Office events", "#FF8000")
        """
        api_name = "SYNO.Cal.Cal"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "create",
                "cal_type": cal_type,
                "cal_displayname": cal_displayname,
                "cal_description": cal_description,
                "cal_color": cal_color,
                "is_hidden_in_cal": is_hidden_in_cal,
                "is_hidden_in_list": is_hidden_in_list,
                "notify_alarm_by_browser": notify_alarm_by_browser,
                "notify_alarm_by_mail": notify_alarm_by_mail,
                "notify_evt_by_browser": notify_evt_by_browser,
                "notify_evt_by_mail": notify_evt_by_mail,
                "notify_import_cal_by_browser": notify_import_cal_by_browser,
                "notify_import_cal_by_mail": notify_import_cal_by_mail,
            },
        )

    def cal_list(
        self, cal_type: str = "all"
    ) -> dict[str, object] | str:
        """
        List calendars and/or task lists.

        Parameters
        ----------
        cal_type : str, optional
            ``"event"``, ``"todo"``, or ``"all"`` (default ``"all"``).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"list": [...]}, "success": True}``.

        Examples
        --------
            >>> cal.cal_list()
            >>> cal.cal_list("todo")
        """
        api_name = "SYNO.Cal.Cal"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "list",
                "cal_type": cal_type,
            },
        )

    def cal_get(self, cal_id: str) -> dict[str, object] | str:
        """
        Get a single calendar by ID.

        Parameters
        ----------
        cal_id : str
            Calendar ID, e.g. ``"/admin/home/"``.

        Returns
        -------
        dict[str, object] or str
            Calendar object.

        Examples
        --------
            >>> cal.cal_get("/admin/home/")
        """
        api_name = "SYNO.Cal.Cal"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "get",
                "cal_id": cal_id,
            },
        )

    def cal_set(
        self,
        cal_id: str,
        cal_type: str,
        original_cal_id: str,
        cal_displayname: str,
        cal_description: str,
        cal_color: str,
        is_hidden_in_cal: bool = False,
        is_hidden_in_list: bool = False,
        notify_alarm_by_browser: bool = True,
        notify_alarm_by_mail: bool = True,
        notify_evt_by_browser: bool = True,
        notify_evt_by_mail: bool = False,
        notify_import_cal_by_browser: bool = True,
        notify_import_cal_by_mail: bool = True,
    ) -> dict[str, object] | str:
        """
        Edit calendar information.

        Parameters
        ----------
        cal_id : str
            Calendar ID, e.g. ``"/admin/home/"``.
        cal_type : str
            ``"event"`` for calendar, ``"todo"`` for task list.
        original_cal_id : str
            Calendar's original ID.
        cal_displayname : str
            Calendar display name.
        cal_description : str
            Calendar description.
        cal_color : str
            Calendar colour in RGB hex, e.g. ``"#E3BD00"``.
        is_hidden_in_cal : bool, optional
            Hide events for this calendar (default False).
        is_hidden_in_list : bool, optional
            Hide calendar from list (default False).
        notify_alarm_by_browser : bool, optional
            Send reminder via browser (default True).
        notify_alarm_by_mail : bool, optional
            Send reminder via email (default True).
        notify_evt_by_browser : bool, optional
            Send event changes via browser (default True).
        notify_evt_by_mail : bool, optional
            Send event changes via email (default False).
        notify_import_cal_by_browser : bool, optional
            Send import results via browser (default True).
        notify_import_cal_by_mail : bool, optional
            Send import results via email (default True).

        Returns
        -------
        dict[str, object] or str
            Updated calendar object.

        Examples
        --------
            >>> cal.cal_set("/admin/home/", "event", "/admin/home/",
            ...             "My Calendar", "", "#E3BD00")
        """
        api_name = "SYNO.Cal.Cal"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "set",
                "cal_id": cal_id,
                "cal_type": cal_type,
                "original_cal_id": original_cal_id,
                "cal_displayname": cal_displayname,
                "cal_description": cal_description,
                "cal_color": cal_color,
                "is_hidden_in_cal": is_hidden_in_cal,
                "is_hidden_in_list": is_hidden_in_list,
                "notify_alarm_by_browser": notify_alarm_by_browser,
                "notify_alarm_by_mail": notify_alarm_by_mail,
                "notify_evt_by_browser": notify_evt_by_browser,
                "notify_evt_by_mail": notify_evt_by_mail,
                "notify_import_cal_by_browser": notify_import_cal_by_browser,
                "notify_import_cal_by_mail": notify_import_cal_by_mail,
            },
        )

    def cal_delete(self, cal_id: str) -> dict[str, object] | str:
        """
        Delete a calendar.

        Parameters
        ----------
        cal_id : str
            Calendar ID.

        Returns
        -------
        dict[str, object] or str
            ``{"success": True}`` on success.

        Examples
        --------
            >>> cal.cal_delete("/admin/abc123/")
        """
        api_name = "SYNO.Cal.Cal"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "delete",
                "cal_id": cal_id,
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Event — Event CRUD
    # ═══════════════════════════════════════════════════════════════════════

    def event_create(
        self,
        cal_id: str,
        original_cal_id: str,
        summary: str,
        is_all_day: bool,
        tz_id: str,
        dtstart: int,
        dtend: int,
        is_repeat_evt: bool = False,
        repeat_setting: dict[str, Any] | None = None,
        color: str = "#000000",
        notify_setting: list[dict[str, Any]] | None = None,
        description: str = " ",
        participant: list[dict[str, Any]] | None = None,
        location_info: dict[str, Any] | None = None,
        from_syno_app_url: dict[str, Any] | None = None,
    ) -> dict[str, object] | str:
        """
        Create a new event.

        Parameters
        ----------
        cal_id : str
            Calendar ID, e.g. ``"/admin/home/"``.
        original_cal_id : str
            Calendar's original ID.
        summary : str
            Event title.
        is_all_day : bool
            Whether this is an all-day event.
        tz_id : str
            Timezone ID, e.g. ``"Europe/Rome"``.
            Use :meth:`timezone_list` to discover available values.
        dtstart : int
            Event start time in Epoch seconds.
        dtend : int
            Event end time in Epoch seconds.
        is_repeat_evt : bool, optional
            Whether this is a recurring event (default False).
        repeat_setting : dict, optional
            Recurrence rule configuration (see API guide for repeat_obj).
        color : str, optional
            Event colour as ``#RRGGBB`` hex, e.g. ``"#00FF00"``.
            Defaults to ``"#000000"`` (black). Required on Calendar 3.x.
        notify_setting : list[dict], optional
            Notification settings (see API guide for notify_obj).
        description : str, optional
            Event description. Defaults to a single space for Calendar 3.x
            compatibility (requires a non-empty value).
        participant : list[dict], optional
            Event participants (see API guide for participant_obj).
        location_info : dict, optional
            Location information (see API guide for location_obj).
        from_syno_app_url : dict, optional
            Source Synology app (e.g. MailPlus).

        Returns
        -------
        dict[str, object] or str
            Created event object with ``evt_id``.

        Examples
        --------
            >>> import time
            >>> now = int(time.time())
            >>> cal.event_create("/admin/home/", "/admin/home/",
            ...     "Team Meeting", False, "Europe/Rome",
            ...     now + 3600, now + 7200,
            ...     color="#3366FF", description="Discuss Q2 roadmap")
        """
        api_name = "SYNO.Cal.Event"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"],
            "method": "create",
            "cal_id": cal_id,
            "original_cal_id": original_cal_id,
            "summary": summary,
            "is_all_day": is_all_day,
            "tz_id": tz_id,
            "dtstart": dtstart,
            "dtend": dtend,
            "is_repeat_evt": is_repeat_evt,
            "color": color,
            "description": description,
        }
        if repeat_setting is not None:
            req["repeat_setting"] = json.dumps(repeat_setting)
        if notify_setting is not None:
            req["notify_setting"] = json.dumps(notify_setting)
        else:
            req["notify_setting"] = json.dumps([])
        if participant is not None:
            req["participant"] = json.dumps(participant)
        else:
            req["participant"] = json.dumps([])
        if location_info is not None:
            req["location_info"] = json.dumps(location_info)
        if from_syno_app_url is not None:
            req["from_syno_app_url"] = json.dumps(from_syno_app_url)
        return self._cal_request(api_name, req)

    def event_list(
        self,
        cal_id_list: list[str] | None = None,
        start: int | None = None,
        end: int | None = None,
        evt_color_list: list[str] | None = None,
        keyword: str = "",
        limit: int | None = None,
        filter_starred: str = "all",
        filter_own: str = "all",
        filter_invited: str = "all",
    ) -> dict[str, object] | str:
        """
        List events with optional filters.

        At least one of ``start``, ``end``, or ``limit`` is required
        by the API.

        Parameters
        ----------
        cal_id_list : list[str], optional
            Calendar IDs to filter by.
        start : int, optional
            Start time in Epoch seconds.
        end : int, optional
            End time in Epoch seconds.
        evt_color_list : list[str], optional
            Event colours to list, e.g. ``["#112233", "#445566"]``.
        keyword : str, optional
            Search keyword in summary, description, and location.
        limit : int, optional
            Maximum number of events to return.
        filter_starred : str, optional
            ``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).
        filter_own : str, optional
            ``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).
        filter_invited : str, optional
            ``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"list": [...]}, "success": True}``.

        Examples
        --------
            >>> import time
            >>> now = int(time.time())
            >>> cal.event_list(start=now, end=now + 86400, limit=50)
        """
        api_name = "SYNO.Cal.Event"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"],
            "method": "list",
            "keyword": keyword,
            "filter_starred": filter_starred,
            "filter_own": filter_own,
            "filter_invited": filter_invited,
        }
        if cal_id_list is not None:
            req["cal_id_list"] = json.dumps(cal_id_list)
        if start is not None:
            req["start"] = start
        if end is not None:
            req["end"] = end
        if evt_color_list is not None:
            req["evt_color_list"] = json.dumps(evt_color_list)
        if limit is not None:
            req["limit"] = limit
        return self._cal_request(api_name, req)

    def event_get(
        self,
        evt_id: int | None = None,
        recurrence_id: str | None = None,
        ical_uid: str | None = None,
        cal_id: str | None = None,
    ) -> dict[str, object] | str:
        """
        Get event or sub-event details.

        Use either ``evt_id`` or ``ical_uid`` (mutually exclusive).
        When using ``ical_uid``, ``cal_id`` must also be provided.

        Parameters
        ----------
        evt_id : int, optional
            Event ID.
        recurrence_id : str, optional
            Sub-event date in ISO 8601 format (``YYYYMMDD`` or
            ``YYYYMMDDThhmmss``).
        ical_uid : str, optional
            Event UID within ICS. Mutually exclusive with ``evt_id``.
        cal_id : str, optional
            Calendar ID. Required when using ``ical_uid``.

        Returns
        -------
        dict[str, object] or str
            Event object.

        Examples
        --------
            >>> cal.event_get(evt_id=1281)
            >>> cal.event_get(ical_uid="20230630T073051-abc@cal.synology.com",
            ...               cal_id="/admin/home/")
        """
        api_name = "SYNO.Cal.Event"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {"version": info["maxVersion"], "method": "get"}
        if evt_id is not None:
            req["evt_id"] = evt_id
        if recurrence_id is not None:
            req["recurrence_id"] = recurrence_id
        if ical_uid is not None:
            req["ical_uid"] = ical_uid
        if cal_id is not None:
            req["cal_id"] = cal_id
        return self._cal_request(api_name, req)

    def event_set(
        self,
        evt_id: int,
        cal_id: str,
        original_cal_id: str,
        dav_etag: str,
        summary: str,
        is_all_day: bool,
        tz_id: str,
        dtstart: int,
        dtend: int,
        is_repeat_evt: bool = False,
        repeat_setting: dict[str, Any] | None = None,
        color: str = "#000000",
        notify_setting: list[dict[str, Any]] | None = None,
        description: str = " ",
        participant: list[dict[str, Any]] | None = None,
        location_info: dict[str, Any] | None = None,
        attachments: list[dict[str, Any]] | None = None,
        exdate: str | None = None,
    ) -> dict[str, object] | str:
        """
        Modify an event. Returns main event info on success.

        .. warning::
           On Calendar 3.x, ``personal_property`` and ``location_info``
           must be passed explicitly for the ``set`` method to succeed.

        Parameters
        ----------
        evt_id : int
            Event ID.
        cal_id : str
            Calendar ID.
        original_cal_id : str
            Calendar's original ID.
        dav_etag : str
            Event timestamp (optimistic locking).
            If this differs from the server value, someone else
            already modified the event.
        summary : str
            Event title.
        is_all_day : bool
            Whether this is an all-day event.
        tz_id : str
            Timezone ID, e.g. ``"Europe/Rome"``.
        dtstart : int
            Event start time in Epoch seconds.
        dtend : int
            Event end time in Epoch seconds.
        is_repeat_evt : bool, optional
            Recurring event (default False).
        repeat_setting : dict, optional
            Recurrence rules.
        color : str, optional
            Event RGB colour.
        notify_setting : list[dict], optional
            Notification settings.
        description : str, optional
            Event description.
        participant : list[dict], optional
            Event participants.
        location_info : dict, optional
            Location information.
        attachments : list[dict], optional
            Attachment information.
        exdate : str, optional
            Delete a specific occurrence of a recurring event
            (ISO 8601 format).

        Returns
        -------
        dict[str, object] or str
            Updated event object.

        Examples
        --------
            >>> cal.event_set(1281, "/admin/home/", "/admin/home/",
            ...     "abc123def", "Updated Meeting", False, "Europe/Rome",
            ...     1686009600, 1686096000,
            ...     description="Updated description")
        """
        api_name = "SYNO.Cal.Event"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"],
            "method": "set",
            "evt_id": evt_id,
            "cal_id": cal_id,
            "original_cal_id": original_cal_id,
            "dav_etag": dav_etag,
            "summary": summary,
            "is_all_day": is_all_day,
            "tz_id": tz_id,
            "dtstart": dtstart,
            "dtend": dtend,
            "is_repeat_evt": is_repeat_evt,
            "color": color,
            "description": description,
        }
        if repeat_setting is not None:
            req["repeat_setting"] = json.dumps(repeat_setting)
        if notify_setting is not None:
            req["notify_setting"] = json.dumps(notify_setting)
        else:
            req["notify_setting"] = json.dumps([])
        if participant is not None:
            req["participant"] = json.dumps(participant)
        else:
            req["participant"] = json.dumps([])
        if location_info is not None:
            req["location_info"] = json.dumps(location_info)
        else:
            req["location_info"] = json.dumps(
                {"name": "", "address": "", "place_id": "",
                 "map_type": "", "gps": {"lat": -1, "lng": -1}}
            )
        if attachments is not None:
            req["attachments"] = json.dumps(attachments)
        else:
            req["attachments"] = json.dumps([])
        req["personal_property"] = json.dumps({"is_visible": True})
        if exdate is not None:
            req["exdate"] = exdate
        return self._cal_request(api_name, req)

    def event_delete(self, evt_id: int) -> dict[str, object] | str:
        """
        Delete an event.

        Parameters
        ----------
        evt_id : int
            Event ID.

        Returns
        -------
        dict[str, object] or str
            ``{"success": True}`` on success.

        Examples
        --------
            >>> cal.event_delete(1281)
        """
        api_name = "SYNO.Cal.Event"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "delete",
                "evt_id": evt_id,
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Todo — Task CRUD
    # ═══════════════════════════════════════════════════════════════════════

    def todo_create(
        self,
        original_cal_id: str,
        summary: str,
        is_all_day: bool = False,
        tz_id: str = "",
        has_start_time: bool = False,
        dtstart: int = 0,
        has_end_time: bool = False,
        due: int = 0,
        notify_setting: list[dict[str, Any]] | None = None,
        description: str = " ",
        percent_complete: int = 0,
        from_syno_app_url: dict[str, Any] | None = None,
    ) -> dict[str, object] | str:
        """
        Create a task.

        Parameters
        ----------
        original_cal_id : str
            Calendar's original ID for the task list.
        summary : str
            Task title.
        is_all_day : bool, optional
            All-day task (default False).
        tz_id : str, optional
            Timezone ID, e.g. ``"Europe/Rome"``.
        has_start_time : bool, optional
            Whether the task has a start time (default False).
        dtstart : int, optional
            Start time in Epoch seconds (0 = not set).
        has_end_time : bool, optional
            Whether the task has a due date (default False).
        due : int, optional
            Due date in Epoch seconds (0 = not set).
        notify_setting : list[dict], optional
            Notification settings.
        description : str, optional
            Task description. Defaults to a single space for Calendar 3.x
            compatibility (requires a non-empty value).
        percent_complete : int, optional
            Completion percentage: 0 or 100 (default 0).
        from_syno_app_url : dict, optional
            Source Synology app.

        Returns
        -------
        dict[str, object] or str
            Created task object with ``evt_id``.

        Examples
        --------
            >>> cal.todo_create("/admin/home_todo/", "Buy groceries",
            ...     description="Milk, eggs, bread", percent_complete=0)
        """
        api_name = "SYNO.Cal.Todo"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": "5",  # Calendar 3.x uses v5 for create
            "method": "create",
            "original_cal_id": original_cal_id,
            "summary": summary,
            "is_all_day": is_all_day,
            "tz_id": tz_id,
            "has_start_time": has_start_time,
            "dtstart": dtstart,
            "has_end_time": has_end_time,
            "due": due,
            "description": description,
            "percent_complete": percent_complete,
        }
        if notify_setting is not None:
            req["notify_setting"] = json.dumps(notify_setting)
        if from_syno_app_url is not None:
            req["from_syno_app_url"] = json.dumps(from_syno_app_url)
        return self._cal_request(api_name, req)

    def todo_set(
        self,
        evt_id: int,
        original_cal_id: str,
        dav_etag: str,
        summary: str,
        is_all_day: bool = False,
        tz_id: str = "",
        has_start_time: bool = False,
        dtstart: int = 0,
        has_end_time: bool = False,
        due: int = 0,
        notify_setting: list[dict[str, Any]] | None = None,
        description: str = " ",
        percent_complete: int = 0,
        priority_order: int = 0,
    ) -> dict[str, object] | str:
        """
        Modify a task.

        .. warning::
           On Calendar 3.x, ``description`` must be non-empty (default ``\" \"``)
           and ``notify_setting`` may need to be passed explicitly.

        Parameters
        ----------
        evt_id : int
            Task ID.
        original_cal_id : str
            Calendar's original ID for the task list.
        dav_etag : str
            Task timestamp (optimistic locking).
        summary : str
            Task title.
        is_all_day : bool, optional
            All-day task (default False).
        tz_id : str, optional
            Timezone ID.
        has_start_time : bool, optional
            Has start time (default False).
        dtstart : int, optional
            Start time in Epoch seconds (0 = not set).
        has_end_time : bool, optional
            Has due date (default False).
        due : int, optional
            Due date in Epoch seconds (0 = not set).
        notify_setting : list[dict], optional
            Notification settings.
        description : str, optional
            Task description. Defaults to a single space for Calendar 3.x
            compatibility (requires a non-empty value).
        percent_complete : int, optional
            Completion: 0 or 100 (default 0).
        priority_order : int, optional
            Task priority.

        Returns
        -------
        dict[str, object] or str
            Updated task object.

        Examples
        --------
            >>> cal.todo_set(1052, "/admin/home_todo/", "abc123",
            ...     "Buy groceries", percent_complete=100)
        """
        api_name = "SYNO.Cal.Todo"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": "5",  # Calendar 3.x uses v5 for set
            "method": "set",
            "evt_id": evt_id,
            "original_cal_id": original_cal_id,
            "dav_etag": dav_etag,
            "summary": summary,
            "is_all_day": is_all_day,
            "tz_id": tz_id,
            "has_start_time": has_start_time,
            "dtstart": dtstart,
            "has_end_time": has_end_time,
            "due": due,
            "description": description,
            "percent_complete": percent_complete,
            "priority_order": priority_order,
        }
        if notify_setting is not None:
            req["notify_setting"] = json.dumps(notify_setting)
        return self._cal_request(api_name, req)

    def todo_list(
        self,
        cal_id_list: list[str] | None = None,
        due: int | None = None,
        filter_complete: str = "all",
        filter_due: str = "all",
        limit: int | None = None,
    ) -> dict[str, object] | str:
        """
        List tasks.

        Parameters
        ----------
        cal_id_list : list[str], optional
            Task list IDs to filter by.
        due : int, optional
            Due date timestamp in Epoch seconds.
        filter_complete : str, optional
            ``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).
        filter_due : str, optional
            ``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).
        limit : int, optional
            Maximum number of tasks to return.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"list": [...]}, "success": True}``.

        Examples
        --------
            >>> cal.todo_list(filter_complete="no", limit=50)
        """
        api_name = "SYNO.Cal.Todo"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {
            "version": info["maxVersion"],
            "method": "list",
            "filter_complete": filter_complete,
            "filter_due": filter_due,
        }
        if cal_id_list is not None:
            req["cal_id_list"] = json.dumps(cal_id_list)
        if due is not None:
            req["due"] = due
        if limit is not None:
            req["limit"] = limit
        return self._cal_request(api_name, req)

    def todo_get(self, evt_id: int) -> dict[str, object] | str:
        """
        Get task details.

        Parameters
        ----------
        evt_id : int
            Task ID.

        Returns
        -------
        dict[str, object] or str
            Task object.

        Examples
        --------
            >>> cal.todo_get(1052)
        """
        api_name = "SYNO.Cal.Todo"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "get",
                "evt_id": evt_id,
            },
        )

    def todo_delete(self, evt_id: int) -> dict[str, object] | str:
        """
        Delete a task.

        Parameters
        ----------
        evt_id : int
            Task ID.

        Returns
        -------
        dict[str, object] or str
            ``{"success": True}`` on success.

        Examples
        --------
            >>> cal.todo_delete(1052)
        """
        api_name = "SYNO.Cal.Todo"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "delete",
                "evt_id": evt_id,
            },
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Setting — User Settings
    # ═══════════════════════════════════════════════════════════════════════

    def setting_get(self) -> dict[str, object] | str:
        """
        Get calendar user settings.

        Returns
        -------
        dict[str, object] or str
            User configuration with date format, default calendar,
            timezone, etc.

        Examples
        --------
            >>> cal.setting_get()
        """
        api_name = "SYNO.Cal.Setting"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {"version": info["maxVersion"], "method": "get"},
        )

    def setting_set(
        self,
        date_format: str | None = None,
        default_alarm: dict[str, Any] | None = None,
        default_alarm_ad: dict[str, Any] | None = None,
        default_cal: str | None = None,
        default_plugin_mode: str | None = None,
        default_todo_view: dict[str, Any] | None = None,
        default_view: str | None = None,
        enable_keyboard_shortcut: bool | None = None,
        last_used_map_type: str | None = None,
        show_week_numbers: bool | None = None,
        time_format: str | None = None,
        time_zone: str | None = None,
        week_start_day: int | None = None,
    ) -> dict[str, object] | str:
        """
        Modify calendar user settings.

        Only the parameters you provide will be updated.

        Parameters
        ----------
        date_format : str, optional
            ``"Y-m-d"``, ``"m/d/Y"``, ``"d/m/Y"``,
            ``"d.m.Y"``, or ``"d-m-Y"``.
        default_alarm : dict, optional
            Default reminder for partial-day events.
        default_alarm_ad : dict, optional
            Default reminder for all-day events.
        default_cal : str, optional
            Default calendar ID for new events.
        default_plugin_mode : str, optional
            ``"nav_panel"`` or ``"todo_plugin"``.
        default_todo_view : dict, optional
            Default task list view configuration.
        default_view : str, optional
            ``"day"``, ``"week"``, ``"month"``, or ``"list"``.
        enable_keyboard_shortcut : bool, optional
            Enable keyboard shortcuts.
        last_used_map_type : str, optional
            ``"none"``, ``"google"``, or ``"baidu"``.
        show_week_numbers : bool, optional
            Show week numbers.
        time_format : str, optional
            ``"12"`` or ``"24"``.
        time_zone : str, optional
            Default timezone, e.g. ``"Europe/Rome"``.
        week_start_day : int, optional
            0=Sunday, 1=Monday, …, 6=Saturday.

        Returns
        -------
        dict[str, object] or str
            Updated user configuration.

        Examples
        --------
            >>> cal.setting_set(default_view="month",
            ...                 time_zone="Europe/Rome")
        """
        api_name = "SYNO.Cal.Setting"
        info = self.gen_list[api_name]
        req: dict[str, Any] = {"version": info["maxVersion"], "method": "set"}
        if date_format is not None:
            req["date_format"] = date_format
        if default_alarm is not None:
            req["default_alarm"] = json.dumps(default_alarm)
        if default_alarm_ad is not None:
            req["default_alarm_ad"] = json.dumps(default_alarm_ad)
        if default_cal is not None:
            req["default_cal"] = default_cal
        if default_plugin_mode is not None:
            req["default_plugin_mode"] = default_plugin_mode
        if default_todo_view is not None:
            req["default_todo_view"] = json.dumps(default_todo_view)
        if default_view is not None:
            req["default_view"] = default_view
        if enable_keyboard_shortcut is not None:
            req["enable_keyboard_shortcut"] = enable_keyboard_shortcut
        if last_used_map_type is not None:
            req["last_used_map_type"] = last_used_map_type
        if show_week_numbers is not None:
            req["show_week_numbers"] = show_week_numbers
        if time_format is not None:
            req["time_format"] = time_format
        if time_zone is not None:
            req["time_zone"] = time_zone
        if week_start_day is not None:
            req["week_start_day"] = week_start_day
        return self._cal_request(api_name, req)

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Timezone — Timezone Listing
    # ═══════════════════════════════════════════════════════════════════════

    def timezone_list(self) -> dict[str, object] | str:
        """
        List available timezone IDs.

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"list": [{"tzid": "Europe/Rome", ...}, ...]}, "success": True}``.

        Examples
        --------
            >>> cal.timezone_list()
        """
        api_name = "SYNO.Cal.Timezone"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {"version": info["maxVersion"], "method": "list"},
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SYNO.Cal.Contact — Invitee Listing
    # ═══════════════════════════════════════════════════════════════════════

    def contact_list(
        self, list_dsm_only: bool = False
    ) -> dict[str, object] | str:
        """
        List calendar contacts (invitees).

        Parameters
        ----------
        list_dsm_only : bool, optional
            List only DSM users (default False).

        Returns
        -------
        dict[str, object] or str
            ``{"data": {"list": [...]}, "success": True}``.

        Examples
        --------
            >>> cal.contact_list()
            >>> cal.contact_list(list_dsm_only=True)
        """
        api_name = "SYNO.Cal.Contact"
        info = self.gen_list[api_name]
        return self._cal_request(
            api_name,
            {
                "version": info["maxVersion"],
                "method": "list",
                "list_dsm_only": list_dsm_only,
            },
        )
