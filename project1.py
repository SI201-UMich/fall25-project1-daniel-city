# Daniel Sun
# 24075563
# danielws@umich.edu
# Collaborated with Micah Santow


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
    if len(d) == 0:
        return "Invalid Input. No Data Found."
    # for crop_variable in header:
    #     d[crop_variable] = {}
    #print(d)
    
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

def region_sunny_days(d):
    # count = 0
    # for value in d.values():
    #     if value[0] == "West":
    #         count +=1
    # print(count)
    region_sunny_days_dict = {}
    north_dict = {}
    south_dict = {}
    north_temp_count = 0
    north_count = 0
    north_sunny_count = 0
    south_temp_count = 0
    south_count = 0
    south_sunny_count = 0
    for value in d.values():
        if value[0] == "North":
            north_temp_count += float(value[4])
            north_count += 1
            if value[7] == "Sunny":
                north_sunny_count += 1
        if value[0] == "South":
            south_temp_count += float(value[4])
            south_count += 1
            if value[7] == "Sunny":
                south_sunny_count += 1
    north_avg_temp = north_temp_count / north_count
    south_avg_temp = south_temp_count / south_count
    north_sunny_proportion = north_sunny_count / north_count
    south_sunny_proportion = south_sunny_count / south_count
    
    region_sunny_days_dict["North"] = {"Average Temperature (Celsius)" : north_avg_temp, "Number of Sunny Days" : north_sunny_proportion}
    region_sunny_days_dict["South"] = {"Average Temperature (Celsius)" : south_avg_temp, "Number of Sunny Days" : south_sunny_proportion}
    print(region_sunny_days_dict)

        
    # return d

#def get_crop_results 

def harvest_irrigation(d):
    print(8/17)

class TestFunctions(unittest.TestCase):
    def SetUp(self):
        self.data = loadresults('test.csv')
    def test_region_sunny_days(self):
        self.assertEqual(region_sunny_days(self.data["North"]), {'Average Temperature (Celsius)': 25.648624717261, 'Number of Sunny Days': 0.5})
        self.assertEqual(region_sunny_days(self.data["South"]), {'Average Temperature (Celsius)': 26.032847771931, 'Number of Sunny Days': 0.6666666666666666})
        #Edge case 1: if the data set is empty
        self.assertEqual(region_sunny_days({}), "Invalid Input. No Data Found")
    def test_harvest_irrigation(self):
        self.assertEqual(harvest_irrigation(self.data), {'Proportion': 0.47058823529411764, 'Rainy': 7, 'Sunny': 6, 'Cloudy': 4})
        self.assertEqual(harvest_irrigation({}), "Invalid Input. No Data Found")

def main():
    #unittest.main(verbosity=2)
    loadresults('crop_yield.csv')
    load_results_dict = loadresults('crop_yield.csv')
    region_sunny_days(load_results_dict)
    harvest_irrigation(load_results_dict)


if __name__ == '__main__':
    main()

