from logic.game_logic.game_state import Game_State

class Global_State:
    game_state = None  # Class-level variable to store the game state

    @staticmethod
    def initialize():
        if Global_State.game_state is None:  # Ensure it only initializes once
            Global_State.game_state = Game_State()  # Assign to the class variable
            print("Success! :3")  # Debug message
        else:
            print("Game state already initialized!")
