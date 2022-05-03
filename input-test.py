import feedparser
import spacy
nlp = spacy.load("fi_core_news_lg")
lemmatizer = nlp.get_pipe("lemmatizer")

def parse_feed():
    summaries = []
    NewsFeed = feedparser.parse("https://www.hs.fi/rss/ulkomaat.xml")
    for entry in NewsFeed.entries:
        summary = entry["summary"]
        print(summary)
        summaries.append(summary)
    return summaries

def parse_doc(input_str):
    doc = nlp(str(input_str))
    #print([token.lemma_ for token in doc])
    #for token in doc:
    #    print(token.text, token.dep_, token.head.text, token.head.pos_,
    #    [child for child in token.children])
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        print(ent)

def main():
    input_strings = parse_feed()
    for input_string in input_strings:
        parse_doc(input_string)

main()