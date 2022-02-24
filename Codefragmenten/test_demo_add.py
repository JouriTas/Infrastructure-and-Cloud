import pytest

def adding(x):
  return x + 10

def test_adding():
  mytest = adding(10)
  assert mytest == 20
  mytest = adding(0)
  assert mytest == 10

