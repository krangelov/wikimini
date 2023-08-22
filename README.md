# WikiMini: a grammar for text generation from Wikidata

By Krasimir Angelov et al. 2023

## The running demo

This repository contains a subset of WordNet needed for the current experiments with NLG for Wikidata. The running demo is available here:

[https://cloud.grammaticalframework.org/wikidata/index.wsgi](https://cloud.grammaticalframework.org/wikidata/index.wsgi)

The web page tries to immitate the actual Wikipedia UI and works in a similar way. In the edit box in the upper right corner, you can search for countries, cities and people and you will see the corresponding article. The current focus is on countries but a bit of work is also done for cities and people. You can also search for "list of sovereign states" and you will get an article which lists all countries. This is useful if you want to check all country articles one by one or if you want to see if the names of all countries are correct.

When you are on a particular article you can click on the "Edit" tab. This lets you see the abstract syntax trees that are used in the current document. In addition when you click on a word in the text, you can see in which sense the word was used as well as its linearization in the selected languages. You can add more than one language by using the checkboxes in the left-side bar.

A slide deck explaining the architecture can be found in

[https://docs.google.com/presentation/d/1HLXph0zTLMt8Jzlqf6cXW2kPbQ-xM3HHtzwaasXAqn4/edit#slide=id.p]

## Editing on the web

If you login on the web page, you will also be able to actually edit the lexicon online. In this case the grammar will be updated dynamically. Currently, however, you still need to click on refresh to update the current document. The list of changes that you made are also collected on the server. To actually commit them to GitHub, click "commit". For the login to work you need to be added to the WordNet repository. Mail me your github account and I will add you.

If you prefer to edit the grammars locally on your computer then you can use the files in this repository. After you did your changes you will have to tell me to update and recompile the grammars on the server. This means that I will patch the WordNet grammar with your changes and I will recompile the grammar on the server. Note that each recompilation takes about an hour, so don't expect things to happen fast. On the other hand the web interface gives you immediate feedback.


## Editing the grammars

If you are a GF programmer, you can edit the grammars in this repository.
They are divided into two modules:

- `Mini`, containing the lexicon, mostly place names but also content words with GF-WordNet identifiers.
- `Wiki`, inheriting the lexicon and adding the part of RGL syntax that is needed in the articles that are covered.

With these grammars, you can test generation in the GF shell with the following ways:

- `rf -file=data/new_trees.txt -lines -tree | l -bind`: a minimum set of sentences covering all syntactic functions and non-name content words
- `rf -file=data/all_trees.txt -lines -tree | l -bind`: a complete set of sentences covering all articles about countries

When you are done with your edits, they will be (with some delay) integrated in the bigger grammar in the running demo.

Here is the workflow more precisely:

1. Fork WikiMini (this repository)
2. Inform everyone what languages you work on (e.g. by email to gf-dev; a better forum coming soon)
3. Test your language with provided treebanks, as explained above
3. Correct errors in lexical linearizations
4. Report on errors in syntactic constructions and idiomacy in an attached document issues/<your-language>.md
5. Make a pull request to integrate your work in the system
6. Participate as a co-author of a great publication (to be started at the GF Summer School in August)



## Known Issues

1. The article always use the pronoun "it" for country but this will change later.
2. Read issues/ on different languages

