odd_number=0
even_number=0
num = int(input("Enter a number or type 0 to stop: "))
while num!=0:
    if num%2 == 1:
        odd_number += 1
    else:
        even_number +=1
            
    num = int(input("Enter a number or type 0 to stop: "))
        
print("Odd numbers count:", odd_number)
print("Even numbers count:", even_number)