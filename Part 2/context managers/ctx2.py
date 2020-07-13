class CustomManager:
    def __init__(self):
        self.obj=None

    def __enter__(self):
        print('entering context...')
        self.obj='the return object'
        return self.obj

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print('exiting context...')
        if ex_type:
            print(f'an error occurred: {ex_type}: {ex_value}')
        return True


with CustomManager() as obj:
    print('inside context')
    raise ValueError('error')


class Resource:
    def __init__(self, name):
        self.name=name
        self.state=None

class ResourceManager:
    def __init__(self, name):
        self.name=name
        self.resource=None

    def __enter__(self):
        print('entering context')
        self.resource=Resource(self.name)
        self.resource.state='created'
        return self.resource

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print('exiting context')
        self.resource.state='destroyed'
        if ex_type:
            print('error occured!')
        return False


with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')
print(f'{res.name} = {res.state}')