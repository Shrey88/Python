"""==============================================================================================
    rolling back the sql statement from committing in database

    if you have not configured the data source then, it will give you warning message that:
        "No sql data source are configured...."
    the intellij is advising us to configure the data source so that it can check the sql
    statement for us.
=============================================================================================="""
import postgresql_connection
import pytz
import datetime
import psycopg2

conn = postgresql_connection.get_connection()
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
""" =======================================================================
    to create composite key you can have more than one key as primary key 
    
    In you want to create additional keys you kind of just drop the PRIMARY
    from the PRIMARY KEY, instead you use word UNIQUE.
=========================================================================== """
cur.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, "
            "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    @staticmethod
    def _current_time():
        local_time = pytz.utc.localize(datetime.datetime.utcnow())
        return local_time

    def __init__(self, name: str, opening_balance: int = 0.0):
        cur.execute("SELECT name, balance FROM accounts WHERE (name = %s)", (name,))
        row = cur.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cur.execute("INSERT INTO accounts VALUES (%s, %s)", (name, opening_balance))
            cur.connection.commit()
            print("Account created for {}.".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            new_balance = self._balance + amount
            deposit_time = Account._current_time()
            try:
                cur.execute("UPDATE accounts SET balance = %s WHERE name = %s", (new_balance, self.name))
                cur.execute("INSERT INTO history VALUES(%s, %s, %s)", (deposit_time, self.name, amount))
            except:
                cur.connection.rollback()
            else:
                cur.connection.commit()
                self._balance = new_balance

            print("{:.2f} depositor".format(amount/100))
        return self._balance / 100

    def withdrawal(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            new_balance = self._balance - amount
            withdrawal_time = Account._current_time()
            try:
                cur.execute("UPDATE accounts SET balance = %s WHERE name = %s", (new_balance, self.name))
                cur.execute("INSERT INTO history VALUES (%s, %s, %s)", (withdrawal_time, self.name, -amount))
            except:
                cur.connection.rollback()
            else:
                cur.connection.commit()
                self._balance -= amount

            print("{:.2f} withdrawn".format(amount/100))
            return amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdrawal(30)
    john.withdrawal(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael", 8000)
    terryG = Account("TerryG", 4000)

    conn.close()
