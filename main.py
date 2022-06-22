import telebot
import speech_recognition as sr
import os
import subprocess
import requests

token = ''

bot = telebot.TeleBot(token)

def audio_to_text(dest_name: str):
    r = sr.Recognizer()
    message = sr.AudioFile(dest_name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language="ru_RU")
    return result

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет!")

@bot.message_handler(content_types=["text"])
def first(message):
    bot.send_message(message.chat.id, "Текст")

@bot.message_handler(content_types=["audio"])
def second(message):
    bot.send_message(message.chat.id, "Аудио")

@bot.message_handler(content_types=["video"])
def third(message):
    bot.send_message(message.chat.id, "Видео")

@bot.message_handler(content_types=["photo"])
def fourth(message):
    bot.send_message(message.chat.id, "Фото")

@bot.message_handler(content_types=["document"])
def five(message):
    bot.send_message(message.chat.id, "Документ")

@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        path = file_info.file_path
        fname = os.path.basename(path)
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
        with open(fname+'.ogg', 'wb') as f:
            f.write(doc.content)
        process = subprocess.run(['ffmpeg', '-i', fname+'.ogg', fname+'.wav'])
        result = audio_to_text(fname+'.wav')
        bot.send_message(message.from_user.id, format(result))
    except sr.UnknownValueError:
        bot.send_message(message.from_user.id,  "Прошу прощения, но я не разобрал сообщение, или оно поустое...")
    except Exception:
        bot.send_message(message.from_user.id,  "Что-то пошло не так...")
    finally:
        os.remove(fname+'.wav')
        os.remove(fname+'.ogg')

bot.polling(none_stop=True)
