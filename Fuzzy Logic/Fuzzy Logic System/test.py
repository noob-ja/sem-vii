from fuzzy_logic_system import *
from inference_engine import *
from knowledge_base import *

a = fls()
a.addinput('weight', (50, 300))
a.input(1).addmf('light', 'trap', [25,50,100,150])
a.input(1).addmf('medium', 'trap', [100,150,200,250])
a.input(1).addmf('heavy', 'trap', [200,250,300,325])

a.addinput('temperature', (250, 400))
a.input(2).addmf('low', 'trap', [249,250,275,300])
a.input(2).addmf('medium', 'trap', [275,300,325,350])
a.input(2).addmf('high', 'trap', [325,350,400,401])

a.addoutput('time', (5, 17.5))
a.output(1).addmf('short', 'trap', [-1,5,7.5,10])
a.output(1).addmf('medium', 'trap', [7.5,10,12.5,15])
a.output(1).addmf('long', 'trap', [12.5,15,17.5,20])

a.addrule([1,0],[1])
a.addrule([2,1],[3])
a.addrule([2,2],[2])
a.addrule([2,3],[1])
a.addrule([3,1],[3])
a.addrule([3,0],[2])
a.addrule([0,1],[3])

print("Output: ", a.infer([220,250]))
