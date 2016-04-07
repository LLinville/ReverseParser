class GrammarNode:
    def __init__(self, tokenType, splitExampleText = None):
        self.tokenType = tokenType
        self.splitExampleText = splitExampleText
        self.expandedGrammarNodeList = []

    @staticmethod
    def literal(textValue):
        return GrammarNode(None, splitExampleText = [textValue])

    def setExpandedGrammarNodeList(self, eGNL):
        self.expandedGrammarNodeList = eGNL
