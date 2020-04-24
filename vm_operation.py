operationObjectList = [
    {
        'operation':'CREATE',
        'targetStatus':'ACTIVE',
        'requiredStatus':['BUILD'], #Note: OpenStack should refactor this status to INITIALIZE
        'params':{'flavor':'m1.small'}
    },
    {
        'operation':'SUSPEND',
        'targetStatus':'SUSPENDED',
        'requiredStatus':['ACTIVE','SHUTOFF'],
        'anonymousFunction':lambda instance: instance.suspend()
    },
    {
        'operation':'RESUME',
        'targetStatus':'ACTIVE',
        'requiredStatus':['SUSPENDED'],
        'anonymousFunction':lambda instance: instance.resume()
    },
    {
        'operation':'STOP',
        'targetStatus':'SHUTOFF', #STOPPED
        'requiredStatus':['ACTIVE','SHUTOFF', 'RESCUED'],
        'anonymousFunction':lambda instance: instance.stop()
    },
    {
        'operation':'SHELVE',
        'targetStatus':'SHELVED_OFFLOADED',
        'requiredStatus':['ACTIVE', 'SHUTOFF', 'SUSPENDED'],
        'anonymousFunction':lambda instance: instance.shelve()
    }
]