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

__version__ = '0.1.0'


# Structure for retrieved database data
class ResultBlock(BoxLayout):
    character = StringProperty('T')
    meanings = ListProperty([])


# Managing the RecycleView with Kanji data
class KanjiResult(RecycleView):
    # Search data
    #data = ListProperty()

    def __init__(self, **kwargs):
        super(KanjiResult, self).__init__(**kwargs)
        self.data = [{'character': '!', 'meanings': ['love', 'like']}, {'character': '@', 'meanings': ['su']}]


# Searches database with argument search method
class searchDatabase():
    def retrieve(self):
        # Just return simple data
        return([{'character': ':)', 'meanings': ['smile', 'like']}])


# Manages the general Kivy interface
class KanjiSearchScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(KanjiSearchScreen, self).__init__(**kwargs)
        self.kanji_result = self.ids.search_result
        self.search_database = searchDatabase()

    # Search database given input and method
    def callDatabaseSearch(self):
        self.kanji_result.data = self.search_database.retrieve()
        print(self.kanji_result.data)


class KanjiSearchApp(App):
    kanji_search_screen = ObjectProperty()

    def build(self):
        self.title = 'KanjiSearch'
        self.kanji_search_screen = KanjiSearchScreen()

        print("Current platform: {}".format(platform))
        if platform == 'win' or platform == 'linux':
            from kivy.core.window import Window
            Window.size = (500, 720)
            inspector.create_inspector(Window, self.kanji_search_screen)

        return(self.kanji_search_screen)


if __name__ == '__main__':
    KanjiSearchApp().run()
