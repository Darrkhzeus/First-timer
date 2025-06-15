
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Football Manager RPG', font_size=32))
        self.options = [
            'View Squad', 'Transfers', 'Tactics', 'Training',
            'Match Day', 'FA Cup', 'Youth Academy', 'Save', 'Exit'
        ]
        for opt in self.options:
            btn = Button(text=opt, size_hint=(1, 0.15))
            btn.bind(on_press=self.handle_action)
            layout.add_widget(btn)
        self.add_widget(layout)

    def handle_action(self, instance):
        title = instance.text
        if title == 'Exit':
            App.get_running_app().stop()
        else:
            content = Label(text=f"Action: {title}\n\nFeature coming soon!", font_size=18)
            popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
            popup.open()

class ManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main'))
        return sm

if __name__ == '__main__':
    ManagerApp().run()
