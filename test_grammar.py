# -*- coding: utf-8 -*-
import pytest
from nltk.grammar import CFG
from nltk.parse.chart import BottomUpChartParser

with open("subject-verb.grammar") as f:
    grammar = CFG.fromstring(f.read(), encoding="utf-8")


@pytest.mark.parametrize("sentence_input", [
    "Je regarde la television",
    "Tu regardes la television",
    "Il regarde la television",
    "Nous regardons la television",
    "Vous regardez la television",
    "Ils regardent la television"])
def test_subject_verb_agreement(sentence_input):

    parser = BottomUpChartParser(grammar)

    trees = parser.parse(sentence_input.lower().split())
    assert(next(trees))


@pytest.mark.parametrize("sentence_input", [
    "le chat",
    "la television",
    "les chats",
    "les televisions",
    "Jackie",
    "Montreal"])
def test_noun_phrases_and_proper_names(sentence_input):

    parser = BottomUpChartParser(grammar)

    trees = parser.parse(sentence_input.lower().split())
    assert(next(trees))

#"Le chat mange le poisson",
