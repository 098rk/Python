# 13. Given a string and a non-negative int n, return a string ouput that is n copies of the original string.
# string_multiplier('Hi', 2) → 'HiHi'
# string_multiplier('Hi', 3) → 'HiHiHi'
# string_multiplier('Hi', 1) → 'Hi'

# s = "Hi"
# a = 2


def string_multiplier(ip_str, num):
    x = ip_str * num
    return x


print(string_multiplier(input("Enter the i/p string you want to multiply: "),
                        int(input("Enter the number by which you want to multiply the string: "))))
