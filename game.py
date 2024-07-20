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
            if firstLayer[0] != "O" or firstLayer[1] !="O" or firstLayer[2] != "O":
                if firstLayer[0] == firstLayer[1] == firstLayer[2] :
                    Game.winner = True
                else: 
                    Game.winner = False
        return Game.winner
    @ classmethod
    def is_game_finished(cls):
        check = False
        for x in Game.game_boxes:
            if x[0] != "O" or x[1] !="O" or x[2] != "O":
                check = True
        return check
    
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
                
    def play_game(self):
        while Game.is_game_finished == False:
            if Game.is_winner():
                print(f"HOORAY!!! {self.name} is the winner")
                break
            else:
                self.player_turn()


    
    #TODO change player's turn after playing
           

    #TODO use the __repr__() to show the object format
    def __repr__(self):
        return f"Player({self.name}, {self.status}, {self.sign})"

player1 = Game(input("Player1 Name: "), True, input("Player1 Sign: "))
#player2 = Game(input("Player2 Name: "), False, input("Player2 Sign: "))

player1.play_game()