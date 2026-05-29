---
sidebar_position: 8
title: ✅ Calendar
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# Calendar
## Overview
Synology Calendar API client.  
  
Manages calendars, events, tasks, settings, and timezone information
via the SYNO.Cal.* WebAPI endpoints.

Requires Synology Calendar 2.5.0+ on the target NAS.  
  
## Methods
### `cal_create`
Create a calendar or task list.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Cal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_type_** `str`  
``"event"`` for calendar, ``"todo"`` for task list.  
  
**_cal_displayname_** `str`  
Calendar display name.  
  
**_cal_description_** `str`  
Calendar description.  
  
**_cal_color_** `str`  
Calendar colour in RGB hex, e.g. ``"#FF8000"``.  
  
**_is_hidden_in_cal_** `bool`  
Hide events for this calendar (default False).  
  
**_is_hidden_in_list_** `bool`  
Hide calendar from list (default False).  
  
**_notify_alarm_by_browser_** `bool`  
Send reminder via browser (default True).  
  
**_notify_alarm_by_mail_** `bool`  
Send reminder via email (default True).  
  
**_notify_evt_by_browser_** `bool`  
Send event changes via browser (default True).  
  
**_notify_evt_by_mail_** `bool`  
Send event changes via email (default False).  
  
**_notify_import_cal_by_browser_** `bool`  
Send import results via browser (default True).  
  
**_notify_import_cal_by_mail_** `bool`  
Send import results via email (default True).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created calendar object with ``cal_id``.  
</div>
  



---


### `cal_list`
List calendars and/or task lists.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Cal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_type_** `str`  
``"event"``, ``"todo"``, or ``"all"`` (default ``"all"``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"list": [...]}, "success": True}``.  
</div>
  



---


### `cal_get`
Get a single calendar by ID.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Cal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_** `str`  
Calendar ID, e.g. ``"/admin/home/"``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Calendar object.  
</div>
  



---


### `cal_set`
Edit calendar information.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Cal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_** `str`  
Calendar ID, e.g. ``"/admin/home/"``.  
  
**_cal_type_** `str`  
``"event"`` for calendar, ``"todo"`` for task list.  
  
**_original_cal_id_** `str`  
Calendar's original ID.  
  
**_cal_displayname_** `str`  
Calendar display name.  
  
**_cal_description_** `str`  
Calendar description.  
  
**_cal_color_** `str`  
Calendar colour in RGB hex, e.g. ``"#E3BD00"``.  
  
**_is_hidden_in_cal_** `bool`  
Hide events for this calendar (default False).  
  
**_is_hidden_in_list_** `bool`  
Hide calendar from list (default False).  
  
**_notify_alarm_by_browser_** `bool`  
Send reminder via browser (default True).  
  
**_notify_alarm_by_mail_** `bool`  
Send reminder via email (default True).  
  
**_notify_evt_by_browser_** `bool`  
Send event changes via browser (default True).  
  
**_notify_evt_by_mail_** `bool`  
Send event changes via email (default False).  
  
**_notify_import_cal_by_browser_** `bool`  
Send import results via browser (default True).  
  
**_notify_import_cal_by_mail_** `bool`  
Send import results via email (default True).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Updated calendar object.  
</div>
  



---


### `cal_delete`
Delete a calendar.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Cal`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_** `str`  
Calendar ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"success": True}`` on success.  
</div>
  



---


### `event_create`
Create a new event.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Event`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_** `str`  
Calendar ID, e.g. ``"/admin/home/"``.  
  
**_original_cal_id_** `str`  
Calendar's original ID.  
  
**_summary_** `str`  
Event title.  
  
**_is_all_day_** `bool`  
Whether this is an all-day event.  
  
**_tz_id_** `str`  
Timezone ID, e.g. ``"Europe/Rome"``.
Use :meth:`timezone_list` to discover available values.  
  
**_dtstart_** `int`  
Event start time in Epoch seconds.  
  
**_dtend_** `int`  
Event end time in Epoch seconds.  
  
**_is_repeat_evt_** `bool`  
Whether this is a recurring event (default False).  
  
**_repeat_setting_** `dict`  
Recurrence rule configuration (see API guide for repeat_obj).  
  
**_color_** `str`  
Event colour as ``#RRGGBB`` hex, e.g. ``"#00FF00"``.
Defaults to ``"#000000"`` (black). Required on Calendar 3.x.  
  
