---
sidebar_position: 20
title: 🚧 NoteStation
---

<!-- -------------------------------------------- -->
<!-- THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  -->
<!-- -------------------------------------------- -->
  
# NoteStation
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
Interface for Synology NoteStation API.  
  
Provides methods to interact with NoteStation features such as retrieving settings,
notebooks, tags, shortcuts, todos, smart notes, and individual notes.  
  
## Methods
### `settings_info`
Retrieve NoteStation settings information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Setting` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing settings information or an error message.  

</div>



---


### `info`
Retrieve NoteStation general information.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Info` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing general information or an error message.  

</div>



---


### `notebooks_info`
Retrieve the list of notebooks.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Notebook` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of notebooks or an error message.  

</div>



---


### `tags_info`
Retrieve the list of tags.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Tag` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of tags or an error message.  

</div>



---


### `shortcuts`
Retrieve the list of shortcuts.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Shortcut` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of shortcuts or an error message.  

</div>



---


### `todo`
Retrieve the list of todo items.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Todo` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of todo items or an error message.  

</div>



---


### `smart`
Retrieve the list of smart notes.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Smart` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of smart notes or an error message.  

</div>



---


### `note_list`
Retrieve the list of notes.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Note` 
</div>
  
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the list of notes or an error message.  

</div>



---


### `specific_note_id`
Retrieve a specific note by its ID.  
  
#### Internal API
<div class="padding-left--md">
`SYNO.NoteStation.Note` 
</div>
  
#### Parameters
<div class="padding-left--md">
**_note_id_** `str or int`  
The ID of the note to retrieve.  
  

</div>
#### Returns
<div class="padding-left--md">
`dict[str, object] or str`  
The API response containing the note data or an error message.  

</div>



---


