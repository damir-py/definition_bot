from loader import dp
from aiogram import types, F
from googletrans import Translator

from utils.get_eng_word import getNEGword

translator = Translator()


@dp.message(F.text)
async def definitionANDtranslation(message: types.Message):
    detected = translator.detect(message.text)
    lang = detected.lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.answer(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word = message.text
        else:
            word = translator.translate(message.text, dest='en').text
        lookup = getNEGword(word)
        if lookup:
            await message.reply(f"Definitions:\n{lookup['definition']}")
            await message.reply_voice(lookup['audio'])
        else:
            await message.reply("We couldn't find the word!")

