import unittest

from lesson import multy


def setUpModule():
    print "Этот метод вызывается ПЕРЕД всеми тестами в этом файле"


def TearDownModule():
    print "Этот метод вызывается ПЕРЕД всеми тестами в этом файле"


class TestSimCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "Этот метод вызывается ПЕРЕД всеми тестами в классе"

    def setUp(self):
        print "Этот метод вызывается ПЕРЕД каждым тестом"

    def tearDown(self):
        print "Этот метод вызывается ПОСЛЕ каждого теста"

    def test_a(self):
        self.assertEqual(9, multy(3,3))

    def test_b(self):
        self.assertNotEqual('aaa', multy('s', 4))

    def test_c(self):
        self.assertIn('5', multy('5', 5))

    @classmethod
    def tearDownClass(cls):
        print "Этот метод вызывается ПОСЛЕ всех тестов в классе"
