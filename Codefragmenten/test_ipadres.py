import pytest

def generate():
  return "192.168.0a.1"

def test_generate():
  mytest = generate()
  mytest_split = mytest.split(".")
  # geen 4 delen
  assert len(mytest_split) == 4
  # niet converteerbaar getal
  assert mytest_split[0].isnumeric()
  assert mytest_split[1].isnumeric()
  assert mytest_split[2].isnumeric()
  assert mytest_split[3].isnumeric()
  # converteren naar ints
  getal1 = int(mytest_split[0])
  getal2 = int(mytest_split[1])
  getal3 = int(mytest_split[2])
  getal4 = int(mytest_split[3])
  # waarde >= 0 en <= 255
  assert getal1 >= 0
  assert getal1 <= 255
  assert getal2 >= 0
  assert getal2 <= 255
  assert getal3 >= 0
  assert getal3 <= 255
  assert getal4 >= 0
  assert getal4 <= 255

