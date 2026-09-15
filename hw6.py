def max_char_rep(a: str):
    prev = ""
    count = 1
    max_count = 0

    for char in a:
        if char != prev:
            count = 1
        else:
            count += 1

        max_count = max(count, max_count)
        
        prev = char

    return max_count

print(max_char_rep("abcd"))
print(max_char_rep("abbbcdd"))
print(max_char_rep("abnncddddd"))
print(max_char_rep(""))