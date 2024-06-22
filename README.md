# CalHacks

# How to start

1. Clone the repository
2. run `./run.sh` in the terminal

## Notes for Windows Users

Windows users may see a firewall nag dialog box appear on Anki startup. This occurs because Anki-Connect runs a local HTTP server in order to enable other applications to connect to it. The host application, Anki, must be unblocked for this plugin to function correctly.

## Notes for MacOS Users

Starting with Mac OS X Mavericks, a feature named App Nap has been introduced to the operating system. This feature causes certain applications which are open (but not visible) to be placed in a suspended state. As this behavior causes Anki-Connect to stop working while you have another window in the foreground, App Nap should be disabled for Anki:

Start the Terminal application.
Execute the following commands in the terminal window:

```
defaults write net.ankiweb.dtop NSAppSleepDisabled -bool true
defaults write net.ichi2.anki NSAppSleepDisabled -bool true
defaults write org.qt-project.Qt.QtWebEngineCore NSAppSleepDisabled -bool true
```

Restart Anki.
