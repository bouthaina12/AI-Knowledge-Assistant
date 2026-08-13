import importlib
import sys
print('importlib module:', importlib)
print('importlib file:', getattr(importlib, '__file__', None))
print('importlib attributes:', [a for a in dir(importlib) if a.startswith('util') or a=='util'])
print('\nSys.path:')
for p in sys.path:
    print('-', p)
