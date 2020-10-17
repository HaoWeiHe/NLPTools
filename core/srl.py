from practnlptools.tools import Annotator

class SRLTagger():
	def getInfo(self,stn):
		annotator =  Annotator()
		return annotator.getAnnotations(stn)['srl']

if __name__ == "__main__":
	SRLTagger().getInfo(stn)

