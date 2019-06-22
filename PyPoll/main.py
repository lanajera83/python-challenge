import os
import csv

bank_csv = os.path.join("../PyPoll", "election_data.csv")

votante = []
condado = []
voto = []
candidatos = []

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        votante.append(row[0])
        condado.append(row[1])
        voto.append(row[2])

def contar(list):
    contar = len(list)
    return contar

resultados1 = [[x,voto.count(x)] for x in set(voto)]
resultados2 = [[x,round(voto.count(x)/contar(votante)*100, 2)] for x in set(voto)]

def most_frequent(List):
    return max(set(List), key = List.count)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {contar(votante)}")
print("-------------------------")
print('Results:', *resultados1, sep='\n')
print("-------------------------")
print('Percentage:', *resultados2, sep='\n')
print("-------------------------")
print(f"The winner is: {most_frequent(voto)}")

output_file = os.path.join("election_data_final.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow("Election Results")
    writer.writerow("-------------------------")
    writer.writerow(f"Total Votes: {contar(votante)}")
    writer.writerow("-------------------------")
    writer.writerow(f"Results: {resultados1}")
    writer.writerow("-------------------------")
    writer.writerow(f"Results: {resultados2}")
    writer.writerow("-------------------------")
    writer.writerow(f"The winner is: {most_frequent(voto)}")
