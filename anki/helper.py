from utils import invoke
from cards import AnkiCards

fake_data = [
    {
        "Q": "Why do we wear jackets in the winter?",
        "A": "We wear jackets in the winter to keep warm because it is cold outside.",
    },
    {
        "Q": "Why do people need to sleep?",
        "A": "People need to sleep to rest and recharge their bodies and minds.",
    },
    {
        "Q": "What do you do when you are thirsty?",
        "A": "When you are thirsty, you should drink water to stay hydrated.",
    },
    {
        "Q": "Why do we use umbrellas when it rains?",
        "A": "We use umbrellas when it rains to keep ourselves dry.",
    },
    {
        "Q": "Why is it important to eat vegetables?",
        "A": "It is important to eat vegetables because they are nutritious and good for our health.",
    },
    {
        "Q": "Why do people brush their teeth?",
        "A": "People brush their teeth to keep them clean and to prevent cavities and gum disease.",
    },
    {
        "Q": "Why do we need to wear seat belts in cars?",
        "A": "We need to wear seat belts in cars to protect ourselves in case of an accident.",
    },
    {
        "Q": "Why do people go to school?",
        "A": "People go to school to learn new things and gain knowledge.",
    },
    {
        "Q": "Why do we need to drink water?",
        "A": "We need to drink water to stay hydrated and keep our bodies functioning properly.",
    },
    {
        "Q": "Why do people exercise?",
        "A": "People exercise to stay healthy, build strength, and improve their overall well-being.",
    },
]

def add_fake_data():
    current_deck = {"name": "CalHacks", "id": 1719082606356}
    ankicards = AnkiCards(current_deck)

    for card in fake_data:
        Question = card["Q"]
        Answer = card["A"]
        invoke("addNote", note={"deckName": current_deck["name"], "modelName": "CalHacks", "fields": {"Question": Question, "Answer": Answer}})
    
    print("Fake data added successfully!")

if __name__ == "__main__":
    add_fake_data()



