import csv

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(row['username'], row['password']) for row in reader]
    return data
