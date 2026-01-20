def keygen_version1(username: str) -> str:
    key = ""
    for u in username:
        key += str(ord(u))
    return key[:8]

def keygen_version2(username: str) -> str:
    key = ""
    for i, u in enumerate(username):
        if i % 2:
            key += str(ord(u.upper()))
        else:
            key += str(ord(u.lower()))
    return key[:8]

def generate_key(username):
    if not 8 <= len(username) <= 12:
        print("username must be between 8 and 12 characters.")
        quit()
    key = ''
    for i, u in enumerate(username):
        if i % 2:
            key += str(ord(u.upper()))
        else:
            key += str(ord(u.lower()))
    return int(key[2*(len(username)-8):][0:8])

if "__main__":
    print(generate_key("99k1kk22"))
