class kb:
    def __init__(self):
        self.rules = []
        self.aux_verb = ['is', 'am', 'are']

    def add_rule(self, string):
        newrule = dict()
        idx = 0
        while len(string)>0:
            idx = string.find(' ')
            if(idx < 0):
                print(string)
                break
            else:
                print(string[:idx])
                string = string[idx+1:]

    def find_pair(self, strarr):
        return False

string = "hello hello test test"

b = kb()
b.add_rule(string)
