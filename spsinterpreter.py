
# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Name: Chandler Teigen

from numbers import Number


import re
import collections.abc



#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    global opstack
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print('Error: Nothing in stack to pop')
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    global opstack
    lookupValue = None
    if isinstance(value, str):
        if value[0] != '/':
            lookupValue = lookup('/' + value)
    if lookupValue is None:
        if isinstance(value, list):
            opstack.append(interpretList(value))
        else:
            opstack.append(value)
    elif isinstance(lookupValue, dict):
        interpretSPS(lookupValue)
    else:
        opstack.append(lookupValue)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    global dictstack

    dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    global dictstack
    dictstack.append(d)

    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    global dictstack
    if len(dictstack) == 0:
        dictstack.append(dict())
    dictstack[-1][name] = value

    #  add name:value pair to the top dictionary in the dictionary stack.
    #  Keep the '/' in the name constant.
    #  Your psDef function should pop the name and value from operand stack and
    #  call the “define” function.

def lookup(name):
    global dictstack
    if name[0] != '/':
        name = '/' + name
    value = None
    for d in reversed(dictstack):
        value = d.get(name)
        if value != None:
            break

    if value != None:
        return value
    else:
        print('variable lookup error: name \'' + name + '\' does not exist...')
        return value

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    count()

    if opPop() >= 2:  # ensure that there is enough operands for add
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, Number) and isinstance(operand2, Number):
            opPush(operand2 + operand1)
        else:
            print('operator error: top two values in operand stack are not numbers...')
            opPush(operand2)
            opPush(operand1)  # restore stack contents
    else:
        print('operator error: too few arguments for \'add\'...')

def sub():
    count()

    if opPop() >= 2:  # ensure that there is enough operands for sub
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, Number) and isinstance(operand2, Number):
            opPush(operand2 - operand1)
        else:
            print('operator error: top two values in operand stack are not numbers...')
            opPush(operand2)
            opPush(operand1)  # restore stack contents
    else:
        print('operator error: too few arguments for \'sub\'...')

def mul():
    count()

    if opPop() >= 2:  # ensure that there is enough operands for mul
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, Number) and isinstance(operand2, Number):
            opPush(operand2 * operand1)
        else:
            print('operator error: top two values in operand stack are not numbers...')
            opPush(operand2)
            opPush(operand1)  # restore stack contents
    else:
        print('operator error: too few arguments for \'mul\'...')

def eq():

    count()

    if opPop() >= 2:
        operand1 = opPop()
        operand2 = opPop()
        opPush(operand1 == operand2)
    else:
        print('operator error: too few arguments for \'eq\'...')

def lt():
    count()

    if opPop() >= 2:
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, Number) and isinstance(operand2, Number):
            opPush(operand2 < operand1)
        else:
            print('operator error: top two values in operand stack are not numbers...')
            opPush(operand2)
            opPush(operand1)  # restore stack contents
    else:
        print('operator error: too few arguments for \'lt\'...')

def gt():
    count()

    if opPop() >= 2:
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, Number) and isinstance(operand2, Number):
            opPush(operand2 > operand1)
        else:
            print('operator error: top two values in operand stack are not numbers...')
            opPush(operand2)
            opPush(operand1)  # restore stack contents
    else:
        print('operator error: too few arguments for \'gt\'...')

def psAnd():
    count()

    if opPop() >= 2:
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, bool) and isinstance(operand2, bool):
            opPush(operand1 and operand2)
        else:
            print('operator error: top two values in operand stack are not boolean...')
            opPush(operand2)
            opPush(operand1)
    else:
        print('operator error: too few arguments for \'and\'')

def psOr():
    count()

    if opPop() >= 2:
        operand1 = opPop()
        operand2 = opPop()
        if isinstance(operand1, bool) and isinstance(operand2, bool):
            opPush(operand1 or operand2)
        else:
            print('operator error: top two values in operand stack are not boolean...')
            opPush(operand2)
            opPush(operand1)
    else:
        print('operator error: too few arguments for \'or\'')

