import base58

def is_valid_tron(addr: str) -> bool:
    try:
        decoded = base58.b58decode_check(addr)
        return len(decoded) == 21 and decoded[0] == 0x41
    except Exception:
        return False

candidates = [
    "TbQ7VgP59z3tdBAJjQPPB895rntc8BPqeg",
    "TDCziX95AowLZKR6aCDhG7LeF7uMCXEJqw",
    "TmqaqHPAzKCAkDaKsffmXkPHThSfRwZGyu",
    "TsMUcsuKB6CiZxxNAvgFta8HGRgEpZbi8W",
    "TZjLqiUdPRzycR6w7Z75ThkegNmL6gCss3",
    "TEBq3hQaxFxUsjNPpvQoxjZp4yYF5KG5fQ",
    "T4ZvXxw5D97dp8fWpqWEunHrzrUUGXhG4U",
    "TSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E",
    "T7FpqJtEhhieDCvrE2MK5Qk9MyffgQyuxQ",
    "TeSrFAVcM9qco5DfZ9DNXu6hpMRe8Kt8nC",
    "TYHrJ58QZ8B3ajSJhRbCcY6guQ3PDjTbxW",
    "TiXRaRQS7GLGxZTLL1jWhMeoSCf5zmcZkq",
    "TYKxkgJGWbjiZhFivxaeW7rMeZt7QELGVL",
    "TiDkwhYup7J8hpMW9c4k53NrccQFFWKRho",
    "Tu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9",
    "Toemgfj74aRX3swtiouboip5JDLAyDE9F1",
    "TbBby2Dxibuv7ZLW3Bs1QEmM7nHjEANfoh",
    "T7Qm3HNJSyXKEEj8AHNxkY3PK8TS2KJvQ7",
    "TGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5Fv",
    "TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH",
    "TEDvdUDz1FwKim7QXWwmHqtdHnRJfhAxEG",
    "TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhV",
    "TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J",
    "TDFJDKPHsxWPAe2JS32t8Xrh37548Ts2gd",
    "TwDbHJFwq2f3YVk8Xahog1snebWiomiTnk",
    "Ty6iyo5RfuvMTxUj9FVBAyuUEUTARhZy64",
    "TzTgAAAAcSURBVHgBYyAX8P8Hgg9EUfxAE",
    "TkDgoiKzhSjhEomFUBvyYvwHeQkSAbgtxk",
    "TDaZAEbibzzVTSEZmp29gpHMpbA3dBkNxM",
    "TAQYCQRSA4dQFkgAUACHVBeoC1SW6weoog",
    "TviReSuaVq1aseDHjvuQJwxn26oKAV7jBe",
    "Td91tnHTa2owCGvdUptzyQC4Lov6ubsukP",
    "TqCwLJYARWo8BiBKxRwBgBB9GEMwLRSVWg",
    "Tg96eUF4APh3V6DUYZ8wZmkEfCzrgxojHd",
    "TN4hAYdsvg7kfoBDwoNCAASCQoFZW4tSU4",
    "TN4hAYdsvg7kfoBDwoNCAASCQoFZW4tVVM",
    "TnPGeGm8ZuWvc2Ci4T184HiU7UeSqMz2Bj",
    "ThfLy7YLJQh32peDreaFBKZV7XjduPrhkh",
    "TVhTonZfnEChUXQb3EF9WGdyb3FYz9yUpv",
    "TCHFcsY7VqTq35c9zZPzKo7JtfNYVAryfu",
    "TVPDxVq3cCCg28bwLrMjhzp3MHBrk3C7dw",
    "TvCJ7Jd7uwWxC4UGGuvDrXB9h8bGFsvTuk",
    "TQ7ZfHywDmgEmxmRUAY2KU67bgyAnJSWgF",
    "TWrU1hJgv9LKXZeNGejepxnDoE8TZrDm9W",
    "TJasSfR1AnKQMNmzPaCFbYXBxUFPDLB8FV",
    "TGB6QFNGVEKKo3TxTy72w35kxPMgBFic88",
    "Tpn5UVFSkke53hfctJZMPmZgSGZhAYk9Gz",
    "ThD5mGCqU2X6bqBjtPkxPyQbGqoqhGFjft"
]

found = False
for c in set(candidates):
    if is_valid_tron(c):
        print(f"VALID: {c}")
        found = True

if not found:
    print("NONE VALID")
