import sys
import csv

jobs_csv = sys.argv[1]

with open(jobs_csv) as f:
    reader = csv.DictReader(f)
    for row in reader:
        if ('external' in row['is_external'].lower()
#            and 'internal' not in row['is_external'].lower()
            and row['deadline'] == '05/31/2012'):
            print row['job_id'], row['position']
