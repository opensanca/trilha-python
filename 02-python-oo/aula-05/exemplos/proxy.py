"""
Implementa um Proxy que proibe acesso a atributos e métodos começados por `_`
para _simular_ atributos protegidos. Isso é feito sobrescrevendo o método
especial `__getattr__`, conforme visto na classe Proxy.

>>> special = Special(2.5, 200)
>>> special.size
2.5
>>> special._value
200
>>> special._protected()
500.0
>>> proxy = Proxy(special)
>>> proxy.size
2.5
>>> proxy.public()
500.0
>>> proxy._protected()
Traceback (most recent call last):
AttributeError: O atributo não existe ou é protegido '_protected'
"""


class Proxy:
    def __init__(self, obj):
        self._object = obj

    def __getattr__(self, attr):  # obj.attr
        if attr.startswith('_'):
            msg = 'O atributo não existe ou é protegido {!r}'
            raise TypeError(msg.format(attr))

        return getattr(self._object, attr)

    def __setattr__(self, attr, value):  # obj.attr = 'fooo'
        pass

    def __delattr__(self, attr):  # del obj.attr
        pass


class Special:
    def __init__(self, size, value):
        self.size = size
        self._value = value

    def _protected(self):
        return self.size * self._value

    def public(self):
        return self._protected()
