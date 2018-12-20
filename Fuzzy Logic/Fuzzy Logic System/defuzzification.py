import copy
from sympy import Symbol as symb
from sympy import integrate as intg
from sympy.solvers import solve

x = symb('x')
class defuzzify:

    def aggregate_output(self, outputs):
        output_ = {}
        for output in outputs:
            if output['deg'] > 0:
                if output['name'] in output_.keys() and output['deg'] > output_[output['name']]['deg']:
                    output_[output['name']] = output
                elif not output['name'] in output_.keys():
                    output_[output['name']] = output
        return output_

    def centroid(self, outputs):
        lines = []
        lines_ = []
        for name, output in outputs.items():
            r = copy.deepcopy(output['range'])
            for i in range(len(r)-1):
                if r[i] >= output['cutoff'][1]:
                    continue
                if r[i+1] >= output['cutoff'][1]:
                    r[i+1] = output['cutoff'][1]
                if r[i] <= output['cutoff'][0]:
                    r[i] = output['cutoff'][0]
                if r[i+1] <= output['cutoff'][0]:
                    continue
                if i == 1:
                    eqt = output['deg']
                    y1 = eqt
                    y2 = eqt
                elif i == 0:
                    y1 = 0
                    y2 = output['deg']
                    eqt = (y1-y2)/(r[i]-r[i+1]) * x + (y2*r[i+1]-y1*r[i+1])/(r[i]-r[i+1])
                else:
                    y1 = output['deg']
                    y2 = 0
                    eqt = (y1-y2)/(r[i]-r[i+1]) * x + (y2*r[i+1]-y1*r[i+1])/(r[i]-r[i+1])
                pair = {'range': [r[i], r[i+1]], 'eqt': eqt}
                lines.append(pair)
                lines_.append([(r[i], y1),(r[i+1], y2)])

        lines = sorted(lines, key=lambda x: x['range'])
        lines_ = sorted(lines_, key=lambda x: x[0][0] + x[1][0])

        for i in range(len(lines)):
            print(lines[i], lines_[i])

        lines__ = copy.deepcopy(lines)
        lines___ = []
        for i in range(len(lines_)):
            for j in range(i+1,len(lines_)):
                l1, l2 = lines_[i], lines_[j]
                if l1[1][0] <= l2[0][0] or l1[0][0] >= l2[1][0]:
                    # lines__.append(lines[i])
                    # lines__.append(lines[j])
                    continue
                else:
                    lines___.append(lines[i])
                    lines___.append(lines[j])

        for i in range(len(lines___)):
            print(lines___[i], 'asldjkdaslksajd')


        # lines__ = copy.deepcopy(lines)
        # for i in range(len(lines_)):
        #     for j in range(i+1,len(lines_)):
        #         l1, l2 = lines_[i], lines_[j]
        #         if l1[1][0] <= l2[0][0] or l1[0][0] >= l2[1][0]:
        #             continue
        #
        #         if l1[0][0] < l2[0][0] < l1[1][0]:
        #             lines__[i]['range'] = [lines[i]['range'][0], l2[0][0]]
        #         elif l2[0][0] < l1[1][0] < l2[1][0]:
        #             lines__[j]['range'] = [lines[i]['range'][1], l2[1][0]]
        #
        #         try:
        #             deg1 = lines[i]['eqt'].subs(x, lines[i]['range'][1])
        #         except:
        #             deg1 = lines[i]['eqt']
        #         try:
        #             deg2 = lines[j]['eqt'].subs(x, lines[j]['range'][0])
        #         except:
        #             deg2 = lines[j]['eqt']
        #
        #         if deg1 > deg2:
        #             lines__[j]['eqt'] = lines__[i]['eqt']
        #         # if l1[0][1] > l2[0][1] and l1[1][1] > l2[1][1]:
        #         #     lines__[j]['eqt'] = lines__[i]['eqt']
        #         # p = self.line_intersection(lines_[i], lines_[j])
        #         # if l1[0][0] < p[0] < l1[1][0] and l2[0][0] < p[0] < l2[1][0]:
        #         #     print('intersect')
        #         #     print(l1,l2,p)
        #         #     print(lines__[i],lines__[j])
        #         #     lines__[i]['range'] = [lines[i]['range'][0], p[0]]
        #         #     lines__[j]['range'] = [p[0], lines[j]['range'][1]]
        #         #     print(lines__[i],lines__[j])
        #         #     print('intersect')
        #         # else:
        #         #     print('no intersect')
        #         #     print(l1,l2,p)
        #         #     print('no intersect')
        #         #     if l1[0][0] < l2[0][0] < l1[1][0]:
        #         #         lines__[i]['range'] = [lines[i]['range'][0], l2[0][0]]
        #         #     elif l2[0][0] < l1[1][0] < l2[1][0]:
        #         #         lines__[j]['range'] = [lines[i]['range'][1], l2[1][0]]
        #         #     if l1[0][1] > l2[0][1] and l1[1][1] > l2[1][1]:
        #         #         lines__[j]['eqt'] = lines__[i]['eqt']

        lines = lines__

        cxx = 0
        cx = 0
        for pair in lines:
            print(pair, 'intg')
            r = pair['range']
            eqt = pair['eqt']
            cxx_ = intg(eqt*x,(x, r[0], r[1]))
            cx_ = intg(eqt,(x, r[0], r[1]))
            cxx += cxx_
            cx += cx_
        return cxx/cx if abs(cx)>0 else 0

    def line_intersection(self, line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
