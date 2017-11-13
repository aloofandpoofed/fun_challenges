# add the numbers where non-numeric characters behave as delimiters

myStr = 'aa11b33'
numList = ['0','1','2','3','4','5','6','7','8','9']

newStr = ''
newList = []
newList2 = []

for x in myStr:
    if x not in numList:
        x = 'a'
    newStr += x

for x in newStr.split('a'):
    if x != '':
        newList.append(x)

for x in newList:
    y = int(x)
    newList2.append(y)

sum(newList2)
