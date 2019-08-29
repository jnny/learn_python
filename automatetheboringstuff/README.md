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

## Section 5: Writing a Complete Program: Guess the Number

### Part 12: Writing a "Guess the Number" Program

## Section 6: Lists

### Part 13: The List Data Type

### Part 14: For Loops with Lists, Multiple Assignment, and Augmented Operators

### Part 15: List Methods

### Part 16: Similarities Between Lists and Strings

## Section 7: Dictionaries

### Part 17: The Dictionary Data Type

### Part 18: Data Structures

## Section 8: More About Strings

### Part 19: Advanced String Syntax

### Part 20: String Methods

### Part 21: String Formatting

## Section 9: Running Programs from the Command Line

### Part 22: Launching Python Programs from Outside IDLE

## Section 10: Regular Expressions

### Part 23. Regular Expression Basics

### Part 24. Regex Groups and the Pipe Character

### Part 25. Repetition in Regex Patterns and Greedy/Nongreedy Matching

### Part 26. Regex Character Classes and the findall() Method

### Part 27. Regex Dot-Star and the Caret/Dollar Characters

### Part 28. Regex sub() Method and Verbose Mode

### Part 29. Regex Example Program: A Phone and Email Scraper

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
