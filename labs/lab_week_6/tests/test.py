from nose.tools import *

def test_anyname():
    eq_(1,1)

@raises(Exception)
def test_exception():
    l = []
    l.pop()
