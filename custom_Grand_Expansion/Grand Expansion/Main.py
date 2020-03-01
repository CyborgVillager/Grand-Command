from custom_source_modules import *

# Initialize the game engine
pygame.init()

DisplayWidth, DisplayHeight = 1000, 800
clock = pygame.time.Clock()

# Prestige Count
global PrestigeCount
PrestigeCount = 0
global MinerBought
MinerBought = False
global AscendCount
AscendCount = 0

# Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Grand Expansion Test")

# Fonts
from fonts import *


# Loading the images
def load_images(path_to_directory, height, width):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img, (int(640 / width), int(640 / height)))
                images[key] = img
    return images


# Multipliers for Prestige
global Mult
# Temp Multi
Mult = {"Wood": 6, "Stones": 6, "Food": 6, "Metal": 6, "Electricity": 6, "Prestige": 6, "Mandorium": 6}

# Map Level
global MapLevel
MapLevel = 2

# Plays the music
pygame.mixer.music.load('Sounds/ambient-guitar-x1-loop-mode.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)
global MusicPaused
MusicPaused = False


# Shorten is a function that takes a number and shortens it while still keeping the value because of the use of letters
def shorten(Num):
    count = 0
    let = ""

    while Num >= 1000:
        Num /= 1000
        count += 1

    Num = str(Num)

    Num2 = ""

    if count >= 1:
        for i in range(Num.index(".") + 2):
            Num2 += Num[i]

        Num = Num2

    if count == 1:
        Num += "K"
    if count == 2:
        Num += "M"
    if count == 3:
        Num += "B"
    if count == 4:
        Num += "T"
    if count == 5:
        Num += "q"
    if count == 6:
        Num += "Q"
    if count == 7:
        Num += "s"
    if count == 8:
        Num += "S"

    return Num


# Checks for all the achviements



# Draws all the tiles
def draw(x, y, Obj, Type, height, width, Images, AnimationStage, Count):
    global MaterialProduction
    if Obj == "Tile":
        if Type == "Grass":
            pygame.draw.rect(gameDisplay, (0, 128, 0), (x, y, (640 / width), (640 / height)), 0)
        if Type.find("Water") != -1:
            # The Animation for water
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






    # Draws the green selection thing
    if Obj == "Selection":
        if int(5 / (int(height / 2) - 3)) != 0:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)),
                             int(5 / (int(height / 2) - 3)))
        else:
            pygame.draw.rect(gameDisplay, (50, 205, 50), (x, y, (640 / width), (640 / height)), 1)


# Generates a board using a height and a width
def gen_Board(board, height, width):
    for j in range(height):
        for i in range(width):
            percent = random.randint(1, 100)
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


# Map Board
def boardUpSize(board, height, width):
    for TileRow in board:
        for i in range(2):
            percent = random.randint(1, 100)
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
            percent = random.randint(1, 100)
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


