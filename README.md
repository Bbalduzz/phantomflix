<h1 align="center">
  Phantomflix
</h1>

<h4 align="center">Python Netflix API Metadata & Downloader for Windows and Linux</h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#how-to-use">How To Use</a>
</p>

## Features
* Get Metadata (title, year, episodes, seasons...) with official Netflix api
* Get medias (videos, audios, audio descriptions, subtitles...)
* Decrypt Widevine DRM protected content
* Automatically mux all your tracks
* Nice pre-made format for file names
* Very fast multi-connection downloads

## Dependencies
> make sure to add these in the PATH on in your working directory
- ![ffmpeg](https://ffmpeg.org/)
- ![aria2](https://github.com/aria2/aria2)
- ![shakra packager](https://github.com/shaka-project/shaka-packager)
- ![MKVToolNix](https://mkvtoolnix.download/)

## How to use
Extract the cookies from Netflix (use an extension like this ![cookie.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)) and place the cookie file in your working directory.

Then you will need a **private L3 CDM**. You can extract one for yourself from an Andoid device using this tool: ![https://github.com/Diazole/dumper](https://github.com/Diazole/dumper), or you can buy one for cheap from me. If you need to contact me you can find me on telegram: [@edobal](https://t.me/edobal). Then place `device_name` with the L3 cdm inside the `devices` folder.

Working folder example:
```bash
│   cookies.txt
│   main.py
│   phantomflix/
└───devices/
    └───<device name>/
            device_client_id_blob
            device_private_key
```

Now open a terminal on the working dir and run:
- `py setup.py install`
- `py main.py`

where `main.py` looks like this:
```pthon

```
