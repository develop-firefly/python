# Import the keyword library
from keyword import kwlist

def reserved_keywords():
    ''' 
    Function to get the list of reserved keywords in Python3
    '''
    return kwlist


print(reserved_keywords.__doc__)
print()
print(f'Here is the <list> of reserved keywords in python3: \n\n {reserved_keywords()}')


# Output
'''
 Function to get the list of reserved keywords in Python3

Here is the <list> of reserved keywords in python3: 

 ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''