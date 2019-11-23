

class GridError(Exception):
    """
    Error to raise if the game grid is wrong
    """
    
    def __init__(self, message='The game grid is wrong'):
        Exception.__init__(self, message)
        
        
class InvalidMove(Exception):
    """
    Error to raise if an invalid move was made
    """
    
    def __init__(self, message='An invalid move was made'):
        Exception.__init__(self, message)
        
        
class InvalidInput(Exception):
    """
    Error to raise if there is an error with the given input
    """
    
    def __init__(self, message='There was an error with the given input'):
        Exception.__init__(self, message)
        

class GameIsOver(Exception):
    """
    Error to raise if the game is already over
    """
    
    def __init__(self, message='The game is already over'):
        Exception.__init__(self, message)