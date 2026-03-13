import inspect
from binance.client import Client

print('Client methods containing request:')
for name, func in inspect.getmembers(Client, predicate=inspect.isfunction):
    if 'request' in name.lower() or 'http' in name.lower():
        print('-', name)

if hasattr(Client, '_request'):
    import textwrap
    src = inspect.getsource(Client._request)
    print('\n--- _request source ---\n')
    print(textwrap.indent(src, '    '))
else:
    print('No _request method on Client')
