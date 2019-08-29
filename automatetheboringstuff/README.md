Automate the Boring Stuff with Python - Notes

Useful resource: pythontutor.com/visualize.html

# Section I: Python Basics

## Part II: Basic Terminology and Using IDLE
* IDLE comes with Python - other popular editors include Sublime and PyCharm
* Expressions = Values and Operators
* Parentheses override precedents
* "ints" and "floats" - complete vs decimals
* adding apostrophes creates a String, unquoted/raw
** add operators to create string concantenations
*** eg; print('Hello' + ' world') becomes 'Hello world'
* assignment statement replaces prior definition
* input() waits for user input
* input always returns a string
* can't do string concantenation on integers - this is how one does math
** eg; int('26') + 1 = 27

## Part III: Writing Our First Program
EXAMPLE: print('You will be ' + str(int(myAge) + 1) + ' in a year.')
---> print('You will be ' + str(int('26') + 1) + ' in a year.')
---> print('You will be ' + str(26+1)+ ' in a year.')
---> print('You will be '27' + ' in a year.')
---> print('You will be 27 in a year.')

Functions learned:
- print - display value passed
- input() - user-created data
- len() - takes a string value and returns an integer value of the string's length
** eg; print(len(myName)) gives the LENgth of characters in the name input 
- str, int, float - convert values' data type

# Section 2: Flow Control

## Part IV: Flow Charts and Basic Flow Concepts
* Boolean data types: True, False
* Comparison Operators: ==, !=, <, >, <=, >=
** integers and strings are never equal to each other, however 
* Boolean Operators: and, or, not
** The 'and Operator's Truth Table': True and True = True, all other combos False
** The 'or Operator's Truth Table': False or False are the only False
** The 'not Operator's Truth Table': evaluates to the opposite Boolean value (not True = False; not False = True)

## Part V: If, Else, and Elif Statements
* Condition: An expression in a flow control statement
** if true, runs the indented code that follows
** you can visualize this step-by-step at pythontutor.com
** indents are referred to as Blocks, and Blocks can contain Blocks etc
*** new blocks begin only after a line ending in a colon:
* If and Else guide through blocks, but Elif allows one to guide through many blocks at once
** can have as many Elif statements as you want! and will print the next block. the rest of the statements following will not be checked
* 'Truthy' and 'Falsey' values: 
** eg: name = input() -> if name:   <-- if anything is input for a name, the 'if name:' statement is 'truthy' and runs the next block
** better to be more specific, eg: if name !='':
** Falsey values are 0, 0.0, and empty strings '' - can check using the bool() function
* Else always comes at the end, executed if all previous conditions have been false


Functions learned:
* bool() returns an equivalent boolean value (True or False) 

## Part VI: While Loops
* So long as the While statements are true, the next block of code executes
* When the execution runs through a loop, we call that an interation. "this while loop iterates x times'
** as opposed to If statements, which execute once and then end
* Possible bug: Infinite loops!
** one fix: break statements - end the loop (doesn't recheck the condition, goes back to start)
** continue statements: skips to the start of the while loop (rechecks the condition)

## Part VII: For Loops
* see forloop_example.py

Functions learned:
* range(101) - range up to but not including 101
** almost interchangeale to a while loop
** range (x, y): x-y range
** step argument: third variable - range (x, y, z) -  range continued up by z

# Section 3: Functions

## Part VIII: Python's Built-in Functions
* first import the function (eg: import random)
** imports the module for the function that exists inside it
** in this example, random.randit imports the random integer function to the program
** can use import * to import all modules in a funciton
* sys.exit function ends the module early
* Third-party modules are installed via pip!
** See Appendix A of this course (automatetheboringstuff/appendixa) for a comprehensive list
* pyperclip: requires install of a clipboard application (eg xclip in linux), then 'import pyperclip' into the shell - then run pyperclip.copy('STRING') and pyperclip.paste() to repaste said string

## Part IX: Writing Your Own Functions
* Mini-program within a program 
* Hugely reduces duplication, excessive copypastas
* Passes strings through functions when called, see hellofunction.py for example
* The 'def' statement defines a function
* Inputs to functions are called Arguments, Output is the return value
* Parameters = variables in between the function's parentheses in the Def statement

Eg:
     >>> 'Hello has ' + str(len('hello')) + ' letters in it.'
     'Hello has 5 letters in it.'

Eg: 
     def plusOne(number):
         return number + 1

     newNumber = plusOne(5)
     print(newNumber)
* When running, result = 6
* Return value is specified using the return statement
* If a function doesn't have a return statement, it defaults to:
** The None Value: similar to True and False - represents a lack of a value
*** prints nothing whatsoever. if your function doesn't have a return value, it defaults to the None value
* can add an 'end' argument to say, the print function, which replaces the newline argument

Eg:
	print('Hello', end='')
	print('World')
	---> HelloWorld

Eg:
	print('cat', 'dog', 'mouse') --> cat dog mouse
	but print('cat', 'dog', 'mouse', sep='ABC') --> catABCdogABCmouse

* Keyword arguments to functions are usually for optional argu,ents. The print() function has keyword arguments 'end' and 'sep'

## Part X: Global and Local Scopes
* A local scope is defined INSIDE a function, eg; 
	def eggs():
		spam = 42 # local variable
* Whereas:
	spam - 42 # global variable
* A variable can't be both local and global. Local variables are temporary and only exist for the lifecycle of a function
* 3 rules: 
** 1. Code in a global scope can't use local variables
** 2. Code in a local scope can access global variables
** 3. Code in one function's local scope cannot use variables in another local scope
** 4. Can use the same name for different variables if they're in different scopes
* Takeaway: local variables exist under the hierarchical nomenclature control of their functions
* Global variables can be run from a local scope:

eg:
	def spam():
		print(eggs)

	eggs = 42
	spam()

--> in this instance, eggs would be considered a global variable 
* if tucked under the local variable statement but wanting to make the variable global, add 'global' as a qualifier before the variable. eg:

	def spam():
		global eggs
		eggs = 'Hello'
		print(eggs)

* Helps streamline whether you need to check local or global code - treat functions as black boxes
* Point is to isolate bugs to particular areas of the program

## Part X1: Try and Except Statements
