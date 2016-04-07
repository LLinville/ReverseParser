from tokentype import TokenType
from tokenexample import TokenExample

class Reader:

    def __init__(self, nodeTypeDict = None, reservedTokenTypeNames = None):
        if nodeTypeDict is None:
            #dictionary of the pairs tokenName:TokenType
            self.nodeTypeDict = {
                "<space>":TokenType("<space>", examples = [TokenExample("<space>",[" "])]),
                "<empty>":TokenType("<empty>", examples = [TokenExample("<empty>",[" "])]),
                "<newline>":TokenType("<newline>", examples = [TokenExample("<newline>",["\n"])])
            }

        if reservedTokenTypeNames is None:
            self.reservedTokenTypeNames = ["<space>","<empty>","<newline>"]

    def parseExampleLine(self, line, tokenTypeName):
        splitLine = line[:].split()
        if splitLine == []:
            return
        if splitLine[-1] == ";":
            #default weight
            tokenExample = TokenExample(tokenTypeName, splitLine[:-1][:])
        else:
            #weight was specified
            tokenExample = TokenExample(tokenTypeName, splitLine[:-2][:], int(splitLine[-1]))

        self.nodeTypeDict[tokenTypeName].addExample(tokenExample)


    def parseDefinitionBody(self, file):
        line = file.readline().strip()
        while line.strip().startswith("//") or line == "\n":
            line = file.readline()
        tokenTypeName = line.strip()
        if tokenTypeName in self.reservedTokenTypeNames:
            print "Error: Tried to rewrite reserved token type: " + tokenTypeName
        if tokenTypeName[:7] == "<number":
            print "Error: Tried to define <number #-#> token"

        if tokenTypeName not in self.nodeTypeDict.keys():
            self.nodeTypeDict[tokenTypeName] = TokenType(tokenTypeName)
            #print "created key for "+tokenTypeName+": "+str(self.nodeTypeDict[tokenTypeName])

        line = file.readline()
        while True:
            line = line.strip()
            if line == "}":
                break
            if line[:2] == "//":
                line = file.readline()
                continue
            self.parseExampleLine(line, tokenTypeName)
            line = file.readline()

    def parseFileBody(self, file):
        line = file.readline().strip()
        while line:
            if line.strip() == "{":
                self.parseDefinitionBody(file)
            line = file.readline()

    def readGrammarFile(self, filename):
        file = open(filename, "r")

        self.parseFileBody(file)

        file.close()

        return self.nodeTypeDict

# tdict = {}
# tdict["noun"] = TokenType("noun")
# tdict["noun"].addExample(TokenExample("noun",["word1"]))
# nounToken = TokenType("noun")
# nounToken.addExample(TokenExample("noun",["a","dog"]))
# verbToken = TokenType("verb")
# for example in verbToken.getExamples():
#     print example.splitExampleText