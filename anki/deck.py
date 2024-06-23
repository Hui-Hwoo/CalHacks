# Fecth Decks information

from .utils import invoke


class AnkiDecks:
    def __init__(self):
        self.decks = []

    def fetch_decks(self):
        resp = invoke("deckNamesAndIds")
        for deckName, deckId in resp.items():
            self.decks.append({"name": deckName, "id": deckId})
        return self.decks

    def fetch_deck_info(self, deckId: str):
        return invoke("deckInfo", deck=deckId)