def psNot():
    count()

    if opPop() > 0:
        operand1 = opPop()
        if isinstance(operand1, bool):
            opPush(not operand1)
        else:
            print('operator error: top value in operand stack is not boolean...')
            opPush(operand1)
    else:
        print('operator error: too few arguments for \'not\'')


#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    count()
    if opPop() > 0:
        array = opPop()
        if isinstance(array, list):
            opPush(len(array))
        else:
            print('operator error: an argument is not of the correct type...')
            opPush(array)
    else:
        print('operator error: incorrect number of arguments for \'length\'')

def get():
    count()
    if opPop() >= 2:
        index = opPop()
        array = opPop()
        if isinstance(index, int) and isinstance(array, list):
            if index <= len(array) - 1:
                opPush(array[index])
            else:
                print('operator error: index out of range for \'get\'')
        else:
            print('operator error: an argument to get is not of the correct type...')
    else:
        print('operator error: too few arguments for \'get\'')

def getinterval():
    count()
    if opPop() >= 3:
        num = opPop()
        index = opPop()
        array = opPop()
        if isinstance(index, int) and isinstance(num, int) and isinstance(array, list):
            if index + num <= len(array):
                opPush(array[index:index + num])
            else:
                print('operator error: interval out of range in \'getinterval\'')
        else:
            print('operator error: incorrect operand types for \'getinterval\'')
            opPush(array)
            opPush(index)
            opPush(num)
    else:
        print('operator error: too few arguments for \'getinterval\'')

def put():
    count()
    if opPop() >= 3:
        value = opPop()
        index = opPop()
        array = opPop()
        if isinstance(index, int) and isinstance(array, list):
            if index <= len(array) - 1:
                array[index] = value
            else:
                print('operator error: index out of range for \'put\'')
        else:
            print('operator error: an argument to put is not of the correct type...')
            opPush(array)
            opPush(index)
            opPush(value)
    else:
        print('operand error: too few arguments for \'put\'')

def putinterval():
    count()
    if opPop() >= 3:
        array2 = opPop()
        index = opPop()
        array1 = opPop()
        if isinstance(array1, list) and isinstance(index, int) and isinstance(array2, list):
            if len(array2) + index <= len(array1):
                array1[index:len(array2) + index] = array2
            else:
                print('operator error: index is out of range in \'put\'interval')
        else:
            print('operator error: an argument is not of the correct type...')
    else:
        print('operator error: too few arguments for \'putinterval\'')


#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    global opstack
    opstack.append(opstack[-1])  # append the last item in the opstack list.

def copy():
    global opstack
    copyList = list()
    numCopy = opPop()  # get the number of items to copy from the top of the stack
    index = -1
    for i in range(numCopy):
        copyList.append(opstack[index])  # make a list of the top values on the stack
        index -= 1
    copyList.reverse()  # list is made in reverse order, so must reverse it to regain correct order
    opstack += copyList  # append list to the stack

def count():
    global opstack
    opstack.append(len(opstack))  # append the value of the length of opstack

def pop():
    opPop()  # call opPop but ignore the popped value

def clear():
    global opstack
    opstack.clear()

def exch():
    global opstack
    topValue = opstack.pop()  # pop and store the top two values on the stack
    secondValue = opstack.pop()
    opstack.append(topValue)  # append the popped values to swap them
    opstack.append(secondValue)

def mark():
    global opstack
    opstack.append('-mark-')

def cleartomark():
    if '-mark-' in opstack:
        while opstack[-1] != '-mark-':
            pop()
        pop()  # make sure to pop the mark as well!
    else:
        print('cleartomark error: no mark in stack')

def counttomark():
    global opstack
    num = 0
    index = -1

    while opstack[index] != '-mark-':
        num += 1
        index -= 1
    opstack.append(num)

def stack():
    global opstack
    for i in range(len(opstack)):
        print(reversed(opstack)[i])


#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    global opstack
    pop()
    newDict = dict()
    opstack.append(newDict)

def begin():
    global opstack
    global dictstack
    if type(opstack[-1]) is dict:
        d = opPop()
        dictPush(d)

def end():
    dictPop()

