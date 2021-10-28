# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:40:05 2020

@author: snarayanan
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight
from a1_p4_swap_pairs import swap_pairs
import dis

checkfor=['len', 'lower','upper', 'isalpha','isnum','isalnum', 'capitalize',' min', ' max', 'sort', 'sorted', 'append', 'find', 'index', 'split', 'strip', 'join','replace']

class TestSwapPairs(unittest.TestCase):
        @weight(5)
        def test1(self):
            self.assertListEqual(swap_pairs([12, 2, 3, 6, 5, 7]),[2, 12, 6, 3, 7, 5] )
        @weight(5)
        def test2(self):
            self.assertListEqual(swap_pairs([8, 7, 6, -5, 4]),[7, 8, -5, 6, 4] ) 
        @weight(5)
        def test3(self):
            self.assertListEqual(swap_pairs([ ]),[ ] )      
        
        def test4(self):
            count=0
            used=[]
            instructions=dis.get_instructions(swap_pairs)
            for i in instructions:
                if i.argrepr in checkfor:
                    count+=1
                    used.append(i.argrepr)
            print(str(count)+" builtin functions used")
            print(used)
        
        
if __name__ == '__main__':
    unittest.main()
