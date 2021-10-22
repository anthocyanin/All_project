import multiprocessing
from time import ctime


def consumer(q):
    print('Into consumer:', ctime())
    while True:
        item = q.get()
        if item is None:
            break
        print('pull', item, 'out of q')
    print('Out of consumer', ctime())


def producer(sequence, q):
    for item in sequence:
        print('Into producer:', ctime())
        q.put(item)
        print('Out of producer:', ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()

    con_p1 = multiprocessing.Process(target=consumer, args=(q,))
    con_p1.start()
    con_p2 = multiprocessing.Process(target=consumer, args=(q,))
    con_p2.start()

    sequence = [1, 2, 3, 4, 5, 6]
    producer(sequence, q)
    q.put(None)
    q.put(None)

    con_p1.join()
    con_p2.join()


