from gc_game_data import *


def draw(x, y, Obj, Type, height, width, Images, AnimationStage, Count):
    global MaterialProduction
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay, (0, 128, 0), (x, y, (640 / width), (640 / height)), 0)
        if Type.find("Water") != -1:

            # Animation 4 water
            if AnimationStage["Water"][0] == 1:
                gameDisplay.blit(Images["Water1"], (x, y))
            if AnimationStage["Water"][0] == 2:
                gameDisplay.blit(Images["Water2"], (x, y))
            if AnimationStage["Water"][0] == 3:
                gameDisplay.blit(Images["Water3"], (x, y))
            if AnimationStage["Water"][1] <= 0:
                AnimationStage["Water"][0] += 1
                AnimationStage["Water"][1] = 0.5
                if AnimationStage["Water"][0] == 4:
                    AnimationStage["Water"][0] = 1
            else:
                AnimationStage["Water"][1] -= 0.025 / Count["Water"]
        # Animation 4 Dam
        if Type == "Dam":
            if AnimationStage["Dam"][0] == 1:
                gameDisplay.blit(Images["Dam1"], (x, y))
            if AnimationStage["Dam"][0] == 2:
                gameDisplay.blit(Images["Dam2"], (x, y))
            if AnimationStage["Dam"][1] <= 0:
                AnimationStage["Dam"][0] += 1
                AnimationStage["Dam"][1] = random.randint(800, 1000)  # random vara for dam to open/close
                if AnimationStage["Dam"][0] == 3:
                    AnimationStage["Dam"][0] = 1
            else:
                AnimationStage["Dam"][1] -= 1 / Count["Dam"]

        # Fishing Boat Animation
        if Type.find("FishingBoat") != -1:
            if Type == 'FishingBoat':
                if AnimationStage["FishingBoat"][0] == 1:
                    gameDisplay.blit(Images["FishingBoat00"], (x, y))
                if AnimationStage["FishingBoat"][0] == 2:
                    gameDisplay.blit(Images["FishingBoat01"], (x, y))
                if AnimationStage["FishingBoat"][0] == 3:
                    gameDisplay.blit(Images["FishingBoat02"], (x, y))
                if AnimationStage["FishingBoat"][1] <= 0:
                    AnimationStage["FishingBoat"][0] += 1
                    AnimationStage["FishingBoat"][1] = random.randint(800, 1000)
                    if AnimationStage["FishingBoat"][0] == 4:
                        AnimationStage["FishingBoat"][0] = 1
                else:
                    AnimationStage["FishingBoat"][1] -= 2 / Count["FishingBoat"]

        # Tile Texture #

        # Stone Gather
        if Type == "Quarry Lv1":
            gameDisplay.blit(Images["Quarry1"], (x, y))
        if Type == "Quarry Lv2":
            gameDisplay.blit(Images["Quarry2"], (x, y))
        if Type == "Quarry Lv3":
            gameDisplay.blit(Images["Quarry3"], (x, y))
        if Type == "Quarry Lv4":
            gameDisplay.blit(Images["Quarry4"], (x, y))

        # Wood Gather
        if Type == "Forest Lv1":
            gameDisplay.blit(Images["Forest1"], (x, y))
        if Type == "Forest Lv2":
            gameDisplay.blit(Images["Forest2"], (x, y))
        if Type == "Forest Lv3":
            gameDisplay.blit(Images["Forest3"], (x, y))
        if Type == "Forest Lv4":
            gameDisplay.blit(Images["Forest4"], (x, y))

        # Farm -> Town
        if Type == "Farm":
            gameDisplay.blit(Images["Farm"], (x, y))
        if Type == "town_00":
            gameDisplay.blit(Images["town_00"], (x, y))
        if Type == "town_01":
            gameDisplay.blit(Images["town_01"], (x, y))
        if Type == "town_02":
            gameDisplay.blit(Images["town_02"], (x, y))
        if Type == "town_03":
            gameDisplay.blit(Images["town_03"], (x, y))
        if Type == "town_04":
            gameDisplay.blit(Images["town_04"], (x, y))
        if Type == "town_05":
            gameDisplay.blit(Images["town_05"], (x, y))

        # Town -> City
        if Type == "City_00":
            gameDisplay.blit(Images["City_00"], (x, y))

        # Factory
        if Type.find("Factory ") != -1 or Type == "Factory":
            gameDisplay.blit(Images["Factory"], (x, y))

        if Type == "Super_Factory":
            gameDisplay.blit(Images["Super_Factory"], (x, y))

        # Military
        if Type == "barracks":
            gameDisplay.blit(Images["barracks"], (x, y))

        # Military Units
        if Type == "squad_trail_fireteam":
            gameDisplay.blit(Images["squad_trail_fireteam"], (x, y))

        # Energy
        if Type == "Solar_Power":
            gameDisplay.blit(Images["Solar_Power"], (x, y))

        # Tile Border
        pygame.draw.rect(gameDisplay, (50, 50, 50), (x, y, (640 / width), (640 / height)), 1)

    # User button click which lights up the selected obj
    # they have choosen on the generated board
    if Obj == "Selection":
        if int(5 / (int(height / 2) - 3)) != 0:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)),
                             int(5 / (int(height / 2) - 3)))
        else:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)), 1)


# Makes the board that the user will see
# generates a random amount of resources that the user can exploit
#Generates a board using a height and a width
def gen_Board(board,height,width):
    for j in range(height):
        for i in range(width):
            percent = random.randint(1,100)
            if percent <= 50:
                board[j][i] = "Grass"
            else:
                if percent <= 60:
                    board[j][i] = "Water"
                elif percent <= 75:
                    board[j][i] = "Forest Lv1"
                else:
                    board[j][i] = "Quarry Lv1"
    return board

def boardUpSize(board,height,width):
    for TileRow in board:
        for i in range(2):
            percent = random.randint(1,100)
            if percent <= 50:
                TileRow.append("Grass")
            else:
                if percent <= 60:
                    TileRow.append("Water")
                elif percent <= 75:
                    TileRow.append("Forest Lv1")
                else:
                    TileRow.append("Quarry Lv1")
    for i in range(2):
        boardline = []
        for i in range(width):
            percent = random.randint(1,100)
            if percent <= 50:
                boardline.append("Grass")
            else:
                if percent <= 60:
                    boardline.append("Water")
                elif percent <= 75:
                    boardline.append("Forest Lv1")
                else:
                    boardline.append("Quarry Lv1")
        board.append(boardline)
    return board
