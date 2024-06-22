# Fetch and Update Cards Information
from .utils import invoke


class AnkiCards:
    def __init__(self, deckInfo: dict) -> None:
        self.deckInfo = deckInfo
        self.cards = []

    def fetch_cards(self):
        self.cards = invoke("findCards", query=f"deck:{self.deckInfo['name']}")
        return self.cards

    def fetch_card_info(self, cardId: str):
        return invoke("cardsInfo", cards=[cardId])
