#!/usr/bin/python3

import contextlib, unittest, longest_cons_char
from io import StringIO

class TestLongestConstantChar(unittest.TestCase):

    cases = ( ("ABAACDDDBBA","D 3"),
            ("AABCDDBBBEA", "B 3") )

    #def setUp(self):
    #    self.held, sys.stdout = sys.stdout, StringIO()

    def test_cases(self):
        for inputt,expected in self.cases:
            stdout = StringIO()
            # Source: https://stackoverflow.com/a/39320622/7057875
            with contextlib.redirect_stdout(stdout):
                longest_cons_char.main(["test",inputt])
            output = stdout.getvalue().strip()
            self.assertEqual(expected,output)

if __name__ == '__main__':
    unittest.main()
