import hashlib

password = 'Hello world'

print(hashlib.md5(password.encode()).hexdigest())

# 3e25960a79dbc69b674cd4ec67a72c62
# 25ce4b187210e8addafef4be38f2e724