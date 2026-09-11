def file_type(s: str):
    substrs = s.split(".")

    if len(substrs) == 1:
        return ""
    else:
        return substrs[-1]

print(file_type("foo.doc"))
print(file_type("foo"))