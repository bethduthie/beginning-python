# Warm-Up Excercises
# Lesser of Two Evens
# version 1:
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             result = a
#         else:
#             result = b
#     else:
#         if a > b:
#             result = a
#         else:
#             result = b
#     return result
# version 2:
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)

# Animal Crackers
# Version 1:
# def animal_crackers(text):
#     wordlist = text.split()
#     first = wordlist[0]
#     second = wordlist[1]
#     return first[0] == second[0]

# Version 2:
def animal_crackers(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1[0]

# Makes 20

def makes_twenty(n1, n2):
    return (n1 + n2 == 20) or n1 == 20 or n2 == 20

