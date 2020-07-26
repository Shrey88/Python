from _decimal import Decimal
from _pydecimal import Decimal

""" *
    *   don't use floating point numbers when it comes to money instead use decimal
    * """

a = Decimal('0.3')
print(a)