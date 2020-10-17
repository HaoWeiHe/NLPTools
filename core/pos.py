from practnlptools.tools import Annotator
class POSTagger():
	def getInfo(self,stn):
		annotator =  Annotator()
		return annotator.getAnnotations(stn)['pos']

if __name__ == "__main__":
	POSTagger().getInfo(stn)

