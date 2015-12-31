import fnmatch
import os
import csv
import time
import datetime
import sys
from dbfread import DBF          # pip install dbfread

for infile in os.listdir('.'):
    if fnmatch.fnmatch(infile, '*.dbf'):
        outfile = infile[:-4] + ".csv"
        print("Converting " + infile + " to " + outfile + ". Each period represents 2,000 records.")
        counter = 0
        starttime=time.clock()
        with open(outfile, 'wb') as csvfile:
            table = DBF(infile)
            writer = csv.writer(csvfile)
            writer.writerow(table.field_names)
            for record in table:
                writer.writerow(list(record.values()))
                counter +=1
                if counter%100000==0:
                    sys.stdout.write('!' + '\r\n')
                    endtime=time.clock()
                    print str("{:,}".format(counter)) + " records in " + str(endtime-starttime) + " seconds."
                elif counter%2000==0:
                    sys.stdout.write('.')
                else:
                    pass
        print("")
        endtime=time.clock()
        print "Processed " + str("{:,}".format(counter)) + " records in " + str(endtime-starttime) + " seconds (" + str((endtime-starttime)/60) + " minutes.)"
        print str(counter / (endtime-starttime)) + " records per second."
        print("")