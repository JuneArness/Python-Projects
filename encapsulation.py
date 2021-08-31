






# This is a protected function:

class Protected:
    def __init__(self):
        self._protectedVar = 0


obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)


# This is a private function:
class Protected:
    def __init__(self):
        self._privateVar = 12

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self_privateVar = private
        
# Here is objects that use them both.
obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
            


if __name__ == "__main__":
    pass
