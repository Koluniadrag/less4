def toot(str):
    if len(str) < 2:
        return ""
    else:
        return str[:2] + str[-2:]
