# numbers=[1,2,-4,-2,3,-9]
# count=0
# for number in numbers:              count postive number
#     if(number>0):
#         count+=1

# print(count)
    

# Numbers=int(input("Enter Numbers"))
# sum=0
                                           # sum of even numbers till n
# for i in range(0,Numbers+1):
#     if(i%2==0):
#         sum+=i
# print(sum)  


# multiplication table but skiping 5th iteration
number=3
for i in range(1,11):
    if i==5:
        continue   # skips the 5th iteration where i==5
    print(number, 'x', i, '=', number*i)