import base58

def is_valid_tron(addr: str) -> bool:
    try:
        decoded = base58.b58decode_check(addr)
        return len(decoded) == 21 and decoded[0] == 0x41
    except Exception:
        return False

candidates = [
    "T5V5nhu2cnruBw1KREgawfxi7xcLwBaQbq",
    "TKT6qZESdF2A8pVqtgDnU4h2pmg4WVoBE1",
    "TAoZkKxkMRZsQKfe3xJEXmtgGdZ8ijh4rB",
    "TvP1aNRikCKxwyXCguw1CtbLGipEf5R1Bc",
    "TAEwcQjNAfrAZvex3uu8xZB4epHSEccV7E",
    "ToSpRm2ZPcBjkz69SBDvP58ZHVwd7wmNob",
    "TFicBUQqVDmASxLzkrRa6LMjpZ2zzJePgm",
    "T51ZPbS5v3DFed6NDF5tCkWSsSxuSWpukM",
    "TsiCec6yfw7VGmErLC5ZSq2X4d2vJc1g8V",
    "TCRcWXnsYhJZV9FYaWqmBBJPKYHPVYPZsD",
    "TZJSweZMFP38SguGYcoFeKFb9TA3KAxeuG",
    "TD5HzcZbUkSAjSeFPaUDE1SXE8cfjN6bS3",
    "TxoEvTkKj558GkW7KNnQT93TWb1iDxkNhj",
    "TnkPA8qKCrxFbegsPUppVD7CeaYSyMXxcp",
    "TbauBcvcwUpej6w9GU7C7WB1K9vBykLVAg",
    "TFiy8shP8sbqjV8QnjAyEUxEM9fMEsxEtq",
    "T2BFfrsU4YjRosoYwjviQYZ4ybPUHNs2iT",
    "TGrMNASRZhdCyvjG817XsYAFs2PJxQDcqS",
    "TFLXVksNb54Dxp6gS1HAviRkRNQzuXSXER"
]

found = False
for c in set(candidates):
    if is_valid_tron(c):
        print(f"VALID: {c}")
        found = True

if not found:
    print("NONE VALID")
