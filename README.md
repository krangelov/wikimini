This repository contains a subset of WordNet needed for the current experiments with NLG for Wikidata. The running demo is available here:

[https://cloud.grammaticalframework.org/wikidata/index.wsgi](https://cloud.grammaticalframework.org/wikidata/index.wsgi)

The web page tries to immitate the actual Wikipedia UI and works in a similar way. In the edit box in the upper right corner, you can search for countries, cities and people and you will see the corresponding article. The current focus is on countries but a bit of work is also done for cities and people. You can also search for "list of sovereign states" and you will get an article which lists all countries. This is useful if you want to check all country articles one by one or if you want to see if the names of all countries are correct.

When you are on a particular article you can click on the "Edit" tab. This lets you to see the abstract syntax trees that are used in the current document. In addition when you click on a word in the text, you can see in which sense the word was used as well as its linearization in the selected languages. You can add more than one language by using the checkboxes in the left-side bar.

If you login on the web page, you will also be able to actually edit the lexicon online. In this case the grammar will be updated dynamically. Currently, however, you still need to click on refresh to update the current document. The list of changes that you made are also collected on the server. To actually commit them to GitHub, click "commit". For the login to work you need to be added to the WordNet repository. Mail me your github account and I will add you.

If you prefer to edit the grammars locally on your computer then you can use the files in this repository. After you did your changes you will have to tell me to update and recompile the grammars on the server. This means that I will patch the WordNet grammar with your changes and I will recompile the grammar on the server. Note that each recompilation takes about an hour, so don't expect things to happen fast. On the other hand the web interface gives you immediate feedback.

Known Issues:

1. The article always use the pronoun "it" for country but this will change later.


Krasimir
