def factorial(n):
    i=1 
    fac=1
    if n==0:
        return 1
    for x in range(n):
        fac=fac*i
        i+=1
    return fac
n=input("enter a number: ")
n=int(n)
x=factorial(n)
print(x)

def prime(n):
    for x in range(2,n-1):
        if n%x==0:
            return False
    return True
n=input("Enter another number:")
n=int(n)
print(prime(n)) 


def search(arr,n,key):
    for x in range(n):
           if arr[x]==key:
               return True
    return False           
name=input("enter your name:")
size=len(name)
if name=="Aryan":
    print("invalid")
else:
 print("size is",size,"meters")  
key=input("")  
print(search(name,size,key)) 

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
exit()
        
  