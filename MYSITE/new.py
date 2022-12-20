import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
# entries = list(map(str, input().split()))
  
# For printing the matrix
arr=[]
for i in range(R):
    entries = list(map(str, input().split()))
    arr.append(entries)
arr.reverse()
ans = np.array(arr)
print(ans)