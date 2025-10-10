import unittest
import os
import csv

def loadresults(f):
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    
    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = list(r)

    header = rows[0]
    
    d = {}

    for i in range(len(rows[1:])):
        d[i+1] = rows[i+1]
    # for crop_variable in header:
    #     d[crop_variable] = {}
    print(d)
    
    # for row in rows[1:]:
    #     region = row[0]
    #     for i, crop_variable in enumerate(header):
    #         d[crop_variable][region] = row[i+1]

    # for row in rows[1:]:
    #     for i, crop_variable in enumerate(header):
    #         d[crop_variable][i] = row[i+1]

    # for row in d:
    #     d[i]
    #print(d)


    return d


#def get_crop_results


def main():
    #unittest.main(verbosity=2)
    loadresults('crop_yield.csv')

if __name__ == '__main__':
    main()

