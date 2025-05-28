PORT = 443
METRICS_PORT = 9157

# USE_CONNECTION_POOL controls whether the proxy uses a connection pool to Telegram servers.
# Set to True to enable connection pooling (recommended for high concurrent users, e.g. >200).
# Set to False to always open a new connection for each client (recommended for low concurrent users).
USE_CONNECTION_POOL = False

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000001",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "music.youtube.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"

TO_CLT_BUFSIZE = 262_144
TO_TG_BUFSIZE  = 262_144