# The main part of the game
def game_loop(height, width, prestige, LoadSave):
    global MinerBought, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, \
        AnimationStage, Count, Achviements, MusicPaused, Images, Mult, MapLevel

    # Declaring the values for resources
    game_run = True
    board = gen_Board([[0] * height for _ in range(width)], height, width)
    CurSelection = [-1, -1]
    ResourceCount = {"Wood": 60, "Stones": 60, "Food": 60, "Metal": 60, "Electricity": 60, "Prestige": prestige,
                     "Mandorium": 0}
    MaterialProduction = {"Wood": 0, "Stones": 0, "Food": 0, "Metal": 0, "Electricity": 0, "Prestige": 0,
                          "Mandorium": 0}
    MaterialsEarned = {"Wood": 250, "Stones": 250, "Food": 15, "Metal": 10, "Electricity": 0, "Prestige": prestige,
                       "Mandorium": 0}
    Cooldown = time.process_time()
    UnUpgradable = ["Water", "Grass", "Quarry Lv3", "Forest Lv3", "Water Fish", "Water Dam"]
    UpgradeInfo = {"Map Upgrades": [], "Forest Lv1": ["10 wood", "0 wood", "1 wood"],
                   "Quarry Lv1": ["15 wood", "0 stones", "1 stones"],
                   "Forest Lv2": ["40 wood", "1 wood", "5 wood"],
                   "Quarry Lv2": ["45 wood", "20 stones", "1 stones", "5 stones"]}

    Achievments = [
        {"Name": "Beginner", "Description": "You gathered 100 wood", "Reward": "Unlocked cities", "wood": 100,
         "Finished": False, "Show Cooldown": 0}

        , {"Name": "Food Man", "Description": "You gathered 50 food", "Reward": "Unlocked Factories", "wood": 300,
           "stones": 100, "food": 50, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Heavy Metal", "Description": "You made 100 metal", "Reward": "Unlocked Electricity",
           "metal": 100, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Shocking", "Description": "You produced 100 Electricity", "Reward": "Unlocked Electric Upgrades",
           "Electricity": 100, "Finished": False, "Show Cooldown": 0}

        , {"Name": "Fast Materials", "Description": "You got a Lvl4 Upgrade", "Reward": "Unlocked Upgraded Factories",
           "Finished": False, "Show Cooldown": 0}

        , {"Name": "Stockpile", "Description": "Have 200 food at any time", "Reward": "Unlocked Fishermen",
           "Finished": False, "Show Cooldown": 0}

        , {"Name": "Restarter", "Description": "You rebirthed 3 times", "Reward": "Unlocked Mandorium",
           "Finished": False, "Show Cooldown": 0}]
    # Tile Images
    Images = []
    Images = load_images("Images", height, width)
    ConfirmMessage = ""
    Confirming = False
    PreviousPos = [0, 0]
    MenuClicking = False
    AnimationStage = {"Water": [1, 0.5], "Dam": [1, 0.5]}
    Count = {"Water": 0, "Dam": 0}
    StartTime = time.process_time()
    hour = 0
    seconds = 0
    minutes = 0
    TimeStart = 0
    SaveMesses = 0
    Secret = False
    SaveCooldown = time.process_time() + 30
    cost = [5, 15]
    cost2 = [10]
    for i in range(MapLevel + 1):
        cost2.append(cost2[len(cost2) - 1] * 10)
    HighMult = 0
    for item in Mult:
        if Mult[item] >= HighMult:
            HighMult = Mult[item]
    for i in range(HighMult):
        cost.append(cost[len(cost) - 1] * 3)
    Saving = 0



    # Saves data(Useful for Prestiges)


    Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar_Power", "Super_Factory", "Forest Lv1",
             "Forest Lv2", "Forest Lv3"
        , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam", "Water Fish",
             "Fisherman", "Dam"
        , "CityFar", "CityFac", "Farm"]


    while game_run == True:

        gameDisplay.fill((150, 150, 150))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Moving your selection with the keys


            # Triggers when you press the mouse


                # Yes or no for Demolishing Buildings


                    # Demolishing Buildings


                # Making the selection


                # Restarts the game


                # Prestige shop


                        # Adds things to cost


                        # Displaying amount of prestige


                        # Wood Upgrade


                        # Stones Upgrade


                        # Food Upgrade


                        # Metal Upgrade


                        # Electricity Upgrade


                        # Map Upgrade


                        # Mandorium Miner


                        # Back button


                # Showing Options


                    # Runs the options window


                        # Handles Events

                                # Exit Options menu

                                # Pause/UnPause music


                                # Saves your data to a save file


                                    # Exports save data


                                # Import save Data:


                        # Displays all the buttons



                # Demolishes Selected Building


                # Will need to re-check & fix readability
                # All of the upgrades


                # Path Choices


        # Counting Tiles for certain animations
        Count = {"Water": 0, "Water Fish": 0,"Dam": 0, "Forest Lv4": 0, "Quarry Lv4": 0, "Super_Factory": 0}
        for j in range(height):
            for i in range(width):
                if board[j][i] == "Water" or board[j][i] == "Water Fish" or board[j][i] == "Water Dam":
                    Count["Water"] += 1
                if board[j][i] == "Water Fish":
                    Count["Water Fish"] += 1
                if board[j][i] == "Dam":
                    Count["Dam"] += 1
                if board[j][i] == "Forest Lv4":
                    Count["Forest Lv4"] += 1
                if board[j][i] == "Quarry Lv4":
                    Count["Quarry Lv4"] += 1
                if board[j][i] == "Super_Factory":
                    Count["Super_Factory"] += 1

        # Drawing all Tiles
        for j in range(height):
            for i in range(width):
                draw(i * (640 / width), j * (640 / height) + 160, "Tile", board[j][i], height, width, Images,
                     AnimationStage, Count)

        # Drawing Selection


        # This is my try at making multiple files. It looks very ineffecient and probably bad to use.
        board, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Count, Achviements, \
        Mult = Menu.menu(board, CurSelection, pygame, gameDisplay,
                         [font_23, font_25, font_30, font_35, font_40, font_50, font_75, font_150],
                         ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo, MaterialsEarned, Count,
                         Achievments, Mult, PrestigeCount, AscendCount)
        # Achvievment Check


        # Display the Achievement


        # Shows a confirm message


        # Auto Save


        # A Miner from the prestige shop


        pygame.display.flip()
        clock.tick(60)


MusicPaused = MainMenu.HomeScreen(pygame, gameDisplay, [font_40, font_50, font_150], clock, MusicPaused)
