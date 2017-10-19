import unittest

from SimCard import SimCard


class TestSimCard(unittest.TestCase):

    def setUp(self):
        """
        Create sim card user before each test
        """
        self.user = SimCard(5734)

    def test_add_money_a(self):
        bal = self.user.add_money(30)
        self.assertEqual(50, bal)

    def test_add_money_b(self):
        bal = self.user.add_money(0)
        self.assertEqual(20, bal)

    def test_add_money_c(self):
        bal = self.user.add_money(1000000000)
        self.assertEqual(1000000020, bal)    

    def test_add_money_d(self):
        bal = self.user.add_money(30.25)
        self.assertEqual(50.25, bal)

    def test_add_money_e(self):
        bal = self.user.add_money(-30)
        self.assertEqual(-1, bal)

    def test_check_balance_a(self):
        ch_bal = self.user.check_balance()
        self.assertEqual(19, ch_bal)

    def test_check_balance_b(self):
        self.user.add_money(20)
        ch_bal = self.user.check_balance()
        self.assertEqual(39, ch_bal)

    def test_check_balance_c(self):
        self.user.add_money(0)
        ch_bal = self.user.check_balance()
        self.assertEqual(19, ch_bal)

    def test_check_balance_d(self):
        for i in range(19):
            ch_bal = self.user.check_balance()
        self.assertEqual(1, ch_bal)

    def test_check_balance_e(self):
        for i in range(20):
            ch_bal = self.user.check_balance()
        self.assertEqual(-1, ch_bal)

    def test_check_balance_f(self):
        self.user.send_sms()
        ch_bal = self.user.check_balance()
        self.assertEqual(14, ch_bal)   

    def test_send_sms_a(self):
        s_sms = self.user.send_sms()
        self.assertEqual(15, s_sms)

    def test_send_sms_b(self):
        self.user.add_money(40)
        s_sms = self.user.send_sms()
        self.assertEqual(55, s_sms)

    def test_send_sms_c(self):
        self.user.add_money(0)
        s_sms = self.user.send_sms()
        self.assertEqual(15, s_sms)

    def test_send_sms_d(self):
        for i in range(20):
            print i
            s_sms = self.user.send_sms()
            print s_sms
        self.assertEqual(5, s_sms)

    def test_send_sms_e(self):
        self.user.check_balance()
        s_sms = self.user.send_sms()
        self.assertEqual(14, s_sms)

    def test_make_call_a(self):
        m_call = self.user.make_call(12)
        self.assertEqual(8, m_call)

    def test_make_call_b(self):
        m_call = self.user.make_call(0)
        self.assertEqual(20, m_call)

    def test_make_call_c(self):
        m_call = self.user.make_call(20)
        self.assertEqual(0, m_call)

        def test_negative_make_call(self):
        """
        Negative test
        Make call 60 sec with balance 20
        """
        self.assertEqual(-1, self.user.make_call(60))

class TestSimCardNotAuthorizedUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create not authorized sim card user before each test
        """
        cls.user = SimCard(555)

    def neg_test_check_balance(self):
        user_balance = self.user.check_balance()
        self.assertEqual(-1, user_balance)
        
    def neg_test_add_money(self):
        user_money = self.user.add_money(10)
        self.assertEqual(-1, user_money)
        
    def neg_test_send_sms(self):
        user_sms = self.user.send_sms()
        self.assertEqual(-1, user_sms)
        
    def neg_test_make_call(self):
        user_call = self.user.make_call(15)
        self.assertEqual(-1, user_call)

if __name__ == '__main__':
    unittest.main()
