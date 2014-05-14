from functools import wraps
 
 
def type_name(x):
    return x.__class__.__name__
 
 
def check_equal(a, b):
    assert a == b, '{}:{} != {}:{}'.format(a, type_name(a), b, type_name(b))
 
 
def checker_fn(fn_apply, fn_assert):
    def inner(a, b):
        return fn_assert(fn_apply(*a), b)
    return inner
 
 
def gentests(fn_apply, fn_assert=check_equal):
    def decorator(func):
        check = checker_fn(fn_apply, fn_assert)
        @wraps(func)
        def decorated():
            for case in func():
                if len(case) > 1:
                    inputs, expected = case[:-1], case[-1]
                else:
                    inputs, expected = case, None
                yield check, inputs, expected                    
        return decorated
    return decorator


# other common checker functions

def check_member(a, b):
    assert b in a, '{}:{} not in {}:{}'.format(a, type_name(a),
                                               b, type_name(b))


def check_none(a, *_):
    assert a is None, '{}:{} is not None'.format(a, type_name(a))


def check_true(a, *_):
    assert a, '{}:{} is not True'.format(a, type_name(a))


def check_false(a, *_):
    assert not a, '{}:{} is not False'.format(a, type_name(a))
