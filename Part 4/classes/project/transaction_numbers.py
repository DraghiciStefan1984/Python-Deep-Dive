# class TransactionID:
#     def __init__(self, start_id):
#         self._start_id=start_id
        
#     def next(self):
#         self._start_id+=1
#         return self._start_id

# def transaction_ids(start_id):
#     while True:
#         start_id+=1
#         yield start_id

import itertools

    
class Account:
    # transaction_counter=transaction_ids(100)
    transaction_counter=itertools.count(100)
    
    def make_transaction(self):
        # new_transaction_id=Account.transaction_counter.next()
        new_transaction_id=next(Account.transaction_counter)
        return new_transaction_id