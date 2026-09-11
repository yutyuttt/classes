print(help(str.upper)) # unbound
print(help("abc".upper)) # bound

x = "abc"
print(x.upper())
print(str.upper(x)) # both work