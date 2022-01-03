# csv reader - writer παράδειγμα
import csv
vouna = [['Όλυμπος',	2917,	'Θεσσαλία'],
        ['Σμόλικας',	2637,	'Ήπειρος'],
        [ 'Βόρας',	2524,	'Μακεδονία']]

for v in vouna:
         print(v)
print('...writing')
with open('vouna.csv', 'wt', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for v in vouna:
        writer.writerow(v)

print('...reading')
with open('vouna.csv', 'rt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
