import csv
import sys
import os
from csv import reader

# Enter file path
user_input = input("Enter the path of your file: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
file_name = os.path.basename(user_input)
#stuff you do with the file goes here
f.close()

with open(user_input, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Iterate over each row in the csv using reader object
    result = {}
    product_names = []
    total_orders = 0
    for row in csv_reader:
        total_orders += 1
        product_name = row[2]
        if (product_name in result.keys()):
            result[product_name]['orders_count'] += 1
            result[product_name]['total_quantity'] += int(row[3])
            brand_name = row[4]
            if (brand_name in result[product_name]['brands_count'].keys()):
                result[product_name]['brands_count'][brand_name] += 1
            else:
                result[product_name]['brands_count'][brand_name] = 1
        else:
            result[product_name] = {}
            result[product_name]['orders_count'] = 1
            result[product_name]['total_quantity'] = int(row[3])
            result[product_name]['brands_count'] = {}
            result[product_name]['brands_count'][row[4]] = 1
    end_result_1 = {}

    for key in result:
        average = result[key]['total_quantity'] / total_orders
        end_result_1[key] = average

    # Calculate average quantity of each product
    with open('0_' + file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for key in end_result_1:
            writer.writerow([key, end_result_1[key]])

    max_value = 0
    selected_brand = ''
    brands_result = {}
    for key in result:
        product_name = key
        brands = result[key]['brands_count']
        for brand in brands:
            brand_count = brands[brand]
            if (brand_count > max_value):
                max_value = brand_count
                selected_brand = brand
            obj = {}
            obj[selected_brand] = max_value
        brands_result[product_name] = {}
        brands_result[product_name] = selected_brand
        max_value = 0

    # Calculate the most popular brand of each product
    with open('1_' + file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for key in brands_result:
            writer.writerow([key, brands_result[key]])
