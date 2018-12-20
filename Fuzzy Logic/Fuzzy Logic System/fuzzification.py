class fuzzify:
    def calcMembership(self, mf, input):
        r = mf['range']
        if r[0] < input < r[len(r)-1]:
            if mf['type'] == 'trap':
                if r[0] < input < r[1]:
                    return (input-r[0])/(r[1]-r[0])
                elif r[1] <= input <= r[2]:
                    return 1
                else:
                    return (r[3]-input)/(r[3]-r[2])
            if mf['type'] == 'tri':
                if r[0] < input < r[1]:
                    return (input-r[0])/(r[1]-r[0])
                else:
                    return (r[2]-input)/(r[2]-r[1])
        return 0

    def calcTerm(self, term, input):
        result = []
        for mf in term.getmf():
            mf['deg'] = self.calcMembership(mf, input)
            result.append(mf)
        return result

    def fuzzify(self, inputs, input):
        inputs_ = []
        for i in range(len(input)):
            inputs_.append(self.calcTerm(inputs.getterm(i), input[i]))
        return inputs_
