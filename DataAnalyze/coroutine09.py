def generator_01(titles):
    yield titles  # 可以这样理解 产生 titles。所以产生一个


def generator_02(titles):
    yield from titles  # 可理解为从 titles 里产生。所以产生一堆


titles = ['Python', 'Java', 'Php']

for title in generator_01(titles):
    print(title)

for title in generator_02(titles):
    print(title)


