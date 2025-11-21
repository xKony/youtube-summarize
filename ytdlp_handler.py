import yt_dlp
from config import SAVE_SUBTITLES
from logger import get_logger
from typing import Any

log = get_logger(__name__)


class YtDlp_Handler:
    def __init__(self, output_subtitles=SAVE_SUBTITLES):
        self.ydl_opts: dict[str, Any] = _get_default_ydl_opts()
        self.ydl_opts["writesubtitles"] = output_subtitles

    def get_available_subtitles(self, video_url: str) -> list[str] | None:
        log.debug(f"Checking available subtitles for video: {video_url}")
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:  # type: ignore[arg-type]
            info_dict = ydl.extract_info(video_url, download=False)
            subtitles = info_dict.get("subtitles", {})
            automatic = info_dict.get("automatic_captions", {})
            if subtitles:
                langs = list(subtitles.keys())
                log.debug(f"Available subtitles: {langs}")
                return langs
            elif automatic:
                langs = list(automatic.keys())
                log.debug(f"Available automatic captions: {langs}")
                return langs
            else:
                log.warning("No subtitles available for this video.")
                return None


def _get_default_ydl_opts() -> dict[str, Any]:
    return {
        "writesubtitles": True,
        "subtitleslangs": ["all"],
        "skip_download": True,
        "outtmpl": "%(id)s.%(ext)s",
        "quiet": True,
    }
