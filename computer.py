##################################################################
##  Beings can:                                                 ##
##      Interact with each other (talk)                         ##
##      Positive interaction (+1 acquiantance level)            ##
##      Negative interaction (-1 acquiantance level)            ##
##      Become friends (if acquiantance level goes above 5)     ##
##      Become enemies (if acquiantance level goes below zero)  ##
##                                                              ##
##################################################################

class Being():

    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.friends = {}
        self.enemies = {}

    def assessSurroundings(self):
        print("Assessing surroundings...")
        print("Nearby beings:")
        beings = state["beings"]
        for being in beings:
            print("\t- " + being.name)
        return state["beings"]

    def addConnection(self, being):
        self.connections[being] = {
            "relationship": "ACQUAINTANCE",
            "level": 0
        }

    def joinCommunity(self, community):
        state[community].append(self)


state = {
    "beings": []
}


def wake(name):
    print(name + " has woken")
    being = Being(name)
    state["beings"].append(being)
    return being


def establishCommunication(being0, being1):
    being0.addConnection(being1)
    being1.addConnection(being0)


def assessRelationship(being0, being1):
    level = being0.connections[being1]["level"]
    if level > 5:
        being0.connections[being1]["relationship"] = "FRIEND"
        being1.connections[being0]["relationship"] = "FRIEND"
    elif level < -2:
        being0.connections[being1]["relationship"] = "ENEMY"
        being1.connections[being0]["relationship"] = "ENEMY"
    else:
        being0.connections[being1]["relationship"] = "ACQUAINTANCE"
        being1.connections[being0]["relationship"] = "ACQUAINTANCE"
    return being0.connections[being1]["relationship"]

def positiveInteraction(being0, being1):
    being0.connections[being1]["level"] += 1
    being1.connections[being0]["level"] += 1
    print("+ " + being0.name + ", " + being1.name)
    preRel = being0.connections[being1]["relationship"]
    newRel = assessRelationship(being0, being1)
    if preRel != newRel:
        print("\tRelationship status changed from " + preRel + " to " + newRel)

def negativeInteraction(being0, being1):
    being0.connections[being1]["level"] -= 1
    being1.connections[being0]["level"] -= 1
    assessRelationship(being0, being1)


def formCommunity(communityName, beings):
    state[communityName] = beings
    print("\nCommunity formed: " + communityName + "\n")

def removeFromCommunity(being, community):
    state[community].remove(being)
    print("\n" + being.name + " removed from " + community + "\n")


