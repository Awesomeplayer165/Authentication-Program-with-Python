# Password-Program-with-Python

## About

Password program will ask for a password and check against a set of rules.
It will repetitively ask for a password until all rules are met.

The first two rules have been programmed.  Now, it's your turn to program
each rule from #3 to #7.

## Rules
1. At least 12 characters
2. Should have numbers
3. Should have special characters
4. Capital letters
5. Lower case letters
6. Should not include your name
7. Should not have the name password

Create two additional rules of **your own**.

Starting Code:

```python
TOTAL_NUMBER_OF_RULES = 2 #total number of rules going to be checked
NUMBERS = "0123456789"
SPECIALCHARACTERS = "!@#$%^&*()"

rulesMet = 0 #count the number of rules met by the password given

while rulesMet != TOTAL_NUMBER_OF_RULES:
    password = input("Please give me a password: ")
    rulesMet = 0 #reset the number of rules met

    #rule 1
    if len(password)>=12:
        print("Good work!  Your password has enough characters.")
        rulesMet += 1
    else:
        print("It's too short! Has to contain at least 12 characters")

    #rule 2
    found = False 
    for n in NUMBERS:
        if n in password:
            rulesMet += 1
            print("Good work!  Your password contains a number.")
            found = True
            break
    if found == False:
        print("Your password does not contain a number.")
        
```
