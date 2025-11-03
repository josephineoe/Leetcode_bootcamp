class MyQueue:
    def __init__(self):
        self._in = []   # push here
        self._out = []  # pop/peek here

    def push(self, x: int) -> None:
        self._in.append(x)

    def _shift(self) -> None:
        if not self._out:                 # move only when needed
            while self._in:
                self._out.append(self._in.pop())

    def pop(self) -> int:
        self._shift()
        return self._out.pop()

    def peek(self) -> int:
        self._shift()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out
