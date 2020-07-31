import sys

n = sys.argv[1]
n = int(n)
for i in range(n):
    while i < n:
      i += 1
      if (n > 1) and (i != n):
        print(' ' * (n-i-1), '#' * i)
      elif (n>1) and (i == n):
          print('#' * n)
      else:
          if n == 1:
              print('#')
          break
    break

