# Automate the Boring Stuff with Python - Notes

__Table of Contents:__
- [Useful resources: ](#useful-resources-)
- [Section I: Python Basics](#section-i-python-basics)
  - [Part 2: Basic Terminology and Using IDLE](#part-2-basic-terminology-and-using-idle)
  - [Part 3: Writing Our First Program](#part-3-writing-our-first-program)
- [Section 2: Flow Control](#section-2-flow-control)
  - [Part 4: Flow Charts and Basic Flow Concepts](#part-4-flow-charts-and-basic-flow-concepts)
  - [Part 5: If, Else, and Elif Statements](#part-5-if-else-and-elif-statements)
  - [Part 6: While Loops](#part-6-while-loops)
  - [Part 7: For Loops](#part-7-for-loops)
- [Section 3: Functions](#section-3-functions)
  - [Part 8: Python's Built-in Functions](#part-8-pythons-built-in-functions)
  - [Part 9: Writing Your Own Functions](#part-9-writing-your-own-functions)
  - [Part 10: Global and Local Scopes](#part-10-global-and-local-scopes)
- [Section 4: Handling Errors with try/except](#section-4-handling-errors-with-tryexcept)
  - [Part 11: Try and Except Statements](#part-11-try-and-except-statements)
- [Section 5: Writing a Complete Program: Guess the Number](#section-5-writing-a-complete-program-guess-the-number)
  - [Part 12: Writing a "Guess the Number" Program](#part-12-writing-a-guess-the-number-program)
- [Section 6: Lists](#section-6-lists)
  - [Part 13: The List Data Type](#part-13-the-list-data-type)
  - [Part 14: For Loops with Lists, Multiple Assignment, and Augmented Operators](#part-14-for-loops-with-lists-multiple-assignment-and-augmented-operators)
  - [Part 15: List Methods](#part-15-list-methods)
  - [Part 16: Similarities Between Lists and Strings](#part-16-similarities-between-lists-and-strings)
- [Section 7: Dictionaries](#section-7-dictionaries)
  - [Part 17: The Dictionary Data Type](#part-17-the-dictionary-data-type)
  - [Part 18: Data Structures](#part-18-data-structures)
- [Section 8: More About Strings](#section-8-more-about-strings)
  - [Part 19: Advanced String Syntax](#part-19-advanced-string-syntax)
  - [Part 20: String Methods](#part-20-string-methods)
  - [Part 21: String Formatting](#part-21-string-formatting)
- [Section 9: Running Programs from the Command Line](#section-9-running-programs-from-the-command-line)
  - [Part 22: Launching Python Programs from Outside IDLE](#part-22-launching-python-programs-from-outside-idle)
- [Section 10: Regular Expressions](#section-10-regular-expressions)
  - [Part 23. Regular Expression Basics](#part-23-regular-expression-basics)
  - [Part 24. Regex Groups and the Pipe Character](#part-24-regex-groups-and-the-pipe-character)
  - [Part 25. Repetition in Regex Patterns and Greedy/Nongreedy Matching](#part-25-repetition-in-regex-patterns-and-greedynongreedy-matching)
  - [Part 26. Regex Character Classes and the findall() Method](#part-26-regex-character-classes-and-the-findall-method)
  - [Part 27. Regex Dot-Star and the Caret/Dollar Characters](#part-27-regex-dot-star-and-the-caretdollar-characters)
  - [Part 28. Regex sub() Method and Verbose Mode](#part-28-regex-sub-method-and-verbose-mode)
  - [Part 29. Regex Example Program: A Phone and Email Scraper](#part-29-regex-example-program-a-phone-and-email-scraper)
- [Section 11: Files](#section-11-files)
  - [Part 30. Filenames and Absolute/Relative File Paths](#part-30-filenames-and-absoluterelative-file-paths)
  - [Part 31. Reading and Writing Plaintext Files](#part-31-reading-and-writing-plaintext-files)
  - [Part 32. Copying and Moving Files and Folders](#part-32-copying-and-moving-files-and-folders)
  - [Part 33. Deleting Files](#part-33-deleting-files)
  - [Part 34. Walking a Directory Tree](#part-34-walking-a-directory-tree)
- [Section 12: Debugging](#section-12-debugging)
  - [Part 35. The raise and assert Statements](#part-35-the-raise-and-assert-statements)
  - [Part 36. Logging](#part-36-logging)
  - [Part 37. Using the Debugger](#part-37-using-the-debugger)
- [Section 13: Web Scraping](#section-13-web-scraping)
  - [Part 38. The webbrowser Module](#part-38-the-webbrowser-module)
  - [Part 39. Downloading from the Web with the Requests Module](#part-39-downloading-from-the-web-with-the-requests-module)
  - [Part 40. Parsing HTML with the Beautiful Soup Module](#part-40-parsing-html-with-the-beautiful-soup-module)
  - [Part 41. Controlling the Browser with the Selenium Module](#part-41-controlling-the-browser-with-the-selenium-module)
- [Section 14: Excel, Word, and PDF Documents](#section-14-excel-word-and-pdf-documents)
  - [Part 42. Reading Excel Spreadsheets](#part-42-reading-excel-spreadsheets)
  - [Part 43. Editing Excel Spreadsheets](#part-43-editing-excel-spreadsheets)
  - [Part 44. Reading and Editing PDFs](#part-44-reading-and-editing-pdfs)
  - [Part 45. Reading and Editing Word Documents](#part-45-reading-and-editing-word-documents)
- [Section 15: Email](#section-15-email)
  - [Part 46. Sending Emails](#part-46-sending-emails)
  - [Part 47. Checking Your Email Inbox](#part-47-checking-your-email-inbox)
- [Section 16: GUI Automation](#section-16-gui-automation)
  - [Part 48. Controlling the Mouse from Python](#part-48-controlling-the-mouse-from-python)
  - [Part 49. Controlling the Keyboard from Python](#part-49-controlling-the-keyboard-from-python)
  - [Part 50. Screenshots and Image Recognition](#part-50-screenshots-and-image-recognition)
  - [Part 51. Congratulations! (And next steps...)](#part-51-congratulations-and-next-steps)

## Useful resources: 
* [PythonTutor's In-browser Visualizer](https://pythontutor.com/visualize.html)
* [Glossary of Python's Built-in Functions](https://docs.python.org/3/library/functions.html)

## Section I: Python Basics

### Part 2: Basic Terminology and Using IDLE
* [IDLE](https://docs.python.org/3/library/idle.html) comes with Python - other popular editors include [Sublime](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/) and [PyCharm](https://www.jetbrains.com/pycharm/)
* _Expressions_ = _Values_ and _Operators_
* Parentheses override precedents
* "ints" and "floats" - complete vs decimals
* adding apostrophes creates a _String_, unquoted/raw
** add operators to create string concantenations
*** eg; _print('Hello' + ' world')_ becomes 'Hello world'
* assignment statement replaces prior definition
* _input()_ waits for user input
* input always returns a string
* can't do string concantenation on integers - this is how one does math:
```python
int('26') + 1 = 27
```

### Part 3: Writing Our First Program
_EXAMPLE:_ 
```python
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
```
1. print('You will be ' + str(int('26') + 1) + ' in a year.')
2. print('You will be ' + str(26+1)+ ' in a year.')
3. print('You will be '27' + ' in a year.')
4. print('You will be 27 in a year.')

#### Functions learned:
- [print](https://docs.python.org/3/library/functions.html#print) - display value passed
- [input](https://docs.python.org/3/library/functions.html#input) - user-created data
- [len](https://docs.python.org/3/library/functions.html#len) - takes a string value and returns an integer value of the string's length. eg:
```python
print(len(myName)) #  gives the LENgth of characters in the name input 
```
- [str](https://docs.python.org/3/library/functions.html#func-str), [int](https://docs.python.org/3/library/functions.html#int), [float](https://docs.python.org/3/library/functions.html#float) - convert values' data type

## Section 2: Flow Control

### Part 4: Flow Charts and Basic Flow Concepts
* Boolean data types: True, False
* Comparison Operators: ==, !=, <, >, <=, >=
    * integers and strings are never equal to each other, however 
* Boolean Operators: and, or, not
    * The 'and Operator's Truth Table': True and True = True, all other combos False
    * The 'or Operator's Truth Table': False or False are the only False
    * The 'not Operator's Truth Table': evaluates to the opposite Boolean value (not True = False; not False = True)

### Part 5: If, Else, and Elif Statements
* Condition: An expression in a flow control statement
    * if true, runs the indented code that follows
    * you can visualize this step-by-step at https://pythontutor.com
    * indents are referred to as Blocks, and Blocks can contain Blocks etc
        * new blocks begin only after a line ending in a colon:
* If and Else guide through blocks, but Elif allows one to guide through many blocks at once
    * can have as many Elif statements as you want! and will print the next block. the rest of the statements following will not be checked
* 'Truthy' and 'Falsey' values: 
```python
name = input() 
```
* --> if name:   <-- if _anything_ is input for a name, the 'if name:' statement is 'truthy' and runs the next block
    * better to be more specific, eg: if name !='':
* _Falsey values_ are 0, 0.0, and empty strings '' - can check using the bool() function
* _Else_ always comes at the end, executed if all previous conditions have been false

#### Functions learned:
* [bool](https://docs.python.org/3/library/functions.html#bool): returns an equivalent boolean value (True or False) 

### Part 6: While Loops
* So long as the While statements are true, the next block of code executes
* When the execution runs through a loop, we call that an _interation_. "this while loop iterates x times'
    * as opposed to _If_ statements, which execute once and then end
* Possible bug: Infinite loops!
    * one fix: break statements - end the loop (doesn't recheck the condition, goes back to start)
    * continue statements: skips to the start of the while loop (rechecks the condition)

### Part 7: For Loops
* see [forloop_example.py](forloop_example.py)

#### Functions learned:
* [range](https://docs.python.org/3/library/functions.html#range) - range up to but not including 101
    * almost interchangeale to a while loop
    * range (x, y): x-y range
    * step argument: third variable - range (x, y, z) -  range continued up by z

## Section 3: Functions

### Part 8: Python's Built-in Functions
* first import the function (eg: _import random_)
    * imports the module for the function that exists inside it
    * in this example, random.randit imports the random integer function to the program
    * can use _import *_ to import all modules in a function
* [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit) function ends the module early
* Third-party modules are installed via pip!
    * See [Appendix A of this course](https://automatetheboringstuff/appendixa) for a comprehensive list
* [pyperclip](https://pypi.org/project/pyperclip/): requires install of a clipboard application (eg xclip in linux), then 'import pyperclip' into the shell - then run pyperclip.copy('STRING') and pyperclip.paste() to repaste said string

#### Functions learned:
* [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit) - ends the module early

### Part 9: Writing Your Own Functions
* Mini-program within a program 
* Hugely reduces duplication, excessive copypastas
* Passes strings through functions when called, see [hellofunction.py](hellofunction.py) for example
* The _def_ statement defines a function
* Inputs to functions are called Arguments, Output is the return value
* Parameters = variables in between the function's parentheses in the Def statement:
```python
'Hello has ' + str(len('hello')) + ' letters in it.'
```     
becomes:

    Hello has 5 letters in it.

Eg: 
```python
 def plusOne(number):
     return number + 1
newNumber = plusOne(5)
print(newNumber)
```
* When running, result = 6
* Return value is specified using the return statement
* If a function doesn't have a return statement, it defaults to:
** The None Value: similar to True and False - represents a lack of a value
*** prints nothing whatsoever. if your function doesn't have a return value, it defaults to the None value
* can add an 'end' argument to say, the print function, which replaces the newline argument:
```python
print('Hello', end='')
print('World')
```
becomes:

    HelloWorld

Eg:
```python
print('cat', 'dog', 'mouse')
```
becomes:

    cat dog mouse

but:
```python
print('cat', 'dog', 'mouse', sep='ABC')
```
becomes:

    catABCdogABCmouse

* Keyword arguments to functions are usually for optional arguments. The print() function has keyword arguments 'end' and 'sep'

### Part 10: Global and Local Scopes
A local scope is defined INSIDE a function, eg; 
```python
def eggs():
	spam = 42 # local variable
```

Whereas:
```python
spam = 42 # this is a _global_ variable
```
* A variable can't be both local and global. Local variables are temporary and only exist for the lifecycle of a function
#### 3 rules: 
1. Code in a global scope can't use local variables
2. Code in a local scope can access global variables
3. Code in one function's local scope cannot use variables in another local scope
** 4. Can use the same name for different variables if they're in different scopes
* Takeaway: local variables exist under the hierarchical nomenclature control of their functions

Global variables can be run from a local scope:
```python
def spam():
    print(eggs)
eggs = 42
spam()
```
* In this instance, eggs would be considered a global variable 

If tucked under the local variable statement but wanting to make the variable global, add 'global' as a qualifier before the variable. eg:
```python
def spam():
	global eggs
	eggs = 'Hello'
	print(eggs)
```
* Helps streamline whether you need to check local or global code - treat functions as black boxes
* Point is to isolate bugs to particular areas of the program

## Section 4: Handling Errors with try/except

### Part 11: Try and Except Statements
* see [tryandexceptexample.py](tryandexceptexample.py) and [howmanycats.py](howmanycats.py)
* used for Input Validation
* add _try:_ clause before the code - if it throws an error, moves on to the _except_ clause and runs that code
* _except_ clauses can either refer directly to the error (eg _ZeroDivisionError_) or standalone to catch all errors, eg:
```python
def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
```

## Section 5: Writing a Complete Program: Guess the Number

### Part 12: Writing a "Guess the Number" Program
* see [guessthenumber.py](guessthenumber.py) 
* will first need to import the _random_ module
* define input variables (here, they are _name_, _secretNumber_, and _guess_)
** secretNumber = random.randint(1, 20)
* create a _for_ loop for the variable _guessesTaken_ in range(1, 7) -> caps the number of guesses to between 1 and 6
* remember to end the _for_ loop with _else: break_
* remember that any integer variable needs a _str()_ to concatenate

## Section 6: Lists

### Part 13: The List Data Type
* a _list_ contains values, called _items_
* lists are comma-delineated: list = ['x','y','z']
* lists use _integer indexes_ to define items' positions in the list: list[0] --> x
* lists can contain lists, eg: list = [['x','y','z'], [1, 2, 3]]
    * list[0] --> ['x','y','z']
    * list[0][1] --> 'y'
    * list[1][3] --> 3
    * list[0][-1] --> 'z'
    * a _slice_ contains start and end indexes separated by a colon, eg: list[1:2] -> 'y'
        * as such, a slice creates a new list value 
* Assignment variables can also define new list values, eg:
```python
spam = ['cat','turtle','lizard']
spam[2] = 'iguana'
spam
```
returns: [cat','turtle','iguana']

and redefining _spam_ as a _slice_ redefines the variables up to but not including the end of the slice. eg:
```python
spam[1:3] = ['RAT', 'pigeon','tigress']
spam
```
returns: ['cat', 'RAT', 'pigeon', 'tigress']

and spam[:2] returns ['cat', 'RAT']

and spam[1:] returns ['RAT', 'pigeon', 'tigress'].

* We can delete an item using _del_:
```python
spam = [1, 2, 3]
del spam[1]
spam
````
which would return [1, 3]

* Lists can also be treated as strings - eg; len([1,2,3]) -> 3, and [1,2,3] * 3 --> [1,2,3,1,2,3,1,2,3]
* Can find an item using _in_, eg: 'RAT' in ['RAT', 'pigeon', 'tigress'] --> True
    * Can do the opposite with _not in_ 

#### Functions learned:
* [list](https://docs.python.org/3/library/functions.html#func-list) - breaks up the value into its components in a list

### Part 14: For Loops with Lists, Multiple Assignment, and Augmented Operators
* Range Objects, eg range(4) is a "list-like" data type (sequences)
* the third integer in the range list is the step vale. eg: range(1, 100, 2) outputs a list from 1 to 100 increasing by 2 each time
```python
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies(i))

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```

Multiple Assignments:
* multiple variables separated by commas on the left side of the list, eg:

```python
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
size
>>> fat
color
>>> orange
disposition
>>> loud
```

Swapping Variables
* multiples variables on either side of the =
** eg: a, b = b, a will swap the variables 

Augmented Assignment Operators
* shortcut for reassigning variable name, eg:
```python
spam = 42
spam = spam + 1
spam += 1 --> spam = 44
```

Augmented assignment statements:
* +=
* -=
* *=
* /=
* %=

### Part 15: List Methods
* like functions, except methods are attached to certain values
* how to use: variable.method, eg:
**  spam.index('x') gets you the position of x in the spam list 
* append(): add new values to a list
* insert(position, value): insert new value in place of position x
* remove(): removes a value entirely from the list
** unlike the _del_ statement, which deletes a value as defined by its position in the list
* list methods only act on the first instance of a variable
* sort(): automatically puts a list in order from least to greatest, or alphabetically if strings
** can add a _reverse_ element to reverse the order: spam.sort(reverse=True)
** upper case values come before lower case unless you add a _key=(str.lower)_ element 

### Part 16: Similarities Between Lists and Strings
* can do many of the same things with both lists and strings
* however, while a list is mutable, a string is immutable - cannot be changed
** to modify a sring, use slices. Eg:
```python
name = "Zophie a cat"
newName = name[0:7] + 'the' + name[8:12]
>>> Zophie the cat
```
* any string, once defined, stores the reference even if the variables are changed afterwards. Eg:
```python
spam = 42
cheese = spam
spam = 100
>>> spam
100
>>> cheese
42
```
* "variables don't contain lists per se, just references to the lists" 
* "Immutable values don't have this problem because they can't be modified 'in place'. They can only be replaced by new values."

#### Passing Lists in Function Calls
* When passing a list argument to a function, you're actually passing the list _reference_
* Changes made to a list in a function will affect the list outside the function

_copy.deepcopy() Function_: duplicates the list and returns a reference to that new list. Eg:
```python
spam = ['A','B','C','D']
cheese = copy.deepcopy(spam)
```
* now we can make changes to the new list, cheese, while the spam list retains its original properties

Line Continuation:
* when defining a list, can continue to the next line to make things line up nicely, either by defining each item followed by a comma, or through the use of _+ \_ at the end of a line

More info:
*["Facts and Myths about Python names and values"](https://youtu.be/_AEJHKGk9ns) by Ned Batchelder

## Section 7: Dictionaries


### Part 17: The Dictionary Data Type
Dictionaries are composed of many values, called key-value pairs, wrapped in curly brackets - eg:
```python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
```
* Lists are unordered
* _keys_ method: list(listName.keys()) - lists all keys
* _values_ method: list(listName.values()) - lists all values
* _items_ method: list(listName.items()) - lists all key-value pairs (items or _tuples_)
* for _for loops_, can call tuples and assign to variables eg:
```python
for k, v in eggs.items():
    print(k, v)
```
* _tuples_: the same thing as lists, except they are immutable and use parentheses instead of square brackets
* _get_ method: takes two arguments: the key of the value and fallback default value returned if that key isn't in the dictionary, eg:
```python
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.get('age', 0)
8
>>> eggs.get('color','')
''
```
* _setdefault_ method: a way to define a default variable in one line of code, eg:
```python
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'Zophie', 'color': 'black', 'species': 'cat', 'age': 8}
```
* can't change the default pair once created
* _.upper_: returns an uppercase form of the string
* _'''_: enables you to input many lines unformatted
* _pprint()_: pretty print module to list items in a dictionary alphabetically.  must prepend your code with 'import pprint'
* _pformat()_: pprint function to return items as a string rather than a long column list
 

### Part 18: Data Structures
* a dictionary could contain multiple lists of key-value pairs
* additional lists can be added to a dictionary using the .append method
* in Al's tic-tac-toe example, _x_ and _o_ are the values, with keys indicating position (top-left, bottom-middle, etc)
* define a function that will use the data structure, eg:
```python
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + | + board('top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + | + board('mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + | + board('low-R'])
```
* type(VALUE) will tell you the class of a value (int, str, dict, etc)

## Section 8: More About Strings

### Part 19: Advanced String Syntax
* escape characters: let you use both single and double quotes in a string
    * \' - single quote
    * \" - double quote
    * \t - Tab
    * \n - Newline
    * \\ - Backslash
* raw string: place a lower-case 'r' before the string: print(r'That is Carol's cat') will include the \
* multi-line: triple double-quotes, """ surround the strings split accross multiple lines
* strings can be treated just like lists - you can find the position (spam[1]), take out slices (spam[1:4]), in/not in, etc

### Part 20: String Methods
* string methods return a new string value rather than modify in place (as they're immutable)
* use _.lower_ method to ignore casing in input value
* _.isupper_ and _.islower_ to ask if a string is all upper- or lower-case
* Can call the method after the string to redefine the string, eg 'Hello'.upper().isupper() evaluates to True

Other string methods:
    * _isalpha()_ - letters only
    * _isalnum()_ - letters and number only
    * _isdecimal()_ - numbers only
    * _isspace()_ - whitespace only
    * _istitle()_ - titlecase only
    * _.startswith_ - beginning characters of a string
    * _.endswith()_ - ending characters of a string
* Can also use an index point to see if value is true only at a point in a string, eg: 'Hello world!'[5].isspace() returns True
* _.join_ - used to join a value in between a list of strings, eg: ', '.join(['cats', 'rats', 'bats']) returns "cats, rats, bats"
* _.split_ - splits up a string by whitespace characters, or a defined value eg .split('m')
* _.rjust()_ - right-justify(totalcharacterlength, separatedBy)
* _.ljust()_ - left-justify(totalcharacterlength, separatedBy) eg; .ljust(10, '*')
* _.center()_ - same as above but centers
* _.strip()_, _.lstrip()_, _.rstrip()_ - removes whitespace or whatever valkue is specified inside ()
* _.replace(characterToReplace, replacementCharacter)

pyperclip
* pyperclip.copy('TEXT') copies TEXT to the clipboard
* pyperclip.paste will paste from the clipboard

### Part 21: String Formatting
* also called String Interpellation: use %s conversion specifiers to indicate a value:
    * 'Hello &s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)

## Section 9: Running Programs from the Command Line

### Part 22: Launching Python Programs from Outside IDLE
All programs begin with a She-bang line:
```python
#! /usr/bin/python3
```

* Batch Files / Shell Scripts: run multiple commands, ends in .bat
* %* - forward any command line arguments to this program
* PATH Environment Variables - list of source folders from which to launch programs

## Section 10: Regular Expressions

### Part 23. Regular Expression Basics
* Mini-programming language for specifying text patterns
* _import re_ module imports the regular expressions module
* _re.compile()_ - where to pass raw strings, eg:
```python
import re

message = 'Call me at 415-555-1234 tomorrow, or at 415-555-9999.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d)

mo = phoneNumRegex.search(message)

print(mo.group())
```
* mo = 'match object' - returned if a pattern is found
   * mo.group() - returns the actual matched text from the searched string
* _.findall_ - will find every occurrence of a pattern in a given string (eg: phoneNumRegex.finall('Call me at 415-555-1234')

### Part 24. Regex Groups and the Pipe Character
* add parentheses to create _groups_ in the regex, then you can use the group() match object to get matching text from one group, eg:
```python
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo.groups()
'415', '555-1234
>>> mo.group(1)
'415'
>>> mo.group(2)
555-1234
>>> mo.group(0)
'415-555-1234'
>>> areaCode, mainNumber = mo.groups()
>>> print(areaCode)
415
``` 
* escape parentheses with a backslash
* Pipes (|) - used to match one of many expressions, eg: >>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

### Part 25. Repetition in Regex Patterns and Greedy/Nongreedy Matching
* _?_ - flags preceding group as an optional pattern match, eg:
```python
phoneRegex = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
>>>phoneRegex.search('My phone number is 555-1234. Call me.')
<_sre.SRE_Match object; span=(19, 27), match='555-1234'>
```
* _*_ - star character means to match 0 or more times (endless part of the pattern, eg 'batwowowowowman'
* _+_ - must appear at least once
* _{x}_ - must match x number of times in a row
* _{x,y}_ - match a range of repetitions between x and y
* 'Greedy' matching means regex will by default find the longest possible match
* _{}?_ = 'Non-greedy' matching, will find the shortest matching string  

### Part 26. Regex Character Classes and the findall() Method
* _findall()_ method: search a regex string for all matches
```python
>>> import re
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneRegex
re.compile(`\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
```
* phoneRegex.search(dataDefined) - returns a _match object_
* phoneRegex.finall(dataDefined) - returns all strings (matches) in the data
** if there are groups (marked with parentheses), findall will return tuples - $

character classes:
* \d - any numeric digit form 0 to 9
* \D - any character NOT a numeric digit from 0-9
* \w - any letter, numeric digit, or the underscore character ("words")
* \W - any character NOT a letter, numeric digit, or the underscore character
* \s - any space, tab, or newline character ("space")
* \S - any character NOT a space, tab, or newline
* + = one or more
* * = zero or more
* ? = 0 or 1 occurences
* [character classes, eg; ranges] - such as: [aeiou], [a-f], [a-z], [a-fA-G]
* ^ = inverted character classes - so anything that's NOT inside the brackets

### Part 27. Regex Dot-Star and the Caret/Dollar Characters
* ^ - match must start at the beginning of the searched text
* $ - at end of regex to indicate it must match at the end of the searched text
* if you have both ^ and $, must begin and end entirely with the regex in betwe$
* . = any character except for newline
* .* to match anything - any pattern whatsoever!
* .*? - non-greedy match, eg: 
```python
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>'
nongreedy.findall(serve)
['To serve humans']

vs:
greedy = re.compile(r'<{.*}>')
greedy.findall(serve)
['To serve humans> for dinner.']
```
* _re.DOTALL_ = dot means everything, including newlines
* _re.IGNORECASE_ - or re.I for short

### Part 28. Regex sub() Method and Verbose Mode
* _sub_ method - basically a find and replace: 
```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('REDACTED','Agent Alice gave the secret document to Agent Bob.')
'REDACTED gave the secret documents to REDACTED.'
    # or match some of the text with:
>>> agentNamesRegex = re.compile(r'Agent (\w*)\w*')
#                                          ^match first letter/#
namesRegex.sub(r'Agent \1******', 'Agent Alice gave the secret documents to Agent Bob.')
'Agent A**** gave the secret documents to Agent B****.'
```  
* _re.VERBOSE_ - can expand the code onto separate lines, add whitespace and comments. add at end of function eg (r'\d\d, re.VERBOSE)
* pass multiple arguments, eg re.DOTALL | re.IGNORECASE using the bitwise operator '|'

### Part 29. Regex Example Program: A Phone and Email Scraper
```python
import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(	# put all of the below into ONE group to satisfy findall()
((\d\d\d)|(\(\d\d\d\)))?    	# area code (optional)
(\s|-)	# first separator
\d\d\d	# first 3 digits
-	# seperator
\d\d\d\d	# last 4 digits
(((ext(\.)?\s)|x)	# extension word-part (optional)
  (\d{2,5}))?	# extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+	# name part
@	# @ symbol
[a-zA-Z0-9_.+]+ # domain name part 

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.finall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
```


## Section 11: Files

### Part 30. Filenames and Absolute/Relative File Paths

### Part 31. Reading and Writing Plaintext Files

### Part 32. Copying and Moving Files and Folders

### Part 33. Deleting Files

### Part 34. Walking a Directory Tree

## Section 12: Debugging

### Part 35. The raise and assert Statements

### Part 36. Logging

### Part 37. Using the Debugger

## Section 13: Web Scraping

### Part 38. The webbrowser Module

### Part 39. Downloading from the Web with the Requests Module

### Part 40. Parsing HTML with the Beautiful Soup Module

### Part 41. Controlling the Browser with the Selenium Module

## Section 14: Excel, Word, and PDF Documents

### Part 42. Reading Excel Spreadsheets

### Part 43. Editing Excel Spreadsheets

### Part 44. Reading and Editing PDFs

### Part 45. Reading and Editing Word Documents

## Section 15: Email

### Part 46. Sending Emails

### Part 47. Checking Your Email Inbox

## Section 16: GUI Automation

### Part 48. Controlling the Mouse from Python

### Part 49. Controlling the Keyboard from Python

### Part 50. Screenshots and Image Recognition

### Part 51. Congratulations! (And next steps...)
