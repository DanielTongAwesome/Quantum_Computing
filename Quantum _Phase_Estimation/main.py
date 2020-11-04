'''
Author: Zitian(Daniel) Tong
Date: 2020-11-03 15:05:33
LastEditTime: 2020-11-03 19:11:03
LastEditors: Zitian(Daniel) Tong
Description: Quantum Phase Esitimation Main File
FilePath: /Quantum_Computing/Quantum _Phase_Estimation/main.py
'''

import pennylane as qml
from pennylane import numpy as np
import math


def fractional_binary_to_float(s):
    """
    Helper function to expand fractional binary numbers as floats

    Param:  s(string): A string in form '0.xxxxx' where the x are 0 or 1s

    Returns: The numerical value of s when converted from fractional binary
    """
    num = s.split('.')
    num_int = int(num[0], 2)  # integer part of the float num, base 2
    num_flt = int(num[1], 2) / math.pow(2, len(num[1]))  # float part of the float num, base 2
    num = num_int + num_flt
    return num


def float_to_fractional_binary(x, max_bits=10):
    """
    Helper function to turn a string to a binary digit

    Param:  x (float): A numerical value between 0 < x < 1, with a decimal point
            max_bit (int): The maximum number of bits in the expansion

    Returns: A string that is the fractional binary representation, formatted as "0.bbbbb"
             where there are up to max_bits b.
    """

    binary = []  # initialize binary array

    '''
    logic here is simple, check remaining of x:
        if > next bit represented value: append 1
        if = next bit represented value: break loop
        if < next bit represented value: append 0
        until reach the maxbit number
    '''
    for i in range(max_bits):
        if x >= pow(2, -1 * (i + 1)):
            binary.append('1')
            x -= pow(2, -1 * (i + 1))
        elif x == 0:
            break
        else:
            binary.append('0')

    # insert '0.' at the beginning the array
    binary.insert(0, '0.')

    # turn array elements into a string, e.g. ['0.', '1'] -> '0.1'
    binary = str(''.join(map(str, binary)))
    return binary






if __name__ == "__main__":
    print(float_to_fractional_binary(0.998))
