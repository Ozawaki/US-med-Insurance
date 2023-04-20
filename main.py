import csv
import matplotlib.pyplot as plt
import numpy as np




age = []
sex = []
bmi = []
children = []
smoker_status = []
region = []
charges = []

with open("insurance.csv", newline = '') as ins_file:
    reader = csv.DictReader(ins_file)
    for row in reader:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker_status.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])

bmi_to_charge = []

def create_bmi_to_charge():
    i = 0
    while i < len(bmi):
        bmi_to_charge.append([bmi[i], charges[i]])
        i += 1
    return bmi_to_charge

create_bmi_to_charge()

bmi_to_charge = sorted(bmi_to_charge, key=lambda x: x[1])



x = []
y = []

def create_cost_to_bmi_plot():
    i = 0
    while i < len(bmi_to_charge):
        x.append(float(bmi_to_charge[i][0]))
        y.append(float(bmi_to_charge[i][1]))
        i += 1



create_cost_to_bmi_plot()

plt.scatter(x, y)
plt.show()



def average_cost(cost, factor, param):
    sum_of_cost = 0
    total_in_factor = 0
    i = 0
    while i < len(cost):
        if factor[i] == param:
            sum_of_cost += float(cost[i])
            total_in_factor += 1
        i = i + 1
    return round(sum_of_cost/total_in_factor, 2)

avg_cost_for_sw = average_cost(charges, region, "southwest")
avg_cost_for_nw = average_cost(charges, region, "northwest")
avg_cost_for_se = average_cost(charges, region, "southeast")
avg_cost_for_ne = average_cost(charges, region, "northeast")
avg_cost_for_male = average_cost(charges, sex, "male")
avg_cost_for_female = average_cost(charges, sex, "female")




print("The average cost for someone living in the southwest is " + str(avg_cost_for_sw))
print("The average cost for someone living in the northwest is " + str(avg_cost_for_nw))
print("The average cost for someone living in the southeast is " + str(avg_cost_for_se))
print("The average cost for someone living in the northeast is " + str(avg_cost_for_ne))
print("The average cost for a male is " + str(avg_cost_for_male))
print("The average cost for a female is " + str(avg_cost_for_female))
