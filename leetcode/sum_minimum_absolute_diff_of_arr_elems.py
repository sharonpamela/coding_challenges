# find the sum of the minimum absolute difference
# of each array element
  
def sumOfMinAbDifferences(arr,n):

    if len(arr) < 2:
        return 0

    arr.sort()
    sum = 0
         
    # 1st array element min absolute difference
    sum += abs(arr[0] - arr[1])
         
    # last array element min absolute difference 
    sum += abs(arr[n - 1] - arr[n - 2])

    # min absolute difference for rest
    for i in range(1, n - 1):
        sum += min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1]))

    return sum
         

arr = [4,6,10,1,20,7]
n = len(arr)
print(sumOfMinAbDifferences(arr, n))