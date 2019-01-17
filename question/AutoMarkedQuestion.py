# !/usr/bin/python
# -*- coding: utf-8 -*-

from question.Question import Question


class AutoMarkedQuestion(Question):
    '''A Question that can be marked automatically'''
    pass


class Calculation(AutoMarkedQuestion):
    pass


class ReorderQuestion(AutoMarkedQuestion):
    pass


class MaQuestion(AutoMarkedQuestion):
    def __init__(self):
        self.details = None

    def get_num_correct_answers(self, ):
        pass


class McQuestion(MaQuestion):
    pass


class TfQuestion(MaQuestion):
    pass