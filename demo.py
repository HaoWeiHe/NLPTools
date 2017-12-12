import os
import sys
from nltk.tokenize import StanfordTokenizer
from nltk.tag import StanfordNERTagger
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from nltk import Tree
from nltk.parse.stanford import StanfordDependencyParser


#Segmentation  
def tokenizer(stn):
	tokenizer = StanfordTokenizer()
	return tokenizer.tokenize(stn)

#POS parser
def pos(stn):
	eng_tagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
	return eng_tagger.tag(stn)


#NER 
def NER(stn):
	eng_tagger = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
	return(eng_tagger.tag(stn))

#syntactic anlysis
def parser(stn):
	eng_parser = StanfordParser()
	res = list(eng_parser.parse(stn))
	
	# draw syntactic tree
	res[0].draw()
	return(res)

#Depependency tree
def dependency(stn):
	eng_parser = StanfordDependencyParser()
	res = list(eng_parser.parse(stn))
	for row in res[0].triples():
	    print(row)


if __name__ == "__main__":
	
	os.environ["CLASSPATH"] = os.getcwd()+"/StanfordNLP/jars"
	os.environ["STANFORD_MODELS"] = os.getcwd()+"/StanfordNLP/models"
	# stn = "That U.S.A. poster-print costs $12.40..."
	stn = sys.argv[2]

	if sys.argv[1] == "tokenizer":
		print(tokenizer(stn))

	# if sys.argv[1] == "pos":
	# 	print(pos(tokenizer(stn)))


	# if sys.argv[1] == "ner":
	# 	print(NER(tokenizer(stn)))

	if sys.argv[1] == "parser":
		print(parser(tokenizer(stn)))

	if sys.argv[1] == "dependency":
		dependency(tokenizer(stn))
