import os
import pandas as pd

xls = pd.ExcelFile('FotoArchivNegativu.xlsx')
df = pd.read_excel(xls, dtype=str)

#print(df)
#print(len(df.columns))

with open('header.txt.txt', 'r', encoding='utf8') as file :
    filedata = file.read()

for i in range(len(df.index)):
    with open('body.txt.txt', 'r', encoding='utf8') as file:
        file = file.read()
    for name, values in df.iteritems():
        print('{name}: {value}'.format(name=name, value=values[i]))
        filedata = filedata.replace('<<' + name + '>>', str(values[0]))



for name, values in df.iteritems():
    print('{name}: {value}'.format(name=name, value=values[0]))
    filedata = filedata.replace('<<' + name + '>>', str(values[0]))

#print(filedata)

with open('file.txt', 'w', encoding='utf8') as file:
    file.write(filedata)

os.system('pdflatex file.txt')

# for i in range(len(df.index)):
#     for name, values in df.iteritems():
        #print('{name}: {value}'.format(name=name, value=values[i]))


