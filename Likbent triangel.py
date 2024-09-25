bas = int(input("Hur stor ska trianglens bas vara?"))

if bas % 2 == 0:
    print("Kommer inte bli en triangel")
else:
    print("triangel")

n = bas
for i in range(n):
    print(n ="*")