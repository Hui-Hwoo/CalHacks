# Fecth Decks information



class AnkiDecks:
    def __init__(self, anki):
        self.decks = []

    def fetch_decks(self):
        self.decks = self._invoke("deckNames")
        return self.decks


