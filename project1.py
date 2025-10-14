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
    #print(3/7)
    return d

def region_sunny_days(d):
    # count = 0
    # for value in d.values():
    #     if value[0] == "West":
    #         count +=1
    # print(count)
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
        if value[0] == "East":
            east_temp_count += float(value[4])
            east_count += 1
            if value[7] == "Sunny":
                east_sunny_count += 1
        if value[0] == "West":
            west_temp_count += float(value[4])
            west_count += 1
            if value[7] == "Sunny":
                west_sunny_count += 1
        if value[0] != "North" and value[0] != "East" and value[0] != "South" and value[0] != "West":
            return "Invalid Input. Please input either North, East, South, or West as a direction."
    east_avg_temp = east_temp_count / east_count
    west_avg_temp = west_temp_count / west_count
    east_sunny_proportion = east_sunny_count / east_count
    west_sunny_proportion = west_sunny_count / west_count
    
    region_sunny_days_dict["East"] = {"Average Temperature (Celsius)" : east_avg_temp, "Number of Sunny Days" : east_sunny_proportion}
    region_sunny_days_dict["West"] = {"Average Temperature (Celsius)" : west_avg_temp, "Number of Sunny Days" : west_sunny_proportion}
    print(region_sunny_days_dict)

        
    return region_sunny_days_dict

#def get_crop_results 

def harvest_irrigation(d):
    harvest_irrigation_dict = {}
    weather_dict = {}
    no_irrigation_count = 0
    days_harvest_count = 0
    for value in d.values():
        if value[6] != "True" and value[6] != "False":
            return "Invalid Input. Please input either True or False for if Irrigation was used"
        if value[6] == "False":
            no_irrigation_count += 1
            if int(value[8]) >= 100:
                days_harvest_count += 1
                weather_dict[value[7]] = weather_dict.get(value[7], 0) + 1
    if no_irrigation_count == 0:
        return "Invalid Input. Division By Zero"
    harvest_proportion = days_harvest_count / no_irrigation_count
    harvest_irrigation_dict['Proportion'] = harvest_proportion
    harvest_irrigation_dict['Weather'] = weather_dict
    print(harvest_irrigation_dict)

def output(region_sunny_days):
    with open("results.txt", "w") as fh:
        fh.write(str(region_sunny_days))
    fh.close()

class TestFunctions(unittest.TestCase):
    def SetUp(self):
        self.data = loadresults('test.csv')
        self.data2 = loadresults('test2.csv')
    def test_region_sunny_days(self):
        self.assertEqual(region_sunny_days(self.data['East']), {'Average Temperature (Celsius)': 27.688129491006, 'Number of Sunny Days': 0.42857142857142855})
        self.assertEqual(region_sunny_days(self.data['West']), {'Average Temperature (Celsius)': 27.09847484545, 'Number of Sunny Days': 0.25})
        #Edge case 1: if the data set is empty
        self.assertEqual(region_sunny_days({}), "Invalid Input. No Data Found")
        self.assertEqual(region_sunny_days(self.data2), "Invalid Input. Please input either North, East, South, or West as a direction.")
    def test_harvest_irrigation(self):
        self.assertEqual(harvest_irrigation(self.data['Proportion']), 0.47058823529411764)
        self.assertEqual(harvest_irrigation(self.data['Weather']), {'Rainy': 7, 'Sunny': 6, 'Cloudy': 4})
        #Edge case 1: if the data set is empty
        self.assertEqual(harvest_irrigation({}), "Invalid Input. No Data Found")
        self.assertEqual(region_sunny_days(self.data2), "Invalid Input. Please input either True or False for if Irrigation was used")

# def write_to_file():
#     #function_1_text = "The Average Temperature of Crops grown in the East region is " + east_avg_temp + "degrees Celsius, and " + west_avg_temp + " degrees Celsius in the West region.\n33.36 percent of the days in the East region were Sunny, compared to 33.43 percent of the days in the West region.\n"
#     with open("results.txt", "w") as f:
#         #f.write(function_1_text)
#         f.write("The Average Temperature of Crops grown in the East region is 27.50 degrees Celsius, and 27.51 degrees Celsius in the West region.\n33.36 percent of the days in the East region were Sunny, compared to 33.43 percent of the days in the West region.\n")
#         f.write("55.65 percentage of crops without the use of Irrigation took 100 or more days to harvest. \nOf these crops, 92,804 were grown in Sunny weather, 93,064 were grown in Rainy weather, and 92,666 were grown in Cloudy weather.")
#     f.close()

def main():
    #unittest.main(verbosity=2)
    loadresults('crop_yield.csv')
    load_results_dict = loadresults('crop_yield.csv')
    region_sunny_days(load_results_dict)
    harvest_irrigation(load_results_dict)
    results = region_sunny_days(load_results_dict)
    output_result = output(results)

if __name__ == '__main__':
    main()

