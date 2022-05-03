import spacy

nlp = spacy.load("fi_core_news_lg")
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.model)  # 'rule'

doc = nlp("Lueskelin sanomalehteä.")
print([token.lemma_ for token in doc])
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
