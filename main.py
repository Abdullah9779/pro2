from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AppApp(MDApp):
    def build(self):
        return MDLabel(text="Hellow Abdullah", halign="center", font_style="H1")


AppApp().run()
