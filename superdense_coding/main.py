'''
Author: Zitian(Daniel) Tong
Date: 2020-10-15 19:13:42
LastEditTime: 2020-10-15 19:44:49
LastEditors: Zitian(Daniel) Tong
Description: EECE 571S Quantum Computing Assignment #4 Question #3 
FilePath: /Quantum_Computing_Assignment/A4Q3.py
'''

import pennylane as qml
from pennylane import numpy as np

'''
wires - Number of subsystems represented by the devices(qbuts)
shots - How many times the circuit should be evaluated
'''

test_dev = qml.device("default.qubit", wires=2)         # for testing package
dev1 = qml.device("default.qubit", shots=1, wires=2)    # for demo the sender's operation
dev2 = qml.device("default.qubit", shots=1, wires=2)    # for demo the receiver's operation

xbit = 0
ybit = 0


# test circuit
@qml.qnode(test_dev)
def test_circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=0)
    return qml.expval(qml.PauliZ(0))


'''
The following function designed for a simple superdense coding:
using 1 qubit to send 2 classical bits
# part a - set up accroding to the super dense coding
# part b - lookup table

Check the following video link for more details:
https://www.youtube.com/watch?v=w5rCn593Dig&ab_channel=MichaelNielsen
'''


@qml.qnode(dev1)
def circuit1():
    # part a - construct super dense coding
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

    # par b - lookup table
    '''
    case1: |00> -> apply I
    case2: |01> -> apply X
    case3: |10> -> apply Z
    case4: |11> -> apply XZ 
    '''
    if xbit == 1:
        qml.PauliZ(wires=0)
    if ybit == 1:
        qml.PauliX(wires=0)

    # return 2 wires measurement
    return qml.probs(wires=[0, 1])


@qml.qnode(dev2)
def circuit2():
    # superdense coding sender
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])

    # sender apply operation
    if xbit == 1:
        qml.PauliZ(wires=0)
    if ybit == 1:
        qml.PauliX(wires=0)

    # receiver perform operation
    qml.CNOT(wires=[0, 1])
    qml.Hadamard(wires=0)

    return qml.probs(wires=[0, 1])


if __name__ == "__main__":
    # test circuit
    # print(test_circuit([0.54, 0.12])) - sender part

    # problem 3 a&b superdense coding
    print("The output when state is |00>: ", circuit1())

    # problem 3 c&d superdense coding   - receiver part
    print("The output of superdense coding is: ", circuit2())

