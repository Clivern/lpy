# 286. unittest
#
# unittest.TestCase is the stdlib test style. assertEqual and assertRaises are the usual
# checks. pytest is more common now; unittest still runs in CI.
#
# Run: python 286_unittest_mod/main.py

import unittest
class T(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
suite = unittest.defaultTestLoader.loadTestsFromTestCase(T)
result = unittest.TextTestRunner(verbosity=0).run(suite)
print(result.wasSuccessful())
