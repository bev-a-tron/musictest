import unittest

class BasicTestCase(unittest.TestCase):
  def runTest(self):
    assert 1 == 1, "Not 1"

# if __name__ == '__main__':
#   unittest.main()
