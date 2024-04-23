class ImmutableMeta(type):
    def __setattr__(self, key, value):
        raise AttributeError("Builtin is immutable and cannot be modified.")

    def __delattr__(self, item):
        raise AttributeError("Builtin is immutable and cannot be modified.")

@immutable
class Builtin:
    cls = 'cls',
    clear = 'clear',