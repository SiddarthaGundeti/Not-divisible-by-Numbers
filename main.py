a=int(input())
divisible_2=(a%2)!=0
divisible_3=(a%3)!=0
divisible_5=(a%5)!=0
divisible_7=(a%7)!=0
Result=divisible_2 and divisible_3 and divisible_5 and divisible_7
print(Result)
