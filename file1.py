# write a function that squares a given number n

# Function syntax
# def <name>(<args>):
#   <statement>

def square(itself):
    square_of_itself = itself * itself
    return square_of_itself

def main():
    val2  = square(23)
    print(val2)


print("Hi")
main()


# while
# Syntax:
# while <condition>:
#   <statement>
# While statement runs until the condition is false
# While statement runs as long as the condition is true

i = 1
while i <= 3:
    print("Hi")
    i = i + 1


# i = 1
#
# python add/subtract/  hacker rank
a = 3
b = 5
print(a + b)
print(a - b)
print(a * b)
# python division hacker rank
print(a//b)
print(a/b)

# hacker rank
def is_leap(year):
    # If the year is divisible by 4 and there is no remainder then it is a leap year 
    # OR If the year is divisible by 100 and the remainder is 0 with also 400 having a remainder of 0 when divided by 4,
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else:
                leap = False    
        else:
            leap = True              
    else:
        leap = False
        
    return leap

    
year = int(input())
print(is_leap(year))