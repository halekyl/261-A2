# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:37:17 2020

@author: snarayanan
"""
from gradescope_utils.autograder_utils.decorators import weight
from a1_p5_camel_case import input_cleanup,is_clean_string,camel_case
import unittest

import dis

checkfor=['len', 'lower','upper', 'isalpha','isnum','isalnum', 'capitalize',' min', ' max', 'sort', 'sorted', 'append', 'find', 'index', 'split', 'strip', 'join','replace']

            


class TestCamelCase(unittest.TestCase):
        #Test cases
        @weight(7)
        def test1(self):
        #Test cases
        #INPUT: _random_ _word_provided
        #OUTPUT: "random_word_provided", "randomWordProvided"
           phrase = "_random_ _word_provided"
           snake_output="random_word_provided"
           camel_output="randomWordProvided"
           self.assertEqual(input_cleanup(phrase),snake_output)
           self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)
        @weight(7)
        def test2(self):
        #INPUT: "@$ptr*4con_",
        #OUTPUT: "ptr_con", "ptrCon"
            phrase = "@$ptr*4con_"
            snake_output="ptr_con"
            camel_output="ptrCon"
            self.assertEqual(input_cleanup(phrase),snake_output)
            self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)
        @weight(7) 
        def test3(self):
        #INPUT: " ran  dom  word",
        #OUTPUT: "ran_dom_word", "ranDomWord"
            phrase = " ran  dom  word"
            snake_output="ran_dom_word"
            camel_output="ranDomWord"
            self.assertEqual(input_cleanup(phrase),snake_output)
            self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)
        @weight(7)
        def test4(self):
        #INPUT:    "example    word   ",
        #OUTPUT: "example_word", "exampleWord"
            phrase = "example    word   "
            snake_output="example_word"
            camel_output="exampleWord"
            self.assertEqual(input_cleanup(phrase),snake_output)
            self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)
        @weight(7)
        def test5(self):
        #INPUT: "ANOTHER_Word",
        #OUTPUT: "another_word", "anotherWord"
            phrase = "ANOTHER_Word"
            snake_output="another_word"
            camel_output="anotherWord"
            self.assertEqual(input_cleanup(phrase),snake_output)
            self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)
        @weight(5)
        def test6(self):
        #INPUT: "_random_ _ ",
        #OUTPUT: "random", None
            phrase = "_random_ _ "
            snake_output="random"
            camel_output= None
            self.assertEqual(input_cleanup(phrase),snake_output)
            self.assertEqual(camel_case(phrase,is_clean_string,input_cleanup),camel_output)

        def test7(self):
            count=0
            used=[]
            instructions_f1=dis.get_instructions(input_cleanup)
            instructions_f2=dis.get_instructions(camel_case)
            for i in instructions_f1:
                if i.argrepr in checkfor:
                    count+=1
                    used.append(i.argrepr)
                    
            for j in instructions_f2:
                if j.argrepr in checkfor:
                    count+=1
                    used.append(j.argrepr)
            print(str(count)+" builtin functions used")
            print(used)    
if __name__ == "__main__":
    unittest.main()
