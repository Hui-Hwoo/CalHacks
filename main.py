from anki.deck import AnkiDecks
from anki.cards import AnkiCards


def main():
    # fetch desk
    ankidesk = AnkiDecks()
    ankidesk.fetch_decks()

    # choose deck
    current_deck = {"name": "CalHacks", "id": 1719082606356}

    # fetch cards
    ankicards = AnkiCards(current_deck)
    ankicards.fetch_cards()

    card_info = ankicards.fetch_card_info()
    # get into conversation


if __name__ == "__main__":
    main()
