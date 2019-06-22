import os
import csv
bank_csv = os.path.join("../PyBank", "budget_data.csv")

meses = []
money = []
money_change = []

with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        meses.append(row[0])
        dinero = float(row[1])
        money.append(dinero)

    for i in range(1,len(money)):
        money_change.append(money[i] - money[i-1])
        avg_change = sum(money_change)/len(money_change)
        max_change = max(money_change)
        min_change =min(money_change)

def contar(list):
    contar = len(list)
    return contar

def sumar(list):
    sumar = sum(list)
    return sumar

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {contar(meses)}")
print(f"Total $: {sumar(money)}")
print(f"Average  Change: $ {avg_change}")
print(f"Greatest Increase in Profits: $ {max_change}")
print(f"Greatest Decrease in Profits: $ {min_change}")

output_file = os.path.join("budget_data_final.txt")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {contar(meses)}"])
    writer.writerow([f"Total $: {sumar(money)}"])
    writer.writerow([f"Average  Change: $ {avg_change}"])
    writer.writerow([f"Greatest Increase in Profits: $ {max_change}"])
    writer.writerow([f"Greatest Decrease in Profits: $ {min_change}"])
