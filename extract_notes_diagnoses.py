from pyhealth.datasets import MIMIC3Dataset
import csv

counts = {}
Adm_diag = {}
with open('DIAGNOSES_ICD.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		seq = row['SEQ_NUM']
		if seq == "1":
			diag = row['ICD9_CODE'][:3]
			Adm_diag[row['HADM_ID']] = diag
			if diag in counts:
				counts[diag]+=1
			else:
				counts[diag] = 1


sorted_diag = sorted(counts.items(), key=lambda x:x[1])	
top_50_diag = sorted_diag[-50:]
top_100_diag = sorted_diag[-100:]

top_50_list = [x[0] for x in top_50_diag]
top_100_list = [y[0] for y in top_100_diag]
print(top_50_list)
print(top_100_list)


with open('filtered_notes.csv', 'w', newline='') as output:
	with open('NOTEEVENTS.csv', mode='r', newline='') as input:
		reader2 = csv.DictReader(input)
		fieldnames = ['DIAG','NOTE']
		writer = csv.DictWriter(output, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader2:
			if "Discharge summary" in row['CATEGORY'] and row['HADM_ID'] in Adm_diag:
				diag = Adm_diag[row['HADM_ID']]
				note = row['TEXT']
				writer.writerow({'DIAG':diag, 'NOTE':note})


count = 0
with open('top_50_notes.csv', 'w', newline='') as output:
	with open('filtered_notes.csv', mode='r', newline='') as input:
		reader2 = csv.DictReader(input)
		fieldnames = ['DIAG','NOTE']
		writer = csv.DictWriter(output, fieldnames=fieldnames)
		writer.writeheader()
		for row in reader2:
			if row['DIAG'] in top_50_list:
				count += 1
				diag = row['DIAG']
				note = row['NOTE']
				writer.writerow({'DIAG':diag, 'NOTE':note})
print(count)
