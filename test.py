import spacy

nlp={}    
for lang in ["en", "es", "pt", "ru"]: # Fill in the languages you want, hopefully they are supported by spacy.
    if lang == "en":
        nlp[lang]=spacy.load(lang + '_core_web_lg')
    else: 
        nlp[lang]=spacy.load(lang + '_core_news_lg')

def entites(text, lang):
     result_list = []
     try:
         nlp2 =nlp[lang]
     except KeyError:
         return Exception(lang + " model is not loaded")
     doc = nlp2(text)
     for entity in doc.ents:
       res = {
           entity.label_: entity.text
       }
       result_list.append(res)
     return result_list

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

entity_result = entites(text, "en")
print("entity_result)
