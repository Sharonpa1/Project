max = 1.0
min = 0.0

for i in range(100000):
   one_plus_test = 0
   test = (max + min) / 2.0
   one_plus_test = 1.0 + test

   if one_plus_test == 1:
      min = test
   else:
      max = test

print("The epsilon machine is:", max)
