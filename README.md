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
- [ffmpeg](https://ffmpeg.org/)
- [aria2](https://github.com/aria2/aria2)
- [shakra packager](https://github.com/shaka-project/shaka-packager)
- [MKVToolNix](https://mkvtoolnix.download/)

## How to use
1. Extract Cookies from Netflix:
    - Use an extension like [cookie.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/) to extract cookies from Netflix.
    - Save the extracted cookie file in your working directory.

2. Obtain a Private L3 CDM (Content Decryption Module):
    - Option 1: Extract it yourself from an Android device using the ![dumper](https://github.com/Diazole/dumper) tool.
    - Option 2: Extract it yourself from an Android emulator. [how to](https://gist.github.com/Bbalduzz/f0ebe75f6c38e0daf0fba0160439e68a)

3. Setup the L3 CDM:
   - Place the L3 CDM file, named as device_name, inside the devices folder in your working environment.
  
Working folder example:
```bash
│   phantomflix/
│   cookies.txt
│   languages.txt
│   setup.py
│   main.py
└───devices/
    └───<device name>/
            device_client_id_blob
            device_private_key
```

Now open a terminal on the working dir and run:
- `py setup.py install`
- `py main.py`

where `main.py` looks like this:
```python
from phantomflix import NetflixClient
import asyncio

client = NetflixClient(
    email="", # Insert your email here
    password="", # Insert your password here
    device="<device_name>", # Insert your CDM folder name here
    quality=1080,
    audio_language=["Italian"],
    language="it-IT", # Metadata language
    video_profile="high",
    quiet=False,
)

async def main():
    # movie
    viewables = client.get_viewables(81500601) # for serie add season=<season_number>, episode=<episode_number>
    for viewable in viewables: print(viewable.title)
    await viewables[0].download()
asyncio.run(main())
```

# Support
We also accept donations, so we can keep this project up!

[![liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/balduzz/donate)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C8T2OJ6)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=3C8G7V8DUWLQG)
