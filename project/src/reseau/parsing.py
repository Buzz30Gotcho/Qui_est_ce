from jeu.src.Phrase import Phrase
from jeu.src.Not import Not
from jeu.src.Or import Or
from jeu.src.And import And

def parse_phrase(d:dict) :
    return Phrase(d["content"]["attribut"], d["content"]["valeur"])

def parse_Not(d:dict):
    une_phraseComplexe_not = Not()
    une_phraseComplexe_not.add_question(parse_question(d["content"]["0"]))
    return une_phraseComplexe_not

def parse_Or(d:dict):
    une_phraseComplexe_or = Or()
    une_phraseComplexe_or.add_question(parse_question(d["content"]["0"]))
    une_phraseComplexe_or.add_question(parse_question(d["content"]["1"]))
    return une_phraseComplexe_or

def parse_And(d:dict):
    une_phraseComplexe_and = And()
    une_phraseComplexe_and.add_question(parse_question(d["content"]["0"]))
    une_phraseComplexe_and.add_question(parse_question(d["content"]["1"]))
    return une_phraseComplexe_and

def parse_question(message:dict):
    q = None
    
    
    typee = message["type"]
    content = message["content"]
    
    
    if typee == "Phrase":
        q = parse_phrase(message)
    elif typee == "Not":
        q = parse_Not(message)
    elif typee == "Or":
        q = parse_Or(content)
    elif typee == "And":
        q = parse_And(content)
        
    
    return q

def parse_reponse(reponse:dict) -> str:
    return reponse["reponse"].__str__()