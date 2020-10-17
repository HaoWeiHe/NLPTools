# Pipeline NLP

Pipeline NLP is a toolkit to demo the different between syntatic information and semantic information.

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
