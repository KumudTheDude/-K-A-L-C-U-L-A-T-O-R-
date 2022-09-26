print(" ")
print(" ")
print ("                                             69  K A L C U L A T O R  69")
print ("                                                 -------------------" ) 
print(" ")
print ("                                              Press 1 for    + ADDITION")
print ("                                              Press 2 for    - SUBTRACTION")
print ("                                              Press 3 for    x MUTIPLACATION")
print ("                                              Press 4 for    / DIVISION")
print (" ")
print ("                                              Select from above ")
print (" ")
print (" ")


def add():  
    print ("you selected                                 ADDITION  +")
    print(" ")
    print(" ")
    num1 = int(input("   Enter the 1st number :   "))    
    print(" ")    
    num2 = int(input("   Enter the 2nd number :   "))    
    sum = num1+num2
    a = sum -69
    b = 69 -sum
    print(" ")
    print(" ")
    print("--Answer----------------------------------🌦-🌦-🌦--------------------------------------- ")
    print(" ")
    print ("          ++++   The sum of" ,num1, "&" ,num2, "is" , sum, "                           ", num1, "  + ", num2, " = ", sum)
    if sum > 69:
        print(" ")
        print(" ")
        print ("           which is  " ,a, " more than 69")
        print(" ")
        print("            also it is ",sum," more than the chances of you getting some bitches. 🍆") 
        
    else:
        print(" ")
        print(" ")
        print("             which is ", b , " less than 69")  
        print(" ")  
        print("             also it is ",sum," units more than the chances of you getting some Bitches. 🍆 ")
    print(" ")
    print("----------------------------- 🦏  🐪  🐫  🦒  🦘  🦬  🐃 --------------------------------")

def sub():  
    print ("you selected                            SUBTRACTION  - ")
    print(" ")
    print(" ")
    num1 = int(input("   Enter The 1st Number :   "))    
    print(" ")    
    num2 = int(input("   Enter The 2nd Number :   "))    
    sub = num1 - num2
    a = sub -69
    b = 69 -sub
    print(" ")
    print(" ")
    print("--Answer--------------------------------🌦-🌦-🌦--------------------------------------- ")
    print(" ")
    print ("           - - -   The Difference Between" ,num1, "&" ,num2, "is  " ,  sub, "                       ", num1, " - ", num2, " = ", sub    )
    if sub > 69:
        print(" ")
        print(" ")
        print ("           which is  " ,a, " more than  69")
        print(" ")
        print("            also, it is ",sub," more than the chances of you getting some bitches.🍆") 
    else:
        print(" ")
        print(" ")
        print("             which is ", b , " less than 69")  
        if sub<0:    
            print(" ")  
            print("          even tho it is a negative number it is still ",- sub," units more than the chances of you getting some Bitches.🍆")
            print(" ")
            print(" ")
        else :
            print(" ")  
            print("             also, it is ",sub," units more than the chances of you getting some Bitches.🍆")
            print(" ") 
            print(" ")  
    print(" -------------------------------- 🌕  🌖  🌗  🌘  🌑  🌒  🌓  🌔  🌕  --------------------------------- ")        

def multi():  
    print ("you Selected                              MULTIPLICATIION  X")
    print(" ")
    print(" ")
    num1 = int(input("   Enter the 1st number :   "))    
    print(" ")    
    num2 = int(input("   Enter the 2nd number :   "))    
    multi = num1*num2
    a = multi -69
    b = 69 -multi
    print(" ")
    print(" ")
    print("--Answer-----------------------------------🌦-🌦-🌦--------------------------------------- ")
    print(" ")
    print ("         x x x x   The Product of" ,num1, "&" ,num2, "is" , multi,"                         ",num1, " X ",num2, " = ", multi)
    if multi > 69:
        print(" ")
        print(" ")
        print ("           which is  " ,a, " more than 69")
        print(" ")
        print("            also it is ",multi," more than the chances of you getting some bitches.🍆") 
    else:
        print(" ")
        print(" ")
        print("             which is ", b , " less than 69")  
        print(" ")  
        print("             also it is ",multi," units more than the chances of you getting some Bitches.🍆 ")
    print(" " )   
    print(" -------------------------------- 🐂  🐄  🐎  🐖  🐏  🐑  🦙  🐐  🦌 ---------------------------------- ")

def div():  
    print ("yoy selected                            DIVISION   a/b")
    print(" ")
    print(" ")
    num1 = int(input("   Enter the 1st number (numerator) :   "))    
    print(" ")    
    num2 = int(input("   Enter the 2nd number (denominator):   "))    
    div = num1/num2
    a = div -69
    b = 69 - div
    print(" ")
    print(" ")
    print("--Answere-------------------------------🌦-🌦-🌦--------------------------------------- ")
    print(" ")
    print ("          / / /   The product of" ,num1, "&" ,num2, "is" , div, "                           ", num1, "/", num2, " = ", div)
    if div > 69:
        print(" ")
        print(" ")
        print ("           which is  " ,a, " more than 69")
        print(" ")
        print("            also it is ",div," more than the chances of you getting some bitches.🍆 ") 
        
    else:
        print(" ")
        print(" ")
        print("             which is ", b , " less than 69")  
        print(" ")  
        print("             also it is ",div," units more than the chances of you getting some Bitches. 🍆 ")
    print(" ")
    print("-----------------------------🚙  🚌  🚎  🏎  🚓  🚑  🚒  🚐  🛻   🚜  🛵  🏍  🛺-------------------------------")
 

i = 0
while i < 10:
    print(" ")
    print("                                                   Choose next opertaion    1:Add,  2:Subtract, 3:Multiply, 4:Divide")
    print("  ")
    operation_select = int(input("Enter Operation number here:  "))
    print(" ")
    if operation_select == 1: 
        add()   
    if operation_select == 2:
        sub()     
    if operation_select == 3:
        multi()     
    if operation_select == 4:
        div()
    i = 0            
                
