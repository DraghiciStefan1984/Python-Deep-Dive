class MyClass:
    def hello():
        print('hello...')
    
    def instance_hello(self):
        print(f'hello from {self}.')

    @classmethod
    def class_hello(cls):
        print(f'hello from {cls}.')

    @staticmethod
    def static_hello():
        print(f'static hello.')


m=MyClass()

print('\ninstance calls')
# m.hello()
m.instance_hello()
m.class_hello()
m.static_hello()

print('\nclass calls')
MyClass.hello()
# MyClass.instance_hello()
MyClass.class_hello()
MyClass.static_hello()


from datetime import datetime, timezone, timedelta

class TimerError(Exception):
    """Custom timer exception"""


class Timer:
    tz=timezone.utc

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz=timezone(timedelta(hours=offset))

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        self._time_start=self.current_dt_utc()
        self._time_end=None

    def stop(self):
        if self._time_start is None:
            raise TimerError('timer must be started before it can be stopped.')

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('timer has not been started.')
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('timer must be started before and elapsed time can be calculated')
        if self._time_end is None:
            elapsed_time=self.current_dt_utc()-self._time_start
        else:
            elapsed_time=self._time_end-self._time_start
        return elapsed_time.total_seconds()

        


t=Timer()
print(t.current_dt_utc())
print(Timer.current_dt_utc())