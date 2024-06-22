# Fetch and Update Cards Information
from utils import invoke


class AnkiCards:
    def __init__(self, deckId: str) -> None:
        self.deckId = deckId

    def fetch_cards(self):
        return invoke("findCards", query=f"deck:{self.deckId}")
