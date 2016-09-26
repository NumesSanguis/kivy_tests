    In main.py:
L131 tries with `self.kanji_result.data = self.search_database.retrieve(s_input, self.s_method)` to update `self.data` of class KanjiResult (L89) which is a RecycleView.
This class uses class ResultBlock (L78) to structure the data.
However even though self.data is updated, this is not reflected in RecycleView.

Do I miss some bind() so that Kivy calls the interface to update?
