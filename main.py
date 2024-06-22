import json
import urllib.request


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(
            urllib.request.Request("http://127.0.0.1:8765", requestJson)
        )
    )
    if len(response) != 2:
        raise Exception("response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("response is missing required error field")
    if "result" not in response:
        raise Exception("response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])
    return response["result"]


# invoke('createDeck', deck='test1')
# result = invoke('deckNames')
# print('got list of decks: {}'.format(result))

# get the list of all cards in the deck
# result = invoke('getDeckConfig', deck='CalHacks')
# print(result)
# result = invoke("getDeckStats", decks=["■  English"])
# deck_id = result["deck_id"]


# get all cards in the deck
result = invoke("findCards", query="deck:CalHacks")
# # result = invoke("findCards", query="deck:current")
# print(result)
card_ids = result

cards_info = invoke("cardsInfo", cards=card_ids)
print(cards_info)


# findNoets: [1716397870329, 1716399687446, 1716399734118, 1716399854243, 1716399957711, 1716400782302, 1716401010200, 1716401181049, 1716401185814, 1716401416772, 1716401638840, 1716401685628, 1716402239740, 1716402668155, 1716402784843, 1716402970472]
# findCards: [1716397870329, 1716399687448, 1716399734119, 1716399854243, 1716399957711, 1716400782303, 1716401010200, 1716401181049, 1716401185814, 1716401416773, 1716401638841, 1716401685628, 1716402239741, 1716402668155, 1716402784844, 1716402970472]
