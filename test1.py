class T(object):
    @classmethod
    def t1(cls):
        print('Hello')
    
    def t2(self):
        print('Calling t1...')
        T.t1()


obj1 = T()
obj1.t2()