import hashlib

class Encoder:
    def encode(self, string):
        result = hashlib.md5(string.encode())
        #print(result.hexdigest())
        return result.hexdigest()

    def decode(self, string, claveMD5):
        string = hashlib.md5(string.encode())
        if string.hexdigest() == claveMD5:
            print("exit")
            return True
        else:
            print("niet")
            return False
