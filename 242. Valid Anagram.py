from collections import Counter

text = "cat"
text2 = "ACt"
sum = 0
for i in text:
    sum += ord(i)
for i in text2:
    sum -= ord(i)

if sum!=0:
    print("False")
else :
    print("True")