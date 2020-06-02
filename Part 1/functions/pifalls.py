from datetime import datetime


def log(msg, *, dt=datetime.utcnow()):
    print(f'{dt}: {msg}')

log('mess 1', dt='2020-06-02 00:00:00:0000')
log('mess 2')
log('mess 3')


def log(msg, *, dt=None):
    if not dt:
        dt=datetime.utcnow()
    print(f'{dt}: {msg}')

log('mess 1', dt='2020-06-02 00:00:00:0000')
log('mess 2')
log('mess 3')