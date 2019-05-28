import socket

# Ensure proper usage (SSL etc.)
print(socket.gethostname() == 'AT.local')
if socket.gethostname() == 'AT.local':
    from .local_settings import *
else:
    from .production_settings import *