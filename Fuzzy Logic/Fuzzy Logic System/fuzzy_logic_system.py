'''
Fuzzy Logic System (Fuzzy Inference System / Fuzzy Rule Based System)
- Fuzzification module
- Inference engine <-> Knowledge Base
- Defuzzification module
'''
from inference_engine import *
from knowledge_base import *
from fuzzification import *
from defuzzification import *

class fls:

    def __init__(self):
        self.rules = rules()
        self.inputs = terms()
        self.outputs = terms()

    '''
    Fuzzification
    -------------
    Convert crisp input into fuzzy sets
    Convert into nested dictionary {'x': {'x1': 'A1', 'x2': 'A2'}}
    '''
    def fuzzify(self, input):
        self.fuzzified = fuzzify().fuzzify(self.inputs, input)

    '''
    Inference Engine
    ----------------
    For each rule: Take the min of multiple antecendent to get the consequent truth value
    Combine all rule: B' = max_min( h(A' intersect Aj) , B)
    '''
    def infer(self, input):
        self.fuzzify(input)
        inference_engine = engine(self.outputs, self.rules)
        self.infered = inference_engine.infer(self.fuzzified, input)
        return self.defuzzify()

    '''
    Defuzzification
    ---------------
    Convert fuzzy output into crisp output
    Convert nested dictionary into dictionary {'y':'B1'}
    '''
    def defuzzify(self):
        self.aggregated = defuzzify().aggregate_output(self.infered)
        return defuzzify().centroid(self.aggregated)

    def addinput(self, _name, _range):
        self.inputs.addterm(_name, _range)

    def addoutput(self, _name, _range):
        self.outputs.addterm(_name, _range)

    def input(self, i):
        return self.inputs.getterm(i-1)

    def output(self, i):
        return self.outputs.getterm(i-1)

    def addrule(self, input, output, weight=1, connection=1):
        self.rules.addrule(input, output, weight, connection)
