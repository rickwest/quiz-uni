# !/usr/bin/python
# -*- coding: utf-8 -*-

from question.Question import Question


class AutoMarkedQuestion(Question):
    '''A Question that can be marked automatically'''
    pass


class Calculation(AutoMarkedQuestion):
    '''An Arithmetic Question'''
    pass


class ReorderQuestion(AutoMarkedQuestion):
    pass


class MaQuestion(AutoMarkedQuestion):
    '''Multiple answer question'''
    def __init__(self, question, answer, tags, points):
        self.details = None
        super().__init__(question, answer, tags, points)

    def get_num_correct_answers(self, ):
        pass


class McQuestion(MaQuestion):
    '''Multiple choice question '''
    pass


class TfQuestion(MaQuestion):
    '''True or False question '''
    pass