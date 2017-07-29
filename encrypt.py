import os
from hashlib import sha1
from base64 import b64decode, b64encode
from gnupg import GPG
from Crypto.Cipher import AES

class LocalEncrypt(object):

    def __init__(self, key):
        self.initialization_vector = '\xbf\xab\x18\x87\x81\t\x99x\x94\xfdy\xc5\xf4`\x80\xfc'
        self.key = sha1(key.encode('utf8')).hexdigest()

    def pad(self, data):
        return data + (16 - len(data) % 16) * chr(16 - len(data) % 16)

    def unpad(self, data):
        return data[:-ord(data[len(data) - 1:])]

    def encrypt(self, raw):
        raw = self.pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.initialization_vector)
        return b64encode(self.initialization_vector + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, enc[:16]).decrypt(enc[16:])
        return self.unpad(cipher).decode('utf8')

class EncServerRequest(object):

    def __init__(self, data, usermail, *args, **kwargs):
        self.gpg = GPG(homedir=os.path.expanduser('~'))
        self.encrypted_data = self.gpg.encrypt(data, usermail)

    def ReqServ(self):
        pass
