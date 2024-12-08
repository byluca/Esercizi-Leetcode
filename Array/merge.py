class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Creo gli iteratori per nums1 e nums2
        it1 = iter(nums1[:m])
        it2 = iter(nums2[:n])

        # Leggo il primo elemento di nums1
        try:
            current1 = next(it1)
        except StopIteration:
            current1 = None

        # Leggo il primo elemento di nums2
        try:
            current2 = next(it2)
        except StopIteration:
            current2 = None

        # Indice per sovrascrivere nums1
        index = 0

        # Fusione degli array
        while current1 is not None or current2 is not None:
            if current1 is not None and (current2 is None or current1 <= current2):
                nums1[index] = current1
                index += 1
                try:
                    current1 = next(it1)
                except StopIteration:
                    current1 = None
            elif current2 is not None:
                nums1[index] = current2
                index += 1
                try:
                    current2 = next(it2)
                except StopIteration:
                    current2 = None


# Funzione di test per verificare la correttezza del metodo
def test_merge():
    # Crea un'istanza della classe Solution
    solution = Solution()

    # Caso di test 1: Merge di array ordinati con elementi comuni
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print("Test 1:")
    print(f"Array unito: {nums1}")  # Dovrebbe essere [1, 2, 2, 3, 5, 6]
    assert nums1 == [1, 2, 2, 3, 5, 6], "Test 1 fallito"

    # Caso di test 2: Merge con array nums2 vuoto
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print("Test 2:")
    print(f"Array unito: {nums1}")  # Dovrebbe essere [1, 2, 3, 0, 0, 0]
    assert nums1 == [1, 2, 3, 0, 0, 0], "Test 2 fallito"

    # Caso di test 3: Merge con array nums1 vuoto
    nums1 = [0, 0, 0, 0, 0, 0]
    m = 0
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print("Test 3:")
    print(f"Array unito: {nums1}")  # Dovrebbe essere [1, 2, 3, 0, 0, 0]
    assert nums1 == [1, 2, 3, 0, 0, 0], "Test 3 fallito"

    # Caso di test 4: Merge di array con un solo elemento
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print("Test 4:")
    print(f"Array unito: {nums1}")  # Dovrebbe essere [1]
    assert nums1 == [1], "Test 4 fallito"

    # Caso di test 5: Merge di array già ordinati di lunghezza uguale
    nums1 = [1, 3, 5, 0, 0, 0]
    m = 3
    nums2 = [2, 4, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print("Test 5:")
    print(f"Array unito: {nums1}")  # Dovrebbe essere [1, 2, 3, 4, 5, 6]
    assert nums1 == [1, 2, 3, 4, 5, 6], "Test 5 fallito"

    print("Tutti i test sono stati superati!")


# Esegui il test
test_merge()
