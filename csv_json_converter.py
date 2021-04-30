## CSV to JASON CONVERTER
import json
import csv

with open("data/days_left.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"counties":[]}
    for row in reader:
        data["counties"].append(
            {"county":row[0],
            "vaccinated":row[1],
            "vacc_rate":row[2],
            "vacc_percent":row[3],
            "days_to_HIT": row[4],
            "population": row[5],
            "pc_uninsured": row[6],
            "pc_poverty": row[7],
            "pop_density": row[8]
        })
    
with open("counties.json", "w") as f:
    json.dump(data, f, indent =4)