# -*- coding: utf-8 -*-
# Creator: SurafuSoft
# Run programma with Python >3 (because unicode encoding in Python 2.7)

import sqlalchemy as sqla
import sqlalchemy.ext.declarative as sqld

sqla_base = sqld.declarative_base()


class tableKanji(sqla_base):
    __tablename__ = 'Kanji'

    id = sqla.Column(sqla.Integer, primary_key=True)
    character = sqla.Column(sqla.String)
    radical = sqla.Column(sqla.Integer)
    heisig6 = sqla.Column(sqla.Integer, unique=True, nullable=True)
    kanjiorigin = sqla.Column(sqla.Integer, unique=True, nullable=True)
    # jlpt = sqla.Column(sqla.Integer)
    # freq = sqla.Column(sqla.Integer)
    # grade = sqla.Column(sqla.Integer)
    # stroke_count = sqla.Column(sqla.Integer)
    cjk = sqla.Column(sqla.String, unique=True, nullable=True)

    def __repr__(self):
        return("<Kanji(id='%s', character='%s', radical='%s', heisig6='%s', kanjiOrigin='%s, cjk='%s')>" %
               (self.id, self.character, self.radical, self.heisig6, self.kanjiorigin, self.cjk))

    # TODO relationship() (if id is deleted, all related objects deleted as well)


class tableMisc(sqla_base):
    __tablename__ = 'Misc'

    kanji_id = sqla.Column(sqla.Integer, sqla.ForeignKey('Kanji.id'), primary_key=True)
    jlpt = sqla.Column(sqla.Integer)
    freq = sqla.Column(sqla.Integer)
    grade = sqla.Column(sqla.Integer)
    stroke_count = sqla.Column(sqla.Integer)

    def __repr__(self):
        return("<Kanji(kanji_id='%s', jlpt='%s', freq='%s', grade='%s', stroke_count='%s')>" %
               (self.kanji_id, self.jlpt, self.freq, self.grade, self.stroke_count))


class tableMeaningEN(sqla_base):
    __tablename__ = 'MeaningEN'

    kanji_id = sqla.Column(sqla.Integer, sqla.ForeignKey('Kanji.id'), primary_key=True)
    meaning = sqla.Column(sqla.String, primary_key=True)

    #__table_args__ = (sqla.UniqueConstraint('kanji_id', 'meaning', name='_kanji_meaning_uc'),)


class tableOriginKanji(sqla_base):
    __tablename__ = 'OriginKanji'

    kanji_id = sqla.Column(sqla.Integer, sqla.ForeignKey('Kanji.id'), primary_key=True)
    okanji_id = sqla.Column(sqla.Integer, sqla.ForeignKey('Kanji.id'), primary_key=True)
    order = sqla.Column(sqla.Integer)