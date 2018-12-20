class rules:
    def __init__(self):
        self.rules = []

    def addrule(self, input, output, weight=1, connection=1):
        rule = {'input': input, 'output': output, 'weight': weight, 'connection': connection}
        self.rules.append(rule)

    def getrule(self, i=-1):
        if i<0:                 return self.rules
        elif i<len(self.rules): return self.rules[i]
        else:                   return []

class terms:
    def __init__(self):
        self.terms = []

    def addterm(self, _name, _range):
        self.terms.append(term(_name, _range))

    def getterm(self, i=-1):
        if i<0:                 return self.terms
        elif i<len(self.terms): return self.terms[i]
        else:                   return []

class term:
    def __init__(self, _name, _range):
        self.name = _name
        (self.min, self.max) = _range
        self.mf = []

    def addmf(self, _name, _type, _range):
        mf = {'name': _name, 'type': _type, 'range': _range}
        self.mf.append(mf)

    def getmf(self, _mf=-1):
        if _mf<0:                           return self.mf
        elif _mf in range(len(self.mf)):    return self.mf[_mf]
        else:                               return []
