import sys
import csv

with open(sys.argv[1], 'r') as original:
    pipe = csv.reader(original, delimiter='|')

    with open(sys.argv[2], 'w') as new:
        comma = csv.writer(new, delimiter=',')

        for line in pipe:
            print(line)
            comma.writerow(line)
            print(line)



