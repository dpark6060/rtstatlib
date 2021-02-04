from rtstatlib.messages import oneoff, verbs, adverbs, nouns, adjectives
import random
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

def sync_log(a=None):
    
    message = ""
    
    prob = random.random()
    
    if prob <= 0.2:
    
        message = random.choice(oneoff)
    
    else:
        prob = random.random()
        
        if prob <= 0.1:
            message += random.choice(adverbs) + " "
        
        adj1 = random.choice(adjectives)
        message += random.choice(verbs) + " " + adj1 + " "
        
        prob = random.random()
        
        if prob <= 0.2:
            
            adj2 = random.choice(adjectives)
            while adj1 == adj2:
                adj2 = random.choice(adjectives)
                
            message += adj2 + " "
        
        message += random.choice(nouns)

    log.info(message)
    print(message)