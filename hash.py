import hashlib

m = hashlib.sha3_256()
m.update(b'Hello World!')
m.digest()
m.hexdigest()

n = hashlib.sha3_256()
n.update(b'Hello World!')
n.digest()
n.hexdigest()

print(m.hexdigest())
print(n.hexdigest()) 
