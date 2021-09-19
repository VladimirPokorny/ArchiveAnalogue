import os
import pandas as pd

xls = pd.ExcelFile('FotoArchivNegativu.xlsx')
df = pd.read_excel(xls, dtype=str)

#print(df)
#print(len(df.columns))

with open('header.txt', 'r', encoding='utf8') as file :
    header = file.read()

main = ''

for i in range(len(df.index)):
    with open('body.txt', 'r', encoding='utf8') as file:
        body = file.read()
    for name, values in df.iteritems():
        print('{name}: {value}'.format(name=name, value=values[i]))
        body = body.replace('<<' + name + '>>', str(values[i]))
    main = main + body
    

filedata = header + main + '\n \end{document}'

with open('file.txt', 'w', encoding='utf8') as file:
    file.write(filedata)

print(filedata)

os.system('pdflatex file.txt')

# for i in range(len(df.index)):
#     for name, values in df.iteritems():
        #print('{name}: {value}'.format(name=name, value=values[i]))


