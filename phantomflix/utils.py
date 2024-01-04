import requests
import random
import os

from http.cookiejar import MozillaCookieJar

metadata_endpoint = 'https://www.netflix.com/nq/website/memberapi/{}/metadata' #va7b420b8

default_file_name = "$ftitle$.$year$.$fseason$$fepisode$.NF.WEBDL.$quality$p.$audios$.$acodec$.$vcodec$-dvx.mkv"

def random_hex(length: int) -> str:
	return "".join(random.choice("0123456789ABCDEF") for _ in range(length))
    
def pretty_size(size: int) -> str:
    return f"{size/float(1<<20):,.0f}MiB"

manifest_esn = f"NFCDIE-03-{random_hex(30)}"
def get_android_esn(q: int):
    _id = 2 if q >= 2160 else 1
    return f"NFANDROID{_id}-PRV-P-SAMSUSM-G950F-7169-{random_hex(30)}"

def shakti_headers(build_id):
    return {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "es,ca;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "www.netflix.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        "X-Netflix.browserName": "Chrome",
        "X-Netflix.browserVersion": "99",
        "X-Netflix.clientType": "akira",
        "X-Netflix.esnPrefix": "NFCDCH-02-",
        "X-Netflix.osFullName": "Windows 10",
        "X-Netflix.osName": "Windows",
        "X-Netflix.osVersion": "10.0",
        "X-Netflix.playerThroughput": "58194",
        "X-Netflix.uiVersion": str(build_id),
    }

def build_headers():
    return {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Accept-Language": "en,en-US;q=0.9",
    }

def get_build_id() -> str:
    r = requests.get("https://www.netflix.com/buildIdentifier")
    if r.status_code != 200:
        raise Exception("Netflix didn't return 200")
    return r.json()["BUILD_IDENTIFIER"]

def read_data(cookies_file):
    if not os.path.exists(cookies_file):
        raise Exception(f"Missing cookie file. ({cookies_file})")
    cj = MozillaCookieJar(cookies_file)
    cj.load()
    cookies = {
        cookie.name: cookie.value
        for cookie in cj
    }
    cookies["build_id"] = get_build_id()
    if "NetflixId" not in cookies:
        raise Exception("Invalid cookies. (Missing NetflixId)")
    return cookies

lang_codes = {
    "fil": ["Filipino", "fil"],
    "cy": ["Welsh", "cym"],
    "cs": ["Czech", "ces"],
    "de": ["German", "ger"],
    "en": ["English", "eng"],
    "es": ["Spanish", "spa"],
    "bg": ["Bulgarian", "bul"],
    "ar-EG": ["Egyptian Arabic", "ara"],
    "ar-SY": ["Syrian Arabic", "ara"],
    "en-GB": ["Britain English", "eng"],
    "es-ES": ["European Spanish", "spa"],
    "fr-CA": ["Canadian French", "fra"],
    "fr": ["French", "fra"],
    "hi": ["Hindi", "hin"],
    "hu": ["Hungarian", "hun"],
    "id": ["Indonesian", "ind"], 
    "it": ["Italian", "ita"],
    "pl": ["Polish", "pol"],
    "pt-BR": ["Brazilian Portuguese", "por"],
    "ru": ["Russian", "rus"],
    "ta": ["Tamil", "tam"],
    "te": ["Telugu", "tel"],
    "th": ["Thai", "tha"],
    "tr": ["Turkish", "tur"],
    "uk": ["Ukrainian", "ukr"],
    "ar": ["Arabic", "ara"],
    "da": ["Danish", "dan"],
    "el": ["Greek", "ell"],
    "fi": ["Finnish", "fin"],
    "he": ["Hebrew", "heb"],
    "hi-Latn": ["Hindi", "hin"],
    "hr": ["Croatian", "hrv"],
    "ja": ["Japanese", "jpn"],
    "ko": ["Korean", "kor"],
    "ms": ["Malay", "msa"],
    "nb": ["Norwegian", "nob"],
    "nl": ["Dutch", "nld"],
    "pt": ["Portuguese", "por"],
    "ro": ["Romanian", "ron"],
    "sv": ["Swedish", "swe"],
    "vi": ["Vietnamese", "vie"],
    "zh": ["Chinese", "zho"],
    "zh-Hans": ["Simplified Chinese", "zho"],
    "zh-Hant": ["Traditional Chinese", "zho"]
}

supported_video_profiles = {
    "high": ["playready-h264hpl{}-dash"],
    "main": ["playready-h264mpl{}-dash"],
    "baseline": ["playready-h264bpl{}-dash"],
    "hevc": ["hevc-main10-L{}-dash-cenc", "hevc-main10-L{}-dash-cenc-prk"],
    "hdr": ["hevc-hdr-main10-L{}-dash-cenc", "hevc-hdr-main10-L{}-dash-cenc-prk"]
}

supported_audio_profiles = {
    "aac": [
        "heaac-5.1-dash",
        "heaac-5.1hq-dash",
        "heaac-2-dash",
        "heaac-2hq-dash",
    ],
    "ac3": [
        "dd-5.1-dash",
        "dd-5.1-elem"
    ],
    "eac3": [
        "ddplus-5.1-dash",
        "ddplus-5.1hq-dash",
        "ddplus-2-dash"
    ],
    "dts": [
        "ddplus-atmos-dash"
    ]
}

def get_profiles(video_profile: str, audio_profile: str, quality: int):
    profiles = ["webvtt-lssdh-ios8"]
    profile = supported_video_profiles.get(video_profile.lower())
    if quality >= 2160:
        profiles += list(map(lambda x: x.format(51), profile))
        profiles += list(map(lambda x: x.format(50), profile))
    if quality >= 1080:
        if video_profile.lower() in ["hevc", "hdr"]:
            profiles += list(map(lambda x: x.format(41), profile))
        profiles += list(map(lambda x: x.format(40), profile))
    if quality >= 720:
        profiles += list(map(lambda x: x.format(31), profile))
    if quality >= 480:
        profiles += list(map(lambda x: x.format(30), profile))
        if video_profile.lower not in ["hevc", "hdr"]:
            profiles += list(map(lambda x: x.format(22), profile))
    profiles += supported_audio_profiles.get(audio_profile.lower())
    return profiles
