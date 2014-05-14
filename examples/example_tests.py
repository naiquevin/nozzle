from nozzle import gentests, check_member, check_none, check_true

## first some functions to tests

def even(x):
    return x % 2 == 0


def min_max(xs):
    return reduce(lambda (a, b), x: (min(x, a), max(x, b)),
                  xs[1:],
                  (xs[0], xs[0]))


def add2(a, b):
    return a+b


GUITARISTS = {'Joe Satriani': ['Ibanez', 'Marshall', 'Peavey', 'Dmarzio', 'Vox'],
              'Paul Gilbert': ['Ibanez', 'Laney', 'Dunlop', 'Boss'],
              'John Petrucci': ['Earnie Ball', 'Dunlop', 'Mesa Boogie']}


def guitarist_gear(state):
    return GUITARISTS.get(state, None)


@gentests(even)
def test_even():
    return [(2, True),
            (3, False),
            (6+4, True)]


@gentests(even, check_true)
def test_even2():
    return [(2,), (6+4,)]


@gentests(min_max)
def test_min_max():
    return [([98, 68, 52, 84, 39, 68, 1, 39, 71, 24], (1, 98)),
            ([93, 10, 69, 14, 42, 67, 98, 71, 69, 58], (10, 98))]


@gentests(add2)
def test_add2():
    return [(2, 3, 5),
            (-1, 4, 3),
            (-10, -6, -16)]


@gentests(guitarist_gear, check_member)
def test_guitarist_gear_in():
    return [('Joe Satriani', 'Ibanez'),
            ('Paul Gilbert', 'Laney'),
            ('John Petrucci', 'Earnie Ball')]


@gentests(guitarist_gear, check_none)
def test_guitarist_gear_none():
    return [('Jimi Hendrix',),
            ('Andy Timmons',)]
