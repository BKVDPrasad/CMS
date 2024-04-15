# def dummy(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
#
# dummy('a;lsdkfj;aslkjdf;laskdfj;as',data='a')


# import gevent
#
#
# def foo():
#     """
#     foo
#     """
#     gevent.sleep(2)
#     print('Running in foo')
#     gevent.sleep(6)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     """bar is fun
#     """
#     print('Explicit context to bar')
#     gevent.sleep(1)
#     print('Implicit context switch back to bar')
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

class UpdateVal:
    def __init__(self, vname):
        self.name = vname

    def update_val(self):
        print(self.name)



import threading
obj = UpdateVal(vname='prasad')
val = threading.Thread(target=obj.update_val)
val.start()

