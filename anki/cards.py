# Fetch and Update Cards Information
from utils import invoke


class AnkiCards:
    def __init__(self, deckInfo: dict) -> None:
        self.deckInfo = deckInfo
        self.cards = []

    def _areDue(self, cards_list: list):
        return invoke("areDue", cards=cards_list)

    def fetch_cards(self):
        cards_list = invoke("findCards", query=f"deck:{self.deckInfo['name']}")
        due_cards = self._areDue(cards_list)

        self.cards = [card for card, due in zip(cards_list, due_cards) if due]
        return self.cards

    def fetch_card_info(self, n: int = 3):
        first_n_cards = self.cards[:n]
        resp = invoke("cardsInfo", cards=first_n_cards)
        self.cards = self.cards[n:]

        return resp

    async def answerCards(self, params: dict):
        performances = params.get("performances", [])
        answers = []
        for performance in performances:
            cardId = performance["questionId"]
            ease = performance["performance"]
            if cardId and ease:
                answers.append({"cardId": cardId, "ease": ease})

        return invoke("answerCards", answers=answers)

    def addCards(self, cards):
        return invoke("addNotes", notes=cards)
