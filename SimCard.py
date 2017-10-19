class SimCard(object):
    """
    Class SimCard describes sim card behaviour
    """
    is_authorized = False
    balance = 20

    def __init__(self, pin):
        if pin == 5734:
            self.is_authorized = True

    def add_money(self, money):
        if not self.is_authorized:
            print "You are not authorized"
            return -1
        self.balance += money
        return self.balance

    def send_sms(self):
        if not self.is_authorized:
            print "You are not authorized"
            return -1
        if self.is_authorized and (self.balance > 5):
            self.balance -= 5
            print "Sms, was sent. It cost you 5, you balance is:", self.balance
            return self.balance
        else:
            print "You don't have enough money to send sms"
            return -1

    def check_balance(self):
        if not self.is_authorized:
            print "You are not authorized"
            return -1
        if self.is_authorized and (self.balance > 1):
            self.balance -= 1
            print "Ha-ha, I shoot -1 for checking, you balance is:", self.balance
            return self.balance
        else:
            print "You don't have enough money to check balance"
            return -1

    def make_call(self, call_duration):
        """
        Allows to make call
        :param call_duration: int in seconds
        :return: balance
        """
        if not self.is_authorized:
            print "You are not authorized"
            return -1
        if self.is_authorized and (self.balance > call_duration):
            self.balance -= call_duration
            print "Call, was successful. You balance is:", self.balance
            return self.balance
        else:
            print "You don't have enough money to check balance"
            return -1

if __name__ == "__main__":
    user = SimCard(5734)
