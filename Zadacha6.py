import os
path_to_file = 'C:/Users/Амир/test/Zadacha6/text.txt'
file = open(path_to_file, "r")

try:
    if (os.stat(path_to_file).st_size > 0):
        print("file opened successfully")
    if (os.stat(path_to_file).st_size == 0):
        print("Error: empty file")
except OSError:
    print("cannot open file")

def Sequence(file, c_1, c_2, c_3, b):
    answer_flag = 1
    string = file.read()
    temp_int = ''
    
    if (len(string) == 0):
        print("Error: empty file")
        exit(-3)
    number_of_integers = len(string.split(" "))
    if (number_of_integers < 3):
        print("Error: there are less then 3 integers in file")
    temp_1 = ''
    t1flag = 0
    index = 0
    
    ## Запоминаем первое число в последовательности:
    
    while (t1flag == 0):
        if (string[index] != " ") and (string[index] != '\n'):
            temp_1 += string[index]
        if (string[index] == " ") or (string[index] == "\n"):
            t1flag += 1
            temp_1 = int(temp_1)
        index += 1
    
    ## Запоминаем второе число в последовательности:
    
    temp_2 = ''
    t2flag = 0
    while (t2flag == 0):
        if (string[index] != " ") and (string[index] != "\n"):
            temp_2 += string[index]
        if (string[index] == " ") or (string[index] == "\n"):
            t2flag += 1
            temp_2 = int(temp_2)
        index += 1
    
    ## Начиная с третьего элемента, идём по последовательности, для каждой тройки проверяя рекуррентное соотношение:
    
    for index_ in range(index, len(string)):
        if (string[index_] != " ") and (string[index_] != "\n"):
            temp_int += string[index_]
        if (string[index_] == " ") or (string[index_] == "\n") or (index_ == (len(string) - 1)):
            try:
                current_integer = int(temp_int)
                if ((temp_1 * c_1 + temp_2 * c_2 + current_integer * c_3) != b):
                    answer_flag = 0
            except ValueError:
                pass ## Ignores non-integer character
            temp_1 = temp_2                       temp_2 = current_integer
            temp_int = ''
            
    return answer_flag
            
                    
def Autotest():
    test_file = open("C:/Users/Амир/test/Zadacha6/test.txt", "r")
    answer = Sequence(test_file, 1,1,1,3)
    if (answer == 1):
        print("Autotest passed...Respect+")
    else:
        print("Autotest not passed")
        exit(-1)

Autotest()

c_1 = int(input("Enter c_1: ")) 
c_2 = int(input("Enter c_2: "))   
c_3 = int(input("Enter c_3: "))   
b = int(input("Enter b: "))   
answer = Sequence(file,c_1, c_2, c_3, b)

if (answer == 1):
    print("Integers in sequence satisfy the recurrent ratio")
else:
    print("Integers in sequence dont satisfy the recurrent ratio")
    