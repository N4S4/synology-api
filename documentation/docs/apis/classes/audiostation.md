---
sidebar_position: 6
title: 🚧 AudioStation
description: "A class to interact with Synology AudioStation API." 
---

{/* -------------------------------------------- */}
{/* THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.  */}
{/* -------------------------------------------- */}
  
# AudioStation
:::warning
 
This API is partially documented or under construction.
 
:::
## Overview
A class to interact with Synology AudioStation API.  
  
  
  
## Methods
### `get_info`
Retrieve general information about the AudioStation service.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.Info`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
A dictionary containing the service information or a string in case of an error.  
</div>
  



---


### `get_playlist_info`
Retrieve information about playlists in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.Playlist`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
A dictionary containing playlist information or a string in case of an error.  
</div>
  



---


### `list_remote_player`
Retrieve a list of remote players available in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
A dictionary containing information about remote players, or a string in case of an error.  
</div>
  



---


### `list_pinned_song`
Retrieve a list of pinned songs in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.Pin`  
</div>
  
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
A dictionary containing information about pinned songs, or a string in case of an error.  
</div>
  



---


### `device_id`
Retrieve the playlist for a specific remote device in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_** `str`  
The ID of the remote device.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object]`  
A dictionary containing the playlist information for the specified device.  
</div>
  



---


### `remote_play`
Start playback on a specified remote device in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_** `str`  
The ID of the remote device on which to start playback.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
A dictionary containing the playback status or a string in case of an error.  
</div>
  



---


### `remote_stop`
Stop playback on a specified remote device in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_** `str`  
The ID of the remote device on which to stop playback.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
A dictionary containing the stop status or a string in case of an error.  
</div>
  



---


### `remote_next`
Skip to the next track on a specified remote device in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_** `str`  
The ID of the remote device on which to skip to the next track.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
A dictionary containing the status of the operation or a string in case of an error.  
</div>
  



---


### `remote_prev`
Skip to the previous track on a specified remote device in AudioStation.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioStation.RemotePlayer`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_device_** `str`  
The ID of the remote device on which to skip to the previous track.  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict[str, object] or str`  
A dictionary containing the status of the operation or a string in case of an error.  
</div>
  



---


### `audiostream_stream`
Start audio streaming for a given media ID.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioPlayer.Stream`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_id_** `str`  
Media ID to stream (from ``list_media_info``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict`  
Stream URL and metadata.  
</div>
  



---


### `audiostream_transcode`
Transcode an audio stream to a different format.  
  
#### Internal API
<div class="padding-left--md">

`SYNO.AudioPlayer.Stream`  
</div>
  
#### Parameters
<div class="padding-left--md">

**_id_** `str`  
Media ID to transcode (from ``list_media_info``).  
  
</div>
  
#### Returns
<div class="padding-left--md">

`dict`  
Transcode stream URL and metadata.  
</div>
  



---


