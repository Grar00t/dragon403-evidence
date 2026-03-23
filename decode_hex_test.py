import base58

hex_bodies = [
    "111d55341baa01db7385ee404994f271561ac8e9",
    "2530b0ff01553915a85b80952bcbcfe51b5ac80a",
    "2f8677bd4655d752ce75d6ac4bc4e9ca09e0bc7a",
    "32a3a44cce0abcf8c5683cdce356bf4c3eb738b1",
    "4b825dc642cb6eb9a060e54bf8d69288fbee4904",
    "570eb82704951a3beeebfa5aa4ca04dc9e4bf44c",
    "65e8c9c7a686fe66f47e7cddb4e3366019e74438",
    "cd43b74fb3e0b35862f8d67015573d1b21118c93",
    "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
    "f3aefeac14e792012845da5af5427a00766eecdf"
]

for body in hex_bodies:
    full_hex = "41" + body
    try:
        addr_bytes = bytes.fromhex(full_hex)
        addr = base58.b58encode_check(addr_bytes).decode()
        print(f"VALID: {addr}")
    except Exception:
        pass
