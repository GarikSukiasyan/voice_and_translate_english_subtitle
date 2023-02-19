from translate import Translator
import pyttsx3
import pytesseract as pt
from PIL import Image
import pyautogui
import keyboard

def voice_text():
    print('Start')

    # Делаем скриншот
    pyautogui.screenshot('screenshot.png')

    # Указываем путь к компьютерному зрению
    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Указываем путь к скриншоту
    img_object = Image.open(r"screenshot.png")

    # Собираем текст с картинки
    img_text = pt.image_to_string(img_object)

    print("Text: " +str(img_text))

    # Переводим текст с английского на русский
    translator = Translator(from_lang="en",to_lang="ru")
    translation = translator.translate(img_text)

    print("Текст: " + str(translation))

    engine = pyttsx3.init()  # Инициализируем
    engine.say(translation)  # Передаем текст
    engine.runAndWait()  # Озвучиваем

    print('End')


# При нажатии Ctrl + t озвучить текст
keyboard.add_hotkey('Ctrl + t', lambda: voice_text())

# При нажатии Ctrl + q выти
keyboard.add_hotkey('Ctrl + q', lambda: exit())

keyboard.wait('Ctrl + Q')