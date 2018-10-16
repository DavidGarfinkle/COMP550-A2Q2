# -*- coding: utf-8 -*-
import pytest
from nltk.grammar import CFG
from nltk.parse.chart import BottomUpChartParser

with open("subject-verb.grammar") as f:
    grammar = CFG.fromstring(f.read(), encoding="utf-8")

tests = {
        "subject_verb_agreement": [
            "Je regarde la television",
            "Tu regardes la television",
            "Il regarde la television",
            "Nous regardons la television",
            "Vous regardez la television",
            "Ils regardent la television"],

        "test_noun_phrases_and_proper_names": [
            "le chat",
            "la television",
            "les chats",
            "les televisions",
            "Jackie",
            "Montreal"],

        "test_direct_object_pronouns": [ "il la regarde" ],

        "test_attribute_adjectives": [
            "le chat noir",
            "le chat heureux",
            "le beau chat",
            "le joli chat",
            "la derniere semaine",
            "la semaine derniere",
            "les chats noirs",
            "la television noire",
            "les televisions noires"]}


@pytest.mark.parametrize("test", ((test_name, sentence) for test_name, sentences in tests.items() for sentence in sentences))
def test(test):
    test_name, sentence = test

    parser = BottomUpChartParser(grammar)

    trees = parser.parse(sentence.lower().split())
    assert(next(trees))


@pytest.mark.parametrize("sentence_input", [
    "je mangent le poisson",
    "les noirs chats mangent le poisson",
    "la poisson mangent les chats",
    "je mange les"])
def test_rejection_set(sentence_input):

    parser = BottomUpChartParser(grammar)

    trees = parser.parse(sentence_input.lower().split())
    pytest.raises(StopIteration)
