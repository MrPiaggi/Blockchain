import hashlib
import time

class block:
    def __init__(self, index, payload, prev_hash=""):
        self.index = index
        self.prev_hash = prev_hash
        self.payload = payload
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calcola_hash()
    
    def calcola_hash(self):
        s = (str(self.index) + str(self.prev_hash) + str(self.payload) + str(self.timestamp) + str(self.nonce))
        return hashlib.sha256(s.encode()).hexdigest()
    
    def mine(self, difficolta):
        target = "0" * difficolta
        while self.hash[:difficolta] != target:
            self.nonce += 1
            self.hash = self.calcola_hash()
        
        print(f" >>>Blocco numero {self.index} minato con successo. Nonce trovato: {self.nonce}")


