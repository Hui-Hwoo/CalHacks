# CalHacks

## How to start

1. Clone the repository
2. run `./run.sh` in the terminal

## Use Case

1. (optional)provide the pdf document -> generate the flashcard content

2. fetch the flashcard content -> generate questions

3. detech the emotional state -> update the flashcard status

## Steps

-   [x] Confirm Anki has a read/write API
-   [x] Understand which API endpoints we'll use to...
    -   [ ] Get due cards from deck
    -   [ ] Set whether user got answer right and how easy it was to recall
-   [x] Try to an LLM (ChatGPT|Hume) to converse with the User in natural language - prompt the flashcard, check whether they got it right, how easy it was to recall.
    -   [ ] Optional flow to demo: User can ask clarifying questions around flashcards
    -   [x] Question: Is Hume's LLM a good enough general LLM, or do we need to use ChatGPT?
            Answer: Hume can use gpt-4o as supplementary LLM.
-   [ x] Make prompt for LLM to read the format properly/generate data to send back to Anki
-   [x] Test function calling for getting flashcards and setting the answers
-   [ ] Write proper set function to update the flashcards' ease of recall only
-   [ ] Test first using a text file that roughly corresponds to Anki's deck/card data structure
-   [ ] Discard the text file - connect to Anki's HTTP API.
-   [x] Add Text to Speech either via Hume or LMNT - so that we're conversing instead of typing
-   [ ] Prototype auto-generating flashcards via AI
    -   [ ] OCR using Intel's platform? Or maybe just GPT-4o...
-   [ ] Add Hume's emotional analysis to gauge how user confidence about the answer

## Example

### Card format

```json
{
    "cardId": 1719083670854,
    "fields": {
        "Question": { "value": "Question for CalHacks", "order": 0 },
        "Answer": { "value": "Answer for CalHacks", "order": 1 },
        "Image": {
            "value": "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg",
            "order": 2
        }
    },
    "fieldOrder": 0,
    "question": "<style>.card {\n    font-family: arial;\n    font-size: 20px;\n    text-align: center;\n    color: black;\n    background-color: white;\n}\n</style>test\n\n<img src=https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg />",
    "answer": "<style>.card {\n    font-family: arial;\n    font-size: 20px;\n    text-align: center;\n    color: black;\n    background-color: white;\n}\n</style>test\n\n<img src=https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg />\n\n<hr id=answer>\n\negts",
    "modelName": "CalHacks",
    "ord": 0,
    "deckName": "CalHacks",
    "css": ".card {\n    font-family: arial;\n    font-size: 20px;\n    text-align: center;\n    color: black;\n    background-color: white;\n}\n",
    "factor": 0,
    "interval": 0,
    "note": 1719083670854,
    "type": 0,
    "queue": 0,
    "due": 20718,
    "reps": 0,
    "lapses": 0,
    "left": 0,
    "mod": 1719083670
}
```

# Project Story

## Inspiration

The potential of AI lies not in performing tasks for humans, but in transforming diverse information formats into accessible and interactive forms. By making sense of chaos, AI can help us complete tasks and extract valuable insights. With the advancements in AI's ability to understand speech and detect emotions, we can increasingly rely on AI to assist in daily decision-making, avoiding the pitfalls of our own biases.

Our project starts from a simple yet powerful idea: using AI to help us manage tasks, emails, and assignments through conversation. Specifically, we aim to enhance the flashcard application Anki. With conversational learning, detailed and customized explanations, and the ability to recognize uncertainty even in our affirmative responses, AI offers a more objective view of our study progress, preventing overconfidence. Imagine giving AI all the files or links you need to review and starting the entire process with a simple "Hello!"—that's what we're building. By creating a conversational interface with otherwise silent files and information sources, we're making language powerful again, enabling us to complete any work by talking. If you lack a clear plan, you can even ask AI to help design one.
