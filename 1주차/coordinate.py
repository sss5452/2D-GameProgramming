Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hello %d % 3.2

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hello %d % 3.2
NameError: name 'hello' is not defined
>>> 'hello %d' % 3.2

'hello 3'
>>> 'hello %f' %3.2
'hello 3.200000'
>>> 'hello %1f' %3.2
'hello 3.200000'
>>> 'hello %1.f' %3.2
'hello 3'
>>> 'coordinate:(%1.f,%1f) %3.145 ,3.2345
SyntaxError: EOL while scanning string literal
>>> 'coordinate:(%1.f,%1f)' %3.145 ,3.2345
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'coordinate:(%1.f,%1f)' %3.145 ,3.2345
TypeError: not enough arguments for format string
>>>  'coordinate:(%1.f,%1f)' %(3.145 ,3.2345)
 
SyntaxError: unexpected indent
>>> coordinate:(%1.f,%1f)' %(3.145 ,3.2345)SyntaxError: unexpected indent
SyntaxError: invalid syntax
>>> 'coordinate:(%1.f,%1f)' %(3.145 ,3.2345)
'coordinate:(3,3.234500)'
>>> 'coordinate:(%1f,%1.f)' %(3.145 ,3.2345)
'coordinate:(3.145000,3)'
>>> coordinate:(%.1f,%.1f)' %(3.145 ,3.2345)
SyntaxError: invalid syntax
>>> 'coordinate:(%.1f,%.1f)' %(3.145 ,3.2345)
'coordinate:(3.1,3.2)'
>>> 