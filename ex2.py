# 1
print(help(str.count))

# 2
txt = "foo.bar.txt"

def last_dot_kept(a: str):
    return a.replace(".", "-dot-", count = a.count(".") - 1)

print(last_dot_kept(txt))