from gc_game_data import *


# Making the window
gameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))
pygame.display.set_caption("Grand Command")

# Fonts
from gc_fonts import *


#Loading the images
def load_images(path_to_directory,height,width):
    images = {}
    for dirpath, dirnames, filenames in os.walk(path_to_directory):
        for name in filenames:
            if name.endswith('.png'):
                key = name[:-4]
                img = pygame.image.load(os.path.join(dirpath, name)).convert()
                img = pygame.transform.scale(img,(int(640/width),int(640/height)))
                images[key] = img
    return images

#Multipliers for Prestige
global Mult
Mult = {"Wood": 10, "Stones": 10, "Food": 10, "Metal": 10, "Electricity": 10,"Prestige": 1, "Mandorium": 1}


#Map Level
global MapLevel
MapLevel = 1

# Music
pygame.mixer.music.load('Sounds/Background_SoundTrack.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)
global MusicPaused
MusicPaused = False

#Shorten


#Generates a board using a height and a width



# Checks for all the achievments
from achievment_check import *






# Tile Information
from tile_information import *









# Main Info for GC
def game_loop(height,width,prestige,LoadSave):
    global AscendCount, MinerBought, ResourceCount, MaterialProduction, Cooldown, UnUpgradable, UpgradeInfo,\
        MaterialsEarned, AnimationStage, Count, Achviements, MusicPaused, Images, Mult, MapLevel, PrestigeCount


    # Declaring a ton of variables
    game_run = True
    board = gen_Board([[0] * height for _ in range(width)], height, width)
    CurSelection = [-1, -1]
    ResourceCount = {"Wood": 10, "Stones": 0, "Food": 0, "Metal": 0, "Electricity": 0, "Prestige": prestige,
                     "Mandorium": 0}
    MaterialProduction = {"Wood": 0, "Stones": 0, "Food": 0, "Metal": 0, "Electricity": 0, "Prestige": 0,
                          "Mandorium": 0}
    MaterialsEarned = {"Wood": 0, "Stones": 0, "Food": 0, "Metal": 0, "Electricity": 0, "Prestige": prestige,
                       "Mandorium": 0}
    Cooldown = time.process_time()
    UnUpgradable = ["Water", "Grass", "Quarry Lv3", "Forest Lv3", "Water Fish", "Water Dam"]
    UpgradeInfo = {"Map Upgrades": [], "Forest Lv1": ["10 wood", "0 wood", "1 wood"],
                   "Quarry Lv1": ["15 wood", "0 stones", "1 stones"], "Forest Lv2": ["40 wood", "1 wood", "5 wood"],
                   "Quarry Lv2": ["45 wood", "20 stones", "1 stones", "5 stones"]}
    Achievments = [
        {"Name": "Beginner", "Description": "You gathered 100 wood", "Reward": "Unlocked cities", "wood": 100,
         "Finished": False, "Show Cooldown": 0}
        , {"Name": "Food Man", "Description": "You gathered 50 food", "Reward": "Unlocked Factories", "wood": 300,
           "stones": 100, "food": 50, "Finished": False, "Show Cooldown": 0}
        , {"Name": "Heavy Metal", "Description": "You made 100 metal", "Reward": "Unlocked Electricity", "metal": 100,
           "Finished": False, "Show Cooldown": 0}
        , {"Name": "Shocking", "Description": "You produced 100 Electricity", "Reward": "Unlocked Electric Upgrades",
           "Electricity": 100, "Finished": False, "Show Cooldown": 0}
        , {"Name": "Fast Materials", "Description": "You got a Lvl4 Upgrade", "Reward": "Unlocked Upgraded Factories",
           "Finished": False, "Show Cooldown": 0}
        , {"Name": "Stockpile", "Description": "Have 200 food at any time", "Reward": "Unlocked Fishermen",
           "Finished": False, "Show Cooldown": 0}
        ,
        {"Name": "Restarter", "Description": "You rebirthed 3 times", "Reward": "Unlocked Mandorium", "Finished": False,
         "Show Cooldown": 0}]
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

    if LoadSave == True:
        SaveFile = open("Save File/SaveFile.txt", "r")
        ask = SaveFile.readline()
        DataList = []
        if ask.count("#") >= 90:
            count = 0
            for i in range(ask.count("#")):
                DataBit = ""
                FindBit = True
                while FindBit == True:
                    if ask[count] != "#":
                        DataBit += ask[count]
                    else:
                        FindBit = False
                    count += 1
                DataList.append(DataBit)

            Count = 0
            if DataList[Count] == "Beta1.6":
                Count += 1
                ItemChecker = [ResourceCount, MaterialProduction, MaterialsEarned]
                for Item in ItemChecker:
                    for item in Item:
                        Item[item] = int(DataList[Count])
                        Count += 1

                for item in Mult:
                    Mult[item] = int(DataList[Count])
                    Count += 1

                for quest in Achievments:
                    if Achievments.index(quest) != 6:
                        quest["Finished"] = DataList[Count]
                        if quest["Finished"] == "True":
                            AchievmentRewards(Achievments.index(quest))
                            quest["Finished"] = True
                        else:
                            quest["Finished"] = False
                        quest["Show Cooldown"] = int(DataList[Count + 1])
                    Count += 2

                height = int(DataList[Count])
                width = int(DataList[Count + 1])
                Count += 2
                Images = load_images("Images", height, width)
                board = [[0] * height for _ in range(width)]

                PrestigeCount = int(DataList[Count])
                AscendCount = int(DataList[Count + 1])
                MinerBought = DataList[Count + 2]
                MusicPaused = DataList[Count + 3]
                if MusicPaused == "True":
                    pygame.mixer.music.pause()
                    MusicPaused = True
                else:
                    MusicPaused = False

                Count += 4

                Tiles = ["Grass", "City", "Factory", "Factory Su", "Factory So", "Solar Power", "Super Factory",
                         "Forest Lv1", "Forest Lv2", "Forest Lv3"
                    , "Forest Lv4", "Quarry Lv1", "Quarry Lv2", "Quarry Lv3", "Quarry Lv4", "Water", "Water Dam",
                         "Water Fish", "Fisherman", "Dam"
                    , "CityFar", "CityFac", "Farm"]
                for j in range(height):
                    for i in range(width):
                        board[j][i] = Tiles[int(DataList[Count])]
                        Count += 1

    # Saves data(Useful for Prestiges)


            # Moving your selection with the keys


            # Triggers when you press the mouse


                # Yes or no for Demolishing Buildings


                # Demolishing Buildings


                # Making the selection


                # Restarts the game


                # Prestige shop


                        # Adds things to cost


                        # Wood Upgrade


                        # Stones Upgrade


                        # Food Upgrade


                        # Metal Upgrade


                        # Electricity Upgrade


                        # Mandorium Miner


                # Showing Options


                    # Runs the options window


                        # Handles Events


                                # Saves your data to a save file


                                    # Exports save data


                                # Import save Data:


                        # Displays all the buttons



                # Demolishes Selected Building


                # All of the upgrades


                # Path Choices


                # Taking you back to mainscreen when you finish and calculates time


        # Counting Tiles for certain animations


        # Drawing all Tiles


        # Drawing Selection


        # This is my try at making multiple files. It looks very ineffecient and probably bad to use.

        # Achvievment Check


        # Display the Achievement


        # Shows a confirm message


        # Auto Save



MusicPaused = mainMenu.HomeScreen(pygame, gameDisplay,[font_40,font_50,font_150], clock, MusicPaused)





