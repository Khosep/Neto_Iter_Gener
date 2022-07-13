from itertools import chain

l1 = (
    ('a', "buy", ",", 'c', [-1, -2]),
    ('d', 'e', '"', 'f', 'h', False),
    (1, 2, None)
)
l2 = [[1, 2, [10, 20, [100, 200, [1000, 2000], 300], 30], 3], [5, 6, [7]]]

l3 = []
for i in range(10):
    l3 = [l3, i]
res_list = [l1, l2, l3]


class FlatIterator:
    def __init__(self, object):
        self.object = object

    def __iter__(self):
        self.iterator = iter(self.object)
        return self

    def __next__(self):
        next_item = next(self.iterator)
        while isinstance(next_item, (list, tuple)):
            self.iterator = chain(iter(next_item), self.iterator)
            next_item = next(self.iterator)
        return next_item


def flat_generator(object):
    for item in object:
        if isinstance(item, (list, tuple)):
            for elem in flat_generator(item):
                yield elem
        else:
            yield item


if __name__ == '__main__':
    for obj in res_list:
        print('object =', obj)
        # print('___FlatIterator: FOR________________')
        # for item in FlatIterator(obj):
        #     print(item)
        print('___FlatIterator: List Compr_________')
        print('it-result-->', [item for item in FlatIterator(obj)])
        print()

        # print('___flat_generator: FOR______________')
        # for item in flat_generator(obj):
        #     print(item)
        print('___flat_generator: List Compr_______')
        print('gen-result->', [item for item in flat_generator(obj)])
        print('***************************************************************************')
