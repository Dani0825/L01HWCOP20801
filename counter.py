class Counter:
    def __init__(self):
        self._strokes = ""
        self._limit = 0

    def setLimit(self, maximum):
        self._limit = maximum
    
    def getValue(self):
        return self._strokes
    
    def click(self):
        self._strokes = self._strokes + '|'
        if len(self._strokes) > self._limit:
            print("Limit Exceeded")
    
    def reset(self):
        self._strokes = ""
    
    
