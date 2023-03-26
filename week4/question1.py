# lambda is a function is like a variable that can be used to call a function
# it is used to create anonymous functions, i.e. functions without a name

# lambda arguments : expression

f = lambda x: x**2

print(f(5)) # 25

x = [f(i) for i in range(30, 51) if i%2==0]

print(x)

type(f) # <class 'function'>

