
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.02, 0.06, 0.12, 1)

class PenaApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.status = Label(
            text="Hello Boss! Ami PENA ❤️",
            font_size="24sp"
        )

        button = Button(
            text="🎤 TALK TO PENA",
            font_size="22sp"
        )
        button.bind(on_press=self.talk)

        layout.add_widget(Label(text="PENA AI", font_size="36sp"))
        layout.add_widget(self.status)
        layout.add_widget(button)

        return layout

    def talk(self, instance):
        self.status.text = "PENA is getting ready..."

PenaApp().run()
