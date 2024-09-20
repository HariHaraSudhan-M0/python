def binary_search(n,arr,low=0,high=None):
    if high is None:
        high=len(arr)-1
    if low>high:
        return -1
    mid=(low+high)//2#gives only the whole number
    if n<arr[mid]:#mid- gives the position, arr[mid]-gives the value
        return binary_search(n,arr,low,mid-1)
    if n>arr[mid]:
        return binary_search(n,arr,mid,None)
    if n==arr[mid]:
        return mid

arr=[1,2,3,4,5,65,78]
m=binary_search(5,arr)
print(m)
