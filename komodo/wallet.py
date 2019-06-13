import rpc_util.rpc as rpc

def getwalletinfo():
    # id field need to be updated
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getwalletinfo", "params": [] }'
    return rpc.rpc_request(data)

def backupwallet(filename):
    '''
        This method requires that the coin daemon have the 'exportdir' runtime parameter enabled.
        exportdir tells the coin daemon where to store the komodo backup files created through the backupwallet and dumpwallet calls.
        Parameters: the 'destination' filename, saved in the directory set by the exportdir runtime parameter
    '''
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "backupwallet", "params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def dumpprivkey(address):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpprivkey", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

def dumpwallet(filename):
    '''
    This method requires that the coin daemon have the 'exportdir' runtime parameter enabled.
    exportdir tells the coin daemon where to store the komodo backup files created through the backupwallet and dumpwallet calls.
    Parameters: the 'destination' filename, saved in the directory set by the exportdir runtime parameter
    '''
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "dumpwallet", "params": ["' + str(filename) + '"] }'
    return rpc.rpc_request(data)

def getaccount(address):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getaccount", "params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

# getbalance with account is deprecated
def getbalance(account='', minconf=1, includeWatchOnly=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getbalance", "params": ["",1] }'
    return rpc.rpc_request(data)

# getnewaddress with account is deprecated
def getnewaddress(account=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getnewaddress", "params": [] }'
    return rpc.rpc_request(data)

# This is for use with raw transactions, NOT normal use.
def getrawchangeaddress():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getrawchangeaddress", "params": [] }'
    return rpc.rpc_request(data)

def getreceivedbyaddress(address, minconf=1):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getreceivedbyaddress", "params": ["' + str(
        address) + '", ' + str(minconf) + '] }'
    return rpc.rpc_request(data)

def gettransaction(txid, includeWatchOnly=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": ["' + str(txid) + ', ' + str(
        includeWatchOnly) + '"] }'
    return rpc.rpc_request(data)

def getunconfirmedbalance():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "getunconfirmedbalance", "params": [] }'
    return rpc.rpc_request(data)

# This call can take an increased amount of time to complete if rescan is true.
def importaddress(address, label='', rescan=True):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "importaddress", "params": ["' + str(address) + '", "' + str(
        label) + '", ' + str(rescan).lower() + '] }'
    return rpc.rpc_request(data)

# This call can take an increased amount of time to complete if rescan is true.
def importprivkey(privKey, label='', rescan=True):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "importprivkey", "params": ["UwibHKsYfiM19BXQmcUwAfw331GzGQK8aoPqqYEbyoPrzc2965nE", "testing", false] }'
    return rpc.rpc_request(data)

def importwallet(path):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "importwallet", "params": ["' + str(path) + '"] }'
    return rpc.rpc_request(data)

def keypoolrefill(newsize=100):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "keypoolrefill", "params": [' + str(newsize) + '] }'
    return rpc.rpc_request(data)

def listaddressgroupings():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listaddressgroupings", "params": [] }'
    return rpc.rpc_request(data)

# See the lockunspent call to lock and unlock transactions for spending.
def listlockunspent():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listlockunspent", "params": [] }'
    return rpc.rpc_request(data)

def listreceivedbyaddress(minconf=1, includeEmpty=False, includeWatchOnly=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listreceivedbyaddress", "params": [' + str(
        minconf) + ', ' + str(includeEmpty).lower() + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)


def listsinceblock(blockhash='', targetconf=1, includeWatchOnly=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listsinceblock", "params": ["' + str(
        blockhash) + '", ' + str(targetconf) + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)

# listtransactions with account is deprecated
def listtransactions(account="*", count=10, skip=0, includeWatchOnly=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listtransactions", "params": ["*", ' + str(
        count) + ', ' + str(skip) + ', ' + str(includeWatchOnly).lower() + '] }'
    return rpc.rpc_request(data)

def listunspent(minconf=1, maxconf=9999999, addresses=[""]):
    addr_list = "[";
    for addr in addresses:
        # it seems Komodo rpc considers ' and " differently.. so instead of just str(addresses), have to do this
        addr_list += "\"" + str(addr) + "\","
    if (len(addresses) > 0):
        addr_list = addr_list[:-1]
    addr_list += "]";
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "listunspent", "params": [' + str(minconf) + ', ' + str(
        maxconf) + ', ' + addr_list + '] }'
    return rpc.rpc_request(data)

# See the listunspent and listlockunspent calls to determine local transaction state and info.
def lockunspent(unlock=False, txid='', vout=0):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "lockunspent", "params": [' + str(
        unlock).lower() + ', [{"txid":"' + str(txid) + '","vout":' + str(vout) + '}]] }'
    return rpc.rpc_request(data)

def resendwallettransactions():
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "resendwallettransactions", "params": [] }'
    return rpc.rpc_request(data)

# account MUST be set to the empty string "" to represent the default account
# incomplete: does not considers last two parameters: subtractFeeFromAmt and address
def sendmany(account='', amounts={'': 0}, minconf=1, comment='', subtractFeeFromAmt=[""], address=''):
    amount_list = "{";
    for amt in amounts:
        amount_list += "\"" + amt + "\":" + str(amounts[amt]) + ","
    if (len(amounts) > 0):
        amount_list = amount_list[:-1]
    amount_list += "}"
    '''
    subtractFeeFrom_list = "[";
    for addr in subtractFeeFromAmt:
        subtractFeeFrom_list += "\""+str(addr)+"\","
    subtractFeeFrom_list = subtractFeeFrom_list[:-1]
    subtractFeeFrom_list += "]"
    '''
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "sendmany", "params": ["", ' + amount_list + ', ' + str(
        minconf) + ', "' + str(comment) + '"] }'
    return rpc.rpc_request(data)

def sendtoaddress(address='', amount=0.0, comment='', comment_to='', subtractFeeFromAmt=False):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["' + str(address) + '", ' + str(
        amount) + ', "' + str(comment) + '", "' + str(comment_to) + '", ' + str(subtractFeeFromAmt).lower() + '] }'
    return rpc.rpc_request(data)

# This method works only once per daemon start. It can't be used to change the pubkey that has already been set.
def setpubkey(pubKey=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "setpubkey", "params": ["' + str(pubKey) + '"] }'
    return rpc.rpc_request(data)

def settxfee(amount=0.0):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "settxfee", "params": [' + str(amount) + '] }'
    return rpc.rpc_request(data)

def signmessage(address='', message=''):
    data = '{"jsonrpc": "1.0", "id":"curltest", "method": "signmessage", "params": ["' + str(address) + '", "' + str(
        message) + '"] }'
    return rpc.rpc_request(data)