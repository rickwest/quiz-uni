# !/usr/bin/python
# -*- coding: utf-8 -*-

import copy


class QuestionCollection:
    pass


class QuestionBank(QuestionCollection):
    pass


class Question:
    def __init__(self, tags, points=10):
        self.__tags = tags
        self.__points = points

    def get_tags(self, ):
        return self.__tags

    def set_tags(self, tags):
        self.__tags = tags

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def make_clone(self):
        return copy.copy(self)




