import hashlib, pickle

 
top_block = { 
    'transacion' : [ 
        { 
            'from' : 'Jace',
            'to' : 'Lucky',
            'amount' : 100
        }, 
        { 
            'from' : 'Mula',
            'to' : 'Jace',
            'amount' : 150
        }, 
        { 
            'from' : 'Lucky',
            'to' : 'Innocent',
            'amount' : 90
        }, 
    ], 
    'last_block' :  n.hexdigest(), 
    'nonce' : 0 
}

pickle.dumps(top_block)

n = hashlib.sha3_256()
n.update(pickle.dumps(top_block())
n.digest()
n.hexdigest()

difficulty = 1
difficulty_string = ''.join(['0' for x in range(difficulty)])

print(difficulty_string)

nonce = 1
top_block['nonce'] = 1
m = hashlib.sha3_256()
while m.hexdigest()[:difficulty] != difficulty_string:
    nonce += 1
    top_block['nonce'] = nonce
    m = hashlib.sha3_256()
    m.update(pickle.dumps(top_block))
    print(nonce,  m,.hexdigest())
