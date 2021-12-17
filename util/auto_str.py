def auto_str(cls):
    def __str__(self):
        return '{}({})'.format(
            type(self).__name__,
            ', '.join('{}={}'.format(*item) for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls
