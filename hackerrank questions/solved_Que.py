# def swap_case(s):
#     result = s.swapcase()
#     return result
# if __name__ == '__main__':
#     s = "HackerRank.com presents 'Pythonist 2'."
#     result = swap_case(s)
#     print(result)


# ********What's Your Name?*********

# def print_full_name(first_name, last_name):
#     if len(first_name) <= 10 and len(last_name) <= 10:
#         print(f"Hello {first_name} {last_name}! You just delved into python.")
#     else:
#         print("Error: Both first_name and last_name should be 10 characters or less.")

# if __name__ == '__main__':
#     first_name = input()
#     last_name= input()
#     print_full_name(first_name, last_name)


# ********Mutation*********

# Eg:-
# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print (string)


def mutate_string(s, i, c):
    return s[:i]+c+s[i+1:]   #or > s= s[:5] + "k" + s[6:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)