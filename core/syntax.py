from practnlptools.tools import Annotator

class SyntaxTree():
	def getInfo(self,stn):
		annotator =  Annotator()
		return annotator.getAnnotations(stn)["syntax_tree"]

if __name__ == "__main__":
	SyntaxTree().getInfo(stn)

