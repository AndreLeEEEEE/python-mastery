# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    Memory Use: Current 123688968, Peak 123723387
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dictionaries
    Memory Use: Current 123688968, Peak 123723387
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

def read_rides_as_classes(filename):
    '''
    Read the bus ride data as a list of classes
    Memory Use: Current 169895816, Peak 169930235
    '''
    class Record:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Record(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_named_tuples(filename):
    '''
    Read the bus ride data as a list of named tuples
    Memory Use: Current 128314583, Peak 128349002
    '''
    from collections import namedtuple
    Record = namedtuple("Record", ["route", "date", "daytype", "rides"])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Record(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_classes_w_slots(filename):
    '''
    Read the bus ride data as a list of classes with slots
    Memory Use: Current 119070776, Peak 119105195
    '''
    class Record:
        __slots__ = ("route", "date", "daytype", "rides")
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Record(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_classes_w_slots('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
