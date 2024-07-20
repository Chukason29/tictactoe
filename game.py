class Game:
    #TODO create class variable
    winner = False  #bool to check for a winner
    game_boxes = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    winnerList = [
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]]
    ]


    #TODO create instance variables of player. playername, status, sign
    def __init__(self, name: str, status: bool, sign: str):
        self.name = name
        self.status = status
        self.sign = sign

    
    #TODO create a method to check if there is a winner
    @classmethod
    def is_winner (cls):
        #TODO This method check if their is winner or the game has ended without a winner
        for firstLayer in Game.winnerList:
            for points in firstLayer:
                print(points)
    @classmethod
    def display_game(cls):
        for x in Game.game_boxes:
            print(x)

    #TODO create a method for each player to play its turn and return to the next player if there is no winner
    def player_turn(self):
        if (self.status == True):
            number_choice = input("Enter Your Numbers: ")
            num1, num2 = map(int, number_choice.split(" "))
            if (num1 < 0 or num1 > 2) or (num2 < 0 or num1 > 2):
                print("Please Enter a number 0-2")
            else:
                Game.game_boxes[num1][num2] = self.sign
                Game.display_game()

    
    #TODO change player's turn after playing

        #==> check if 
    
    


    
     
    

            

    #TODO use the __repr__() to show the object format
    def __repr__(self):
        return f"Player({self.name}, {self.status}, {self.sign})"

player1 = Game(input("Player1 Name: "), True, input("Player1 Sign: "))
#player2 = Game(input("Player2 Name: "), False, input("Player2 Sign: "))

player1.player_turn()