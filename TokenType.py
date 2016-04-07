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
        totalAdjustedWeight = 0
        for example in self.examples:
            if example.weight == 0:
                totalAdjustedWeight += 1
            else:
                totalAdjustedWeight += example.weight
        averageWeight = totalAdjustedWeight * 1.0 / len(self.examples)
        target = random.randrange(0,totalAdjustedWeight)
        weightSoFar = 0
        for example in self.examples:
            if example.weight == 0:
                weightSoFar += averageWeight
            else:
                weightSoFar += example.weight
            if weightSoFar > target:
                return example