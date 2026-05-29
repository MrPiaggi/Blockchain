import block as b

class blockchain:
    def __init__(self, difficolta):
        self.chain = []
        self.difficolta = difficolta
        self.genesi()
    
    def genesi(self):
        first_block = b.block(0,"Primo blocco della catena","0")
        first_block.mine(self.difficolta)
        self.chain.append(first_block)

    def last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.prev_hash = self.last_block().hash
        new_block.mine(self.difficolta)
        self.chain.append(new_block)

    def show_chain(self):
        print("\n--------------- VISUALIZZAZIONE BLOCKCHAIN ---------------")
        for b in self.chain:
            print(f"Blocco #{b.index} [Payload: '{b.payload}']")
            print(f"    Hash Precedente: {b.prev_hash}")
            print(f"    Hash Attuale:    {b.calcola_hash()}")
            print("---------------------------------------------------------------")

    def hack_block(self, index, new_data):
        if 0 <= index < len(self.chain):
            self.chain[index].payload = new_data
            print("-> Payload modificato nel database locale.")
        else:
            print(f"L'indice {index} non corrisponde a nessun blocco.")

    def check_chain(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            if block.hash != block.calcola_hash():
                print(f"Il contenuto del blocco numero {block.index} è stato modificato")
                return False
        return True
    