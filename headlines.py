#Nathan Garino
#7/16/24
#clickbait

#init
import random
#Functions




def headline1():
    name = input("enter a name:")
    number = input("enter a number:")
    return("In an amazing performance " + name + " ate " + number + " hot dogs!!")
def headline2():
    verb = input("enter a verb:")
    company = input("enter a company:")
    animal = input("enter an animal:")
    return("A man from florida was " + verb + " while on his way to " + company + " when he spotted a " + animal + " he then wrestled the " + animal + " to the ground.")

def headline3():
    event = input("enter a famous event:")
    noun = input("enter a noun")
    return("A " + noun + " was discovered to have played a large part in " + event)

def headline4():
    number = input("enter a number:")
    a = random.randint(0,3)
    if a == 0:
        d = "tesla"
    elif a == 1:
        d = "Google"
    elif a == 2:
        d = "apple"
    elif a == 3:
        d = "microsoft"
    return("After massive losses this past week " + d + " has layed off " + number + "000 people from its workforce.")



def headline5():
    problem = input ("enter a problem")
    return("this term the president has vowed to do something about " + problem)
def headline():
    b = random.randint(1,5)
    if b == 1:
        print(headline1())
    elif b == 2:
        print(headline2())
    elif b == 3:
        print(headline3())
    elif b == 4:
        print(headline4())
    else:
        print(headline5())

def article():
    while True:
        headline()
        c = input("want another headline?")
        if c == "no":
            break
#Main
article()



