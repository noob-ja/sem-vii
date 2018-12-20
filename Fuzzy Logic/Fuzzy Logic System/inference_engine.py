import copy
from sympy import Symbol as symb
from sympy import integrate as intg

class engine:
    def __init__(self, outputs, rules):
        self.outputs = outputs
        self.rules = rules

    def calcRange(self, term, i, deg):
        result = []
        mf = copy.deepcopy(term.getmf(i))
        if deg == 1:
            pass
        elif deg == 0:
            mf['range'] = [0,0,0,0]
        else:
            r = mf['range']
            if mf['type'] == 'trap':
                r1 = deg * (r[1]-r[0]) + r[0]
                r2 = deg * (r[2]-r[3]) + r[3]
                mf['range'] = [r[0],r1,r2,r[3]]
            elif mf['type'] == 'tri':
                r1 = deg * (r[1]-r[0]) + r[0]
                r2 = deg * (r[1]-r[2]) + r[2]
                mf['range'] = [r[0],r1,r2,r[2]]
        mf['deg'] = deg
        mf['cutoff'] = [term.min, term.max]
        result.append(mf)
        return result


    def infer(self, inputs, input):
        outputs = []
        results = []
        for rule in self.rules.getrule():
            input_ = rule['input']
            result = 1
            for i in range(len(input_)):
                select = input_[i]-1
                if select < 0:  continue
                deg = inputs[i][select]['deg']
                if result>deg:
                    result = deg
            output_ = rule['output']
            for i in range(len(output_)):
                select = output_[i]-1
                output = self.outputs.getterm(i)
                outputs += self.calcRange(output, select, result)
        return outputs
