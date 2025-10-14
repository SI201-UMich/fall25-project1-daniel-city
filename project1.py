# Daniel Sun
# 24075563
# danielws@umich.edu
# Collaborated with Micah Santow. I also went to Office Hours.
# Used AI to help debug my code, specifically to address AttributeError: 'float' object has no attribute 'values'


import unittest
import os
import csv

def loadresults(f):
    
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    
    with open(full_path) as fh:
        r = csv.reader(fh)
        rows = list(r)

    try:
        header = rows[0]
    except:
        return "Invalid Input. No Data Found."
    
    d = {}

    #Inside of my dictionary, the keys will be numbers to help organize my data. The values will be the data from each row, in the format of lists"
    for i in range(len(rows[1:])):
        d[i+1] = rows[i+1]
    return d

def region_sunny_days(d):
    region_sunny_days_dict = {}
    east_dict = {}
    west_dict = {}
    east_temp_count = 0
    east_count = 0
    east_sunny_count = 0
    west_temp_count = 0
    west_count = 0
    west_sunny_count = 0
    for value in d.values():
        #value[0] is the indexing for Region
        if value[0] == "East":
            east_temp_count += float(value[4])
            east_count += 1
            #value[7] is the indexing for Weather_Condition
            if value[7] == "Sunny":
                east_sunny_count += 1
        if value[0] == "West":
            west_temp_count += float(value[4])
            west_count += 1
            if value[7] == "Sunny":
                west_sunny_count += 1
        if value[0] != "North" and value[0] != "East" and value[0] != "South" and value[0] != "West":
            return "Invalid Input. Please input either North, East, South, or West as a direction."
    #I'm using the try and excepts to prevent the Zero Division Error if none of each region was found (eg. if no crops were grown in the East)
    try:
        east_avg_temp = east_temp_count / east_count
    except:
        east_avg_temp = 0
    try:
        west_avg_temp = west_temp_count / west_count
    except:
        west_avg_temp = 0
    try:
        east_sunny_proportion = east_sunny_count / east_count
    except:
        east_sunny_proportion = 0
    try:
        west_sunny_proportion = west_sunny_count / west_count
    except:
        west_sunny_proportion = 0
    
    region_sunny_days_dict["East"] = {"Average Temperature (Celsius)" : east_avg_temp, "Number of Sunny Days" : east_sunny_proportion}
    region_sunny_days_dict["West"] = {"Average Temperature (Celsius)" : west_avg_temp, "Number of Sunny Days" : west_sunny_proportion}
    print(region_sunny_days_dict)
    return region_sunny_days_dict

def harvest_irrigation(d):
    if len(d) == 0:
        return "Invalid Input. No Data Found."
    harvest_irrigation_dict = {}
    weather_dict = {}
    no_irrigation_count = 0
    days_harvest_count = 0
    for value in d.values():
        #value[6] is the indexing for Irrigation_Used
        if value[6] != "True" and value[6] != "False":
            return "Invalid Input. Please input either True or False for if Irrigation was used"
        if value[6] == "False":
            no_irrigation_count += 1
            #value[8] is the indexing for Days_To_Harvest
            if int(value[8]) >= 100:
                days_harvest_count += 1
                #value[7] is the indexing for Weather_Condition
                weather_dict[value[7]] = weather_dict.get(value[7], 0) + 1
    if no_irrigation_count == 0:
        return "Invalid Input. Division By Zero"
    #I'm using the try and except to prevent the Zero Division Error if all of the data found had crops with Irrigation Used (meaning no_irrigation_count would stay at 0)
    try:
        harvest_proportion = days_harvest_count / no_irrigation_count
    except:
        harvest_proportion = 0
    #appending the proportion (float value) and weather (dictionary) into my main dictionary that I will return
    harvest_irrigation_dict['Proportion'] = harvest_proportion
    harvest_irrigation_dict['Weather'] = weather_dict
    return harvest_irrigation_dict

def output(region_sunny_days, harvest_irrigation):
    #writing my code into a .txt file
    with open("results.txt", "w") as fh:
        fh.write(str(region_sunny_days) + "\n" + str(harvest_irrigation))
    fh.close()

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data = loadresults('test.csv')
        self.data2 = loadresults('test2.csv')
        self.data3 = loadresults('test3.csv')
    def test_region_sunny_days(self):
        region_test_case = region_sunny_days(self.data)
        region_test_case2 = region_sunny_days(self.data2)
        region_test_case3 = region_sunny_days(self.data3)
        #Testing to see if the Average Temperature for the East region is correct
        self.assertAlmostEqual(region_test_case['East']['Average Temperature (Celsius)'], 27.688, places=3)
        #Testing to see if the Number of Sunny Days for the East Region is correct
        self.assertAlmostEqual(region_test_case['East']['Number of Sunny Days'], 0.429, places=3)
        #Testing to see if the dictionary (including Average Temperature and Number of Sunny Days) for the West Region is correct
        self.assertEqual(region_test_case['West'], {'Average Temperature (Celsius)': 27.098474845450426, 'Number of Sunny Days': 0.2})
        #Edge case 1: Resolving dvision by zero error
        self.assertEqual(region_test_case3['East']['Average Temperature (Celsius)'], 0)
        #Edge case 2: if something other than North, East, South, or West was provided for the Region column
        self.assertEqual(region_test_case2, "Invalid Input. Please input either North, East, South, or West as a direction.")
    def test_harvest_irrigation(self):
        harvest_test_case = harvest_irrigation(self.data)
        harvest_test_case2 = harvest_irrigation(self.data2)
        harvest_test_case3 = harvest_irrigation(self.data3)
        #Testing to see if the proportion value is correct
        self.assertEqual(harvest_test_case['Proportion'], 0.47058823529411764)
        #Testing to see if the weather dictionary key/values are correct
        self.assertEqual(harvest_test_case['Weather'], {'Sunny': 4, 'Rainy': 2, 'Cloudy': 2})
        #Edge case 1: Resolving dvision by zero error
        self.assertEqual(harvest_test_case3['Proportion'], 0)
        #Edge case 2: if neither True or False is provided for the Irrigation_Used column
        self.assertEqual(harvest_test_case2, "Invalid Input. Please input either True or False for if Irrigation was used")

def main():
    loadresults('crop_yield.csv')
    load_results_dict = loadresults('crop_yield.csv')
    region_sunny_days(load_results_dict)
    harvest_irrigation(load_results_dict)
    results1 = region_sunny_days(load_results_dict)
    results2 = harvest_irrigation(load_results_dict)
    output_result = output(results1, results2)

if __name__ == '__main__':
    main()

unittest.main()

