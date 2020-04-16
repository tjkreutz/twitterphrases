# Twitterphrases
Generate optimal phrases for tapping the [Twitter Streaming API](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) .

# Requirements
Currently, the language identification relies on a 176-class [FastText language model](https://fasttext.cc/blog/2017/10/02/blog-post.html) (and in effect the fastText package for python3) which can be found [here](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin).

The format that is assumed of your data input and output is [JSON lines](http://jsonlines.org/), which essentially means a json object can be read on each line to do lazy loading at steps where it is required.

# Example
A basic example of generating optimal precision phrases for Dutch is included in main.py. The link to the FastText blogpost lists possible iso language codes for generating twitterphrases for other languages. 

# Cite
The optimal key phrase lists for the 50 most common languages on Twitter can also be directly downloaded via the links in the below performance table. The table also lists expected performance when using the list for a particular language. Please cite the following paper:

[Kreutz,  T.  and Daelemans,  W.  (2019).  How  to Optimize your Twitter Collection. Computational Linguistics in the Netherlands Journal, 9:55–66.](https://clinjournal.org/clinj/article/download/92/83)

# Results

| Language | ISO (link) | Precision | Bound Recall | F-score |
| -------- | ---------- | --------- | ------------ | ------- |
| English | [en](https://www.clips.uantwerpen.be/twitter/phrases/en.txt) | 40.21% | 1.81% | 3.46% | 
| Japanese | [ja](https://www.clips.uantwerpen.be/twitter/phrases/ja.txt) | 65.82% | 2.96% | 5.66% | 
| Spanish | [es](https://www.clips.uantwerpen.be/twitter/phrases/es.txt) | 24.40% | 2.18% | 4.01% | 
| Arabic | [ar](https://www.clips.uantwerpen.be/twitter/phrases/ar.txt) | 80.03% | 6.07% | 11.28% | 
| Portuguese | [pt](https://www.clips.uantwerpen.be/twitter/phrases/pt.txt) | 89.36% | 8.80% | 16.03% | 
| Korean | [ko](https://www.clips.uantwerpen.be/twitter/phrases/ko.txt) | 97.73% | 10.95% | 19.70% | 
| Thai | [th](https://www.clips.uantwerpen.be/twitter/phrases/th.txt) | 86.80% | 11.20% | 19.83% | 
| Turkish | [tr](https://www.clips.uantwerpen.be/twitter/phrases/tr.txt) | 94.64% | 20.13% | 33.19% | 
| French | [fr](https://www.clips.uantwerpen.be/twitter/phrases/fr.txt) | 95.65% | 22.28% | 36.15% | 
| Chinese | [zh](https://www.clips.uantwerpen.be/twitter/phrases/zh.txt) | 29.98% | 3.64% | 6.50% | 
| German | [de](https://www.clips.uantwerpen.be/twitter/phrases/de.txt) | 91.44% | 34.05% | 49.62% | 
| Indonesian | [id](https://www.clips.uantwerpen.be/twitter/phrases/id.txt) | 94.51% | 39.04% | 55.25% | 
| Russian | [ru](https://www.clips.uantwerpen.be/twitter/phrases/ru.txt) | 99.26% | 56.17% | 71.74% | 
| Italian | [it](https://www.clips.uantwerpen.be/twitter/phrases/it.txt) | 93.75% | 48.48% | 63.91% | 
| Telugu | [tl](https://www.clips.uantwerpen.be/twitter/phrases/tl.txt) | 96.84% | 81.02% | 88.23% | 
| Catalan | [ca](https://www.clips.uantwerpen.be/twitter/phrases/ca.txt) | 97.74% | 68.35% | 80.44% | 
| Hindi | [hi](https://www.clips.uantwerpen.be/twitter/phrases/hi.txt) | 99.63% | 97.86% | 98.74% | 
| Polish | [pl](https://www.clips.uantwerpen.be/twitter/phrases/pl.txt) | 98.87% | 59.60% | 74.37% | 
| Dutch | [nl](https://www.clips.uantwerpen.be/twitter/phrases/nl.txt) | 98.25% | 66.12% | 79.04% | 
| Persian | [fa](https://www.clips.uantwerpen.be/twitter/phrases/fa.txt) | 99.36% | 59.14% | 74.15% | 
| Malaysian | [ms](https://www.clips.uantwerpen.be/twitter/phrases/ms.txt) | 93.45% | 58.05% | 71.62% | 
| Egyptian Ar. | [arz](https://www.clips.uantwerpen.be/twitter/phrases/arz.txt) | 99.78% | 54.77% | 70.73% | 
| Urdu | [ur](https://www.clips.uantwerpen.be/twitter/phrases/ur.txt) | 99.54% | 87.52% | 93.15% | 
| Greek | [el](https://www.clips.uantwerpen.be/twitter/phrases/el.txt) | 99.69% | 82.69% | 90.39% | 
| Esperanto | [eo](https://www.clips.uantwerpen.be/twitter/phrases/eo.txt) | 81.03% | 8.47% | 15.33% | 
| Finnish | [fi](https://www.clips.uantwerpen.be/twitter/phrases/fi.txt) | 92.08% | 27.70% | 42.59% | 
| Swedish | [sv](https://www.clips.uantwerpen.be/twitter/phrases/sv.txt) | 97.42% | 63.76% | 77.07% | 
| Bulgarian | [bg](https://www.clips.uantwerpen.be/twitter/phrases/bg.txt) | 94.47% | 72.51% | 82.04% | 
| Tamil | [ta](https://www.clips.uantwerpen.be/twitter/phrases/ta.txt) | 99.80% | 79.79% | 88.68% | 
| Ukranian | [uk](https://www.clips.uantwerpen.be/twitter/phrases/uk.txt) | 94.62% | 44.33% | 60.38% | 
| Hungarian | [hu](https://www.clips.uantwerpen.be/twitter/phrases/hu.txt) | 88.78% | 25.06% | 39.09% | 
| Serbian | [sr](https://www.clips.uantwerpen.be/twitter/phrases/sr.txt) | 93.14% | 58.11% | 71.57% | 
| Galician | [gl](https://www.clips.uantwerpen.be/twitter/phrases/gl.txt) | 49.28% | 8.67% | 14.75% | 
| Cebuano | [ceb](https://www.clips.uantwerpen.be/twitter/phrases/ceb.txt) | 89.63% | 57.10% | 69.76% | 
| Czech | [cs](https://www.clips.uantwerpen.be/twitter/phrases/cs.txt) | 98.06% | 43.64% | 60.40% | 
| Vietnamese | [vi](https://www.clips.uantwerpen.be/twitter/phrases/vi.txt) | 96.06% | 76.45% | 85.14% | 
| Kurdish | [ckb](https://www.clips.uantwerpen.be/twitter/phrases/ckb.txt) | 99.51% | 36.72% | 53.64% | 
| Norwegian | [no](https://www.clips.uantwerpen.be/twitter/phrases/no.txt) | 96.05% | 51.92% | 67.41% | 
| Danish | [da](https://www.clips.uantwerpen.be/twitter/phrases/da.txt) | 97.14% | 56.03% | 71.07% | 
| Romanian | [ro](https://www.clips.uantwerpen.be/twitter/phrases/ro.txt) | 95.59% | 52.53% | 67.80% | 
| Hebrew | [he](https://www.clips.uantwerpen.be/twitter/phrases/he.txt) | 99.95% | 77.91% | 87.56% | 
| Nepali | [ne](https://www.clips.uantwerpen.be/twitter/phrases/ne.txt) | 99.32% | 88.09% | 93.37% | 
| Bengali | [bn](https://www.clips.uantwerpen.be/twitter/phrases/bn.txt) | 99.94% | 69.82% | 82.21% | 
| Macedonian | [mk](https://www.clips.uantwerpen.be/twitter/phrases/mk.txt) | 99.01% | 62.42% | 76.57% | 
| Mongolian | [mn](https://www.clips.uantwerpen.be/twitter/phrases/mn.txt) | 99.83% | 81.35% | 89.65% | 
| Azerbaijani | [az](https://www.clips.uantwerpen.be/twitter/phrases/az.txt) | 96.97% | 33.98% | 50.32% | 
| Marathi | [mr](https://www.clips.uantwerpen.be/twitter/phrases/mr.txt) | 97.87% | 68.31% | 80.46% | 
| Gujarati | [gu](https://www.clips.uantwerpen.be/twitter/phrases/gu.txt) | 99.60% | 80.15% | 88.82% | 
| Albanian | [sq](https://www.clips.uantwerpen.be/twitter/phrases/sq.txt) | 98.18% | 64.01% | 77.50% | 
| Kannada | [kn](https://www.clips.uantwerpen.be/twitter/phrases/kn.txt) | 98.72% | 60.61% | 75.11% | 


