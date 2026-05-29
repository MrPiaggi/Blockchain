import block as b
import blockchain as c

print("\n--------------- CREAZIONE DELLA BLOCKCHAIN ---------------")
    
blockchain_trasazioni = c.blockchain(difficolta=2)

print("\n--------------- AGGIUNTA DEI BLOCCHI CON I DATI ---------------")
    
tx1 = b.block(index=1, payload="Dall'indirizzo A all'indirizzo B: 0.5 BTC")
blockchain_trasazioni.add_block(tx1)

tx2 = b.block(index=2, payload="Dall'indirizzo C all'indirizzo D: 1.3 BTC")
blockchain_trasazioni.add_block(tx2)

tx3 = b.block(index=3, payload="Dall'indirizzo E all'indirizzo F: 0.3 BTC")
blockchain_trasazioni.add_block(tx3)

while True:
        print("\n---------------------------------------------------------------")
        print("     MENU BLOCKCHAIN INTERATTIVO")
        print("---------------------------------------------------------------")
        print("1. Visualizza la Blockchain")
        print("2. Manometti un blocco")
        print("3. Controlla la validità della blockchain")
        print("0. Esci dall'applicazione")
        print("\n---------------------------------------------------------------")
        
        scelta = input("Seleziona un'opzione: ")
        
        match scelta:
            case "1":
                blockchain_trasazioni.show_chain()
                
            case "2":
                try:
                    index = int(input("\nQuale blocco vuoi manomettere? indice: "))
                    nuovo_payload = input("Inserisci il nuovo payload: ")
                    blockchain_trasazioni.hack_block(index, nuovo_payload)
                except ValueError:
                    print("Errore: Inserisci un numero valido per l'indice del blocco.")
                    
            case "3":
                is_valida = blockchain_trasazioni.check_chain()
                if is_valida:
                    print("La blockchain è INTEGRA e VALIDA.")
                    
            case "0":
                break
            case _:
                print("Opzione non valida. Inserisci un numero da 0 a 3.")
        