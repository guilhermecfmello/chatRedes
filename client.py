"""
  ____                              _                   _ _
 / ___|_ __ _   _ _ __   ___     __| | ___  ___   _ __ (_) | ____ _
| |  _| '__| | | | '_ \ / _ \   / _` |/ _ \/ __| | '_ \| | |/ / _` |
| |_| | |  | |_| | |_) | (_) | | (_| | (_) \__ \ | |_) | |   < (_| |
 \____|_|   \__,_| .__/ \___/   \__,_|\___/|___/ | .__/|_|_|\_\__,_|
                 |_|                             |_|
"""

class Client:
    port = 5007
    ip = "127.0.0.1"
    name = "test"
    age = 999
    profession = "test"
    email = "test@test.com"
    buffer_size = 1024

    def __init__(self, name, ip, port, age, profession, email):
        self.name, self.ip, self.port = name, ip, port
        self.age, self.profession, self.email = age, profession, email
