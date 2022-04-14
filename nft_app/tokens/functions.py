from web3 import Web3
from web3.middleware import geth_poa_middleware
import os


def get_total_supply():
    w3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_URL')))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    abi = os.getenv('CONTRACT_ABI')
    address = os.getenv('CONTRACT_ADDRESS')

    contract = w3.eth.contract(address=address, abi=abi)
    return contract.functions.totalSupply().call()


def create_token(owner, unique_hash, media_url):
    w3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_URL')))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    abi = os.getenv('CONTRACT_ABI')
    address = os.getenv('CONTRACT_ADDRESS')

    contract = w3.eth.contract(address=address, abi=abi)

    transaction = contract.functions.mint(owner, unique_hash, media_url).buildTransaction()
    transaction.update({'gas': 2000000})
    transaction.update({'nonce': w3.eth.get_transaction_count(os.getenv('MY_ADDRESS'))})
    signed_tx = w3.eth.account.sign_transaction(transaction, os.getenv('PRIVATE_KEY'))

    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return Web3.toHex(tx_hash)
