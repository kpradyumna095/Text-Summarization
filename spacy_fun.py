# NLP
import spacy
import pandas as pd
nlp = spacy.load("en_core_web_lg")
from spacy import displacy

# function to capture all token_type with token in dataframe 
def token_type(data):
    text = []
    label = []
    for ent in data.ents:
        text.append(ent.text)
        label.append(ent.label_)

    df = pd.DataFrame()
    df['text'] = text
    df['label'] = label
    
    return df

def view_entity(data):
	
	xy = displacy.render(nlp(data),style='ent',jupyter=False)
	return xy

# funciton to capture specific token_type
def text_label(label, dfrm):
	text_label_li = []
	for i in range(len(dfrm['label'])):
		if dfrm['label'][i] == label.upper():
			text_label_li.append(dfrm['text'][i])
	return text_label_li


# capturing all entity type tokens and number of tokens
def task_opt_org(data):
	doc = nlp(data[0:500])
	dfrm = token_type(doc)
	rel = set(text_label('org', dfrm))
	l_rel = len(rel)
	return rel, l_rel

def task_opt_name(data):
	doc = nlp(data)
	dfrm = token_type(doc)
	rel = set(text_label('Person', dfrm))
	l_rel = len(rel)
	return rel, l_rel

def task_opt_place(data):
	doc = nlp(data)
	dfrm = token_type(doc)
	rel = set(text_label('GPE', dfrm))
	l_rel = len(rel)
	return rel, l_rel

def task_opt_law(data):
	doc = nlp(data)
	dfrm = token_type(doc)
	rel = set(text_label('LAW', dfrm))
	l_rel = len(rel)
	return rel, l_rel


def task_opt_quantity(data):
	doc = nlp(data)
	dfrm = token_type(doc)
	rel = set(text_label('quantity', dfrm))
	l_rel = len(rel)
	return rel, l_rel

def task_opt_product(data):
	doc = nlp(data)
	dfrm = token_type(doc)
	rel = set(text_label('product', dfrm))
	l_rel = len(rel)
	return rel, l_rel
