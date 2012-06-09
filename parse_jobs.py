import sys
import csv
import webbrowser
from collections import defaultdict
	
def get_max_lengths(csv_file):
	lengths = defaultdict(list)
	with open(jobs_csv) as f:
		reader = csv.DictReader(f)
		for row in reader:
			for k, v in row.iteritems():
				lengths[k].append(len(v))

	for k, v in lengths.iteritems():
		print k, max(v)
		
if __name__ =="__main__":
	jobs_csv = sys.argv[1]
	get_max_lengths(jobs_csv)
