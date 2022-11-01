class NonPositiveError(Exception):
    pass

class PositiveList(list):
    
    def __init__(self):
        None

    def append(self, x):
        if (x > 0):
            super().append(x)
        else:
            raise NonPositiveError
        

d = PositiveList()
d.append(3)
print(d)
#d.append(3)
#d.append(3)
#print(d.list())
