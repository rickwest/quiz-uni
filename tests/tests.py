import unittest
from question.Question import Question


class QuestionTest(unittest.TestCase):
    """A set of tests for the Question class"""

    def testStringInputToListMethod(self):
        """Test that this static method takes a string, splits on a comma and returns a list,
        also making sure remove any empty strings from the list"""

        # assert that passing an empty string returns an empty list
        self.assertListEqual(Question.stringInputToList(''), [])

        # assert that empty strings are removed from list.
        # we want to ensure that if two commas are together (,,) the resulting empty string is removed from the list
        s = 'math,add,subtract,,divide'
        self.assertListEqual(Question.stringInputToList(s), ['math', 'add', 'subtract', 'divide'])

        # assert that any trailing or leading whitespace is stripped
        s = '   apple,banana   , pear, melon,     ,,     strawberry   ,'
        self.assertListEqual(Question.stringInputToList(s), ['apple', 'banana', 'pear', 'melon', 'strawberry'])


if __name__ == '__main__':
    unittest.main()
