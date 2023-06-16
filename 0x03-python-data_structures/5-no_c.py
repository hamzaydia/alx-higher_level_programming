#!/usr/bin/python3
def no_c(my_string):
    return ''.join([i for i in my_string if i.lower() != 'c'])

# Example usage
result = no_c("Hello, World!")  # 'Hello, World!'
print(result)

