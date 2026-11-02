from urllib.parse import urlparse

class PlatformDetector:

    PLATFORM_MAP = {
        "youtube.com": "YouTube",
        "www.youtube.com": "YouTube",
        "youtu.be": "YouTube",

        "instagram.com": "Instagram",
        "www.instagram.com": "Instagram",

        "tiktok.com": "TikTok",
        "www.tiktok.com": "TikTok",

        "github.com": "GitHub",
        "www.github.com": "GitHub",
    }
    @staticmethod
    def detect(value:str)->str:
        if not value:
            return ValueError("Value required")
        parsed = urlparse(value)
        domain = parsed.netloc.lower()
        return PlatformDetector.PLATFORM_MAP.get(domain, "")
