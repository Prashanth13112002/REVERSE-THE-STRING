def array_reverse(arr,start,end):
    while(start<end):
        # to swap the arr element
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

a=list(map(int,input().split()))
b=int(input())
c=int(input())
print(array_reverse(a,b,c))

