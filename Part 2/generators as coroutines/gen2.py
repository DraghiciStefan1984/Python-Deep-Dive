import csv
import itertools
import os


def parse_file(f_name):
    print('opening file...')
    f=open(os.path.join(f_name), 'r')
    try:
        dialect=csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader=csv.reader(f, dialect=dialect)
        for row in reader:
            yield row
    except Exception as ex:
        print('some error', str(ex))
    except GeneratorExit:
        print('generator was closed')
    finally:
        print('closing file...')
        f.close()

parser=parse_file('cars.csv')
for row in itertools.islice(parser, 10):
    print(row)

parser.close()