class A:
    def __init__(self):
        print("A")
        super().__init__()


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class X:
    def __init__(self):
        print("X")
        super().__init__()


class Forward(B, X):
    def __init__(self):
        print("Forward")
        super().__init__()


class Backward(X, B):
    print("Backward")
    super().__init__()