**_notify_setting_** `list[dict]`  
Notification settings (see API guide for notify_obj).  
  
**_description_** `str`  
Event description. Defaults to a single space for Calendar 3.x
compatibility (requires a non-empty value).  
  
**_participant_** `list[dict]`  
Event participants (see API guide for participant_obj).  
  
**_location_info_** `dict`  
Location information (see API guide for location_obj).  
  
**_from_syno_app_url_** `dict`  
Source Synology app (e.g. MailPlus).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created event object with ``evt_id``.  
</div>
  



---


### `event_list`
List events with optional filters.  
At least one of ``start``, ``end``, or ``limit`` is required
by the API.  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Event`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_list_** `list[str]`  
Calendar IDs to filter by.  
  
**_start_** `int`  
Start time in Epoch seconds.  
  
**_end_** `int`  
End time in Epoch seconds.  
  
**_evt_color_list_** `list[str]`  
Event colours to list, e.g. ``["#112233", "#445566"]``.  
  
**_keyword_** `str`  
Search keyword in summary, description, and location.  
  
**_limit_** `int`  
Maximum number of events to return.  
  
**_filter_starred_** `str`  
``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).  
  
**_filter_own_** `str`  
``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).  
  
**_filter_invited_** `str`  
``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"list": [...]}, "success": True}``.  
</div>
  



---


### `event_get`
Get event or sub-event details.  
Use either ``evt_id`` or ``ical_uid`` (mutually exclusive).
When using ``ical_uid``, ``cal_id`` must also be provided.  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Event`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Event ID.  
  
**_recurrence_id_** `str`  
Sub-event date in ISO 8601 format (``YYYYMMDD`` or
``YYYYMMDDThhmmss``).  
  
**_ical_uid_** `str`  
Event UID within ICS. Mutually exclusive with ``evt_id``.  
  
**_cal_id_** `str`  
Calendar ID. Required when using ``ical_uid``.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Event object.  
</div>
  



---


### `event_set`
Modify an event. Returns main event info on success.  
.. warning::
   On Calendar 3.x, ``personal_property`` and ``location_info``
   must be passed explicitly for the ``set`` method to succeed.  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Event`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Event ID.  
  
**_cal_id_** `str`  
Calendar ID.  
  
**_original_cal_id_** `str`  
Calendar's original ID.  
  
**_dav_etag_** `str`  
Event timestamp (optimistic locking).
If this differs from the server value, someone else
already modified the event.  
  
**_summary_** `str`  
Event title.  
  
**_is_all_day_** `bool`  
Whether this is an all-day event.  
  
**_tz_id_** `str`  
Timezone ID, e.g. ``"Europe/Rome"``.  
  
**_dtstart_** `int`  
Event start time in Epoch seconds.  
  
**_dtend_** `int`  
Event end time in Epoch seconds.  
  
**_is_repeat_evt_** `bool`  
Recurring event (default False).  
  
**_repeat_setting_** `dict`  
Recurrence rules.  
  
**_color_** `str`  
Event RGB colour.  
  
**_notify_setting_** `list[dict]`  
Notification settings.  
  
**_description_** `str`  
Event description.  
  
**_participant_** `list[dict]`  
Event participants.  
  
**_location_info_** `dict`  
Location information.  
  
**_attachments_** `list[dict]`  
Attachment information.  
  
**_exdate_** `str`  
Delete a specific occurrence of a recurring event
(ISO 8601 format).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Updated event object.  
</div>
  



---


### `event_delete`
Delete an event.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Event`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Event ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"success": True}`` on success.  
</div>
  



---


### `todo_create`
Create a task.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Todo`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_original_cal_id_** `str`  
Calendar's original ID for the task list.  
  
**_summary_** `str`  
Task title.  
  
**_is_all_day_** `bool`  
All-day task (default False).  
  
**_tz_id_** `str`  
Timezone ID, e.g. ``"Europe/Rome"``.  
  
**_has_start_time_** `bool`  
Whether the task has a start time (default False).  
  
**_dtstart_** `int`  
Start time in Epoch seconds (0 = not set).  
  
**_has_end_time_** `bool`  
Whether the task has a due date (default False).  
  
**_due_** `int`  
Due date in Epoch seconds (0 = not set).  
  
**_notify_setting_** `list[dict]`  
Notification settings.  
  
**_description_** `str`  
Task description. Defaults to a single space for Calendar 3.x
compatibility (requires a non-empty value).  
  
**_percent_complete_** `int`  
Completion percentage: 0 or 100 (default 0).  
  
**_from_syno_app_url_** `dict`  
Source Synology app.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Created task object with ``evt_id``.  
</div>
  



---


### `todo_set`
Modify a task.  
.. warning::
   On Calendar 3.x, ``description`` must be non-empty (default ``" "``)
   and ``notify_setting`` may need to be passed explicitly.  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Todo`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Task ID.  
  
