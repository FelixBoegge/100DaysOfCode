class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = []

    def add(self, num: int) -> None:
        if num == 1:
            self.prefix_prod.append(num)
        elif num == 0:
            self.prefix_prod = []
        else:
            self.prefix_prod = list(map(lambda x: x * num, self.prefix_prod)) + [num]

    def getProduct(self, k: int) -> int:
        if k <= len(self.prefix_prod):
            return self.prefix_prod[-k]
        else:
            return 0