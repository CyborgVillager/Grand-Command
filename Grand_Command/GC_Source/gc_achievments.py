from gc_source_mod import *


def Achviement(Achviements):
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count, PrestigeCount
    count = 0
    for Quest in Achviements:
        if count == 0:
            if Quest["wood"] <= MaterialsEarned["Wood"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(0)
        if count == 1:
            if Quest["food"] <= MaterialsEarned["Food"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(1)
        if count == 2:
            if Quest["metal"] <= MaterialsEarned["Metal"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(2)
        if count == 3:
            if Quest["Electricity"] <= MaterialsEarned["Electricity"] and Quest["Finished"] == False:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(3)
        if count == 4:
            if Count["Forest Lv4"] > 0 or Count["Quarry Lv4"] > 0:
                if Quest["Finished"] == False:
                    Quest["Finished"] = True
                    Quest["Show Cooldown"] = 10
                    AchievmentRewards(4)
        if count == 5:
            if Quest["Finished"] == False and ResourceCount["Food"] >= 200:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
                AchievmentRewards(5)
        if count == 6:
            if Quest["Finished"] == False and PrestigeCount >= 3:
                Quest["Finished"] = True
                Quest["Show Cooldown"] = 10
        count += 1

    return Achviements


def AchievmentRewards(Num):
    global ResourceCount, MaterialProduction, UnUpgradable, UpgradeInfo, MaterialsEarned, Unlocked, Count

    if Num == 0:
        UnUpgradable.pop(UnUpgradable.index("Grass"))
        UnUpgradable.append("CityFac")
        UnUpgradable.append("City")
        UnUpgradable.append("CityFar")
        UpgradeInfo["Grass"] = ["50 Wood", "20 Stones", "0 Food", "1 Food"]
    if Num == 1:
        UnUpgradable.pop(UnUpgradable.index("CityFac"))
        UnUpgradable.pop(UnUpgradable.index("CityFar"))
        UnUpgradable.append("Farm")
        UnUpgradable.append("Factory Su")
        UnUpgradable.append("Factory")
        UnUpgradable.append("Factory So")
        UpgradeInfo["CityFar"] = ["100 Wood", "50 food", "1 Food", "3 Food"]
        UpgradeInfo["CityFac"] = ["50 stones", "1 food per second", "1 Food", "1 Metal"]
    if Num == 2:
        UnUpgradable.pop(UnUpgradable.index("Water Dam"))
        UnUpgradable.append("Dam")
        UpgradeInfo["Water Dam"] = ["200 Wood", "50 metal", "0 Electricity", "1 Electricity"]
    if Num == 3:
        UnUpgradable.pop(UnUpgradable.index("Forest Lv3"))
        UnUpgradable.append("Forest Lv4")
        UnUpgradable.pop(UnUpgradable.index("Quarry Lv3"))
        UnUpgradable.append("Quarry Lv4")
        UpgradeInfo["Forest Lv3"] = ["100 Metal", "1 Electricity per second", "5 wood", "15 wood"]
        UpgradeInfo["Quarry Lv3"] = ["150 Metal", "1 Electricity per second", "5 stones", "15 stones"]
    if Num == 4:
        UnUpgradable.pop(UnUpgradable.index("Factory So"))
        UnUpgradable.pop(UnUpgradable.index("Factory Su"))
        UnUpgradable.append("Super Factory")
        UnUpgradable.append("Solar Power")
        UpgradeInfo["Factory Su"] = ["100 Metal", "2 Electricity per second", "1 metal", "5 Metal"]
        UpgradeInfo["Factory So"] = ["100 Metal", "1 Food per second", "1 metal", "3 Electricity"]
    if Num == 5:
        UnUpgradable.pop(UnUpgradable.index("Water Fish"))
        UnUpgradable.append("Fisherman")
        UpgradeInfo["Water Fish"] = ["100 Wood", "25 metal", "0 Food", "2 Food"]
from global_info import *