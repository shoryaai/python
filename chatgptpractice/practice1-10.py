
# # # # # # # Q1. Even or Odd

# # # # # # # User se ek number input lo aur check karo ki number Even hai ya Odd

# # # # # # sum = input( " whats your fav number ")

# # # # # # sum = 5
# # # # # # print ( type( sum ) )

# # # # # # Q2. Largest Number

# # # # # # User se 3 numbers input lo aur unmein se sabse bada number print karo

# # # # # # sum = input( " type your 3 fav number")

# # # # # sum2 = 5,6,7
# # # # # sum3 = 7
# # # # # print( f" {sum3} is a biggest number ")

# # # # # Q3. Reverse String

# # # # # User se ek string input lo aur usko reverse karke print karo

# # # # s = (" shorya ")
# # # # reversed_s = s[ :: - 1 ]
# # # # print( reversed_s)

# # # # Q4. Multiplication Table

# # # # User se ek number lo aur uska 1 se 10 tak multiplication table print karo.

# # # # sum = 2
# # # # for digits in range ( 2 , 21 , 2 ):
# # # #     print( digits)

# # # #     Q5. Sum of List

# # # # Ek list banao:
# # # # numbers = [10, 20, 30, 40, 50]



# # # # Loop use karke saare numbers ka sum nikalo. sum() function use nahi karna.

# # # sum = [ 10 , 20 , 30 , 40 , 50 ]

# # # total = 0

# # # for num in sum:
# # #      total =  total + sum
# # # print(" total sum:" + total )

# # # Q7. Vowel Counter

# # # User se ek sentence input lo aur count karo ki usmein kitne vowels (a, e, i, o, u) hain

# # # input(" enter your sentence ")

# # # str = (" shorya is a best boy" )
# # # vowels = "aeiouAEIOU"


# # # print("total vowels ": , str )

# # # Q8. Remove Duplicates

# # # Ek list di gayi hai:
# # # numbers = [1, 2, 3, 2, 4, 1, 5, 3]



# # # Duplicates remove karke unique numbers ki list banao.

# # # Expected output:
# # # [1, 2, 3, 4, 5]

# # # Original order maintain karna hai.


# # # number = set[ 1,2,3,2,4,1 ,5,3]
# # # type ( number)
# # # print ( number )

# # # number = { 1,2,3,2,4,1,5,3}
# # # print ( number )

# # # number = list{1,2,3,4,5}
# # # print( number)

# # # Q9. Frequency Counter

# # # Ek string di gayi hai:
# # # text = "banana"

# # # Dictionary use karke har character kitni baar aaya hai, count karo.

# # # Expected output:

# # # text = "{"

# # # " fruit " : "banana",


# # # print(str.count ( fruit ))

# # # Q10. Number Guessing Game

# # # Ek secret number rakho. User ko guess karna hai.
# # # - Guess chhota hai toh Too Low
# # # - Guess bada hai toh Too High
# # # - Sahi hai toh You Won
# # # while loop use karna hai.


# # secretno = 16

# # while True:
 
# #  guess = int(input(" enter your secret number ") )


# # if guess < secretno: 

# #  print(" too low ")

# # input(" enter your secret number ")
# # if guess>secretno:

# #  print(" too high ")

# # input(" enter your number ")
# # if secretno == 16:

# #    print (" you won ")

# # Q11. Second Largest Number

# # Ek list di gayi hai:
# # numbers = [10, 50, 20, 80, 40, 80]

# # List ka second-largest unique number find karo.

# numbers = [ 10, 50 , 20 , 80 , 40 , 80 ]

# print (set( numbers) )

# num = 50
# print (f" biggest second numbers { num }")

# Q12. Prime Numbers

# User se ek number input lo aur 2 se lekar us number tak saare prime numbers print karo.

# Example:
# Input: 10
# Output: 2, 3, 5, 7


for a in range ( 3 , 11 , 2 ):
     print ( a )