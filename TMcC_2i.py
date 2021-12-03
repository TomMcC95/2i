#  Coding challenge for 2i

#  Tom McClelland

#  In a language of your choice could you please provide
#  code that iterates in multiples of 7 up until 100,
#  then in multiples of 8 up to 200, then multiples of 9 up to 300.
 
#  You have until Sunday to complete the above and send a link
#  to your github, after that your code will be reviewed and we will provide feedback.


#  Solution 1

x = 0
solution_1_list = []

while x <= 100:
    print(x)
    solution_1_list.append(x)
    x += 7

while x <= 200:
    print(x)
    solution_1_list.append(x)
    x += 8

while x <= 300:
    print(x)
    solution_1_list.append(x)
    x += 9

#  Solution 2

y = 0
solution_2_list = []

while y <= 300:
    if y == 0:
        while y <= 200:
            if y == 0:
                while y <= 100:
                    print(y)
                    solution_2_list.append(y)
                    y +=7
            else:
                print(y)
                solution_2_list.append(y)
                y += 8
    else:
        print(y)
        solution_2_list.append(y)
        y += 9

#  Solution 3

solution_3_list = []

i = 0

while i <= 300:
    if i <= 100:
        print(i)
        solution_3_list.append(i)
        i += 7
    elif i <= 200:
        print(i)
        solution_3_list.append(i)
        i += 8
    else:
        print(i)
        solution_3_list.append(i)
        i += 9

# Test solutions to ensure they all provide same answer.

if solution_1_list == solution_2_list == solution_3_list:
    print("SUCCESS")