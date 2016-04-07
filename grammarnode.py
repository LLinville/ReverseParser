class GrammarNode:
    def __init__(self, tokenType, splitExampleText):
        self.tokenType = tokenType
        self.splitExampleText = splitExampleText

    @staticmethod
    def literal(textValue):
        return GrammarNode(None, [textValue])