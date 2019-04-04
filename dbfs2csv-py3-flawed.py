from dbfread import DBF, FieldParser, InvalidValue          # pip install -r requirements.txt
from tqdm import tqdm

import glob
import csv
import time
import datetime
import sys


class MyFieldParser(FieldParser):
    def parse(self, field, data):
        try:
            return(FieldParser.parse(self, field, data))
        except ValueError:
            return(InvalidValue(data))


debugmode = True         # Set to True to report errors. Set to False, to, er, not.

filestobeprocessed = glob.glob("*.dbf")
for filecounter, infile in enumerate(filestobeprocessed):
    print(f"Processing file {filecounter + 1}/{len(filestobeprocessed)}: {infile}")
    outfile = infile[:-4] + ".csv"
    with open(outfile, 'w', newline='') as csvfile:
        table = DBF(infile, parserclass=MyFieldParser)
        writer = csv.writer(csvfile)
        writer.writerow(table.field_names)
        for i, record in tqdm(enumerate(table)):
            for name, value in record.items():
                if isinstance(value, InvalidValue):
                    if debugmode:
                        print('records[{}][{!r}] == {!r}'.format(i, name, value))
            writer.writerow(list(record.values()))
