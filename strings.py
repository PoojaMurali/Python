			
1.Find number of characters in the string?
>>>str1="Hello World"
>>> str2="How are you"
>>>print(len(str1)+len(str2))
Ans.22
2. Do string operations upper,lower,split,replace,startswith,endswith?
>>>str1.upper()
'HELLO WORLD'
>>>str2.lower()
'how are you'
>>> print str1.split()   str1=”hello world”
['Hello', 'World']    str1.replace(“hello”,”hi”)
>>>print str2.split(' ' , 1)
['How', 'are you']
>>>print str2.split(' ', 2)
['How', 'are', 'you']
>>> str1.replace("Hello", "hi")
'hi World'
>>> print str2.startswith( 'hello')   str2=”hiworld”
False
>>> print str1.startswith( 'How')
True
>>> print str1.endswith('World')
True
>>> print str2.endswith('yo')
False
3. str2 replace 'you' by 'me'?
>>>str2.replace('you','me')
'How are me'
4. print str1[0]='p', check this operation is performing or not if you face any error why error is happening?
Ans. Because strings are immutable, it cannot be modified but it can be replaced by whole word.
Eg. Hello world can be replaced by Hi world.

5. Swap two strings?
>>> str1, str2 = "Hello World" ,"How are you"
>>> str1, str2 = str2, str1
>>> str2
'Hello World'
>>> str1
'How are you'

6. a="   hello  " Do strip string operation?
>>> print a.strip('l')
hello
>>> a=' hello '
>>> print a.strip('l')
 helo 
>>> a='000hello000' 
>>> print a.strip('0')
Hello
7. a="pooja" convert string a to list?
>>> str1.split()
['how', 'are', 'you']

8. split str1 by space?
>>> string= str1+ " "+str2
>>> print(string)
Hello World How are you
9. Reverse of the string using slicing Concept?
>>>str2[::-1]
'dlroW olleH'
10. Print str1 output as "Hello"?
>>>str2[0:5]
'Hello'