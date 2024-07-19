class Game:
    #TODO create class variable
    winner = False  #bool to check for a winner
    game_boxes = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]


    #TODO create instance variables of player. playername, status, sign
    def __init__(self, name: str, status: bool, sign: str):
        self.name = name
        self.status = status
        self.sign = sign

    
    #TODO create a method to create player instance based on the input of each player
    

    #TODO create a method for each player to play its turn and return to the next player if there is no winner


    #TODO use the __repr__() to show the object format
    def __repr__(self):
        return f"Player({self.name}, {self.status}, {self.sign})"

player1 = Game(input("Player1 Name: "), False, input("Player1 Sign: "))
player2 = Game(input("Player2 Name: "), False, input("Player2 Sign: "))
