import re
import os
from hashlib import md5

from cPickle \
    import \
        load, dump, dumps

from toydist.core.utils \
    import \
        pprint

class Task(object):
    def __init__(self, name, outputs, inputs, func=None, deps=None):
        if isinstance(inputs, basestring):
            self.inputs = [inputs]
        else:
            self.inputs = inputs
        if isinstance(outputs, basestring):
            self.outputs = [outputs]
        else:
            self.outputs = outputs
        self.name = name or ""
        self.uid = None
        self.func = func
        if deps is None:
            self.deps = []
        else:
            self.deps = deps
        self.cache = None
        self.env = None
        self.env_vars = None
        self.scan = None

    # UID and signature functionalities
    #----------------------------------
    def get_uid(self):
        if self.uid is None:
            m = md5()
            up = m.update
            up(self.__class__.__name__)
            for x in self.inputs + self.outputs:
                up(x)
            self.uid = m.digest()
        return self.uid

    def signature(self):
        if self.cache is None:
            sig = self._signature()
            self.cache = sig
            return sig
        else:
            return self.cache

    def _signature(self):
        m = md5()

        self._sig_explicit_deps(m)
        for k in self.env_vars:
            m.update(dumps(self.env[k]))
        return m.digest()

    def _sig_explicit_deps(self, m):
        for s in self.inputs + self.deps + self.outputs:
            #if os.path.exists(s):
            #    m.update(open(s).read())
            m.update(open(s).read())
        return m.digest()
        
    # execution
    #----------
    def run(self):
        self.func(self)
