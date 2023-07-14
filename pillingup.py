t=int(input())
for tc in range(t):
    n=int(input())
    sides=list(map(int,input().split(' ')))
    revsides=sides[::-1] #creating reversed list of sides
    zipped=list(zip(sides,revsides)) #zip'em up
    palindrome=[]
    for i in zipped:
        palindrome.append(max(i))
    a=n//2
    success=0
    for i in range(a):
        if palindrome[i]>=palindrome[i+1]:
            success+=1
            pass
        else:
            print('No')
            break
    if success==a:
        print('Yes')