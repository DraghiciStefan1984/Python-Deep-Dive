
class Language:
    MAJOR=3
    MINOR=7
    REVISION=4

    @property
    def version(self):
        return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'

    @classmethod
    def cls_version(cls):
        return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'

    @staticmethod
    def static_version():
        return f'{self.MAJOR}.{self.MINOR}.{self.REVISION}'