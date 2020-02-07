import pickle

 
block = { 
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
    ]
}

pickle.dumps(block)
