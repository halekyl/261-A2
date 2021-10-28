# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:40:05 2020

@author: snarayanan
"""

import unittest
from gradescope_utils.autograder_utils.decorators import weight
from a1_p3_matrix_add import matrix_add
import dis

checkfor=['len', 'lower','upper', 'isalpha','isnum','isalnum', 'capitalize',' min', ' max', 'sort', 'sorted', 'append', 'find', 'index', 'split', 'strip', 'join','replace']


class TestMatrixAdd(unittest.TestCase):
        @weight(3)
        def test1(self):
            """Test with valid inputs """
            m1 = [ [1, 2, 3], [2, 3, 4] ]
            m2 = [ [5, 6, 7], [8, 9, 10] ]
            self.assertListEqual(matrix_add(m1,m2),[[6, 8, 10], [10, 12, 14]] )
            
        @weight(3)    
        def test2(self):
            """Test with valid inputs """
            m1 = [ [1, 2, 3], [2, 3, 4] ]
            self.assertListEqual(matrix_add(m1,m1),[[2, 4, 6], [4, 6, 8]] )
            
        @weight(3)    
        def test3(self):
                """Test with valid inputs """
                self.assertListEqual(matrix_add( [[]], [[]] ),[[]] )
        @weight(3)    
        def test4(self):
            """Test with invalid inputs """
            m1 = [ [1, 2, 3], [2, 3, 4] ]
            m3 = [ [1, 2], [3, 4], [5, 6] ]
            self.assertEqual(matrix_add( m1, m3 ),None )
            
        @weight(3)    
        def test5(self):
            """Test with valid inputs """
            m1 = [ [1, 2, 3], [2, 3, 4] ]
            self.assertEqual(matrix_add( [[]], m1 ),None)
        
        def test6(self):
            count=0
            used=[]
            instructions=dis.get_instructions(matrix_add)
            for i in instructions:
                if i.argrepr in checkfor:
                    count+=1
                    used.append(i.argrepr)
            print(str(count)+" builtin functions used")
            print(used)
        
        
if __name__ == '__main__':
    unittest.main()
