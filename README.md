# Coding challenge Apertium GSoC 2014


## Documentation

Documentation about this challenge is available [here](http://wiki.apertium.org/wiki/Ideas_for_Google_Summer_of_Code/Improving_support_for_non-standard_text_input).


## Tasks

### 1. Make a test corpus of non-standard texts



The corpus was created using the ``Twython`` Python library (``src/twitter.py`` module). The corpus has 100 different tweets written in English and is store in the ``resource/data_twitter.txt`` file.



### 2. Translate them with Apertium

All the tweets were translated to Spanish (``resource/data_translated.txt`` file).


### 3. Come up with examples of non-standard features that effect translation quality
- Spelling Mistakes: gurl (girl), smokin (smoking)
- Two words together: youand (you and), chestand (chest and)
- Abbreviation and Internet slang: u (you), tgthr (together)
- Missing apostrophe: wouldnt (wouldn't), dont (don't), Im (I'm) 


### 4. Propose ways in which they might be solved


- Spelling Mistakes: gurl (girl), smokin (smoking)
	- Using the Levenshtein distance and a dictionary (correct words) to find the minimum distance between the wrong word and one dictionary word.
- Two words together: youand (you and), chestand (chest and)
	- Split the word in two strings and verify iteratively if the two strings are contained in a dictionary (correct words).
- Abbreviation and Internet slang: u (you), tgthr (together)
	- Using a dictionary like [this](http://en.wiktionary.org/wiki/Appendix:English_internet_slang) or other bigger and map them to their meanings.

- Missing apostrophe: wouldnt (wouldn't), dont (don't), Im (I'm) 
	- Creating a list of commons apostrophe occurrences for these cases. However: shell (she'll or shell) has ambiguity. The Trigram Language Model can help to resolve the ambiguity. I think that there are few similar cases, but a deeper analysis can help better.

###  5. Program 1

The program (``src/candidates_generator.py`` module) produces candidates for strings
with repeated letters (>=3) and reduce them to 1/2 letters.

#### Usage:
``echo 'helllooo worrrddd!!!' | python candidates_generator.py``

#### Output:

- ^helllooo/helloo/hello/heloo/helo$
- ^worrrddd/worrdd/worrd/wordd/word$
- ^!!!/!!!$

#### Other examples:
- ^Nossssaaa/nossaa/nossa/nosaa/nosa$
- ^!!/!!$
- ^muito/muito$
- ^chique/chique$
- ^hein/hein$
- ^!!!!!/!!!!!$

### 6. Program 2

With all the candidates the Program 2 (``src/candidates_selector.py`` module) selects one candidate using a morphological dictionary. In addition to the English (**'en'**), I aggregate support for Spanish (**'es'**) and Portuguese (**'pt'**).

#### Usage:
``echo 'helllooo worrrddd!!!' | python candidates_generator.py | python candidates_selector.py 'en'``

#### Output:
- ^helllooo/hello$
- ^worrrddd/word$
- ^!!!/!!!$
- **hello word !!!**


#### Other examples:
- ^Orrriginnnal/original$
- ^!!!/!!!$
- ^houseeeeeeeeeeee/house$
- ^apertium/apertium$



