import json
import csv

def write_json_result(filename, collection, conf, date_time):
    filename = "%s%s-%s" %(conf['outputDirectory'], date_time, filename)
    #filename should be .json
    with open(filename, 'w') as file:
        file.write(json.dumps(collection))

def write_csv_result(file, collection, conf, date_time):
    file = "%s%s-%s" %(conf['outputDirectory'], date_time, file)
    
    keys = collection[0].keys()
    
    with open(file, 'w', encoding='utf8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter='|')
        dict_writer.writeheader()
        dict_writer.writerows(collection)
