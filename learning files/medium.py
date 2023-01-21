import spacy
import numpy as np
import requests

nlp = spacy.load("en_core_web_md")
with open ("ece216.txt", "r") as f:
    text = f.read()
doc = nlp(text)
sentence1 = list(doc.sents)[0]
# print(sentence1)

# Text comparision
# say i want to know how a word, homework, is similar to other words in our model
your_word = "homework"
ms = nlp.vocab.vectors.most_similar(np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
# print(words)

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
doc3 = nlp("The bruh bruh is in New York.")
# print(doc1 , "<->", doc2, doc1.similarity(doc3))

## Sentencizer example (adding a pipeline)
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")
nlp.analyze_pipes()

