import datetime
import pytz


class Accounts:
    """ Simple account class with balance """

    """
    static method is shared by all instances of the class
    """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        # self.name = name
        # self.balance = balance
        # self.transaction_list = [(Accounts._current_time(), self.balance)]
        self._name = name
        # self._balance = balance
        self.__balance = balance
        self._transaction_list = [(Accounts._current_time(), self.__balance)]
        print("Account created for " + self._name)
        self.show_balance()

    """
    Here we are using class name then the name of the method i.e. self
    even if you call that method with self it will work but their is no advantage to doing so 
    and in fact performance slightly suffers because python will first attempt to find the method in the instance
    namespace and when it fails it then checks the class namespace 
    """
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Accounts._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = 'withdraw'
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))


if __name__ == '__main__':
    # tim = Accounts("Tim", 0)
    # tim.show_balance()
    #
    # tim.deposit(1000)
    # # tim.show_balance()
    # tim.withdraw(500)
    # # tim.show_balance()
    #
    # tim.withdraw(2000)
    # tim.show_transactions()

    steph = Accounts("Steph", 800)
    """
    here it is not stopping us from changing the balance value
    so if you see the balance is not matching the transaction history
    
    so again there is no indication that the client accessing this class shouldn't 
    directly modify the balance data attribute
    so renaming all the three attributes, so that their names start with underscore
    """
    # steph.balance = 200

    """
    here intellij is not giving us any warning when we assign a new value to balance variable 
    so when it comes to classes it is down to us to remember this convention, so the rule is attributes whose 
    name starts with a single underscore are for internal use only.
    """
    # steph._balance = 200

    """
    2 underscores at the start of a name is intended for use when subclassing
    the idea is to prevent the name clashes and it causes Python to perform name mangling 
    on the attribute or method name so that its not accidentally reused by sub class
    
    so now the balance is matching with the transaction history.
    even though the attribute name is correct here, still it is doing some strange things.
    so we will print _dict_ for steph instance and understand what is really going here.
    
    steph has an attribute called underscore underscore balance with a value of $200, 
    now this data attribute was created when we assign the value of 200 to it.
    
    Python didn't find an attribute with that name in steph namespace
    so it looked at the namespace from the class and didn't find it there either now as a result it created a new data attribute
    we have seen that happening earlier with kettle class.
    
    2nd reason is python didn't find the balance attribute is because there is already a data attribute called account balance
    and again that's got the expected value of 700.
    so by prefixing the name balanced with two underscores we are asking python to perform name mangling, so it automatically 
    renames the attribute to start with an underscore and name of the class.
    
    just for information by putting 2 underscores you can't force priate access it doesn't work for one thing and it's still
    possible to access real attribute using the form underscore class-name underscore underscore attribute-name 
    """
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)