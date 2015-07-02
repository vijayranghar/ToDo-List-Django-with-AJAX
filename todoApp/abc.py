import os
print __file__
base_dir=os.path.abspath(os.path.dirname(__file__))
b=os.path.realpath(os.path.dirname(__file__))
print(os.path.join(base_dir,"templates"))
print(os.path.join(b,"templates"))
print "hello"