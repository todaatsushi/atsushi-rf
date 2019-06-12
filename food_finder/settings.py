import socket

# Ensure proper usage (SSL etc.)
if socket.gethostname() == 'AT.local':
    from .local_settings import *
else:
    from .production_settings import *