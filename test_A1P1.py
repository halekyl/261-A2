"""
@@ CS 261 Assignment 1 - Divisibility Tester
@@ Solution Test Script
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight
from a1_p1_divisibility import is_divisible
import dis

checkfor=['len', 'lower','upper', 'isalpha','isnum','isalnum', 'capitalize',' min', ' max', 'sort', 'sorted', 'append', 'find', 'index', 'split', 'strip', 'join','replace']

            

class TestDivisibility(unittest.TestCase):#TestCases
    @weight(2)
    def test1(self):
        """Test with incorrect(non-positive)inputs """
        expected ='Incorrect input'
        self.assertEqual(is_divisible(-7, -2, 2, 3), expected)
        
    @weight(4.5)
    def test2(self):
        """Test with valid inputs """
        list1 = ['Num\tDiv by 2 and/or 4?', '---\t-------------------', '24\tboth', '23\tNone', '22\tdiv by 2', '21\tNone', '20\tboth', '19\tNone', '18\tdiv by 2', '17\tNone', '16\tboth', '15\tNone', '14\tdiv by 2', '13\tNone', '12\tboth', '11\tNone', '10\tdiv by 2', '9\tNone', '8\tboth', '7\tNone', '6\tdiv by 2', '5\tNone', '4\tboth', '3\tNone', '2\tdiv by 2'] 
        self.assertListEqual(is_divisible(2, 24, 2, 4),list1)
        print(*is_divisible(2, 24, 2, 4), sep = "\n")
        
    @weight(2)
    def test3(self):
        """Test with incorrect(invalid range)inputs"""
        expected ='Incorrect input'
        self.assertEqual(is_divisible(20, 3, 2, 3), expected)

    @weight(4.5)
    def test4(self):
        """Test with valid inputs """
        list2 = ['Num\tDiv by 6 and/or 4?', '---\t-------------------', '28\tdiv by 4', '27\tNone', '26\tNone', '25\tNone', '24\tboth', '23\tNone', '22\tNone', '21\tNone', '20\tdiv by 4', '19\tNone', '18\tdiv by 6', '17\tNone', '16\tdiv by 4', '15\tNone', '14\tNone', '13\tNone', '12\tboth', '11\tNone', '10\tNone', '9\tNone', '8\tdiv by 4', '7\tNone', '6\tdiv by 6', '5\tNone', '4\tdiv by 4', '3\tNone'] 
        self.assertListEqual(is_divisible(3,28, 6, 4),list2)
        print(*is_divisible(3,28, 6, 4), sep = "\n")
        
    @weight(2)
    def test5(self):
        """Tests with incorrect(the divisors should be different)inputs"""
        expected ='Incorrect input'
        self.assertEqual(is_divisible(2, 20, 2, 2), expected)
        
    def test6(self):
        count=0
        used=[]
        instructions=dis.get_instructions(is_divisible)
        for i in instructions:
            if i.argrepr in checkfor:
                count+=1
                used.append(i.argrepr)
        print(str(count)+" builtin functions used")
        print(used)    
    
if __name__ == '__main__':
    unittest.main()


        
