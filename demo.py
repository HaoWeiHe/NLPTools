import os
import sys

from practnlptools.tools import Annotator

if __name__ == "__main__":

	stn = sys.argv[2]
	annotator = Annotator()

	if sys.argv[1] == "pos":
		print(annotator.getAnnotations(stn)['pos'])
		

	if sys.argv[1] == "srl":
		
		print(annotator.getAnnotations(stn)['srl'])
	
	if sys.argv[1] == "ner":
		print(annotator.getAnnotations(stn)['ner'])

	if sys.argv[1] == "parser":
		print(annotator.getAnnotations(stn))

	if sys.argv[1] == "dependency":

		print(annotator.getAnnotations(stn,dep_parse=True))
