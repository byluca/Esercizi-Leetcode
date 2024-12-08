class Solution(object):
    def removeElement(self, nums, val):
        it = iter(nums)  # Crea un iteratore sull'array nums
        k = 0  # Indice per posizionare gli elementi non uguali a 'val'

        # Usa un ciclo while per scansionare l'array con l'iteratore
        while True:
            try:
                current = next(it)  # Ottiene il prossimo elemento dall'iteratore
                if current != val:
                    nums[k] = current  # Posiziona l'elemento valido alla posizione 'index'
                    k += 1  # Incrementa l'indice
            except StopIteration:
                break  # Esce dal ciclo quando non ci sono più elementi

        return k  # Restituisce il numero di elementi rimanenti


# Funzione di test per verificare la correttezza del metodo
def test_removeElement():
    # Crea un'istanza della classe Solution
    solution = Solution()

    # Caso di test 1: Rimozione di elementi con valori presenti
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print("Test 1:")
    print(f"Numero di elementi rimanenti: {k}")  # Dovrebbe essere 2
    print(f"Array modificato: {nums[:k]}")  # Dovrebbe essere [2, 2]
    assert k == 2, "Test 1 fallito"
    assert nums[:k] == [2, 2], "Test 1 fallito"

    # Caso di test 2: Nessun elemento da rimuovere
    nums = [1, 2, 3, 4, 5]
    val = 6
    k = solution.removeElement(nums, val)
    print("Test 2:")
    print(f"Numero di elementi rimanenti: {k}")  # Dovrebbe essere 5
    print(f"Array modificato: {nums[:k]}")  # Dovrebbe essere [1, 2, 3, 4, 5]
    assert k == 5, "Test 2 fallito"
    assert nums[:k] == [1, 2, 3, 4, 5], "Test 2 fallito"

    # Caso di test 3: Tutti gli elementi sono uguali a 'val'
    nums = [3, 3, 3, 3, 3]
    val = 3
    k = solution.removeElement(nums, val)
    print("Test 3:")
    print(f"Numero di elementi rimanenti: {k}")  # Dovrebbe essere 0
    print(f"Array modificato: {nums[:k]}")  # Dovrebbe essere []
    assert k == 0, "Test 3 fallito"
    assert nums[:k] == [], "Test 3 fallito"

    # Caso di test 4: L'array è vuoto
    nums = []
    val = 1
    k = solution.removeElement(nums, val)
    print("Test 4:")
    print(f"Numero di elementi rimanenti: {k}")  # Dovrebbe essere 0
    print(f"Array modificato: {nums[:k]}")  # Dovrebbe essere []
    assert k == 0, "Test 4 fallito"
    assert nums[:k] == [], "Test 4 fallito"

    print("Tutti i test sono stati superati!")

# Esegui il test
test_removeElement()
