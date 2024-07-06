import spacy

nlp = spacy.load("en_core_web_sm")
text = ("Your account for the SmarTeam system was modified as requested in IDM request 10848501")
print(text)

doc = nlp(text)
print(doc)

for tokens in doc:
    print(token)

for tokens in doc:
    if tokens.pos == 'NOUN':
        print(tokens)