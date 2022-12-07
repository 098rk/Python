# 12. Write a program to find the count of "triple" value in a string.
# A "triple" in a string is a sequence of characters appearing thrice times in a row.
# Return the count of triples in the given string. The triples may overlap
# Sample:
# triple_counter("defXXXdef") returns 1
# triple_counter("zzzabxxxxcd") returns 3 since xxx and xxx is present but in overlapping state
# triple_counter("f") → 0
# =========================================================
s = input("Enter the string :")


def triple_counter(x):
    count = 0
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            count += 1
    return count


print(triple_counter(s))

# =================Vaibhav code===========================
