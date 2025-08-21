import csv
with open("python_intermedio\\archivos\\datos.csv") as archivos:
    reader = csv.reader(archivos)
    for row in reader:
        print(row)