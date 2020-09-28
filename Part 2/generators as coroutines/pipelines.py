import csv
import itertools


def parse_data(f_name):
    f=open(f_name)
    try:
        dialect=csv.Sniffer.sniff(f.read(2000))
        f.seek(0)
        next(f)
        yield from csv.reader(f, dialect=dialect)
    finally:
        f.close()


def filter_data(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row