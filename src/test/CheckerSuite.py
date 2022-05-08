import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        """Simple program: int main() {} """
        input = Program([ClassDecl(Id('Program'), [])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_401(self):
        input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([]))])])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))