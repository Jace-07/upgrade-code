import hashlib, pickle

 
top_block = { 
    'transacion' : [ 
        { 
            'from' : 'Jace',
            'to' : 'Lucky',
            'amount' : 10
        }, 
        { 
            'from' : 'Mula',
            'to' : 'Jace',
            'amount' : 10
        }, 
        { 
            'from' : 'Lucky',
            'to' : 'Innocent',
            'amount' : 10
        }, 
    ]
}

pickle.dumps(top_block)

m = hashlib.sha3_256()
m.update(pickle.dumps(top_block))
m.digest()
m.hexdigest()

difficulty = 1
difficulty_string = ''.join(['0' for x in range(difficulty)])

nonce = 1
top_block['nonce'] = nonce
p = hashlib.sha3_256()
while p.hexdigest()[:difficulty] != difficulty_string:
    nonce += 1
    top_block['nonce'] = nonce
    p = hashlib.sha3_256()
    p.update(pickle.dumps(top_block))
    print(nonce,  m.hexdigest())