**_original_cal_id_** `str`  
Calendar's original ID for the task list.  
  
**_dav_etag_** `str`  
Task timestamp (optimistic locking).  
  
**_summary_** `str`  
Task title.  
  
**_is_all_day_** `bool`  
All-day task (default False).  
  
**_tz_id_** `str`  
Timezone ID.  
  
**_has_start_time_** `bool`  
Has start time (default False).  
  
**_dtstart_** `int`  
Start time in Epoch seconds (0 = not set).  
  
**_has_end_time_** `bool`  
Has due date (default False).  
  
**_due_** `int`  
Due date in Epoch seconds (0 = not set).  
  
**_notify_setting_** `list[dict]`  
Notification settings.  
  
**_description_** `str`  
Task description. Defaults to a single space for Calendar 3.x
compatibility (requires a non-empty value).  
  
**_percent_complete_** `int`  
Completion: 0 or 100 (default 0).  
  
**_priority_order_** `int`  
Task priority.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Updated task object.  
</div>
  



---


### `todo_list`
List tasks.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Todo`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_cal_id_list_** `list[str]`  
Task list IDs to filter by.  
  
**_due_** `int`  
Due date timestamp in Epoch seconds.  
  
**_filter_complete_** `str`  
``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).  
  
**_filter_due_** `str`  
``"yes"``, ``"no"``, or ``"all"`` (default ``"all"``).  
  
**_limit_** `int`  
Maximum number of tasks to return.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"list": [...]}, "success": True}``.  
</div>
  



---


### `todo_get`
Get task details.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Todo`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Task ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Task object.  
</div>
  



---


### `todo_delete`
Delete a task.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Todo`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_evt_id_** `int`  
Task ID.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"success": True}`` on success.  
</div>
  



---


### `setting_get`
Get calendar user settings.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Setting`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
User configuration with date format, default calendar,
timezone, etc.  
</div>
  



---


### `setting_set`
Modify calendar user settings.  
Only the parameters you provide will be updated.  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Setting`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_date_format_** `str`  
``"Y-m-d"``, ``"m/d/Y"``, ``"d/m/Y"``,
``"d.m.Y"``, or ``"d-m-Y"``.  
  
**_default_alarm_** `dict`  
Default reminder for partial-day events.  
  
**_default_alarm_ad_** `dict`  
Default reminder for all-day events.  
  
**_default_cal_** `str`  
Default calendar ID for new events.  
  
**_default_plugin_mode_** `str`  
``"nav_panel"`` or ``"todo_plugin"``.  
  
**_default_todo_view_** `dict`  
Default task list view configuration.  
  
**_default_view_** `str`  
``"day"``, ``"week"``, ``"month"``, or ``"list"``.  
  
**_enable_keyboard_shortcut_** `bool`  
Enable keyboard shortcuts.  
  
**_last_used_map_type_** `str`  
``"none"``, ``"google"``, or ``"baidu"``.  
  
**_show_week_numbers_** `bool`  
Show week numbers.  
  
**_time_format_** `str`  
``"12"`` or ``"24"``.  
  
**_time_zone_** `str`  
Default timezone, e.g. ``"Europe/Rome"``.  
  
**_week_start_day_** `int`  
0=Sunday, 1=Monday, …, 6=Saturday.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
Updated user configuration.  
</div>
  



---


### `timezone_list`
List available timezone IDs.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Timezone`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"list": [{"tzid": "Europe/Rome", ...}, ...]}, "success": True}``.  
</div>
  



---


### `contact_list`
List calendar contacts (invitees).  
  
#### Internal API
<div class="padding-left--md">

`SYNO.Cal.Contact`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_list_dsm_only_** `bool`  
List only DSM users (default False).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
``{"data": {"list": [...]}, "success": True}``.  
</div>
  



---


