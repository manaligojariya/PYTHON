'''Write a Python program to find the first appearance of the substring 'not'
and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string.
'''
def not_poor(mystr1):
  snot = mystr1.find('not')
  spoor = mystr1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    mystr1 = mystr1.replace(mystr1[snot:(spoor+4)], 'good')
    return mystr1
  else:
    return mystr1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
