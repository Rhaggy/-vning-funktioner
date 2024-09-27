bas = int(input("Hur stor ska trianglens bas vara? "))

if bas % 2 == 1:
    for i in range(1,bas+1,2):
     print(f"{'*'*(i):^{bas}}")
else:
   print("Inte triangel")