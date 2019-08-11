import unittest
from Libs.tools import VerifyClass
from Po.MyP2P.BankCard import BankCardApi

class TestBankCard(VerifyClass):
    def setUp(self):
        self.bc = BankCardApi()

    def test001(self):

        # 发送银行卡请求
        result = self.bc.bindBankCard()
        self.verify_json_data(result,'info','保存成功')

    def test002(self):

        result = self.bc.bindBankCard()
        self.verify_json_data(result,'info','该银行卡已存在')


if __name__ == '__main__':
    unittest.main(verbosity=2)
