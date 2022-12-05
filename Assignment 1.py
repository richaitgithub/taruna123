#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/
+
6Values = 'hello', -87.8, 6
Expression = *, -, /, +2. What is the difference between string and variable?String:
A string is a type of value that can be stored in a variable. A String is usually words, enclosed with "" , Eg String x ="Welcome to ineuron" x is the Variable, and we declared it as a String, use the single = to assign the text to it.

Variable:
Variables are symbols that you can use to store data in a program. 
3. Describe three different data types.Numeric data type:
In Python, numeric data type represent the data which has numeric value. Numeric value can be integer, floating number or even complex numbers. These values are defined as int, float and complex class in Python.

Sequence data type:
In Python, sequence is the ordered collection of similar or different data types. Sequences allows to store multiple values in an organized and efficient fashion. There are several sequence types in Python –
-> String
-> List
-> Tuple

Boolean data type:
Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false).
4. What is an expression made up of? What do all expressions do?An expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operatorsAn expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operators5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?An expression evaluates to a single value. A statement does not.6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1The bacon variable is set to 22. The bacon + 1 expression does not reassign the value in bacon (that would need an assignment statement: bacon = bacon + 1)
7. What should the values of the following two terms be?
'spam'+'spamspam'
'spam'*3
# In[5]:


'spam'+'spamspam'


# In[6]:


'spam'*3

The values of following two terms should be same.8. Why is eggs a valid variable name while 100 is invalid?variable name cannot begin with number9. What three functions can be used to get the integer, floating-point number, or string
version of a value?The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 +'burritos.'The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator. The correct way is I have eaten ' + str(99) + ' burritos.'.
# In[10]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




