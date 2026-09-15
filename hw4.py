# method 1
def file_type(s: str):
    substrs = s.split(".")

    if len(substrs) == 1:
        return ""
    else:
        return substrs[-1]

print(file_type("foo.doc"))
print(file_type("foo"))

# method 2
def file_type2(s: str):
    last_dot = s.rfind(".")
    if last_dot == -1:
        return ""
    
    ext = s[last_dot + 1:]
    return ext

print(file_type2("foo.doc"))
print(file_type2("foo"))