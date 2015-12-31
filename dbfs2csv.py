import fnmatch
import os
import csv
import time
import datetime
import sys
from dbfread import DBF, FieldParser, InvalidValue          # pip install dbfread

class MyFieldParser(FieldParser):
    def parse(self, field, data):
        try:
            return FieldParser.parse(self, field, data)
        except ValueError:
            return InvalidValue(data)

            
debugmode=0         # Set to 1 to catch all the errors.            

for infile in os.listdir('.'):
    if fnmatch.fnmatch(infile, '*.dbf'):
        outfile = infile[:-4] + ".csv"
        print("Converting " + infile + " to " + outfile + ". Each period represents 2,000 records.")
        counter = 0
        starttime=time.clock()
        with open(outfile, 'wb') as csvfile:
            table = DBF(infile, parserclass=MyFieldParser)
            writer = csv.writer(csvfile)
            writer.writerow(table.field_names)
            for i, record in enumerate(table):
                for name, value in record.items():
                    if isinstance(value, InvalidValue):
                        if debugmode == 1:
                            print('records[{}][{!r}] == {!r}'.format(i, name, value))
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