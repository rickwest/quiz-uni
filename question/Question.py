# !/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import random


class QuestionCollection:
    """A wrapper around a dictionary of Questions"""

    def __init__(self):
        self.__questions = {}

    @property
    def questions(self):
        return list(self.__questions.values())

    def add(self, question):
        if not question in self.__questions.values():
            self.__questions[question.ident] = question
            return True
        return False

    def __str__(self):
        for question in self.__questions:
            return question

    def __len__(self):
        return len(self.__questions)


class QuestionBank(QuestionCollection):
        """badly implemented Singleton to create ONE list of questions to be used in the tests
    	    'static' methods used to populate the stock, which is an instance of BookCollection"""
        __instance = None

        @classmethod
        def getInstance(cls):
            if not cls.__instance:
                cls.__instance = QuestionBank()
                cls.__instance.__bank = QuestionCollection()
            return cls.__instance


class Question:
    __identifiers = []

    def __init__(self, question, answer, tags=['1'], points=10, ident=''):
        self.__question = question
        self.__answer = answer
        self.__tags = tags
        self.__points = points

        if ident:
            self._ident = ident
        else:
            ident = random.randint(1000, 9999)
            while ident in type(self).__identifiers:
                ident = random.randint(1000, 9999)
            type(self).__identifiers += [ident]
            self._ident = "question" + str(ident)

    @property
    def ident(self):
        return self._ident

    def get_tags(self):
        return self.__tags

    def set_tags(self, tags):
        self.__tags = tags

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def make_clone(self):
        return copy.copy(self)


