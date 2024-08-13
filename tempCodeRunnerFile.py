def reverse(arr):
    n=len(arr)
    i=0
    reverse=""
    for x in range (int(n)):
        a=arr[n-1-i]
        reverse=reverse+a
        i=i+1
    return reverse    
    
arr=input("enter name")
print(reverse(arr))