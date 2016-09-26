#!/usr/bin/kivy
# -*- coding: utf-8 -*-
# Creator: SurafuSoft

from kivy.app import App
from kivy import platform
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.modules import inspector
# import sqlalchemy as sqla
# import sqlalchemy.orm as sqlo
# import tableclass as tc

__version__ = '0.1.0'

from kivy.core.text import LabelBase

# Set font that supports Japanese Kanji
KIVY_FONTS = [
    {
        "name": "MeiryoUI",
        "fn_regular": "meiryo.ttc",
        "fn_italic": "meiryo.ttc",
    }
]

for font in KIVY_FONTS:
    LabelBase.register(**font)

Clipboard = None
#CutBuffer = None


# Introduces on_double_tap function for label to copy Kanji to clipboard
class TouchLabel(Label):
    def __init__(self, **kwargs):
        self._touch_count = 0
        super(TouchLabel, self).__init__(**kwargs)
        self.register_event_type('on_double_tap')

        if platform == 'linux':
            self._ensure_clipboard()

    # Necessary for Linux
    def _ensure_clipboard(self):
        global Clipboard  # , CutBuffer
        if not Clipboard:
            from kivy.core.clipboard import Clipboard  # CutBuffer

    # Receives touch info when Widget is touched, then check if it is a double tap
    def on_touch_down(self, touch):
        #print("hello")
        if self.disabled:
            return

        touch_pos = touch.pos
        if not self.collide_point(*touch_pos):
            return False
        if super(TouchLabel, self).on_touch_down(touch):
            return True

        touch.grab(self)
        self._touch_count += 1
        if touch.is_double_tap:
            self.dispatch('on_double_tap')

    # Copy data to clipboard
    def on_double_tap(self, *args):
        Clipboard.copy(self.text)  # <-- How do I do this the correct way?
        print("Copied :D")


# Structure for retrieved database data
class ResultBlock(BoxLayout):
    character = StringProperty('T')
    meanings = ListProperty([])
    origins = ListProperty([])

    # Currently doesn't do anything, because on_double_tap: Clipboard.copy(self.text) doesn't exist for Label
    def tapCopy(self):
        print("tap")


# Managing the RecycleView with Kanji data
class KanjiResult(RecycleView):
    # Search data
    #data = ListProperty()

    def __init__(self, **kwargs):
        super(KanjiResult, self).__init__(**kwargs)
        self.data = [{'character': '愛', 'meanings': ['love', 'like']}, {'character': 'ス', 'meanings': ['su']}]  # [ResultBlock()] {'text': str(x)} for x in range(5)


# Searches database with argument search method
class searchDatabase():
    # def __init__(self):
    #     self.db_name = "sqlite:///Kanji_story.db"
    #     self.engine = sqla.create_engine(self.db_name, echo=True)
    #
    #     # Bind the engine to the metadata of the Base class so that the
    #     # declaratives can be accessed through a DBSession instance
    #     tc.sqla_base.metadata.bind = self.engine

    def retrieve(self, s_input, s_method):
        print("Retrieving results with input: {} and method: {}".format(s_input, s_method))

        return([{'character': ':)', 'meanings': ['smile', 'like']}])


# Manages the general Kivy interface
class KanjiSearchScreen(BoxLayout):
    s_method = StringProperty('')
    def __init__(self, **kwargs):
        super(KanjiSearchScreen, self).__init__(**kwargs)
        self.s_method = 'Kanji'
        self.kanji_result = KanjiResult()
        self.search_database = searchDatabase()

    # How should the database be searched
    def setSearchMethod(self, method):
        self.s_method = method
        print(self.s_method)

    # Search database given input and method
    def callDatabaseSearch(self):
        s_input = ':)'
        self.kanji_result.data = self.search_database.retrieve(s_input, self.s_method)
        print(self.kanji_result.data)


class KanjiSearchApp(App):
    kanji_search_screen = ObjectProperty()

    def build(self):
        self.title = 'KanjiSearch'
        self.db = "Kanji_story.db"

        self.kanji_search_screen = KanjiSearchScreen()

        print("Current platform: {}".format(platform))
        if platform == 'win' or platform == 'linux':
            from kivy.core.window import Window
            Window.size = (500, 720)
            inspector.create_inspector(Window, self.kanji_search_screen)

        return(self.kanji_search_screen)

    def on_pause(self):
        # Background persistence support for Android/iOS.
        return(True)


if __name__ == '__main__':
    KanjiSearchApp().run()
