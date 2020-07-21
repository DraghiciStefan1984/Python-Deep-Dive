import itertools
from timezone import TimeZone
import numbers


class Account:
    transaction_counter=itertools.count(100)
    _interest_rate=0.5
    _transaction_codes={'deposit':'D', 'withdraw':'W', 'interest':'I', 'rejected':'X'}

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        self._account_number=account_number
        self.first_name=first_name
        self.last_name=last_name

        if timezone is None:
            timezone=TimeZone('UTC', 0, 0)
        self.timezone=timezone

        self._balance=float(initial_balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last')

    def validate_and_set_name(self, attr_name, value, field_title):
        if len(str(value).strip())==0 or value is None:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone instance')
        self._timezone=value

    @property
    def balance(self):
        return self._balance

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number')
        if value<0:
            raise ValueError('Interest rate cannot be negative')
        cls._interest_rate=value