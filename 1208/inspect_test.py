import inspect
def func():
    pass


result = inspect.getmembers(func)
for k, v in result:
    print(f'{k}=>{v}')



'''

【実行結果】例
__annotations__=>{}
__call__=><method-wrapper '__call__' of function object at
0x7f3f66c8f620>
__class__=><class 'function'>
__closure__=>None
__code__=><code object func at 0x7f3f68b468a0, file
"/home/yoshimura/Dropbox/2020 Trident/前期/講義資料/python/Python
Scripts/13scope/inspect_test.py", line 3>
__defaults__=>None
__delattr__=><method-wrapper '__delattr__' of function object at
0x7f3f66c8f620>
__dict__=>{}
__dir__=><built-in method __dir__ of function object at 0x7f3f66c8f620>
__doc__=>None
__eq__=><method-wrapper '__eq__' of function object at 0x7f3f66c8f620>
__format__=><built-in method __format__ of function object at
0x7f3f66c8f620>5
__ge__=><method-wrapper '__ge__' of function object at 0x7f3f66c8f620>
__get__=><method-wrapper '__get__' of function object at 0x7f3f66c8f620>
__getattribute__=><method-wrapper '__getattribute__' of function object
at 0x7f3f66c8f620>
__globals__=>{'__name__': '__main__', '__doc__': None, '__package__':
None, '__loader__': <_frozen_importlib_external.SourceFileLoader object
at 0x7f3f68b4f080>, '__spec__': None, '__annotations__': {},
'__builtins__': <module 'builtins' (built-in)>, '__file__':
'/home/yoshimura/Dropbox/2020 Trident/前期/講義資料/python/Python
Scripts/13scope/inspect_test.py', '__cached__': None, 'inspect': <module
'inspect' from '/usr/lib/python3.6/inspect.py'>, 'func': <function func
at 0x7f3f66c8f620>, 'result': [('__annotations__', {}), ('__call__',
<method-wrapper '__call__' of function object at 0x7f3f66c8f620>),
('__class__', <class 'function'>), ('__closure__', None), ('__code__',
<code object func at 0x7f3f68b468a0, file "/home/yoshimura/Dropbox/2020
Trident/前期/講義資料/python/Python Scripts/13scope/inspect_test.py", line
3>), ('__defaults__', None), ('__delattr__', <method-wrapper
'__delattr__' of function object at 0x7f3f66c8f620>), ('__dict__', {}),
('__dir__', <built-in method __dir__ of function object at
0x7f3f66c8f620>), ('__doc__', None), ('__eq__', <method-wrapper '__eq__'
of function object at 0x7f3f66c8f620>), ('__format__', <built-in method
__format__ of function object at 0x7f3f66c8f620>), ('__ge__', <methodwrapper '__ge__' of function object at 0x7f3f66c8f620>), ('__get__',
<method-wrapper '__get__' of function object at 0x7f3f66c8f620>),
('__getattribute__', <method-wrapper '__getattribute__' of function
object at 0x7f3f66c8f620>), ('__globals__', {...}), ('__gt__', <methodwrapper '__gt__' of function object at 0x7f3f66c8f620>), ('__hash__',
<method-wrapper '__hash__' of function object at 0x7f3f66c8f620>),
('__init__', <method-wrapper '__init__' of function object at
0x7f3f66c8f620>), ('__init_subclass__', <built-in method
__init_subclass__ of type object at 0x9c85c0>), ('__kwdefaults__', None),
('__le__', <method-wrapper '__le__' of function object at
0x7f3f66c8f620>), ('__lt__', <method-wrapper '__lt__' of function object
at 0x7f3f66c8f620>), ('__module__', '__main__'), ('__name__', 'func'),
('__ne__', <method-wrapper '__ne__' of function object at
0x7f3f66c8f620>), ('__new__', <built-in method __new__ of type object at
0x9c85c0>), ('__qualname__', 'func'), ('__reduce__', <built-in method
__reduce__ of function object at 0x7f3f66c8f620>), ('__reduce_ex__',
<built-in method __reduce_ex__ of function object at 0x7f3f66c8f620>),
('__repr__', <method-wrapper '__repr__' of function object at
0x7f3f66c8f620>), ('__setattr__', <method-wrapper '__setattr__' of6
function object at 0x7f3f66c8f620>), ('__sizeof__', <built-in method
__sizeof__ of function object at 0x7f3f66c8f620>), ('__str__', <methodwrapper '__str__' of function object at 0x7f3f66c8f620>),
('__subclasshook__', <built-in method __subclasshook__ of type object at
0x9c85c0>)], 'k': '__globals__', 'v': {...}}
__gt__=><method-wrapper '__gt__' of function object at 0x7f3f66c8f620>
__hash__=><method-wrapper '__hash__' of function object at
0x7f3f66c8f620>
__init__=><method-wrapper '__init__' of function object at
0x7f3f66c8f620>
__init_subclass__=><built-in method __init_subclass__ of type object at
0x9c85c0>
__kwdefaults__=>None
__le__=><method-wrapper '__le__' of function object at 0x7f3f66c8f620>
__lt__=><method-wrapper '__lt__' of function object at 0x7f3f66c8f620>
__module__=>__main__
__name__=>func
__ne__=><method-wrapper '__ne__' of function object at 0x7f3f66c8f620>
__new__=><built-in method __new__ of type object at 0x9c85c0>
__qualname__=>func
__reduce__=><built-in method __reduce__ of function object at
0x7f3f66c8f620>
__reduce_ex__=><built-in method __reduce_ex__ of function object at
0x7f3f66c8f620>
__repr__=><method-wrapper '__repr__' of function object at
0x7f3f66c8f620>
__setattr__=><method-wrapper '__setattr__' of function object at
0x7f3f66c8f620>
__sizeof__=><built-in method __sizeof__ of function object at
0x7f3f66c8f620>
__str__=><method-wrapper '__str__' of function object at 0x7f3f66c8f620>
__subclasshook__=><built-in method __subclasshook__ of type object at
0x9c85c0>

'''