def is_isogram(string):
    #your code he
    strings=string.lower()
    if len(strings) != len(set(strings)):
        return False
    else:
        return True