from anki.deck import AnkiDecks
from anki.cards import AnkiCards


def main():
    # fetch desk
    ankidesk = AnkiDecks()
    ankidesk.fetch_decks()

    # choose deck
    # current_deck = ankidesk.decks
    current_deck = {"name": "CalHacks", "id": 1719082606356}

    # fetch cards
    ankicards = AnkiCards(current_deck)
    ankicards.fetch_cards()

    # fetch card info
    cardId = ankicards.cards[0]
    card_info = ankicards.fetch_card_info(cardId)

    # deal with card info

    # update card info


if __name__ == "__main__":
    main()
