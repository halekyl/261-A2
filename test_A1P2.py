# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:40:05 2020
@author: snarayanan
"""
import unittest
from gradescope_utils.autograder_utils.decorators import weight
from a1_p2_minmax import min_max
import dis

checkfor=['len', 'lower','upper', 'isalpha','isnum','isalnum', 'capitalize',' min', ' max', 'sort', 'sorted', 'append', 'find', 'index', 'split', 'strip', 'join','replace']
class TestMinMax(unittest.TestCase):#Test cases
    @weight(5)
    def test1(self):
        """Test with valid inputs """
        self.assertEqual(min_max([1, 2, 3, 4, 5]),(1,5))
    @weight(5)    
    def test2(self):
        """Test with valid inputs """
        self.assertEqual(min_max([8, 7, 6, -5, 4]),((-5, 8))) 

    @weight(5) 
    def test3(self):
        """Test with invalid inputs """
        self.assertEqual(min_max([]),((None, None)))
        
    def test4(self):
        count=0
        used=[]
        instructions=dis.get_instructions(min_max)
        for i in instructions:
            if i.argrepr in checkfor:
                count+=1
                used.append(i.argrepr)
        print(str(count)+" builtin functions used")
        print(used)
if __name__ == '__main__':
    unittest.main()
 
