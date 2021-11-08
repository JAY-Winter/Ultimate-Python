
scores = (1,2,3,4,5,6)

low, *others, high = scores


def foo() :
    return 1,2,3,4

val = foo()

print(val)

print(val[1])


a = tuple("python")

print(a)

b = ("b")

print(type(b))

c = ("c",)

print(type(c))