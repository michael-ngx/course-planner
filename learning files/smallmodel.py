import spacy
nlp = spacy.load("en_core_web_sm")

with open("ece216.txt","r") as f:
    text = f.read()

doc = nlp(text)

# for token in doc[:10]:
    # print (token)

# for sents in doc.sents:     # We must do list(doc.sents) in order to index the sentences
#     print (sents)

# text = "Mike enjoys playing football."
# doc2 = nlp(text)
# for token in doc2:
#     print(token.text, token.pos_, token.dep_)

# from spacy import displacy
# displacy.render(doc2, style="dep")

for ent in doc.ents:
    print(ent.text, ent.label_)