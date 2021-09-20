# Python Pre-work 1-5

# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name)
    print("hello" + user_name.upper())

hello_name("JD")

#Should output, hello_JD

# Another solution

def hello_two(user_name):
    print("Hello " + user_name.upper() + "!")

hello_two("jd")

#Should output, Hello JD!

#Question 2
#Print first 100 odd numbers in Python.

odd_numbers = list(range(1,100,2))
print(odd_numbers)

#Different method

for value in range(1,201,2):
    print(value)

#Third method

odd_nums = list(range(1,101))

for number in odd_nums:
    if number % 2 != 0:
        print(number)
    else:
        print("Even")

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    max = a_list[0]
    for n in a_list:
        if n > max:
            max = n
    return max

#Another method

def max_num_in_list(a_list):
    print(max(a_list))   #or return max(a_list)

#Another method

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_a_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:    
                return True  
        else:
            return True        
    else:
        return False            

#Another method

def is_a_leap_year(a_year)


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

number_list_all = [[1,2,3,4,5,6,7,8],[1,2,3,4,5],[52,63,45,678]]
def is_consecutive(a_list):
    number_check = min(a_list)
    max_number = max(a_list)
    for number == max_number:
        return True
    elif number == number_check+1:
        number_check +=1
    else:
        return False
for list in number_list_all:
    print("Checking list..." + str(list))
    print(is_consecutive(list)) 

#Another method

def is_consec(a_list):
    min_num = min(a_list)
    max_num = max(a_list)
    consecutive = list(range(min_num,max_num+1))
    if a_list == consecutive:
        return True
     else:
         return False
            