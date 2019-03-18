# Twitterphrases
Generate optimal phrases for doing Twitter tracking for smaller languages.

# Requirements
Currently, the language identification relies on a 176-class [FastText language model](https://fasttext.cc/blog/2017/10/02/blog-post.html) (and in effect the fastText package for python3) which can be found [here](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

The format that is assumed of your data input and output is [JSON lines](http://jsonlines.org/), which essentially means a json object can be read on each line to do lazy loading at steps where it is required.

# Example
A basic example of generating optimal precision phrases for Dutch is included in main.py. The link to the FastText blogpost lists possible iso language codes for generating twitterphrases for other languages. 

Keyword sets for Dutch can also directly be downloaded from here: [Precision](https://www.clips.uantwerpen.be/twitter/phrases/precision), [Recall](https://www.clips.uantwerpen.be/twitter/phrases/recall). 

