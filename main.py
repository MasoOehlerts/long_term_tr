from googletrans import Translator 

words = input("Enter your text here!")

translator = Translator()
text_translate = words
translated_text = translator.translate(text_translate, dest='en')
print(translated_text.text)