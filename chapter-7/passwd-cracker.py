import string
import itertools

def every_password(n):
    for i in range(0, n):
        for j in itertools.product(string.ascii_lowercase, repeat=n):
            print(j)
                
every_password(3)
  


