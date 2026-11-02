import requests
from bs4 import BeautifulSoup

from dataclasses import dataclass


@dataclass
class ExtractionResult:
    success:bool
    metadata:dict
    reason:str=""

class MetaExtractor:
    @staticmethod
    def extract(url:str)->dict:
        response = requests.get(
            url=url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                )
            },
            timeout=400
        )
        print(response.status_code)
        print(response.text[:500])  
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        def get_meta(property_name):
            tag = soup.find(
                "meta",
                property=property_name
            )
            return tag.get("content") if tag else ""
        
        metadata = {
            "title": get_meta("og:title"),
            "description": get_meta("og:description"),
            "thumbnail": get_meta("og:image"),
            "site_name": get_meta("og:site_name"),
        }
        if any(metadata.values()):
            return ExtractionResult(
                success=True,
                metadata=metadata        
            )

        return ExtractionResult(
            success= False,
            metadata={},
            reason= f"No OpenGraph metadata found {metadata}"
        )