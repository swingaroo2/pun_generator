pun_generator
=============

Independent Natural Language Processing project that I worked on by myself in Python. I am fascinated with the myriad ways in which puns cleverly maneuver linguistic ambiguities and wanted to create a program that could generate puns with no runtime human interaction. My work was based on Kim Binstead's 1996 paper detailing the Joke Analysis and Production Engine. My program is driven by schemata, special data structures that find linguistic relationships between words from the linguistic database, WordNet, and generate keywords. These keywords are passed into template functions, which form the question and answer segments of puns. One such schema extracts noun phrases from WordNet, splits each noun phrase into its component words, finds a homophone and hypernym of the first and second word, respectively, and a meronym of the homophone. The homophone, meronym and hypernym are passed into a template function. This may produce a pun such as "What do you call a record with spinning? A whirled record." I plan to continue this project so that it can generate a more diverse array of puns. I may even re-implement it in Java and use it as part of an android app project.

Requires NLTK

FILES

relations.py

Contains helper functions to evaluate linguistic relationships between words
(i.e. if two words are homophones or synonyms)

templates.py

Contains helper functions to write the surface forms of puns

schemata.py

Contains the schema that generate different formats of puns