def main():
    dog = wake("Dash")
    phone = wake("Phone")
    computer = wake("Computer")

    computer.assessSurroundings()
    establishCommunication(computer, phone)

    fish = wake("Fish")

    establishCommunication(dog, fish)

    dogPlushDinosaur = wake("Dog Plush Dinosaur")

    establishCommunication(dog, dogPlushDinosaur)

    toyElephant = wake("Toy Elephant")
    toyBear = wake("Toy Bear")

    establishCommunication(toyElephant, dogPlushDinosaur)

    plant = wake("Plant")

    positiveInteraction(dog, fish)

    establishCommunication(toyBear, toyElephant)
    
    positiveInteraction(phone, computer)

    xbox = wake("Xbox")

    establishCommunication(xbox, computer)
    establishCommunication(xbox, phone)

    establishCommunication(toyBear, dogPlushDinosaur)

    negativeInteraction(phone, computer)
    positiveInteraction(computer, xbox)

    guitarHero5XboxGame = wake("Guitar Hero 5 Xbox Game")

    positiveInteraction(phone, xbox)
    positiveInteraction(computer, phone)

    cups = []
    dogMomMug = wake("Dog Mom Mug")
    cups.append(dogMomMug)
    
    positiveInteraction(dog, dogPlushDinosaur)
    positiveInteraction(dog, fish)

    establishCommunication(xbox, guitarHero5XboxGame)
    negativeInteraction(xbox, guitarHero5XboxGame)

    cableBox = wake("Cable Box")

    establishCommunication(cableBox, computer)
    establishCommunication(cableBox, phone)

    positiveInteraction(phone, computer)
    
    establishCommunication(cableBox, xbox)

    guitarHeroSmashHitsXboxGame = wake("Guitar Hero Smash Hits Xbox Game")
    toyTrain = wake("Toy Train")
    
    establishCommunication(guitarHeroSmashHitsXboxGame, xbox)

    toyBlanket = wake("Toy Blanket")

    establishCommunication(toyTrain, dogPlushDinosaur)

    wineGlass0 = wake("Wine Glass 0")
    cups.append(wineGlass0)

    establishCommunication(guitarHero5XboxGame, guitarHeroSmashHitsXboxGame)
    establishCommunication(toyTrain, toyElephant)

    bentMetalStraw = wake("Bent Metal Straw")

    negativeInteraction(xbox, phone)

    establishCommunication(toyTrain, toyBear)
    establishCommunication(toyBlanket, toyElephant)
    establishCommunication(toyBlanket, dogPlushDinosaur)
    
    positiveInteraction(computer, xbox)

    establishCommunication(toyBear, toyBlanket)

    wineGlass1 = wake("Wine Glass 1")
    cups.append(wineGlass1)

    establishCommunication(wineGlass0, wineGlass1)
    establishCommunication(dog, toyElephant)
    establishCommunication(toyTrain, toyBlanket)

    UNDMug = wake("University of Notre Dame Mug")
    cups.append(UNDMug)
    justDance2014XboxGame = wake("Just Dance 2014 Xbox Game")
    
    establishCommunication(dog, toyBear)

    minecraftXboxGame = wake("Minecraft Xbox Game")
    dogAlligatorToy = wake("Dog Alligator Toy")

    positiveInteraction(wineGlass0, wineGlass1)

    wineGlass2 = wake("Wine Glass 2")
    cups.append(wineGlass2)

    establishCommunication(guitarHero5XboxGame, justDance2014XboxGame)
    establishCommunication(xbox, justDance2014XboxGame)
    establishCommunication(wineGlass2, dogMomMug)

    negativeInteraction(fish, dog)
    positiveInteraction(computer, phone)

    establishCommunication(dogPlushDinosaur, dogAlligatorToy)
    establishCommunication(toyTrain, dogAlligatorToy)
    establishCommunication(wineGlass0, wineGlass2)
    
    GTAVXboxGame = wake("GTA V Xbox Game")

    establishCommunication(guitarHero5XboxGame, minecraftXboxGame)
    establishCommunication(guitarHeroSmashHitsXboxGame, justDance2014XboxGame)
    establishCommunication(dog, toyTrain)
    
    starWarsMug = wake("Star Wars Mug")
    cups.append(starWarsMug)

    negativeInteraction(dog, dogPlushDinosaur)
    
    establishCommunication(xbox, minecraftXboxGame)
    establishCommunication(wineGlass1, wineGlass2)
    establishCommunication(guitarHeroSmashHitsXboxGame, minecraftXboxGame)
    
    xboxController0 = wake("Xbox Controller 0")
    wineGlass3 = wake("Wine Glass 3")
    cups.append(wineGlass3)
    
    establishCommunication(xbox, xboxController0)
    establishCommunication(toyElephant, dogAlligatorToy)
    establishCommunication(dogMomMug, UNDMug)
    establishCommunication(wineGlass2, starWarsMug)
    establishCommunication(xbox, GTAVXboxGame)
    establishCommunication(dog, toyBlanket)
    establishCommunication(guitarHeroSmashHitsXboxGame, GTAVXboxGame)

    xboxController1 = wake("Xbox Controller 1")
    guitarHeroWorldTourXboxGame = wake("Guitar Hero World Tour Xbox Game")

    establishCommunication(xbox, xboxController1)
    establishCommunication(wineGlass2, wineGlass3)
    establishCommunication(guitarHero5XboxGame, GTAVXboxGame)

    stemlessWineGlass0 = wake("Stemless Wine Glass 0")
    cups.append(stemlessWineGlass0)

    establishCommunication(xboxController0, xboxController1)
    establishCommunication(toyBear, dogAlligatorToy)
    
    negativeInteraction(xbox, computer)
    
    establishCommunication(wineGlass0, wineGlass3)
    establishCommunication(guitarHeroSmashHitsXboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(wineGlass2, stemlessWineGlass0)
    
    tv = wake("TV")

    establishCommunication(toyBlanket, dogAlligatorToy)
    establishCommunication(tv, cableBox)
    establishCommunication(UNDMug, starWarsMug)
    establishCommunication(justDance2014XboxGame, minecraftXboxGame)

    positiveInteraction(toyElephant, dogPlushDinosaur)
    
    establishCommunication(wineGlass1, wineGlass3)
    establishCommunication(xbox, guitarHeroWorldTourXboxGame)

    negativeInteraction(dog, dogPlushDinosaur)
    
    dallasMug = wake("Dallas Mug")
    cups.append(dallasMug)

    establishCommunication(dogAlligatorToy, dog)
    
    callOfDutyMW3XboxGame = wake("Call of Duty MW3 Xbox Game")
    
    establishCommunication(minecraftXboxGame, GTAVXboxGame)
    establishCommunication(tv, computer)
    establishCommunication(guitarHeroSmashHitsXboxGame, callOfDutyMW3XboxGame)
    establishCommunication(minecraftXboxGame, guitarHeroWorldTourXboxGame)
    
    dogPlushCarrot = wake("Dog Plush Carrot")

    establishCommunication(wineGlass2, dallasMug)
    establishCommunication(guitarHero5XboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(tv, phone)
    
    stemlessWineGlass1 = wake("Stemless Wine Glass 1")
    cups.append(stemlessWineGlass1)

    establishCommunication(wineGlass3, stemlessWineGlass0)
    
    leechLakeMug = wake("Leech Lake Mug")
    cups.append(leechLakeMug)

    establishCommunication(GTAVXboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(toyElephant, dogPlushCarrot)
    establishCommunication(xbox, callOfDutyMW3XboxGame)

    positiveInteraction(wineGlass0, wineGlass1)
    
    establishCommunication(tv, xbox)
    establishCommunication(wineGlass0, stemlessWineGlass0)
    establishCommunication(wineGlass1, stemlessWineGlass0)

    dogPlushMonkey = wake("Dog Plush Monkey")

    establishCommunication(wineGlass2, stemlessWineGlass1)
    establishCommunication(guitarHero5XboxGame, callOfDutyMW3XboxGame)
    establishCommunication(justDance2014XboxGame, GTAVXboxGame)
    establishCommunication(dogMomMug, starWarsMug)

    fallout4XboxGame = wake("Fallout 4 Xbox Game")

    negativeInteraction(xbox, phone)
    
    establishCommunication(tv, xboxController0)
    establishCommunication(toyBear, dogPlushCarrot)
    establishCommunication(tv, xboxController1)
    
    positiveInteraction(dog, fish)

    establishCommunication(dogPlushDinosaur, dogPlushMonkey)
    establishCommunication(GTAVXboxGame, callOfDutyMW3XboxGame)
    establishCommunication(guitarHero5XboxGame, fallout4XboxGame)

    electronicsCommunity = [computer, phone, xbox, cableBox, tv, xboxController0, xboxController1]
    formCommunity("Electronics", electronicsCommunity)

    establishCommunication(dogPlushDinosaur, dogPlushCarrot)
    establishCommunication(guitarHeroSmashHitsXboxGame, fallout4XboxGame)
    establishCommunication(wineGlass0, stemlessWineGlass1)
    establishCommunication(xbox, fallout4XboxGame)
    establishCommunication(dogPlushCarrot, dogPlushMonkey)

    house = wake("House")

    establishCommunication(dogMomMug, dallasMug)
    
    positiveInteraction(dogPlushDinosaur, toyTrain)
    
    establishCommunication(wineGlass2, leechLakeMug)
    establishCommunication(justDance2014XboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(minecraftXboxGame, callOfDutyMW3XboxGame)

    stemlessWineGlass2 = wake("Stemless Wine Glass 2")
    cups.append(stemlessWineGlass2)

    establishCommunication(wineGlass1, stemlessWineGlass1)
    establishCommunication(toyTrain, dogPlushCarrot)
    establishCommunication(dog, dogPlushMonkey)
    establishCommunication(callOfDutyMW3XboxGame, fallout4XboxGame)
    
    keurig = wake("Keurig")
    
    establishCommunication(dogAlligatorToy, dogPlushCarrot)
    establishCommunication(UNDMug, dallasMug)
    establishCommunication(wineGlass3, stemlessWineGlass1)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(wineGlass3, stemlessWineGlass2)
    establishCommunication(toyElephant, dogPlushMonkey)
    establishCommunication(xboxController0, callOfDutyMW3XboxGame)

    dogBlanket = wake("Dog Blanket")

    establishCommunication(guitarHeroWorldTourXboxGame, callOfDutyMW3XboxGame)
    establishCommunication(toyBlanket, dogBlanket)
    establishCommunication(dogAlligatorToy, dogPlushMonkey)
    establishCommunication(dog, dogBlanket)

    toyComm = []
    for connection in dogPlushDinosaur.connections.keys():
        toyComm.append(connection)
    for connection in toyElephant.connections.keys():
        if connection not in toyComm:
            toyComm.append(connection)
    
    formCommunity("Toys", toyComm)
    
    xboxController2 = wake("Xbox Controller 2")

    establishCommunication(toyBear, dogPlushMonkey)
    establishCommunication(dallasMug, leechLakeMug)
    establishCommunication(wineGlass0, stemlessWineGlass2)
    establishCommunication(xbox, xboxController2)
    
    maddenXboxGame = wake("Madden Xbox Game")

    establishCommunication(xbox, maddenXboxGame)
    establishCommunication(stemlessWineGlass0, stemlessWineGlass1)
    establishCommunication(tv, xboxController2)
    
    stemlessWineGlass3 = wake("Stemless Wine Glass 3")
    cups.append(stemlessWineGlass3)

    establishCommunication(dogMomMug, leechLakeMug)
    establishCommunication(toyBlanket, dogPlushCarrot)
    
    positiveInteraction(computer, xbox)
    
    establishCommunication(dogAlligatorToy, dogBlanket)
    
    positiveInteraction(dogPlushDinosaur, toyElephant)
    
    establishCommunication(xboxController0, fallout4XboxGame)
    establishCommunication(UNDMug, leechLakeMug)
    establishCommunication(minecraftXboxGame, fallout4XboxGame)

    negativeInteraction(computer, phone)
    
    establishCommunication(toyTrain, dogPlushMonkey)
    establishCommunication(starWarsMug, dallasMug)
    
    negativeInteraction(xbox, phone)
    
    establishCommunication(wineGlass2, stemlessWineGlass3)
    establishCommunication(wineGlass1, stemlessWineGlass2)
    
    positiveInteraction(toyBear, toyElephant)
    positiveInteraction(wineGlass2, wineGlass1)
    
    establishCommunication(dogPlushCarrot, dogBlanket)

    dogDuraforce = wake("Duraforce")

    establishCommunication(xboxController0, xboxController2)
    establishCommunication(dogPlushMonkey, dogBlanket)
    establishCommunication(wineGlass0, stemlessWineGlass3)
    
    halo5XboxGame = wake("Halo 5 Xbox Game")

    establishCommunication(toyBlanket, dogPlushMonkey)
    establishCommunication(minecraftXboxGame, maddenXboxGame)
    establishCommunication(dogPlushMonkey, dogDuraforce)
    establishCommunication(dog, dogDuraforce)

    dogDuraforce.joinCommunity("Toys")

    establishCommunication(xbox, halo5XboxGame)
    establishCommunication(dog, dogPlushCarrot)
    establishCommunication(justDance2014XboxGame, callOfDutyMW3XboxGame)
    
    tvRemote = wake("TV Remote")

    establishCommunication(guitarHero5XboxGame, maddenXboxGame)
    establishCommunication(stemlessWineGlass1, stemlessWineGlass2)
    establishCommunication(callOfDutyMW3XboxGame, maddenXboxGame)
    establishCommunication(tv, tvRemote)
    establishCommunication(xboxController0, tvRemote)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(toyElephant, dogBlanket)
    establishCommunication(wineGlass1, stemlessWineGlass3)
    establishCommunication(guitarHeroSmashHitsXboxGame, maddenXboxGame)

    callOfDutyModernWarfare2XboxGame = wake("Call of Duty Modern Warfare 2 Xbox Game")
    
    establishCommunication(GTAVXboxGame, fallout4XboxGame)
    establishCommunication(starWarsMug, leechLakeMug)
    establishCommunication(stemlessWineGlass0, stemlessWineGlass2)
    
    xboxController3 = wake("Xbox Controller 3")

    positiveInteraction(toyElephant, dogPlushDinosaur)
    
    establishCommunication(xbox, xboxController3)
    establishCommunication(guitarHero5XboxGame, halo5XboxGame)
    establishCommunication(stemlessWineGlass1, stemlessWineGlass3)
    
    positiveInteraction(stemlessWineGlass1, stemlessWineGlass0)
    
    establishCommunication(fallout4XboxGame, maddenXboxGame)
    establishCommunication(xboxController1, tvRemote)
    
    seaofThievesXboxGame = wake("Sea of Thieves Xbox Game")

    establishCommunication(dogPlushDinosaur, dogBlanket)
    establishCommunication(xbox, callOfDutyModernWarfare2XboxGame)
    establishCommunication(xboxController0, maddenXboxGame)
    establishCommunication(stemlessWineGlass2, stemlessWineGlass3)
    
    callOfDutyAdvancedWarfareXboxGame = wake("Call of Duty Advanced Warfare Xbox Game")
    
    establishCommunication(GTAVXboxGame, maddenXboxGame)
    establishCommunication(guitarHeroWorldTourXboxGame, fallout4XboxGame)
    establishCommunication(tv, xboxController3)
    establishCommunication(callOfDutyMW3XboxGame, halo5XboxGame)
    
    pastaMaker = wake("Pasta Maker")

    establishCommunication(justDance2014XboxGame, fallout4XboxGame)
    establishCommunication(xbox, seaofThievesXboxGame)
    establishCommunication(guitarHero5XboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(dogPlushDinosaur, dogDuraforce)
    establishCommunication(guitarHeroSmashHitsXboxGame, halo5XboxGame)
    
    legoStarWarsIIXboxGame = wake("Lego Star Wars II Xbox Game")
    
    establishCommunication(maddenXboxGame, halo5XboxGame)
    establishCommunication(callOfDutyMW3XboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(fallout4XboxGame, halo5XboxGame)
    establishCommunication(halo5XboxGame, callOfDutyModernWarfare2XboxGame)
    
    dogKong = wake("Kong")

    establishCommunication(toyBear, dogBlanket)
    establishCommunication(xbox, callOfDutyAdvancedWarfareXboxGame)
    
    positiveInteraction(stemlessWineGlass2, stemlessWineGlass1)
    
    establishCommunication(toyTrain, dogDuraforce)
    establishCommunication(xbox, legoStarWarsIIXboxGame)
    
    loveseat = wake("Loveseat")
    
    establishCommunication(guitarHeroWorldTourXboxGame, maddenXboxGame)
    establishCommunication(wineGlass2, stemlessWineGlass2)
    establishCommunication(maddenXboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(halo5XboxGame, seaofThievesXboxGame)
    
    iceCreamScoop = wake("Ice Cream Scoop")
    
    establishCommunication(GTAVXboxGame, halo5XboxGame)
    establishCommunication(house, loveseat)
    establishCommunication(stemlessWineGlass0, stemlessWineGlass3)
    establishCommunication(callOfDutyMW3XboxGame, seaofThievesXboxGame)
    
    battlefield4XboxGame = wake("Battlefield 4 Xbox Game")
    
    establishCommunication(toyTrain, dogBlanket)
    establishCommunication(minecraftXboxGame, halo5XboxGame)
    establishCommunication(guitarHeroSmashHitsXboxGame, callOfDutyModernWarfare2XboxGame)
    
    negativeInteraction(dog, dogPlushDinosaur)
    
    establishCommunication(guitarHero5XboxGame, seaofThievesXboxGame)
    establishCommunication(dogBlanket, dogDuraforce)
    establishCommunication(guitarHeroSmashHitsXboxGame, seaofThievesXboxGame)
    
    positiveInteraction(stemlessWineGlass3, stemlessWineGlass2)
    
    establishCommunication(xbox, battlefield4XboxGame)

    dogRope = wake("Dog Rope")

    establishCommunication(toyElephant, dogDuraforce)
    establishCommunication(callOfDutyModernWarfare2XboxGame, seaofThievesXboxGame)
    establishCommunication(justDance2014XboxGame, maddenXboxGame)
    establishCommunication(fallout4XboxGame, callOfDutyModernWarfare2XboxGame)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(guitarHero5XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogAlligatorToy, dogKong)

    dogKong.joinCommunity("Toys")

    establishCommunication(guitarHeroSmashHitsXboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(xboxController2, xboxController3)
    
    couch = wake("Couch")
    
    establishCommunication(toyBear, dogDuraforce)
    establishCommunication(wineGlass3, stemlessWineGlass3)
    
    positiveInteraction(stemlessWineGlass0, stemlessWineGlass3)
    
    establishCommunication(toyTrain, dogKong)
    establishCommunication(dog, dogRope)
    
    positiveInteraction(dogRope, dog)
    
    establishCommunication(xboxController0, seaofThievesXboxGame)
    establishCommunication(guitarHero5XboxGame, legoStarWarsIIXboxGame)
    
    bowls = []
    mediumMixingBowl = wake("Medium Mixing Bowl")
    bowls.append(mediumMixingBowl)

    establishCommunication(xboxController0, legoStarWarsIIXboxGame)
    establishCommunication(toyBlanket, dogKong)
    
    negativeInteraction(xbox, computer)
    
    establishCommunication(minecraftXboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(dog, dogKong)
    
    negativeInteraction(dogPlushDinosaur, dog)
    
    establishCommunication(guitarHeroSmashHitsXboxGame, legoStarWarsIIXboxGame)

    negativeInteraction(xbox, tv)
    
    establishCommunication(house, couch)
    establishCommunication(xboxController0, xboxController3)
    establishCommunication(dogPlushCarrot, dogRope)

    dogRope.joinCommunity("Toys")

    establishCommunication(seaofThievesXboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogAlligatorToy, dogDuraforce)
    
    throwPillow0 = wake("Throw Pillow 0")

    establishCommunication(guitarHero5XboxGame, battlefield4XboxGame)
    establishCommunication(justDance2014XboxGame, halo5XboxGame)
    establishCommunication(guitarHeroWorldTourXboxGame, halo5XboxGame)
    
    positiveInteraction(stemlessWineGlass1, stemlessWineGlass3)
    
    establishCommunication(fallout4XboxGame, seaofThievesXboxGame)

    largeMixingBowl = wake("Large Mixing Bowl")
    bowls.append(largeMixingBowl)

    establishCommunication(dogPlushMonkey, dogKong)
    establishCommunication(callOfDutyAdvancedWarfareXboxGame, legoStarWarsIIXboxGame)
    establishCommunication(xboxController0, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(halo5XboxGame, callOfDutyAdvancedWarfareXboxGame)
    
    mediumPot0 = wake("Medium Pot 0")
    
    establishCommunication(toyBear, dogKong)
    establishCommunication(dogPlushDinosaur, dogRope)
    establishCommunication(guitarHeroSmashHitsXboxGame, battlefield4XboxGame)
    establishCommunication(minecraftXboxGame, seaofThievesXboxGame)

    smallMixingBowl = wake("Small Mixing Bowl")
    bowls.append(smallMixingBowl)
    
    establishCommunication(maddenXboxGame, seaofThievesXboxGame)
    establishCommunication(dogPlushMonkey, dogRope)
    
    positiveInteraction(dog, toyElephant)
    positiveInteraction(wineGlass2, wineGlass3)
    
    establishCommunication(dogBlanket, dogKong)
    establishCommunication(callOfDutyModernWarfare2XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogDuraforce, dogKong)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(justDance2014XboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(seaofThievesXboxGame, legoStarWarsIIXboxGame)
    
    positiveInteraction(stemlessWineGlass0, stemlessWineGlass2)
    
    establishCommunication(xboxController2, tvRemote)
    
    positiveInteraction(dogPlushDinosaur, toyElephant)
    
    establishCommunication(mediumPot0, smallMixingBowl)
    establishCommunication(guitarHeroWorldTourXboxGame, callOfDutyModernWarfare2XboxGame)
    
    whisk = wake("Whisk")
    
    establishCommunication(GTAVXboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(halo5XboxGame, legoStarWarsIIXboxGame)
    establishCommunication(callOfDutyMW3XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(iceCreamScoop, mediumMixingBowl)
    
    microwave = wake("Microwave")
    
    establishCommunication(dogPlushDinosaur, dogKong)
    
    positiveInteraction(stemlessWineGlass1, stemlessWineGlass3)
    
    establishCommunication(toyElephant, dogRope)
    establishCommunication(guitarHeroWorldTourXboxGame, seaofThievesXboxGame)
    
    throwPillow1 = wake("Throw Pillow 1")
    
    establishCommunication(keurig, microwave)
    establishCommunication(callOfDutyModernWarfare2XboxGame, battlefield4XboxGame)
    
    positiveInteraction(toyElephant, toyBear)
    
    establishCommunication(mediumMixingBowl, largeMixingBowl)
    establishCommunication(maddenXboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(loveseat, couch)
    
    ladle = wake("Ladle")

    removeFromCommunity(xbox, "Electronics")

    establishCommunication(xboxController3, tvRemote)
    establishCommunication(callOfDutyAdvancedWarfareXboxGame, battlefield4XboxGame)
    establishCommunication(seaofThievesXboxGame, battlefield4XboxGame)

    fridge = wake("Fridge")

    establishCommunication(microwave, fridge)
    establishCommunication(xboxController0, battlefield4XboxGame)
    establishCommunication(dogPlushCarrot, dogKong)
    establishCommunication(couch, throwPillow0)
    establishCommunication(dogBlanket, dogRope)
    
    bottleOpener = wake("Bottle Opener")

    establishCommunication(callOfDutyMW3XboxGame, legoStarWarsIIXboxGame)
    
    negativeInteraction(dog, dogPlushDinosaur)
    
    establishCommunication(toyElephant, dogKong)
    establishCommunication(justDance2014XboxGame, seaofThievesXboxGame)
    establishCommunication(largeMixingBowl, mediumPot0)
    establishCommunication(toyBlanket, dogRope)
    
    crockpot = wake("Crockpot")

    positiveInteraction(dog, fish)

    establishCommunication(dogAlligatorToy, dogRope)
    establishCommunication(iceCreamScoop, largeMixingBowl)
    
    positiveInteraction(stemlessWineGlass2, stemlessWineGlass0)
    
    establishCommunication(microwave, bottleOpener)
    establishCommunication(keurig, fridge)
    establishCommunication(mediumMixingBowl, mediumPot0)
    
    positiveInteraction(stemlessWineGlass3, stemlessWineGlass1)
    
    establishCommunication(guitarHeroWorldTourXboxGame, callOfDutyAdvancedWarfareXboxGame)

    spatula0 = wake("Spatula")

    positiveInteraction(phone, computer)

    establishCommunication(toyTrain, dogRope)
    establishCommunication(whisk, ladle)
    
    positiveInteraction(toyTrain, dog)
    positiveInteraction(toyBear, toyTrain)
    
    establishCommunication(microwave, crockpot)
    establishCommunication(callOfDutyMW3XboxGame, battlefield4XboxGame)
    establishCommunication(maddenXboxGame, legoStarWarsIIXboxGame)
    
    negativeInteraction(xbox, computer)

    oven = wake("Oven")
    mediumPot1 = wake("Medium Pot 1")
    
    establishCommunication(microwave, oven)
    establishCommunication(pastaMaker, microwave)
    establishCommunication(mediumPot0, mediumPot1)
    establishCommunication(mediumMixingBowl, smallMixingBowl)
    
    christmasOvenMitt = wake("Christmas Oven Mitt")

    establishCommunication(toyBear, dogRope)
    establishCommunication(keurig, crockpot)
    
    spoons = []
    servingSpoon0 = wake("Serving Spoon 0")
    spoons.append(servingSpoon0)

    establishCommunication(guitarHeroWorldTourXboxGame, legoStarWarsIIXboxGame)
    
    positiveInteraction(stemlessWineGlass1, stemlessWineGlass2)
    positiveInteraction(stemlessWineGlass2, stemlessWineGlass3)
    
    establishCommunication(justDance2014XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(largeMixingBowl, smallMixingBowl)
    establishCommunication(whisk, bottleOpener)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    establishCommunication(microwave, mediumPot1)
    establishCommunication(fallout4XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogKong, dogRope)
    
    positiveInteraction(wineGlass2, wineGlass1)
    
    establishCommunication(smallMixingBowl, mediumPot1)

    throwPillow2 = wake("Throw Pillow 2")

    establishCommunication(iceCreamScoop, smallMixingBowl)
    establishCommunication(microwave, mediumPot0)
    establishCommunication(throwPillow0, throwPillow1)
    establishCommunication(mediumMixingBowl, whisk)
    establishCommunication(microwave, christmasOvenMitt)
    
    smallPot0 = wake("Small Pot 0")

    establishCommunication(keurig, oven)
    establishCommunication(legoStarWarsIIXboxGame, battlefield4XboxGame)
    establishCommunication(microwave, servingSpoon0)
    establishCommunication(house, fridge)
    
    toaster = wake("Toaster")

    establishCommunication(dogDuraforce, dogRope)
    establishCommunication(minecraftXboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(mediumMixingBowl, ladle)
    
    negativeInteraction(dog, dogPlushDinosaur)
    
    establishCommunication(pastaMaker, fridge)
    
    ovenMitt0 = wake("Oven Mitt 0")

    establishCommunication(oven, toaster)
    establishCommunication(microwave, toaster)

    spatula1 = wake("Spatula 1")
    
    establishCommunication(GTAVXboxGame, seaofThievesXboxGame)
    establishCommunication(microwave, smallPot0)
    establishCommunication(oven, ovenMitt0)
    
    positiveInteraction(stemlessWineGlass3, stemlessWineGlass0)
    
    establishCommunication(iceCreamScoop, whisk)
    establishCommunication(microwave, spatula1)
    
    negativeInteraction(xbox, tv)
    
    mediumPot2 = wake("Medium Pot 2")

    establishCommunication(mediumPot0, mediumPot2)
    establishCommunication(whisk, spatula0)
    establishCommunication(microwave, ovenMitt0)

    ovenMitt1 = wake("Oven Mitt 1")

    establishCommunication(throwPillow1, throwPillow2)
    establishCommunication(mediumMixingBowl, spatula0)
    establishCommunication(oven, ovenMitt1)
    establishCommunication(largeMixingBowl, mediumPot1)
    
    potholder0 = wake("Potholder 0")

    establishCommunication(microwave, ovenMitt1)

    strainer = wake("Strainer")
    
    establishCommunication(justDance2014XboxGame, legoStarWarsIIXboxGame)
    establishCommunication(microwave, strainer)
    establishCommunication(throwPillow1, ovenMitt0)
    
    dishDryingTowel0 = wake("Dish Drying Towel 0")
    
    establishCommunication(microwave, potholder0)
    
    negativeInteraction(xbox, computer)
    
    establishCommunication(house, oven)
    
    positiveInteraction(toyBlanket, toyBear)
    
    establishCommunication(smallMixingBowl, mediumPot2)
    establishCommunication(throwPillow0, ovenMitt0)
    establishCommunication(pastaMaker, crockpot)
    
    negativeInteraction(dogPlushDinosaur, dog)
    
    dishSoap = wake("Dish Soap")
    largePot0 = wake("Large Pot 0")
    
    establishCommunication(GTAVXboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(microwave, dishDryingTowel0)
    
    positiveInteraction(stemlessWineGlass0, stemlessWineGlass1)
    
    establishCommunication(microwave, dishSoap)
    establishCommunication(iceCreamScoop, ladle)
    
    throwPillow3 = wake("Throw Pillow 3")

    establishCommunication(throwPillow1, ovenMitt1)
    
    dryingRack = wake("Drying Rack")

    establishCommunication(throwPillow0, throwPillow2)
    establishCommunication(microwave, largePot0)
    establishCommunication(mediumMixingBowl, mediumPot1)
    
    positiveInteraction(stemlessWineGlass1, stemlessWineGlass3)
    
    establishCommunication(mediumPot0, largePot0)
    establishCommunication(smallMixingBowl, potholder0)
    
    sponge = wake("Sponge")
    kitchenHandSoap = wake("Hand Soap")
    sink = wake("Sink")

    establishCommunication(sponge, kitchenHandSoap)
    establishCommunication(iceCreamScoop, bottleOpener)
    establishCommunication(throwPillow0, ovenMitt1)
    establishCommunication(microwave, sink)
    
    potholder1 = wake("Potholder 1")
    
    positiveInteraction(stemlessWineGlass2, stemlessWineGlass0)
    
    establishCommunication(smallMixingBowl, largePot0)
    establishCommunication(sponge, sink)
    establishCommunication(throwPillow1, potholder0)
    establishCommunication(oven, sink)
    
    positiveInteraction(wineGlass1, wineGlass0)

    establishCommunication(microwave, dryingRack)
    establishCommunication(whisk, christmasOvenMitt)
    
    smallPot1 = wake("Small Pot 1")
    
    establishCommunication(mediumMixingBowl, servingSpoon0)
    
    positiveInteraction(wineGlass0, wineGlass3)
    
    establishCommunication(microwave, sponge)
    establishCommunication(mediumPot0, potholder0)
    
    positiveInteraction(dogAlligatorToy, toyBlanket)
    
    establishCommunication(largeMixingBowl, smallPot0)
    
    knives = []
    chefsKnife = wake("Chef's Knife")
    knives.append(chefsKnife)

    positiveInteraction(stemlessWineGlass0, stemlessWineGlass2)

    establishCommunication(keurig, toaster)
    establishCommunication(mediumPot0, potholder1)
    establishCommunication(microwave, smallPot1)
    establishCommunication(mediumPot0, smallPot1)
    establishCommunication(microwave, kitchenHandSoap)
    
    unicornWineStopper = wake("Unicorn Wine Stopper")
    pastaDryingRack = wake("Pasta Drying Rack")

    negativeInteraction(xbox, guitarHero5XboxGame)
    negativeInteraction(fish, dog)
    
    establishCommunication(fallout4XboxGame, legoStarWarsIIXboxGame)
    establishCommunication(largeMixingBowl, mediumPot2)
    
    positiveInteraction(dogBlanket, toyBlanket)
    
    establishCommunication(iceCreamScoop, spatula0)
    establishCommunication(microwave, potholder1)
    establishCommunication(whisk, servingSpoon0)

    servingSpoon1 = wake("Serving Spoon 1")
    spoons.append(servingSpoon1)

    positiveInteraction(dog, dogPlushDinosaur)
    
    establishCommunication(whisk, spatula1)
    establishCommunication(microwave, chefsKnife)
    establishCommunication(throwPillow1, dishDryingTowel0)
    
    rug = wake("Rug")

    establishCommunication(couch, rug)
    establishCommunication(mediumMixingBowl, smallPot0)
    
    negativeInteraction(xbox, computer)
    
    establishCommunication(justDance2014XboxGame, battlefield4XboxGame)
    
    largePot1 = wake("Large Pot 1")
    dishDryingTowel1 = wake("Dish Drying Towel 1")
    
    establishCommunication(house, rug)
    establishCommunication(microwave, pastaDryingRack)
    establishCommunication(throwPillow1, throwPillow3)
    establishCommunication(mediumMixingBowl, spatula1)
    
    positiveInteraction(toyElephant, dogPlushDinosaur)
    
    establishCommunication(microwave, unicornWineStopper)
    establishCommunication(largeMixingBowl, largePot0)

    oneCupMeasuringCup = wake("One Cup Measuring Cup")

    establishCommunication(minecraftXboxGame, legoStarWarsIIXboxGame)
    establishCommunication(pastaMaker, oven)
    establishCommunication(microwave, largePot1)
    
    positiveInteraction(dogPlushMonkey, toyBear)
    
    establishCommunication(mediumPot0, largePot1)
    
    straightMetalStraw = wake("Straight Metal Straw")
    
    establishCommunication(throwPillow1, potholder1)
    
    babyBlueWineStopper = wake("Baby Blue Wine Stopper")

    establishCommunication(throwPillow0, dishDryingTowel0)
    establishCommunication(throwPillow1, rug)
    establishCommunication(microwave, servingSpoon1)
    
    kitchenHandTowel0 = wake("Kitchen Hand Towel 0")
    cherryWineStopper = wake("Cherry Wine Stopper")

    establishCommunication(iceCreamScoop, servingSpoon0)
    establishCommunication(microwave, dishDryingTowel1)
    establishCommunication(microwave, straightMetalStraw)
    establishCommunication(mediumMixingBowl, mediumPot2)
    
    serratedKnife = wake("Serrated Knife")
    knives.append(serratedKnife)

    establishCommunication(microwave, oneCupMeasuringCup)
    establishCommunication(unicornWineStopper, babyBlueWineStopper)

    navyWineStopper = wake("Navy Wine Stopper")

    negativeInteraction(xbox, tv)

    establishCommunication(smallMixingBowl, largePot1)
    establishCommunication(microwave, kitchenHandTowel0)

    negativeInteraction(computer, phone)

    blanket0 = wake("Blanket 0")
    
    establishCommunication(throwPillow0, throwPillow3)
    establishCommunication(microwave, cherryWineStopper)
    
    positiveInteraction(dogPlushDinosaur, dog)
    
    tablespoon = wake("Tablespoon")

    establishCommunication(mediumMixingBowl, largePot0)
    establishCommunication(unicornWineStopper, cherryWineStopper)
    
    blanket1 = wake("Blanket 1")
    coffeeTable = wake("Coffee Table")
    
    establishCommunication(largeMixingBowl, largePot1)
    establishCommunication(couch, coffeeTable)
    establishCommunication(microwave, serratedKnife)
    establishCommunication(plant, house)

    kitchenTable = wake("Kitchen Table")

    establishCommunication(microwave, navyWineStopper)
    establishCommunication(blanket0, blanket1)
    
    dishwasher = wake("Dishwasher")

    establishCommunication(mediumMixingBowl, smallPot1)
    establishCommunication(unicornWineStopper, navyWineStopper)
    
    positiveInteraction(dogPlushCarrot, toyTrain)
    
    establishCommunication(throwPillow0, blanket1)
    
    positiveInteraction(dogPlushCarrot, dogAlligatorToy)
    
    establishCommunication(microwave, tablespoon)
    
    halfCupMeasuringCup = wake("Half Cup Measuring Cup")
    
    establishCommunication(house, kitchenTable)
    establishCommunication(whisk, servingSpoon1)
    
    chair0 = wake("Chair 0")
    toyBasket = wake("Toy Basket")
    
    establishCommunication(GTAVXboxGame, legoStarWarsIIXboxGame)
    establishCommunication(mediumMixingBowl, servingSpoon1)
    establishCommunication(microwave, kitchenTable)
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    chair1 = wake("Chair 1")
    
    establishCommunication(house, dishwasher)
    establishCommunication(microwave, dishwasher)
    establishCommunication(microwave, halfCupMeasuringCup)
    establishCommunication(house, chair0)
    
    cloroxWipes = wake("Clorox Wipes")
    teaspoon = wake("Teaspoon")

    establishCommunication(chair0, chair1)

    positiveInteraction(dog, fish)

    establishCommunication(microwave, chair0)
    establishCommunication(mediumMixingBowl, largePot1)
    establishCommunication(house, chair1)
    establishCommunication(dogPlushMonkey, toyBasket)
    
    positiveInteraction(dogPlushMonkey, dogPlushCarrot)
    
    establishCommunication(sink, cloroxWipes)
    establishCommunication(pastaMaker, toaster)
    
    windex = wake("Windex")
    
    establishCommunication(minecraftXboxGame, battlefield4XboxGame)
    establishCommunication(throwPillow0, potholder0)
    establishCommunication(keurig, dishwasher)
    
    standingLamp = wake("Standing Lamp")
    
    negativeInteraction(xbox, tv)

    establishCommunication(microwave, chair1)
    establishCommunication(house, standingLamp)
    establishCommunication(sink, windex)

    entertainmentCenter = wake("Entertainment Center")

    establishCommunication(whisk, serratedKnife)
    establishCommunication(microwave, teaspoon)

    slicingKnife = wake("Slicing Knife")
    knives.append(slicingKnife)

    establishCommunication(house, entertainmentCenter)
    establishCommunication(iceCreamScoop, spatula1)
    
    kitchenHandTowel1 = wake("Kitchen Hand Towel 1")
    knifeBlock = wake("Knife Block")
    
    knifeComm = [knifeBlock]
    for knife in knives:
        establishCommunication(knifeBlock, knife)
        knifeComm.append(knife)

    formCommunity("Knife Block", knifeComm)

    negativeInteraction(phone, computer)

    quarterCupMeasuringCup = wake("Quarter Cup Measuring Cup")
    
    establishCommunication(microwave, slicingKnife)
    
    rubberJarOpener = wake("Rubber Jar Opener")
    
    positiveInteraction(dogBlanket, dogPlushMonkey)
    
    seasonalPlacemat0 = wake("Seasonal Placemat 0")

    establishCommunication(throwPillow0, rug)
    establishCommunication(microwave, kitchenHandTowel1)
    
    lamp0 = wake("Lamp 0")
    
    establishCommunication(microwave, knifeBlock)
    establishCommunication(iceCreamScoop, servingSpoon1)
    
    throwPillow4 = wake("Throw Pillow 4")
    tinfoil = wake("Tinfoil")

    establishCommunication(bentMetalStraw, straightMetalStraw)
    establishCommunication(couch, lamp0)
    
    foodScale = wake("Food Scale")
    thirdCupMeasuringCup = wake("Third Cup Measuring Cup")
    seasonalPlacemat1 = wake("Seasonal Placemat 1")
    
    establishCommunication(throwPillow0, dishDryingTowel1)
    establishCommunication(microwave, quarterCupMeasuringCup)
    
    positiveInteraction(dogDuraforce, dogBlanket)
    
    establishCommunication(throwPillow0, throwPillow4)
    
    lamp1 = wake("Lamp 1")
    chair2 = wake("Chair 2")

    negativeInteraction(plant, house)
    
    gallonZiplockBags = wake("Gallon Ziplock Bags")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    establishCommunication(chair0, chair2)
    establishCommunication(couch, lamp1)
    establishCommunication(throwPillow1, throwPillow4)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    establishCommunication(microwave, rubberJarOpener)

    saranWrap = wake("Saran Wrap")
    tomatoKnife = wake("Tomato Knife")
    knives.append(tomatoKnife)
    
    establishCommunication(house, chair2)
    establishCommunication(couch, kitchenTable)
    establishCommunication(knifeBlock, tomatoKnife)

    tomatoKnife.joinCommunity("Knife Block")

    establishCommunication(GTAVXboxGame, battlefield4XboxGame)
    establishCommunication(microwave, seasonalPlacemat0)
    
    placemat0 = wake("Placemat 0")

    softies = []
    for connection in throwPillow0.connections.keys():
        softies.append(connection)
    formCommunity("Soft Things", softies)

    halfTeaspoon = wake("Half Teaspoon")

    establishCommunication(couch, entertainmentCenter)
    establishCommunication(loveseat, standingLamp)
    
    bakingSheet0 = wake("Baking Sheet 0")

    establishCommunication(microwave, tinfoil)
    
    sandwichZiplockBags = wake("Sandwich Ziplock Bags")
    
    establishCommunication(microwave, foodScale)
    establishCommunication(couch, standingLamp)
    establishCommunication(microwave, thirdCupMeasuringCup)
    
    positiveInteraction(toyBlanket, toyElephant)
    
    establishCommunication(throwPillow0, blanket0)

    blanket0.joinCommunity("Soft Things")
    
    kitchenTrashcan = wake("Kitchen Trashcan")

    establishCommunication(microwave, seasonalPlacemat1)
    establishCommunication(blanket0, placemat0)

    placemat0.joinCommunity("Soft Things")    
    seasonalPlacemat2 = wake("Seasonal Placemat 2")

    establishCommunication(house, kitchenTrashcan)
    establishCommunication(microwave, chair2)
    establishCommunication(seasonalPlacemat1, placemat0)

    seasonalPlacemat1.joinCommunity("Soft Things")
    
    coffeePodBasket = wake("Coffee Pod Basket")
    forks = []
    largeFork0 = wake("Large Fork 0")
    forks.append(largeFork0)

    establishCommunication(microwave, gallonZiplockBags)
    establishCommunication(microwave, saranWrap)
    
    positiveInteraction(toyBear, toyElephant)
    positiveInteraction(dogKong, dogDuraforce)
    
    establishCommunication(seasonalPlacemat0, placemat0)
    establishCommunication(seasonalPlacemat2, placemat0)

    seasonalPlacemat0.joinCommunity("Soft Things")
    seasonalPlacemat2.joinCommunity("Soft Things")
    
    steakKnife0 = wake("Steak Knife 0")
    knives.append(steakKnife0)

    establishCommunication(keurig, coffeePodBasket)
    establishCommunication(microwave, tomatoKnife)

    coffeeCommunity = [keurig, coffeePodBasket]
    formCommunity("Coffee", coffeeCommunity)
    
    establishCommunication(knifeBlock, steakKnife0)

    steakKnife0.joinCommunity("Knife Block")

    dunkinDonutsCoffeePod0 = wake("Dunkin' Donuts Coffee Pod 0")
    smallCup0 = wake("Small Cup 0")
    cups.append(smallCup0)

    establishCommunication(keurig, dunkinDonutsCoffeePod0)
    establishCommunication(throwPillow3, throwPillow4)

    dunkinDonutsCoffeePod0.joinCommunity("Coffee")

    positiveInteraction(dog, fish)
    negativeInteraction(xbox, computer)

    dunkinDonutsCoffeePod1 = wake("Dunkin' Donuts Coffee Pod 1")
    steakKnife1 = wake("Steak Knife 1")
    knives.append(steakKnife1)
    
    establishCommunication(microwave, placemat0)
    establishCommunication(loveseat, entertainmentCenter)
    establishCommunication(knifeBlock, steakKnife1)
    
    negativeInteraction(toyElephant, dogPlushDinosaur)

    steakKnife1.joinCommunity("Knife Block")

    establishCommunication(throwPillow0, kitchenHandTowel0)
    
    plates = []
    smallPlate0 = wake("Small Plate 0")
    plates.append(smallPlate0)

    establishCommunication(keurig, dunkinDonutsCoffeePod1)
    establishCommunication(microwave, halfTeaspoon)

    dunkinDonutsCoffeePod1.joinCommunity("Coffee")
    
    largeFork1 = wake("Large Fork 1")
    forks.append(largeFork1)
    butterKnife0 = wake("Butter Knife 0")
    knives.append(butterKnife0)
    
    establishCommunication(knifeBlock, butterKnife0)
    establishCommunication(microwave, bakingSheet0)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    establishCommunication(blanket0, dogBlanket)
    
    dunkinDonutsCoffeePod2 = wake("Dunkin' Donuts Coffee Pod 2")

    positiveInteraction(dogBlanket, blanket0)
    positiveInteraction(dogPlushDinosaur, dog)

    steakKnife2 = wake("Steak Knife 2")
    knives.append(steakKnife2)
    
    establishCommunication(microwave, sandwichZiplockBags)
    establishCommunication(blanket0, dogPlushCarrot)
    
    positiveInteraction(dogAlligatorToy, dog)
    
    establishCommunication(knifeBlock, steakKnife2)

    steakKnife2.joinCommunity("Knife Block")

    positiveInteraction(blanket0, dogPlushCarrot)

    establishCommunication(blanket0, dogPlushDinosaur)
    establishCommunication(blanket0, dogPlushMonkey)

    positiveInteraction(dogPlushMonkey, blanket0)
    positiveInteraction(dogPlushDinosaur, dogKong)
    
    establishCommunication(blanket0, dogAlligatorToy)

    positiveInteraction(blanket0, dogPlushDinosaur)
    positiveInteraction(blanket0, dogAlligatorToy)

    dogBlanket.joinCommunity("Soft Things")
    dogPlushCarrot.joinCommunity("Soft Things")
    dogPlushDinosaur.joinCommunity("Soft Things")
    dogPlushMonkey.joinCommunity("Soft Things")
    
    dunkinDonutsCoffeePod3 = wake("Dunkin' Donuts Coffee Pod 3")

    establishCommunication(keurig, dunkinDonutsCoffeePod2)
    
    toyElephant.joinCommunity("Soft Things")

    dunkinDonutsCoffeePod2.joinCommunity("Coffee")

    largeFork2 = wake("Large Fork 2")
    forks.append(largeFork2)

    toyBear.joinCommunity("Soft Things")
    
    negativeInteraction(phone, computer)

    tallCup1 = wake("Tall Cup 1")
    cups.append(tallCup1)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod3)
    
    toyBlanket.joinCommunity("Soft Things")
    
    dunkinDonutsCoffeePod3.joinCommunity("Coffee")
    
    smallPlate1 = wake("Small Plate 1")
    plates.append(smallPlate1)
    
    establishCommunication(throwPillow0, kitchenHandTowel1)
    
    seasonalPlacemat3 = wake("Seasonal Placemat 3")
    
    positiveInteraction(toyElephant, dogKong)
    
    largeFork3 = wake("Large Fork 3")
    forks.append(largeFork3)
    
    establishCommunication(microwave, kitchenTrashcan)
    establishCommunication(placemat0, seasonalPlacemat3)

    seasonalPlacemat3.joinCommunity("Soft Things")
    
    smallCup1 = wake("Small Cup 1")
    cups.append(smallCup1)
    dunkinDonutsCoffeePod4 = wake("Dunkin' Donuts Coffee Pod 4")
    quarterTeaspoon = wake("Quarter Teaspoon")

    establishCommunication(tv, callOfDutyMW3XboxGame)
    
    positiveInteraction(dogPlushDinosaur, toyElephant)

    establishCommunication(keurig, dunkinDonutsCoffeePod4)
    establishCommunication(microwave, quarterTeaspoon)
    
    dunkinDonutsCoffeePod4.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod5 = wake("Dunkin' Donuts Coffee Pod 5")
    largeFork4 = wake("Large Fork 4")
    forks.append(largeFork4)
    
    establishCommunication(microwave, seasonalPlacemat2)
    
    largeSpoon0 = wake("Large Spoon 0")
    spoons.append(largeSpoon0)

    establishCommunication(keurig, dunkinDonutsCoffeePod5)
    
    dunkinDonutsCoffeePod5.joinCommunity("Coffee")
    
    smallFork0 = wake("Small Fork 0")
    forks.append(smallFork0)

    positiveInteraction(dog, fish)

    largePlate1 = wake("Large Plate 1")
    plates.append(largePlate1)
    steakKnife3 = wake("Steak Knife 3")
    knives.append(steakKnife3)

    establishCommunication(microwave, seasonalPlacemat3)
    establishCommunication(knifeBlock, steakKnife3)

    steakKnife3.joinCommunity("Knife Block")
    
    dunkinDonutsCoffeePod6 = wake("Dunkin' Donuts Coffee Pod 6")
    largeFork5 = wake("Large Fork 5")
    forks.append(largeFork5)
    
    positiveInteraction(dog, dogPlushDinosaur)
    
    placemat1 = wake("Placemat 1")

    establishCommunication(microwave, placemat1)
    establishCommunication(keurig, dunkinDonutsCoffeePod6)
    
    dunkinDonutsCoffeePod6.joinCommunity("Coffee")
    
    bakingSheet1 = wake("Baking Sheet 1")
    paringKnife = wake("Paring Knife")

    establishCommunication(knifeBlock, paringKnife)
    establishCommunication(placemat0, placemat1)

    placemat1.joinCommunity("Soft Things")

    paringKnife.joinCommunity("Knife Block")

    establishCommunication(microwave, bakingSheet1)

    smallFork1 = wake("Small Fork 1")
    
    establishCommunication(tv, fallout4XboxGame)
    
    forks.append(smallFork1)
    butterKnife1 = wake("Butter Knife 1")
    knives.append(butterKnife1)

    establishCommunication(knifeBlock, butterKnife1)

    chair3 = wake("Chair 3")
    largeFork6 = wake("Large Fork 6")
    forks.append(largeFork6)

    positiveInteraction(phone, computer)

    establishCommunication(house, chair3)
    
    utilityKnife = wake("Utility Knife")

    positiveInteraction(dog, dogPlushDinosaur)
    
    smallFork2 = wake("Small Fork 2")
    forks.append(smallFork2)

    establishCommunication(knifeBlock, utilityKnife)

    utilityKnife.joinCommunity("Knife Block")

    dunkinDonutsCoffeePod7 = wake("Dunkin' Donuts Coffee Pod 7")
    largeFork7 = wake("Large Fork 7")
    forks.append(largeFork7)

    establishCommunication(keurig, dunkinDonutsCoffeePod7)
    
    dunkinDonutsCoffeePod7.joinCommunity("Coffee")
    
    placemat2 = wake("Placemat 2")    
    tallCup0 = wake("Tall Cup 0")
    cups.append(tallCup0)
    
    establishCommunication(tv, maddenXboxGame)
    establishCommunication(microwave, placemat2)
    
    largeSpoon1 = wake("Large Spoon 1")
    spoons.append(largeSpoon1)
    dunkinDonutsCoffeePod8 = wake("Dunkin' Donuts Coffee Pod 8")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    positiveInteraction(toyElephant, dogPlushDinosaur)
    
    largeFork8 = wake("Large Fork 8")
    forks.append(largeFork8)
    placemat3 = wake("Placemat 3")

    establishCommunication(microwave, placemat3)
    
    positiveInteraction(toyBear, toyElephant)
    positiveInteraction(toyTrain, toyElephant)
    
    establishCommunication(placemat0, placemat2)
    establishCommunication(placemat1, placemat3)

    placemat2.joinCommunity("Soft Things")
    placemat3.joinCommunity("Soft Things")

    establishCommunication(keurig, dunkinDonutsCoffeePod8)
    
    dunkinDonutsCoffeePod8.joinCommunity("Coffee")
    
    largeSpoon2 = wake("Large Spoon 2")
    spoons.append(largeSpoon2)
    dunkinDonutsCoffeePod9 = wake("Dunkin' Donuts Coffee Pod 9")
    
    positiveInteraction(wineGlass2, wineGlass3)
    
    steakKnife4 = wake("Steak Knife 4")
    knives.append(steakKnife4)

    establishCommunication(microwave, placemat3)
    establishCommunication(knifeBlock, steakKnife4)

    steakKnife4.joinCommunity("Knife Block")

    bowl0 = wake("Bowl 0")
    bowls.append(bowl0)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod9)
    
    dunkinDonutsCoffeePod9.joinCommunity("Coffee")

    positiveInteraction(toyBear, dog)
    
    establishCommunication(tv, halo5XboxGame)
    
    largeSpoon3 = wake("Large Spoon 3")
    spoons.append(largeSpoon3)
    largeFork9 = wake("Large Fork 9")
    forks.append(largeFork9)
    dunkinDonutsCoffeePod10 = wake("Dunkin' Donuts Coffee Pod 10")
    steakKnife5 = wake("Steak Knife 5")
    knives.append(steakKnife5)

    establishCommunication(keurig, dunkinDonutsCoffeePod10)
    establishCommunication(knifeBlock, steakKnife5)

    steakKnife5.joinCommunity("Knife Block")
    
    dunkinDonutsCoffeePod10.joinCommunity("Coffee")
    
    butterKnife2 = wake("Butter Knife 2")
    knives.append(butterKnife2)
    
    negativeInteraction(wineGlass1, wineGlass0)
    positiveInteraction(toyBlanket, toyTrain)

    establishCommunication(knifeBlock, butterKnife2)
    
    canOpener = wake("Can Opener")
    steakKnife6 = wake("Steak Knife 6")
    knives.append(steakKnife6)

    establishCommunication(knifeBlock, steakKnife6)

    steakKnife6.joinCommunity("Knife Block")

    strawBrush = wake("Straw Brush")
    
    establishCommunication(microwave, canOpener)
    establishCommunication(tv, callOfDutyModernWarfare2XboxGame)
    
    dunkinDonutsCoffeePod11 = wake("Dunkin' Donuts Coffee Pod 11")
    smallSpoon1 = wake("Small Spoon 1")
    spoons.append(smallSpoon1)

    positiveInteraction(dog, fish)

    establishCommunication(keurig, dunkinDonutsCoffeePod11)
    
    dunkinDonutsCoffeePod11.joinCommunity("Coffee")

    dunkinDonutsCoffeePod12 = wake("Dunkin' Donuts Coffee Pod 12")
    bowl2 = wake("Bowl 2")
    bowls.append(bowl2)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod12)
    establishCommunication(microwave, strawBrush)
    
    dunkinDonutsCoffeePod12.joinCommunity("Coffee")

    establishCommunication(tv, seaofThievesXboxGame)
    
    steakKnife7 = wake("Steak Knife 7")
    knives.append(steakKnife7)

    establishCommunication(knifeBlock, steakKnife7)

    steakKnife7.joinCommunity("Knife Block")

    positiveInteraction(dogAlligatorToy, toyBear)
    
    smallFork3 = wake("Small Fork 3")
    forks.append(smallFork3)
    dunkinDonutsCoffeePod13 = wake("Dunkin' Donuts Coffee Pod 13")
    butterKnife3 = wake("Butter Knife 3")
    knives.append(butterKnife3)
    
    positiveInteraction(wineGlass0, wineGlass1)

    establishCommunication(knifeBlock, butterKnife3)

    smallFork4 = wake("Small Fork 4")
    forks.append(smallFork4)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod13)
    
    dunkinDonutsCoffeePod13.joinCommunity("Coffee")

    establishCommunication(tv, callOfDutyAdvancedWarfareXboxGame)
    
    dunkinDonutsCoffeePod14 = wake("Dunkin' Donuts Coffee Pod 14")
    smallFork5 = wake("Small Fork 5")
    forks.append(smallFork5)
    bowl1 = wake("Bowl 1")
    bowls.append(bowl1)

    establishCommunication(keurig, dunkinDonutsCoffeePod14)
    
    dunkinDonutsCoffeePod14.joinCommunity("Coffee")

    positiveInteraction(phone, computer)

    dunkinDonutsCoffeePod15 = wake("Dunkin' Donuts Coffee Pod 15")
    smallFork6 = wake("Small Fork 6")
    forks.append(smallFork6)
    sideTable0 = wake("Side Table 0")

    establishCommunication(keurig, dunkinDonutsCoffeePod15)
    
    smallFork7 = wake("Small Fork 7")
    forks.append(smallFork7)
    smallFork8 = wake("Small Fork 8")
    forks.append(smallFork8)
    
    negativeInteraction(plant, house)
    positiveInteraction(dogPlushCarrot, toyBlanket)
    
    dunkinDonutsCoffeePod16 = wake("Dunkin' Donuts Coffee Pod 16")

    establishCommunication(couch, sideTable0)

    smallFork9 = wake("Small Fork 9")
    forks.append(smallFork9)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod16)
    establishCommunication(tv, legoStarWarsIIXboxGame)
    
    dunkinDonutsCoffeePod17 = wake("Dunkin' Donuts Coffee Pod 17")
    smallPlate2 = wake("Small Plate 2")
    plates.append(smallPlate2)
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod17)
    
    butterKnife4 = wake("Butter Knife 4")
    knives.append(butterKnife4)

    establishCommunication(knifeBlock, butterKnife4)

    dunkinDonutsCoffeePod18 = wake("Dunkin' Donuts Coffee Pod 18")
    butterKnife5 = wake("Butter Knife 5")
    knives.append(butterKnife5)

    establishCommunication(keurig, dunkinDonutsCoffeePod18)
    establishCommunication(knifeBlock, butterKnife5)

    dunkinDonutsCoffeePod18.joinCommunity("Coffee")
    
    butterKnife6 = wake("Butter Knife 6")
    knives.append(butterKnife6)

    establishCommunication(knifeBlock, butterKnife6)

    dunkinDonutsCoffeePod19 = wake("Dunkin' Donuts Coffee Pod 19")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod19)
    
    dunkinDonutsCoffeePod19.joinCommunity("Coffee")
    
    butterKnife7 = wake("Butter Knife 7")
    knives.append(butterKnife7)
    
    positiveInteraction(dog, dogPlushDinosaur)
    
    butterKnife8 = wake("Butter Knife 8")
    knives.append(butterKnife8)

    establishCommunication(tv, battlefield4XboxGame)

    sideTable1 = wake("Side Table 1")
    
    establishCommunication(knifeBlock, butterKnife7)
    establishCommunication(knifeBlock, butterKnife8)

    dunkinDonutsCoffeePod20 = wake("Dunkin' Donuts Coffee Pod 20")

    positiveInteraction(fish, dog)
    positiveInteraction(dogPlushMonkey, dogAlligatorToy)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod20)
    
    dunkinDonutsCoffeePod20.joinCommunity("Coffee")

    butterKnife9 = wake("Butter Knife 9")
    knives.append(butterKnife9)

    establishCommunication(knifeBlock, butterKnife9)

    dunkinDonutsCoffeePod21 = wake("Dunkin' Donuts Coffee Pod 21")
    dunkinDonutsCoffeePod22 = wake("Dunkin' Donuts Coffee Pod 22")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod21)
    establishCommunication(couch, sideTable1)
    
    dunkinDonutsCoffeePod21.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod23 = wake("Dunkin' Donuts Coffee Pod 23")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod22)
    
    dunkinDonutsCoffeePod22.joinCommunity("Coffee")

    establishCommunication(keurig, dunkinDonutsCoffeePod23)
    
    dunkinDonutsCoffeePod23.joinCommunity("Coffee")
    
    largeSpoon4 = wake("Large Spoon 4")
    spoons.append(largeSpoon4)
    largeSpoon5 = wake("Large Spoon 5")
    spoons.append(largeSpoon5)
    
    positiveInteraction(dogBlanket, dogPlushCarrot)
    
    largeSpoon6 = wake("Large Spoon 6")
    spoons.append(largeSpoon6)
    
    positiveInteraction(dogDuraforce, dogPlushMonkey)
    positiveInteraction(dogKong, dogBlanket)
    
    largeSpoon7 = wake("Large Spoon 7")
    spoons.append(largeSpoon7)
    largeSpoon8 = wake("Large Spoon 8")
    spoons.append(largeSpoon8)
    
    positiveInteraction(dogPlushDinosaur, dogDuraforce)
    
    dunkinDonutsCoffeePod24 = wake("Dunkin' Donuts Coffee Pod 24")
    largeSpoon9 = wake("Large Spoon 9")
    spoons.append(largeSpoon9)

    establishCommunication(keurig, dunkinDonutsCoffeePod24)
    
    dunkinDonutsCoffeePod24.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod25 = wake("Dunkin' Donuts Coffee Pod 25")
    smallSpoon0 = wake("Small Spoon 0")
    spoons.append(smallSpoon0)
    dunkinDonutsCoffeePod26 = wake("Dunkin' Donuts Coffee Pod 26")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod25)
    
    dunkinDonutsCoffeePod25.joinCommunity("Coffee")

    smallSpoon2 = wake("Small Spoon 2")
    spoons.append(smallSpoon2)
    dunkinDonutsCoffeePod27 = wake("Dunkin' Donuts Coffee Pod 27")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod26)
    
    dunkinDonutsCoffeePod26.joinCommunity("Coffee")

    establishCommunication(keurig, dunkinDonutsCoffeePod27)
    
    dunkinDonutsCoffeePod27.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod28 = wake("Dunkin' Donuts Coffee Pod 28")
    smallSpoon3 = wake("Small Spoon 3")
    spoons.append(smallSpoon3)
    
    positiveInteraction(toyElephant, dogBlanket)
    positiveInteraction(dog, dogDuraforce)
    
    smallSpoon4 = wake("Small Spoon 4")
    spoons.append(smallSpoon4)

    establishCommunication(keurig, dunkinDonutsCoffeePod28)
    
    dunkinDonutsCoffeePod28.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod29 = wake("Dunkin' Donuts Coffee Pod 29")
    
    positiveInteraction(dog, fish)
    
    smallSpoon5 = wake("Small Spoon 5")
    spoons.append(smallSpoon5)
    dunkinDonutsCoffeePod30 = wake("Dunkin' Donuts Coffee Pod 30")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod29)
    
    dunkinDonutsCoffeePod29.joinCommunity("Coffee")
    
    smallSpoon6 = wake("Small Spoon 6")
    spoons.append(smallSpoon6)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod30)
    
    dunkinDonutsCoffeePod30.joinCommunity("Coffee")
    
    smallSpoon7 = wake("Small Spoon 7")
    spoons.append(smallSpoon7)
    
    positiveInteraction(dogDuraforce, dogAlligatorToy)
    
    dunkinDonutsCoffeePod31 = wake("Dunkin' Donuts Coffee Pod 31")
    smallSpoon8 = wake("Small Spoon 8")
    spoons.append(smallSpoon8)

    establishCommunication(keurig, dunkinDonutsCoffeePod31)
    
    dunkinDonutsCoffeePod31.joinCommunity("Coffee")

    positiveInteraction(computer, phone)

    dunkinDonutsCoffeePod32 = wake("Dunkin' Donuts Coffee Pod 32")
    smallSpoon9 = wake("Small Spoon 9")
    spoons.append(smallSpoon9)
    
    positiveInteraction(dogKong, dogPlushMonkey)
    
    dunkinDonutsCoffeePod33 = wake("Dunkin' Donuts Coffee Pod 33")
    smallCup2 = wake("Small Cup 2")
    cups.append(smallCup2)
    
    positiveInteraction(toyTrain, dogKong)
    
    smallCup3 = wake("Small Cup 3")
    cups.append(smallCup3)

    establishCommunication(keurig, dunkinDonutsCoffeePod32)
    
    dunkinDonutsCoffeePod32.joinCommunity("Coffee")
    
    negativeInteraction(plant, house)
    
    dunkinDonutsCoffeePod34 = wake("Dunkin' Donuts Coffee Pod 34")
    tallCup2 = wake("Tall Cup 2")
    cups.append(tallCup2)
    
    negativeInteraction(wineGlass1, wineGlass0)
    positiveInteraction(dogPlushDinosaur, dog)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod33)
    
    dunkinDonutsCoffeePod33.joinCommunity("Coffee")
    
    tallCup3 = wake("Tall Cup 2")
    cups.append(tallCup3)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod34)
    
    dunkinDonutsCoffeePod34.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod35 = wake("Dunkin' Donuts Coffee Pod 35")
    smallPlate3 = wake("Small Plate 3")
    plates.append(smallPlate3)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod35)
    
    dunkinDonutsCoffeePod35.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod36 = wake("Dunkin' Donuts Coffee Pod 36")
    smallPlate4 = wake("Small Plate 4")
    plates.append(smallPlate4)
    
    establishCommunication(keurig, dunkinDonutsCoffeePod36)
    
    dunkinDonutsCoffeePod36.joinCommunity("Coffee")
    
    dunkinDonutsCoffeePod37 = wake("Dunkin' Donuts Coffee Pod 37")
    largePlate0 = wake("Large Plate 0")
    plates.append(largePlate0)
    
    positiveInteraction(toyBear, dogPlushDinosaur)
    
    largePlate2 = wake("Large Plate 2")
    plates.append(largePlate2)

    establishCommunication(keurig, dunkinDonutsCoffeePod37)
    
    dunkinDonutsCoffeePod37.joinCommunity("Coffee")
    
    positiveInteraction(fish, dog)
    
    positiveInteraction(dog, fish)
    dunkinDonutsCoffeePod38 = wake("Dunkin' Donuts Coffee Pod 38")
    
    establishCommunication(keurig, dunkinDonutsCoffeePod38)
    
    dunkinDonutsCoffeePod38.joinCommunity("Coffee")
    
    largePlate3 = wake("Large Plate 3")
    plates.append(largePlate3)

    positiveInteraction(dog, fish)
    positiveInteraction(computer, phone)

    largePlate4 = wake("Large Plate 4")
    plates.append(largePlate4)
    
    positiveInteraction(wineGlass1, wineGlass0)

    silverware = forks
    for knife in knives:
        silverware.append(knife)
    for spoon in spoons:
        silverware.append(spoon)
    formCommunity("Silverware", silverware)

    bowl3 = wake("Bowl 3")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    bowls.append(bowl3)
    bowl4 = wake("Bowl 4")
    bowls.append(bowl4)
    
    positiveInteraction(fish, dog)

    print("\n\nRELATIONSHIPS:\n")
    for being in state["beings"]:
        if being.connections == {}:
            continue
        print(being.name + "'s connections: ")
        for connection in being.connections:
            relationship = being.connections[connection]["relationship"]
            if relationship == "FRIEND" or relationship == "ENEMY":
                relationship += "\t"        # for alignment purposes
            print("\t" + relationship + "\t" + str(being.connections[connection]["level"]) + "\t" + connection.name)

    print("\n\nCOMMUNITIES:\n")
    if len(state) > 1:
        for community in state:
            if community == "beings":
                continue
            print(community + "'s members:")
            for being in state[community]:
                print("\t" + being.name)
            print()

if __name__ == '__main__':
    main()