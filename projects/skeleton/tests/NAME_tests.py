from nose.tools import *
import NAME


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    '''
    : this runs by default when you run nosetests
    : print doesn't show unless assert(False)
    '''
    print("I RAN!")
    assert(True)