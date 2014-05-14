Nozzle
======

(Even more) Simpler nose tests.


Installation
------------

:todo: 

Not on PyPI yet. For now you may download ``nozzle.py`` and try it
out.


Quickstart
----------

Let's first define a few simple functions to test,

.. code-block:: python

    def even(x):
        return x % 2 == 0

    def min_max(xs):
        return reduce(lambda (a, b), x: (min(x, a), max(x, b)),
                      xs[1:],
                      (xs[0], xs[0]))

    def add2(a, b):
        return a+b


Now we add tests using nozzle,

.. code-block:: python

    from nozzle import gentests

    @gentests(even)
    def test_even():
        return [(2, True),
                (3, False),
                (6+4, True)]
    
    @gentests(min_max)
    def test_min_max():
        return [([98, 68, 52, 84, 39, 68, 1, 39, 71, 24], (1, 98)),
                ([93, 10, 69, 14, 42, 67, 98, 71, 69, 58], (10, 98))]
    
    @gentests(add2)
    def test_add2():
        return [(2, 3, 5),
                (-1, 4, 3),
                (-10, -6, -16)]


Explanation
~~~~~~~~~~~

Here, we have defined three functions each returning an interable of
tuples. ``nozzle`` provides ``gentests``, a function that takes as
input, the main function to be tested and returns a decorator. The
tuples are n-tuples such that the first ``n-1`` items are the input to
the function to be tested and the last element is the expected output.

``gentests`` optionally take as second argument, a function that
handles assertions. It's passed two args, the result and the expected
value. The default function is ``nozzle.check_equal`` that asserts
that the result is equal to the expected value.

Those familiar with nose must have already figured out that the
decorator converts the function into a `test generator
<http://nose.readthedocs.org/en/latest/writing_tests.html#test-generators>`_
that yields tests from the returned interable. So the above test code
will yield 8 tests as follows,

.. code-block:: bash

    $ nosetests -v tests.py
    example_tests.test_add2((2, 3), 5) ... ok
    example_tests.test_add2((-1, 4), 3) ... ok
    example_tests.test_add2((-10, -6), -16) ... ok
    example_tests.test_even((2,), True) ... ok
    example_tests.test_even((3,), False) ... ok
    example_tests.test_even((10,), True) ... ok
    example_tests.test_min_max(([98, 68, 52, 84, 39, 68, 1, 39, 71, 24],), (1, 98)) ... ok
    example_tests.test_min_max(([93, 10, 69, 14, 42, 67, 98, 71, 69, 58],), (10, 98)) ... ok
    
    ----------------------------------------------------------------------
    Ran 8 tests in 0.002s
    
    OK


For more examples see ``examples/examples_tests.py``.


Alerts!
-------

* This is highly experimental stuff so use with caution.
* It's one of those libs that make simple things simpler, but with a
  possibility of making difficult things impossible to achieve! You
  can still fallback to writing normal assertions based test functions
  or class based testcases (unittest).


LICENSE
-------

MIT (See LICENSE)

