import unittest
import os
from src.web3sample.web3 import Web3Handler


class Web3Test(unittest.TestCase):
    def setUp(self):
        self.w3_url = os.getenv("WEB3_PROVIDER_URL")

    def test_web3(self):
        print(Web3Handler(web3_url=self.w3_url).block_number())
