from grammarnode import GrammarNode

class Generator:
    def __init__(self, tokenTypeDict, startingTokenTypeName = "<start>"):
        self.tokenTypeDict = tokenTypeDict
        self.startingNode = GrammarNode(tokenTypeDict[startingTokenTypeName], tokenTypeDict[startingTokenTypeName].randomExample())