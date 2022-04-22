
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pywhatkit
import re
from googlesearch import search
import webbrowser

import wikipedia

def answer_finder(que):
    que1=que+"filetype:pdf"
    for i in search(que1, tld="co.in", num=5, stop=10, pause=2):
        if (re.search("pdf", i)):
            webbrowser.open(i)
        else:
            print("match not found")
def text_to_handrwitten(title):
    info = wikipedia.summary(title, 4)
    pywhatkit.text_to_handwriting(info, 'converted.png')
    from PIL import Image
    im = Image.open("converted.png")
    im.show()

class main(App):

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source="logo2.png"))

        self.greeting = Label(text="STUDENTBAE", font_size=28, color='#FAA0A0')
        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 0.4))
        self.window.add_widget(self.user)

        self.button = Button(text="HAND WRITTEN", size_hint=(0.4, 0.3), bold=True, background_color='#FAA0A0')

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        self.button = Button(text="NOTES", size_hint=(0.4, 0.3), bold=True, background_color='#FAA0A0')

        self.button.bind(on_press=self.callback2)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = text_to_handrwitten(self.user.text)
        print("callback:-", text_to_handrwitten(self.user.text))

    def callback2(self, instance):
        self.greeting.text = answer_finder(self.user.text)
        print("callback:-", answer_finder(self.user.text))


if __name__ == "__main__":
    main().run()



