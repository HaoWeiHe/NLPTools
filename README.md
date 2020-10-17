# Pipeline NLP

Pipeline NLP is a toolkit to demo the different between syntatic information and semantic information. See attachment pdf to get more information.

## Functionality
```
* SRL (Semantic Role Labeling)
* POS Tagging (Part of Speech Tagging) 
* Syntactic Parsing
```

## What's New

### 1.2

* Reorganize every single function to moudle 
* Added `pos.POSTagger` class to get the result of pos tagging. 
* Added `srl.SRLTagger` class to get the result of srl. 
* Added `syntax.SyntaxTree` class to get the result of syntax. 
* Remove  `stanfordcore` dependency. POS and Syntaxtree are performed using practNLPTools.
* Remove  `requirments.txt` file. 
* Remove  `demo.py` file. The functions in this file move to module - core.

### 1.1

* Added `pos` function.
* Added `ner` function.
* Added `srl` function.
* Added `syntax` function.


## Requirements

Pipleline NLp has been tested on Python 2.7.

### Python Dependencies

* [practNLPTools](https://github.com/biplab-iitb/practNLPTools)

## Basic Usages

Import module as first step

```
>>> from core import *
```

predict POS(part-of-speech) tagging from sentence:

```
>>> POSTagger.getInfo("how are you?")
[('how', 'WRB'), ('are', 'VBP'), ('you', 'PRP'), ('?', '.')]
```

predict SRL(semantic role labeling) from sentence:

```
>>> SRL_Tagger.getInfo("I ate an apple")
[{'A1': 'an apple', 'A0': 'I', 'V': 'ate'}]
>>> SRL_Tagger.getInfo("An apple was eaten by me")
[{'A1': 'An apple', 'A0': 'by me', 'V': 'eaten'}]
```


predict syntatic parsing tree from sentence:
```
>>> Syntax_Tree.getInfo("I ate an apple")
'(S1(S(NP(PRP I))(VP(VBD ate)(NP(DT an)(NN apple)))))'
>>> Syntax_Tree.getInfo("An apple was eaten by me")
'(S1(S(NP(DT An)(NN apple))(VP(VBD was)(VP(VBN eaten)(PP(IN by)(NP(PRP me)))))))'
```
