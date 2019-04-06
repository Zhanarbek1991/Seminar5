class PriorityQueue :
    def __init__( self ):
        self._qList = list()
    def isEmpty( self ):
        return len( self ) == 0
    def __len__( self ):
        return len( self._qList )
    def enqueue( self, item, priority ):
        entry = _PriorityQEntry( item, priority )
        self._qList.append( entry )
    def dequeue( self ) :
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        highest = self._qList[i].priority
        for i in range( self.len() ) :
            if self._qList[i].priority < highest :
                highest = self._qList[i].priority
            entry = self._qList.pop( highest )
            return entry.item
class _PriorityQEntry( object ):
    def __init__( self, item, prioity ):
        self.item = item
        self.priority = priority
