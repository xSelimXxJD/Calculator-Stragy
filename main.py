#import
import sys
import time

#1 by 1
def printy(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

printy("Before we start, please choose your language")
time.sleep(1)
printy("Enter the number beside the language you want")
time.sleep(1)
language=int(input("[1] English"))

#English
if language==1:
 printy("Hello! Im A Calculator. My Name Is Stragy")
 time.sleep(1)
 printy("You can calculate 4 types of method")
 time.sleep(1)
 printy("Please type the number of the method you want")
 time.sleep(1)
 x = int(input("[1] Addition [2] Subtraction [3] Multiplication   [4] Division :"))

#Addition
 if x == 1:
  printy("Ok, so you want the Additon method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a+b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a + b)
  time.sleep(1)
  r = input("Are you happy with the answer?(y/n) :")
  if r == "y" or r == "Y":
      print("Hehe, Im Calculator")
  elif r == "n" or r == "N":
        print("Why????")
  else:
    print("See You Next Time!")

#Subtraction
 elif x == 2:
  printy("Ok, so you want the Subtraction method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a-b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a - b)
  r = input("Are you happy with the answer?(y/n) :")
  if r == "y" or r == "Y":
      print("Hehe, Im Calculator")
  elif r == "n" or r == "N":
      print("Why????")
  else:
    print("See You Next Time!")

#Multiplication
 elif x == 3:
  printy("Ok, so you want the Multiplication method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a×b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  print("Aha! The answer is", a * b)
  r = input("Are you happy with the answer?(y/n) :")
  if r == "y" or r == "Y":
   printy("Hehe, Im Calculator")
  elif r == "n" or r == "N":
   printy("Why????")
  else:
   printy("See You Next Time!" )

#Division
 elif x == 4:
  printy("Ok, so you want the Division method")
  time.sleep(1)
  printy("Look carefully the format is like this")
  time.sleep(1)
  printy("“ a÷b=c　“")
  time.sleep(1)
  a = int(input("What you want <a> to be? :"))
  b = int(input("What you want <b> to be? :"))
  printy("Calculating....")
  time.sleep(2)
  try:
    ans = a/b
    print("Aha! The answer is", a / b)
    r = input("Are you happy with the answer?(y/n) :")
    if r == "y" or r == "Y":
        printy("Hehe, Im Calculator")
    elif r == "n" or r == "N":
        printy("Why????")
    else:
        printy("See You Next Time!")
  except:
      printy("An error has been detected, pleasetry again")


#Error
 else:
  printy("Hey! This is not a valid number!")
  printy("Please try again")

else:
  printy("This language doesn't exist")