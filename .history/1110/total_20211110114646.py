'''

【test.csv】
氏名,国語,算数,理科,社会
A,50,80,90,90
B,70,70,70,80
C,90,90,70,70
D,60,70,80,90


【実行結果】
> python total.py
A 310
B 290
C 320
D 300

'''

import csv
import pprint

with open('./test.csv') as f:
    print(f.read())



