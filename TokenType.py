import random
class TokenType:
    def __init__(self, type, examples = None):
        self.type = type
        if examples is None:
            self.examples = []

    def getExamples(self):
        return self.examples

    def addExample(self, tokenExample):
        self.examples.append(tokenExample)

    def randomExample(self):
        totalWeight = sum([example.weight for example in self.examples])
        target = random.randrange(0,totalWeight)
        weightSoFar = 0
        for example in self.examples:
            weightSoFar += example.weight
            if weightSoFar > target:
                return example