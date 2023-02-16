def compare_version(vers_1: str, vers_2: str):
    if isinstance(vers_1, str) and isinstance(vers_2, str):
        vers_1, vers_2 = int(vers_1.replace('.', '')), int(vers_2.replace('.', ''))
    else:
        return 'Error: type of args must be a string.'

    if vers_1 < vers_2:
        return -1
    elif vers_1 == vers_2:
        return 0
    elif vers_1 > vers_2:
        return 1

# print(compare_version('1.1', '1.10'))