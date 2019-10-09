import mymodule as mx
import platform
#import only part from a module
from mymodule import greeting

a=mx.info["name"]
print(a)

#device sysytem
a=platform.system()
print(a)

#sow all the function and var
b=dir(platform)
print(b)

greeting("Sara")