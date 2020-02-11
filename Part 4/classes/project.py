# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:31:40 2020

@author: Stefan Draghici
"""

import numbers
import itertools
from datetime import timedelta, datetime
from collections import namedtuple


Confirmation=namedtuple('Confirmation', 'account_number transaction_code transaction_id time_utc time')


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip())==0:
            raise ValueError('TimeZone name cannot be empty')
        
        self._name=str(name).strip()
        
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer')
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer')
        if offset_minutes>59 or offset_minutes<-59:
            raise ValueError('Minutes must be between -59 and 59.')
        
        offset=timedelta(hours=offset_hours, minutes=offset_minutes)
        
        if offset>timedelta(hours=-12, minutes=0) or offset>timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00')
        
        self._offset_hours=offset_hours
        self._offset_minutes=offset_minutes
        self._offset=offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name==other.name and
                self._offset_hours==other._offset_hours and
                self._offset_minutes==other._offset_minutes)
        
    def __repr__(self):
        return f'TimeZone(name={self.name}, offset_hours={self.offset_hours}, offset_minutes={self.offset_minutes})'
    

class Account:
    transaction_counter=itertools.count(100)
    _interest_rate=0.05
    _transaction_codes={'deposit':'d', 'withdraw':'w', 'interest':'i', 'rejected':'x'}
    
    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):
        self._account_number=account_number
        self._first_name=first_name
        self._last_name=last_name
        
        if timezone is None:
            timezone=TimeZone('utc', 0, 0)
        self._timezone=timezone
        
        self._balance=float(initial_balance)
        
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def timezone(self):
        return self._timezone
    
    @property
    def balance(self):
        return self._balance
    
    @first_name.setter
    def first_name(self, value):
        self._first_name=self.validate_and_set_name('_first_name', value, 'First Name')
        
    @last_name.setter
    def last_name(self, value):
        self._last_name=self.validate_and_set_name('_last_name', value, 'Last Name')
        
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone instance.')
        self._timezone=value
        
    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate
    
    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number.')
        if value<0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate=value
        
    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts=confirmation_code.split('-')
        if len(parts)!=4:
            raise ValueError('invalid confirmation code')
        transaction_code, account_number, raw_dt_utc, transaction_id=parts
        try:
            dt_utc=datetime.strptime(raw_dt_utc, '%d.%m.%Y-%H:%M')
        except ValueError as ex:
            raise ValueError('Invalid transaction datetime') from ex
        if preferred_time_zone is None:
            preferred_time_zone=TimeZone('utc', 0, 0)
        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError('Invalid TimeZone specified.')
        dt_preferred=dt_utc+preferred_time_zone.offset
        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred)
    
    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')
        if min_value is not None and value<min_value:
            raise ValueError(f'Value must be at least {min_value}.')
        return value
        
    def validate_and_set_name(self, value, attr_name, field_title):
        if len(str(value).strip())==0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)
        
    def generate_confirmation_code(self, transaction_code):
        dt_str=datetime.utcnow().strftime('%d.%m.%YT%H:%M:%S')
        return f'{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_counter)}'

    def deposit(self, value):
        value=Account.validate_real_number(value, min_value=0.01)
        transaction_code=Account._transaction_codes['deposit']
        confirmation_code=self.generate_confirmation_code(transaction_code)
        self._balance+=value
        return confirmation_code

    def withdraw(self, value):
        transaction_code=None
        accepted=False
        value=Account.validate_real_number(value, min_value=0.01)
        if self.balance-value<0:
            transaction_code=Account._transaction_codes['rejected']
        else:    
            accepted=True
            transaction_code=Account._transaction_codes['withdraw']
        confirmation_code=self.generate_confirmation_code(transaction_code)
        if accepted:
            self._balance-=value
        return confirmation_code
    
    def pay_interest(self):
        interest=self._balance*Account.get_interest_rate()/100
        confirmation_code=self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance+=interest
        return confirmation_code