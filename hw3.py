def dashify_substring(s, sub):
    return s.replace(sub, f"-{sub}-", count=1)

print(dashify_substring("foo", "o"))