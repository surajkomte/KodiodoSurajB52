string=input("enter word:")
vowels=['A','E','I','O','U','a','e','i','o','u']
a=0
for i in (string):
    if i in vowels:
        a+=1
        print("number of vowel",a)
