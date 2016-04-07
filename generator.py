from grammarnode import GrammarNode

class Generator:
    def __init__(self, tokenTypeDict, startingTokenTypeName = "<start>"):
        self.tokenTypeDict = tokenTypeDict
        self.startingNode = GrammarNode(tokenTypeDict[startingTokenTypeName], tokenTypeDict[startingTokenTypeName].randomExample())


    def expandGrammarNodeOneLayer(self, grammarNode):
        if grammarNode.tokenType is None:
            #literal grammar node, don't expand
            return
        tokenType = grammarNode.tokenType
        splitExampleText = tokenType.randomExample().splitExampleText
        grammarNodeList = []
        for word in splitExampleText:
            if word[0] == "<" and word[-1] == ">":
                grammarNodeList.append(GrammarNode(self.tokenTypeDict[word]))
            else:
                #at a literal, make new leaf in the tree
                grammarNodeList.append(GrammarNode.literal(word))
        grammarNode.setExpandedGrammarNodeList(grammarNodeList)

    def expandAllTheWay(self, startingNode = None):
        if startingNode is None:
            startingNode = self.startingNode
        self.expandGrammarNodeOneLayer(startingNode)
        for node in startingNode.expandedGrammarNodeList:
            self.expandAllTheWay(startingNode = node)
        return startingNode

    @staticmethod
    def toString(fullyExpandedGrammarNode):
        if fullyExpandedGrammarNode.tokenType is None:
            literal = fullyExpandedGrammarNode.splitExampleText[0]
            if literal in ",.":
                return literal
            return " " + literal

        text = ""
        for node in fullyExpandedGrammarNode.expandedGrammarNodeList:
            text += Generator.toString(node)
        return text


