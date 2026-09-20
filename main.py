import asyncio
from rubka.asynco import Robot
from rubka.context import Message
from translate import Translator
from gtts import gTTS
import os

bot = Robot("YOUR_TOKEN")
state = {}
langs = {
    "English": "en",
    "Persian": "fa",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Italian": "it",
    "Turkish": "tr",
    "Arabic": "ar",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko"
}
def trans(txt, fromlang, tolang):
    translator = Translator(
        from_lang=fromlang,
        to_lang=tolang
    )
    result = translator.translate(txt)
    return result
@bot.on_message_text()
async def main(bot: Robot, msg: Message):
    text = msg.text
    chatid = msg.chat_id
    if text == "/start":
        state[chatid] = {
            "state": "waiting_lang1"
        }
        await msg.reply("""
Please select the source language:

English
Persian
German
French
Spanish
Italian
Turkish
Arabic
Russian
Chinese
Japanese
Korean
""")
        return
    if state.get(chatid, {}).get("state") == "waiting_lang1":
        if text not in langs:
            await msg.reply(
                "Please select a language from the list."
            )
            state.pop(chatid, None)
            return
        state[chatid]["l1"] = langs[text]
        state[chatid]["state"] = "waiting_lang2"
        await msg.reply("""
Please select the target language:

English
Persian
German
French
Spanish
Italian
Turkish
Arabic
Russian
Chinese
Japanese
Korean
""")
        return
    if state.get(chatid, {}).get("state") == "waiting_lang2":
        if text not in langs:
            await msg.reply(
                "Please select a language from the list."
            )
            state.pop(chatid, None)
            return
        state[chatid]["l2"] = langs[text]
        state[chatid]["state"] = "waiting_txt"
        await msg.reply("Send your text.")
        return
    if state.get(chatid, {}).get("state") == "waiting_txt":
        state[chatid]["txt"] = text
        fromlang = state[chatid]["l1"]
        tolang = state[chatid]["l2"]
        txt = state[chatid]["txt"]
        try:
            result = trans(
                txt,
                fromlang,
                tolang
            )
            await msg.reply(f"""
Input text:
{txt}

Source language:
{fromlang}

Target language:
{tolang}

Translated text:
♦ {result} ♦
""")
            tts = gTTS(
                text=result,
                lang=tolang
            )
            tts.save(f"{chatid}.mp3")
            await msg.reply_music(f"{chatid}.mp3")
            os.remove(f"{chatid}.mp3")
        except Exception as e:
            await msg.reply(f"Translation error: {e}")
        finally:
            if os.path.exists(f"{chatid}.mp3"):
                os.remove(f"{chatid}.mp3")
        state.pop(chatid, None)
        return

if __name__ == "__main__":
    asyncio.run(bot.run())
