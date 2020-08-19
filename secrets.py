import secrets
n=16
print(secrets.token_bytes(n))
print(secrets.token_hex(n))
print(secrets.token_urlsafe(n))
print(secrets.choice('abcdefghijklmnopqrstuvwxyz'))