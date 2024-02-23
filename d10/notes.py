def outer_function(z, x):
    def inner_function(c, d):
        return c + d
    return inner_function(z, x)

result = outer_function(5, 10)
print(result)
