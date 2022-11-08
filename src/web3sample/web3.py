from argparse import ArgumentError
from web3 import Web3
from web3.middleware import geth_poa_middleware


class Web3Handler:
    def __init__(self, web3_url=""):
        if not web3_url:
            raise ArgumentError("Invalid web3 provider")
        self.w3 = Web3(
            Web3.HTTPProvider("https://{web3_url}".format(web3_url=web3_url))
        )
        self.w3.middleware_onion.inject(
            geth_poa_middleware, layer=0
        )  # https://stackoverflow.com/questions/68449832/web3-extradatalength-error-on-the-binance-smart-chain-using-python

    def block_number(self):
        self.w3.eth.getBlock("latest")  # get latest block details
        return self.w3.eth.blockNumber  # get latest block number