def psDef():
    value = opPop()
    name = opPop()

    if isinstance(name, str) and name[0] == '/':
        define(name, value)
    else:
        print('operator error: incorrect operand types for \'def\'')
        opPush(name)
        opPush(value)





def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s.replace('\n', ''))
    
# takes in an item in postscript style and returns the python equivalent
def psToPython(s):
    if s.isnumeric() or s[0]=='-':  # check if the number is alphanumeric or if it starts with -. it should only start with - if it can be parsed as an int
        return int(s)
    elif s=='false':
        return False
    elif s=='true':
        return True
    elif s[0]=='[':
        return psArrayToList(s)
    else:
        return s
# converts a string that is in the form of a postscript array into a python list
def psArrayToList(s):
    res = []
    s = s.strip("[]")
    strlist = s.split()
    for c in strlist:
        res.append(psToPython(c))
    return res


def interpretList(L):
    count()
    startcount = opPop() # find the intial opstack size

    stack = list()
    for item in L: # interpet the code that is in the list, just in case there are any operators in there
        func = getSPSFunction(item)
        if func != False:
            func()
        else:
            opPush(item)
    count()
    endcount = opPop()  # find the new size of the stack

    oL = opstack[startcount:endcount] # find the slice of the list that corresponds to the contents of the interpreted input list
    for i in range(endcount - startcount):
        opPop()  # pop the values from the stack that shouldn't really be there
    return oL


# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner
            # parenthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(psToPython(c))
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(psToPython(c))
    return {'codearray':res}

def psIf():
    code = opPop()
    condition = opPop()
    if condition:
        return interpretSPS(code)

def psIfElse():
    elseCode = opPop()
    ifCode = opPop()
    condition = opPop()

    if condition:
        return interpretSPS(ifCode)
    else:
        return interpretSPS(elseCode)


def psRepeat():
    code = opPop()
    n = opPop()
    for i in range(n):  # repeat n times
        interpretSPS(code)
def forall():
    code = opPop()
    array = opPop()
    for item in array:
        opPush(item)
        interpretSPS(code)

def getSPSFunction(s):
    switcher = {
        'dup': dup,
        'mul': mul,
        'add': add,
        'sub': sub,
        'eq': eq,
        'lt': lt,
        'gt': gt,
        'and': psAnd,
        'or': psOr,
        'not': psNot,
        'length': length,
        'get': get,
        'getinterval': getinterval,
        'put': put,
        'putinterval': putinterval,
        'copy': copy,
        'count': count,
        'pop': pop,
        'clear': clear,
        'exch': exch,
        'mark': mark,
        'cleartomark': cleartomark,
        'counttomark': counttomark,
        'stack': stack,
        'dict': psDict,
        'begin': begin,
        'end': end,
        'def': psDef,
        'if': psIf,
        'ifelse': psIfElse,
        'repeat': psRepeat,
        'forall': forall,
    }
    if isinstance(s, collections.Hashable):  # we can't search our switcher dict using a non hashable value...
        return(switcher.get(s, False))
    else:
        return False



# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
def interpretSPS(code): # code is a code array
    codeList = code.get('codearray', code)
    for item in codeList:
        func = getSPSFunction(item)
        if func != False:
            func()  # if the item is found in the dictionary of operators, call the appropriate function
        else:
            opPush(item)  # otherwise, push the item onto the op stack



# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}': #non matching closing parenthesis; return false since there is
            # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(psToPython(c))
    return {'codearray':res}

def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


input1 = """
            /square {dup mul} def
            0 [-5 -4 3 -2 1]
            {square add} forall
            55 eq false and
        """


def main():

    s = "/sumArray { 0 exch {add} forall } def /x 5 def /y 10 def [1 2 3 add 4 x] sumArray [x 7 8 9 y] sumArray [y 2 5 mul 1 add 12] sumArray"
    s = tokenize(s)
    print(s)
    s = parse(s)
    print(s)
    interpretSPS(s)

if __name__ == '__main__':
    main()


# print(tokenize(input1))
# print(parse(tokenize(input1)))
# print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))

