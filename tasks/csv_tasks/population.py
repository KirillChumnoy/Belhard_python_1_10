"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv


def max_delta(file_name: str):
    perc = 0
    year = {}
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if float(row['ChangePerc']) > perc:
                perc = float(row['ChangePerc'])
                year[perc] = row['Year']
        return year[perc]
