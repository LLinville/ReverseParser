from generator import Generator
from reader import Reader

reader = Reader()
tokenTypeDict = reader.readGrammarFile("FileFormat.g")
generator = Generator(tokenTypeDict)
expandedNode = generator.expandAllTheWay(generator.startingNode)
print "done"