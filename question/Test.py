from question.Question import QuestionCollection


class Test(QuestionCollection):
    def __init__(self):
        self.currentDate = None
        self.currentClass = None
        self.results = None
        self.runBy = None
        self.history = None

    def getCurrentDate(self, ):
        pass

    def setCurrentDate(self, value):
        pass

    def getCurrentClass(self, ):
        pass

    def setCurrentClass(self, value):
        pass

    def getResults(self, ):
        pass

    def setResults(self, value):
        pass

    def getRunBy(self, ):
        pass

    def setRunBy(self, value):
        pass

    def getHistory(self, ):
        pass

    def setHistory(self, value):
        pass


class TestHistory:
    def __init__(self):
        self.usedBy = None
        self.previousResults = None

