import feedparser
import spacy
nlp = spacy.load("fi_core_news_lg")
lemmatizer = nlp.get_pipe("lemmatizer")
entity_dictionary = {}

def parse_feed():
    summaries = []
    NewsFeed = feedparser.parse("https://www.hs.fi/rss/ulkomaat.xml")
    for entry in NewsFeed.entries:
        summary = entry["summary"]
        summaries.append(summary)
    return summaries

def parse_doc(input_str):
    doc = nlp(str(input_str))
    #print([token.lemma_ for token in doc])
    #for token in doc:
    #    print(token.text, token.dep_, token.head.text, token.head.pos_,
    #    [child for child in token.children])
    parse_intent(doc)
    parse_entities(doc)
    #ents = [(e.text, e.label_, e.kb_id_) for e in doc.ents]
    #for ent in doc.ents:
    #    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    #    print(ent)

def parse_intent(doc):
    for token in doc:
        print(token.text, token.dep_, token.head.text, token.head.pos_,
        [child for child in token.children])

def parse_entities(doc):
    global entity_dictionary
    ents = [(e.text, e.label_, e.kb_id_) for e in doc.ents]
    for ent in ents:
        print(ent[0], ent[1], ent[2])
        entity_seen = entity_dictionary.get(ent[0])
        if entity_seen:
            entity_seen = entity_seen + 1
            entity_dictionary.update({ent[0]: entity_seen})
        else:
            entity_dictionary.update({ent[0]: 1})

def main():
    global entity_dictionary
    input_strings = parse_feed()
    for input_string in input_strings:
        parse_doc(input_string)
    print(entity_dictionary)

main()