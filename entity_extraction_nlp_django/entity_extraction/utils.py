import spacy
from spacy import displacy
from collections import Counter
from pprint import pprint


import en_core_web_sm
nlp = en_core_web_sm.load()
nlp_keyword = spacy.load("en_core_sci_lg")


def naturalLP(doc):

    doc = nlp(doc)

    dick = [(X.text, X.label_) for X in doc.ents]

    html = displacy.render(doc,page=True, style='ent')

    # print(type(displacy.render(doc, page=True, style='ent')))
    # print(html)
    return html


def naturalLPlist(doc):

    doc = nlp(doc)

    dick = [(X.text, X.label_) for X in doc.ents]

    # html = displacy.render(nlp(doc), jupyter=True, style='ent')

    return dick

def keyextract(doc):

    doc = nlp_keyword(doc)

    return doc.ents