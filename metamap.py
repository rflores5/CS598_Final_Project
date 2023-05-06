from pymetamap import MetaMap
import os
from time import sleep
import pandas as pd
import csv

metamap_base_dir = '/mnt/c/Users/Owner/metamap/public_mm/'
metamap_bin_dir = 'bin/metamap20'
metamap_pos_server_dir = 'bin/skrmedpostctl'
metamap_wsd_server_dir = 'bin/wsdserverctl'

#os.system(metamap_base_dir + metamap_pos_server_dir + ' start')
#os.system(metamap_base_dir + metamap_wsd_server_dir + ' start')

metam = MetaMap.get_instance(metamap_base_dir + metamap_bin_dir)


with open('symptoms.txt', 'w') as output:
	with open('top_50_notes.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			text = row['NOTE']
			lines = text.split("\n\n")
		
			cons, errs = metam.extract_concepts(lines, word_sense_disambiguation=True, restrict_to_sts=['sosy'], composite_phrase=0, prune=30)

			symptoms = [cc[3] for cc in cons]
			line = row['DIAG'] + "|" + "|".join(symptoms) + "\n"
			output.write(line)

#os.system(metamap_base_dir + metamap_pos_server_dir + ' stop')
#os.system(metamap_base_dir + metamap_wsd_server_dir + ' stop')
