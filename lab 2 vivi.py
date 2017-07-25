Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> "don't" + "forget" + "to" + "conserve" + "water"
"don'tforgettoconservewater"
>>> 'don't + ' forget' + 'to' + ' conserve ' + 'water'
SyntaxError: invalid syntax
>>> "the"*3
'thethethe'
>>> 'the' + 3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'the' + 3
TypeError: Can't convert 'int' object to str implicitly
>>> "the"*3 + "beautiful" + "earth"
'thethethebeautifulearth'
>>> 28"true"
SyntaxError: invalid syntax
>>> a='save'
>>> b='the'
>>> c='planet'
>>> a + ' ' + b + ' ' +c
'save the planet'
>>> test = "Hi! I'm vivian! "'the'
>>> n = "vivian"
>>> type(n)
<class 'str'>
>>> len(n)
6
>>> len(test)
19
>>> test.upper
<built-in method upper of str object at 0x7f9b81caea98>
>>> test.upper()
"HI! I'M VIVIAN! THE"
>>> "HI! I'M VIVIAN! THE"
"HI! I'M VIVIAN! THE"
>>> 
>>> v= "hi! i'm vivian"
>>> v.lower()
"hi! i'm vivian"
>>> v="Hi! I'm vivian"
>>> v.lower()
"hi! i'm vivian"
>>> v.capitalize()
"Hi! i'm vivian"
>>> n="hi ksdkdnfjnh"
>>> n.capitalize()
'Hi ksdkdnfjnh'
>>> v.swapcase()
"hI! i'M VIVIAN"
>>> v.replace("o","i")
"Hi! I'm vivian"
>>> v.replace("i","o")
"Ho! I'm vovoan"
>>> a="meet"
>>> a="MEET'
SyntaxError: EOL while scanning string literal
>>> a="MEET"
>>> b='meet'
>>> c="Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a!=b
True
>>> a!=c
True
>>> b!=c
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> (5+3) == 8
True
>>> 7 == 8
False
>>> 7 != 8
True
>>> (5+3) != 8
False
>>> a!=b
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> my_string = 'alexadamfarahkatamir'
>>>  my_string =“bananayellowthinkhatgreyBIGcalifornia314”
 
SyntaxError: unexpected indent
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314"

>>> my_string[12:17]
'think'
>>> my_string[12:17]
'think'

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>>  my_string[12:17,25:28]
 
SyntaxError: unexpected indent
>>> my_string[12:17,25:28]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    my_string[12:17,25:28]
TypeError: string indices must be integers
>>> my_string[12:17]
'think'
>>> a=my_string[12:17]
>>> b=my_string[24:27]
>>> a+b
'thinkBIG'
>>> a+' ' +b
'think BIG'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> (a+ ' ' +b).upper
<built-in method upper of str object at 0x7f9b81cba830>
>>> (a+ ' ' +b).upper()
'THINK BIG'
>>> 
