from generator import Generator
from reader import Reader

reader = Reader()
tokenTypeDict = reader.readGrammarFile("grammars/Kant.g")
generator = Generator(tokenTypeDict)
expandedNode = generator.expandAllTheWay(generator.startingNode)
print Generator.toString(expandedNode)
print " "
print "done"