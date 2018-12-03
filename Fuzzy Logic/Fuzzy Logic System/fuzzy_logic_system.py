'''
Fuzzy Logic System (Fuzzy Inference System / Fuzzy Rule Based System)
- Fuzzification module
- Inference engine <-> Knowledge Base
- Defuzzification module
'''

class fls:

    rules = {}

    '''
    Fuzzification
    -------------
    Convert crisp input into fuzzy sets
    Convert into nested dictionary {'x': {'x1': 'A1', 'x2': 'A2'}}
    '''
    def fuzzify(self):
        return False

    '''
    Inference Engine
    ----------------
    For each rule: Take the min of multiple antecendent to get the consequent truth value
    Combine all rule: B' = max_min( h(A' intersect Aj) , B)
    '''
    def infer(self):
        return False

    '''
    Defuzzification
    ---------------
    Convert fuzzy output into crisp output
    Convert nested dictionary into dictionary {'y':'B1'}
    '''
    def defuzzify(self):
        return False

    '''
    Knowledge Base
    --------------
    Rules of the system
    Store using dictionary {'x': {'x1':'A1'}}
    Return dictionary {'y': 'B1'}
    '''
    def kb(self):
        return False
