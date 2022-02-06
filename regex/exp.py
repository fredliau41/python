import re

pattern = r"([qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([AEIOUaeiou]{2,})([qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])"
match_lst = re.finditer(pattern, input())
print(list(match_lst))
print(len(list(match_lst)))
if len(list(match_lst)) > 0:
    for match in match_lst:
        print(match.group(2))
else:
    print("-1")

