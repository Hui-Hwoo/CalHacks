# CalHacks

## How to start

1. Clone the repository
2. run `./run.sh` in the terminal

## Use Case

1. (optional)provide the pdf document -> generate the flashcard content

2. fetch the flashcard content -> generate questions

3. detech the emotional state -> update the flashcard status

## Steps 
 - [x] Confirm Anki has a read/write API
 - [x] Understand which API endpoints we'll use to...
     - [ ] Get due cards from deck
     - [ ] Set whether user got answer right and how easy it was to recall
 - [x] Try to an LLM (ChatGPT|Hume) to converse with the User in natural language - prompt the flashcard, check whether they got it right, how easy it was to recall.
     - [ ] Optional flow to demo: User can ask clarifying questions around flashcards
     - [ ] Question: Is Hume's LLM a good enough general LLM, or do we need to use ChatGPT?
 - [ ] Make prompt for LLM to read the format properly/generate data to send back to Anki
 - [ ] Add Text to Speech either via Hume or LMNT - so that we're conversing instead of typing
 - [ ] Prototype auto-generating flashcards via AI
    - [ ] OCR using Intel's platform? Or maybe just GPT-4o...
 - [ ] Add Hume's emotional analysis to gauge how user confidence about the answer

## Example

### Card format

```json
{
    "answer": "back content",
    "question": "front content",
    "deckName": "Default",
    "modelName": "Basic",
    "fieldOrder": 1,
    "fields": {
        "Front": { "value": "front content", "order": 0 },
        "Back": { "value": "back content", "order": 1 }
    },
    "css": "p {font-family:Arial;}",
    "cardId": 1498938915662,
    "interval": 16,
    "note": 1502298033753,
    "ord": 1,
    "type": 0,
    "queue": 0,
    "due": 1,
    "reps": 1,
    "lapses": 0,
    "left": 6,
    "mod": 1629454092
}
```

## Notes

### for Windows Users

Windows users may see a firewall nag dialog box appear on Anki startup. This occurs because Anki-Connect runs a local HTTP server in order to enable other applications to connect to it. The host application, Anki, must be unblocked for this plugin to function correctly.

### for MacOS Users

Starting with Mac OS X Mavericks, a feature named App Nap has been introduced to the operating system. This feature causes certain applications which are open (but not visible) to be placed in a suspended state. As this behavior causes Anki-Connect to stop working while you have another window in the foreground, App Nap should be disabled for Anki:

Start the Terminal application.
Execute the following commands in the terminal window:

```
defaults write net.ankiweb.dtop NSAppSleepDisabled -bool true
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
defaults write org.qt-project.Qt.QtWebEngineCore NSAppSleepDisabled -bool true
```

Restart Anki.
