from collections import namedtuple
Result = namedtuple('Result', 'count average')


def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count

    return Result(count, average)


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    print(results)
#     report(results)
#
#
# def report(results):
#     for key, result in sorted(results.items()):
#         group, unit = key.split(';')
#         print('{:2} {:5} averaging {:2f}{}'.format(result.count, group, result.average, unit))

data = {
    'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
}


if __name__ == '__main__':
    main(data)


