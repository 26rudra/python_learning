# print("I love to play football")
# print("I can play it anytime")    1
# first_name = "bro"
# second_name = "code"
# full_name = first_name + " " + second_name
# print("hello "+full_name)   #2
# print(type(name))
# age = 21
# age += 1
# print("your age is : "+str(age))
# print(age)
# print(type(age))
# height = 150.5
# print("your height is : "+str(height))
# print(type(height))
# human = True
# print(type(human))
# print("are you a human : "+str(human))     #time:17:01

#  MULTIPLE ASSIGNMENT BY BRO CODE (18:04)
# name , age , attractive = "rudraksh" , 20 , True
# print(name)
# print(age)
# print(attractive)   # if all elements have similar value then below:
# gopu = muniya = raghav = chotu = 20
# print(gopu)
# print(raghav)
# print(muniya)
# print(chotu)
# name = "rudraksh bohra"    #len function also counts spaces so instead of 13 it's going to print 14
# print(len(name))
# print(name.find("r"))      # find function only gives the index of first element to be found for eg i there are 3 r then it will give the index of first r to be found
# print(name.capitalize())      # it will not capitalize the word after space
# print(name.upper())           # will convert into upper case similarly we can use .lower 
# print(name.isdigit())         #return true if our string is numeric value else false
# print(name.isalpha())       # if there is alphabets in string then true but if there is space between two alphabets then it will return false
# print(name.count("r"))        #prints the count of characters within our string
# print(name.replace("r","m"))  # if we want to replace certain character with other character
# print(name*3)            #if we want to print name multiple times

#TYPECASTING IN PYTHON  25:22
# x = 1      #int
# y = 2.0    #float
# z = "3"    #str
# y = int(y)   #this is permanent tye cast in which if we print y we will get it value 2
# print(x)
# print(int(y))   # this is not permanent typecast
# print(z)
# print("x is "+z)
# print("x is "+x)  #it will print error so we have to typecast int and float value in string value in this situation

#HOW WE CAN ACCEPT SOME USER INPUT IN PYTHON(31:00)
# name = input("what is your name?: ")
# age = int(input("how old are you?: "))
# height = float(input("how tall are you?: "))
# age = age + 1
# print("Hello "+name)
# print("you are "+str(age)+" year old")
# print("you are "+str(height)+"cm tall")

#USEFUL FUNCTIONS RELATED TO NUMBERS IN PYTHON(37:09)
# import math
# pi = 3.14  # "import math"   to access these functions
# print(round(pi))   
# print(math.ceil(pi))   # use to rounded up for the particular value
# print(math.floor(pi))  #rounded down for the particular value
# print(abs(pi))         #give the absolute value i.e. how much the value is far from zero
# print(pow(pi, 2))      #print the power of any certain value
# print(math.sqrt(pi))   # to find the square root of any value
# x = 1
# y = 2
# z = 3
# print(max(x,y,z))       # print the maximum of these values
# print(min(x,y,z))       # min for lowest

#STRING SLICING IN PYTHON(41:05)   slicing creates a substring by extracting elements from another string 
# two ways by indexing[] or by slice() function   [start:stop:step] 
# name = "rudraksh bohra"
# first_name = name[0:8]    #can also be done by name[:8]  , empty space will take default start value
# print(first_name)
# second_name = name[9:14]  # can also be done by name[9:] , default stop value
# print(second_name)
# funky_name = name[13:-15:-1]     # we can also do it by name[::-1] or name[13::-1]
# print(funky_name)
# print(name[::2])
#STRING SLICING USING SLICE FUNCTION
# website1 = "http://google.com"
# website2 = "http://linkedIn.com"

# slice = slice(7,-4)

# print(website1[slice])
# print(website2[slice])




