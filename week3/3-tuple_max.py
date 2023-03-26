#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Manipulation of nested tuples of integers

Consider a nested tuple T. For example,

    T =  ((10, -8), ((-9, 3, 6, -7), (6,), (2, 7), 6))

You can get an indented display of its associated tree 
with a call to print_nested_tuple(T) that will output in this case

    || 10
    || -8
    |
    ||| -9
    ||| 3
    ||| 6
    ||| -7
    ||
    ||| 6
    ||
    ||| 2
    ||| 7
    ||
    || 6
    |

The function 'generate_nested_tuple' creates random nested tuples

The function 'get_max' compute the maximum of a nested tuple and its location

Last modified on 2022/01/31  by f.maire@qut.edu.au

"""

from random import randint


def generate_nested_tuple(max_depth=4, max_branch=4, max_abs_value=10):
    '''
    Create and return a nested tuple of integers.    
    
    @param
        max_depth: upper bound for the depth of the associated tree
        max_branch: upper bound for the brancing factor of the associated tree
        max_abs_value: upper bound for the abs values of the associated tree
    '''
    if max_depth==0:
        return randint(-max_abs_value,max_abs_value)
    else:
        return tuple( 
                generate_nested_tuple(randint(0,max_depth-1), max_branch, max_abs_value)
                for _ in range(randint(1,max_branch))
                    )


def get_max(T):
    '''
    Return the pair  v,I   where
     v is the maximum value of the nested tuple
    and I is the index sequence to reach this value.
    
    For example,
    if  
      T =  ((-3, (-6,), 3), -9, ((-8, -6, 9, -5), (-3,), -2))
    then 
       v, I =  9, [2, 0, 2]
    
    @param 
     T : a nested tuple of numbers
    @return
     v, I : max value and index sequence 
    '''
    ############### ANSWER #################
    max_val = float('-inf')
    max_index = []

    # recursive function that traverses the nested loop
    def helper(T, index):
        nonlocal max_val, max_index

        # if T is a tuple, recursively call helper on element with updated index
        if isinstance(T, tuple):
            for i, val in enumerate(T):
                helper(val, index + [i])
            
        else:
            if T > max_val:
                max_val = T
                max_index = index
    # call the helper function with nested tupe and initial index sequence
    helper(T, [])

    return max_val, max_index



def print_nested_tuple(T, margin=''):
    if not (type(T) == tuple):
        # T is a scalar
        print(margin,T)
    else: # scan the top level
        for t in T:
            print_nested_tuple(t, margin=margin+'|')
        print(margin)
    
def test_1():
    '''
    Test the function 'get_max' on an example
    '''
    T  = ((-2, (-6, -1, 7, 1)), (8, -8), ((2, -5), -6, (-3, -5, -6, -3), (-4,)))
    v_max, I_max = get_max(T)
    print('T = ' ,T)
    print('v_max = ', v_max)
    print('I_max = ', I_max)
    assert v_max== 8
    assert I_max == [1,0]
   
def test_2():
    '''
    Test the function 'get_max' on a random example
    '''

    T  = generate_nested_tuple(max_depth=5)
    v_max, I_max = get_max(T)
    print('T = ' ,T)
    print('v_max = ', v_max)
    print('I_max = ', I_max)
    
    
def test_3():
    '''
    Test the function 'print_nested_tuple' on a random example
    '''
    T  = generate_nested_tuple(max_depth=5)
#    T =  (((3, -6, 7), 6, -2, (-2,)), -10)
#    T =  (((3,), -6, 7), 6, (-2,4,), -10)
#    T =  (((3,), -6, 7), 6, (-2,),(4,), -10)
    T =  (((5,),), ((5, -3, 9, -1),), (-1, ((2,), (-9, 7, -10)), (4, 1), (-8, 1, -2, -7)))    
        
    print('T = ' ,T)
    print('-------')
    print_nested_tuple(T)
    
    
    
if __name__ == '__main__':
    test_1()
    test_2()
