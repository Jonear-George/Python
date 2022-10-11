print("This is program IQ calculate number")
n=int(input(f'Please enter number(>0) :'))
i=1
while n>0:
    sum=(i+i)*(i+i)
    print(f'{i}{i}x{i}{i}={sum}')
    n-=1
    i+=1