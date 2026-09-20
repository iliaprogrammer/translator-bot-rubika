````markdown
# Rubika Translator Bot

A simple translation bot built with Python for Rubika.

The bot allows users to select a source language, choose a target language, translate their text, and receive the translated result as both text and audio.

## Features

- Source and target language selection
- Text translation
- Text-to-speech with gTTS
- Sends translated text
- Sends translated audio
- Temporary audio files are deleted after sending
- Per-user conversation state
- Error handling for invalid language selections

## Supported Languages

- English
- Persian
- German
- French
- Spanish
- Italian
- Turkish
- Arabic
- Russian
- Chinese
- Japanese
- Korean

## Requirements

- Python 3.10+
- Internet connection
- Rubika bot token

## Installation

Clone the repository:

```bash
git clone https://github.com/iliaprogrammer/translator-bot-rubika.git
cd translator-bot-rubika
````

Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Open `main.py` and add your Rubika bot token:

```python
bot = Robot("YOUR_BOT_TOKEN")
```

Never publish your real bot token on GitHub.

## Run

Start the bot with:

```bash
python main.py
```

Then send `/start` to the bot.

The bot will guide you through:

1. Selecting the source language
2. Selecting the target language
3. Sending the text
4. Receiving the translated text
5. Receiving the translated audio

## How It Works

```text
/start
   ↓
Select source language
   ↓
Select target language
   ↓
Send text
   ↓
Translate text
   ↓
Generate audio with gTTS
   ↓
Send translated text
   ↓
Send translated audio
   ↓
Delete temporary audio file
```

## Technologies

* Python
* Rubka
* translate
* gTTS

## Project Structure

```text
translator-bot-rubika/
│
├── main.py
├── requirements.txt
└── README.md
```

## Notes

The translation and text-to-speech features require an internet connection.

Audio files are generated temporarily and deleted after they are sent.

## Author

**Ilia**

GitHub: https://github.com/iliaprogrammer

```
```
