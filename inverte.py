str = 'string'

def reverse(str, start, end):
    if(start >= end):
        return 
    str[start], str[end] = str[end], str[start]
    reverse(str, start + 1, end - 1)

str = list(str)
reverse(str, 0, len(str) - 1)

str = "".join(str)
print(str)
