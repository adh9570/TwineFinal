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

    toyElephant = wake("Elephant")
    toyBear = wake("Bear")

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

    establishCommunication(toyTrain, toyBear)
    establishCommunication(toyBlanket, toyElephant)
    establishCommunication(toyBlanket, dogPlushDinosaur)
    establishCommunication(toyBear, toyBlanket)

    wineGlass1 = wake("Wine Glass 1")
    cups.append(wineGlass1)

    establishCommunication(wineGlass0, wineGlass1)
    establishCommunication(toyTrain, toyBlanket)

    UNDMug = wake("University of Notre Dame Mug")
    cups.append(UNDMug)
    justDance2014XboxGame = wake("Just Dance 2014 Xbox Game")
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
    
    starWarsMug = wake("Star Wars Mug")
    cups.append(starWarsMug)
    
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
    establishCommunication(wineGlass0, wineGlass3)
    establishCommunication(guitarHeroSmashHitsXboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(wineGlass2, stemlessWineGlass0)
    
    tv = wake("TV")

    establishCommunication(toyBlanket, dogAlligatorToy)
    establishCommunication(tv, cableBox)
    establishCommunication(UNDMug, starWarsMug)
    establishCommunication(justDance2014XboxGame, minecraftXboxGame)
    establishCommunication(wineGlass1, wineGlass3)
    establishCommunication(xbox, guitarHeroWorldTourXboxGame)

    dallasMug = wake("Dallas Mug")
    cups.append(dallasMug)
    
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
    establishCommunication(tv, xbox)
    establishCommunication(wineGlass0, stemlessWineGlass0)
    establishCommunication(wineGlass1, stemlessWineGlass0)

    dogPlushMonkey = wake("Dog Plush Monkey")

    establishCommunication(wineGlass2, stemlessWineGlass1)
    establishCommunication(guitarHero5XboxGame, callOfDutyMW3XboxGame)
    establishCommunication(justDance2014XboxGame, GTAVXboxGame)
    establishCommunication(dogMomMug, starWarsMug)

    fallout4XboxGame = wake("Fallout 4 Xbox Game")

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
    establishCommunication(wineGlass2, leechLakeMug)
    establishCommunication(justDance2014XboxGame, guitarHeroWorldTourXboxGame)
    establishCommunication(minecraftXboxGame, callOfDutyMW3XboxGame)

    stemlessWineGlass2 = wake("Stemless Wine Glass 2")
    cups.append(stemlessWineGlass2)

    establishCommunication(wineGlass1, stemlessWineGlass1)
    establishCommunication(toyTrain, dogPlushCarrot)
    
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
    establishCommunication(dogAlligatorToy, dogBlanket)
    establishCommunication(xboxController0, fallout4XboxGame)
    establishCommunication(UNDMug, leechLakeMug)
    establishCommunication(minecraftXboxGame, fallout4XboxGame)

    negativeInteraction(computer, phone)
    
    establishCommunication(toyTrain, dogPlushMonkey)
    establishCommunication(starWarsMug, dallasMug)
    establishCommunication(wineGlass2, stemlessWineGlass3)
    establishCommunication(wineGlass1, stemlessWineGlass2)
    establishCommunication(dogPlushCarrot, dogBlanket)

    dogDuraforce = wake("Duraforce")

    establishCommunication(xboxController0, xboxController2)
    establishCommunication(dogPlushMonkey, dogBlanket)
    establishCommunication(wineGlass0, stemlessWineGlass3)
    
    halo5XboxGame = wake("Halo 5 Xbox Game")

    establishCommunication(toyBlanket, dogPlushMonkey)
    establishCommunication(minecraftXboxGame, maddenXboxGame)
    establishCommunication(dogPlushMonkey, dogDuraforce)
    establishCommunication(xbox, halo5XboxGame)
    establishCommunication(justDance2014XboxGame, callOfDutyMW3XboxGame)
    
    tvRemote = wake("TV Remote")

    establishCommunication(guitarHero5XboxGame, maddenXboxGame)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(toyElephant, dogBlanket)
    establishCommunication(wineGlass1, stemlessWineGlass3)
    establishCommunication(guitarHeroSmashHitsXboxGame, maddenXboxGame)

    callOfDutyModernWarfare2XboxGame = wake("Call of Duty Modern Warfare 2 Xbox Game")
    
    establishCommunication(GTAVXboxGame, fallout4XboxGame)
    establishCommunication(starWarsMug, leechLakeMug)
    establishCommunication(stemlessWineGlass0, stemlessWineGlass2)
    
    xboxController3 = wake("Xbox Controller 3")

    establishCommunication(xbox, xboxController3)
    establishCommunication(guitarHero5XboxGame, halo5XboxGame)
    
    seaofThievesXboxGame = wake("Sea of Thieves Xbox Game")

    establishCommunication(dogPlushDinosaur, dogBlanket)
    establishCommunication(xbox, callOfDutyModernWarfare2XboxGame)
    establishCommunication(xboxController0, maddenXboxGame)
    
    callOfDutyAdvancedWarfareXboxGame = wake("Call of Duty Advanced Warfare Xbox Game")
    
    establishCommunication(GTAVXboxGame, maddenXboxGame)
    establishCommunication(guitarHeroWorldTourXboxGame, fallout4XboxGame)
    establishCommunication(tv, xboxController3)
    
    pastaMaker = wake("Pasta Maker")

    establishCommunication(justDance2014XboxGame, fallout4XboxGame)
    establishCommunication(xbox, seaofThievesXboxGame)
    establishCommunication(guitarHero5XboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(dogPlushDinosaur, dogDuraforce)
    establishCommunication(guitarHeroSmashHitsXboxGame, halo5XboxGame)
    
    legoStarWarsIIXboxGame = wake("Lego Star Wars II Xbox Game")
    dogKong = wake("Kong")

    establishCommunication(toyBear, dogBlanket)
    establishCommunication(xbox, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(toyTrain, dogDuraforce)
    establishCommunication(xbox, legoStarWarsIIXboxGame)
    
    loveseat = wake("Loveseat")

    establishCommunication(guitarHeroWorldTourXboxGame, maddenXboxGame)
    establishCommunication(wineGlass2, stemlessWineGlass2)
    
    iceCreamScoop = wake("Ice Cream Scoop")
    
    establishCommunication(GTAVXboxGame, halo5XboxGame)
    establishCommunication(stemlessWineGlass0, stemlessWineGlass3)
    
    battlefield4XboxGame = wake("Battlefield 4 Xbox Game")
    
    establishCommunication(toyTrain, dogBlanket)
    establishCommunication(minecraftXboxGame, halo5XboxGame)
    establishCommunication(guitarHeroSmashHitsXboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(guitarHero5XboxGame, seaofThievesXboxGame)
    establishCommunication(dogBlanket, dogDuraforce)
    establishCommunication(guitarHeroSmashHitsXboxGame, seaofThievesXboxGame)
    establishCommunication(xbox, battlefield4XboxGame)

    dogRope = wake("Dog Rope")

    establishCommunication(toyElephant, dogDuraforce)
    establishCommunication(justDance2014XboxGame, maddenXboxGame)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(guitarHero5XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogAlligatorToy, dogKong)
    establishCommunication(guitarHeroSmashHitsXboxGame, callOfDutyAdvancedWarfareXboxGame)
    
    couch = wake("Couch")

    establishCommunication(toyBear, dogDuraforce)
    establishCommunication(wineGlass3, stemlessWineGlass3)
    establishCommunication(toyTrain, dogKong)
    establishCommunication(xboxController0, seaofThievesXboxGame)
    establishCommunication(guitarHero5XboxGame, legoStarWarsIIXboxGame)
    
    bowls = []
    mediumMixingBowl = wake("Medium Mixing Bowl")
    bowls.append(mediumMixingBowl)

    establishCommunication(xboxController0, legoStarWarsIIXboxGame)
    establishCommunication(toyBlanket, dogKong)
    establishCommunication(minecraftXboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(guitarHeroSmashHitsXboxGame, legoStarWarsIIXboxGame)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(xboxController0, xboxController3)
    establishCommunication(dogPlushCarrot, dogRope)
    establishCommunication(dogAlligatorToy, dogDuraforce)
    
    throwPillow0 = wake("Throw Pillow 0")

    establishCommunication(guitarHero5XboxGame, battlefield4XboxGame)
    establishCommunication(justDance2014XboxGame, halo5XboxGame)
    establishCommunication(guitarHeroWorldTourXboxGame, halo5XboxGame)

    largeMixingBowl = wake("Large Mixing Bowl")
    bowls.append(largeMixingBowl)

    establishCommunication(dogPlushMonkey, dogKong)
    establishCommunication(xboxController0, callOfDutyAdvancedWarfareXboxGame)
    
    mediumPot0 = wake("Medium Pot 0")
    
    establishCommunication(toyBear, dogKong)
    establishCommunication(dogPlushDinosaur, dogRope)
    establishCommunication(guitarHeroSmashHitsXboxGame, battlefield4XboxGame)
    establishCommunication(minecraftXboxGame, seaofThievesXboxGame)

    smallMixingBowl = wake("Small Mixing Bowl")
    bowls.append(smallMixingBowl)

    establishCommunication(dogPlushMonkey, dogRope)
    establishCommunication(dogBlanket, dogKong)
    establishCommunication(dogDuraforce, dogKong)
    
    negativeInteraction(xbox, tv)
    
    establishCommunication(justDance2014XboxGame, callOfDutyModernWarfare2XboxGame)
    establishCommunication(guitarHeroWorldTourXboxGame, callOfDutyModernWarfare2XboxGame)
    
    whisk = wake("Whisk")

    establishCommunication(GTAVXboxGame, callOfDutyModernWarfare2XboxGame)
    
    microwave = wake("Microwave")

    establishCommunication(dogPlushDinosaur, dogKong)
    establishCommunication(toyElephant, dogRope)
    establishCommunication(guitarHeroWorldTourXboxGame, seaofThievesXboxGame)
    
    throwPillow1 = wake("Throw Pillow 1")
    ladle = wake("Ladle")

    removeFromCommunity(xbox, "Electronics")

    fridge = wake("Fridge")

    establishCommunication(xboxController0, battlefield4XboxGame)
    establishCommunication(dogPlushCarrot, dogKong)
    establishCommunication(dogBlanket, dogRope)
    
    bottleOpener = wake("Bottle Opener")

    establishCommunication(toyElephant, dogKong)
    establishCommunication(justDance2014XboxGame, seaofThievesXboxGame)
    establishCommunication(toyBlanket, dogRope)
    
    crockpot = wake("Crockpot")

    positiveInteraction(dog, fish)

    establishCommunication(dogAlligatorToy, dogRope)
    establishCommunication(guitarHeroWorldTourXboxGame, callOfDutyAdvancedWarfareXboxGame)

    spatula0 = wake("Spatula")

    positiveInteraction(phone, computer)

    establishCommunication(toyTrain, dogRope)

    oven = wake("Oven")
    mediumPot1 = wake("Medium Pot 1")
    christmasOvenMitt = wake("Christmas Oven Mitt")

    establishCommunication(toyBear, dogRope)
    
    spoons = []
    servingSpoon0 = wake("Serving Spoon 0")
    spoons.append(servingSpoon0)

    establishCommunication(guitarHeroWorldTourXboxGame, legoStarWarsIIXboxGame)
    establishCommunication(justDance2014XboxGame, callOfDutyAdvancedWarfareXboxGame)
    establishCommunication(dogKong, dogRope)

    throwPillow2 = wake("Throw Pillow 2")
    smallPot0 = wake("Small Pot 0")
    toaster = wake("Toaster")

    establishCommunication(dogDuraforce, dogRope)
    establishCommunication(minecraftXboxGame, callOfDutyAdvancedWarfareXboxGame)

    ovenMitt0 = wake("Oven Mitt 0")
    spatula1 = wake("Spatula 1")
    
    establishCommunication(GTAVXboxGame, seaofThievesXboxGame)
    
    negativeInteraction(xbox, tv)
    
    mediumPot2 = wake("Medium Pot 2")
    ovenMitt1 = wake("Oven Mitt 1")
    potholder1 = wake("Potholder 1")
    strainer = wake("Strainer")
    
    establishCommunication(justDance2014XboxGame, legoStarWarsIIXboxGame)
    
    dishDryingTowel0 = wake("Dish Drying Towel 0")
    dishSoap = wake("Dish Soap")
    largePot0 = wake("Large Pot 0")
    
    establishCommunication(GTAVXboxGame, callOfDutyAdvancedWarfareXboxGame)
    
    throwPillow3 = wake("Throw Pillow 3")
    dryingRack = wake("Drying Rack")
    sponge = wake("Sponge")
    kitchenHandSoap = wake("Hand Soap")
    sink = wake("Sink")
    potholder0 = wake("Potholder 0")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    smallPot1 = wake("Small Pot 1")
    knives = []
    chefsKnife = wake("Chef's Knife")
    knives.append(chefsKnife)
    unicornWineStopper = wake("Unicorn Wine Stopper")
    pastaDryingRack = wake("Pasta Drying Rack")

    negativeInteraction(xbox, guitarHero5XboxGame)
    negativeInteraction(fish, dog)
    
    servingSpoon1 = wake("Serving Spoon 1")
    spoons.append(servingSpoon1)
    rug = wake("Rug")
    
    establishCommunication(justDance2014XboxGame, battlefield4XboxGame)
    
    largePot1 = wake("Large Pot 1")
    dishDryingTowel1 = wake("Dish Drying Towel 1")
    oneCupMeasuringCup = wake("One Cup Measuring Cup")

    establishCommunication(minecraftXboxGame, legoStarWarsIIXboxGame)
    
    straightMetalStraw = wake("Straight Metal Straw")
    babyBlueWineStopper = wake("Baby Blue Wine Stopper")
    kitchenHandTowel0 = wake("Kitchen Hand Towel 0")
    cherryWineStopper = wake("Cherry Wine Stopper")
    serratedKnife = wake("Serrated Knife")
    knives.append(serratedKnife)
    navyWineStopper = wake("Navy Wine Stopper")

    negativeInteraction(xbox, tv)
    negativeInteraction(computer, phone)

    blanket0 = wake("Blanket 0")
    tablespoon = wake("Tablespoon")
    blanket1 = wake("Blanket 1")
    coffeeTable = wake("Coffee Table")
    
    establishCommunication(plant, house)

    kitchenTable = wake("Kitchen Table")
    dishwasher = wake("Dishwasher")
    halfCupMeasuringCup = wake("Half Cup Measuring Cup")
    chair0 = wake("Chair 0")
    toyBasket = wake("Toy Basket")
    
    establishCommunication(GTAVXboxGame, legoStarWarsIIXboxGame)
    
    chair1 = wake("Chair 1")
    cloroxWipes = wake("Clorox Wipes")
    teaspoon = wake("Teaspoon")

    positiveInteraction(dog, fish)

    windex = wake("Windex")
    
    establishCommunication(minecraftXboxGame, battlefield4XboxGame)
    
    standingLamp = wake("Standing Lamp")
    
    negativeInteraction(xbox, tv)

    entertainmentCenter = wake("Entertainment Center")
    slicingKnife = wake("Slicing Knife")
    knives.append(slicingKnife)
    kitchenHandTowel1 = wake("Kitchen Hand Towel")
    knifeBlock = wake("Knife Block")

    negativeInteraction(phone, computer)

    quarterCupMeasuringCup = wake("Quarter Cup Measuring Cup")
    rubberJarOpener = wake("Rubber Jar Opener")
    seasonalPlacemat0 = wake("Seasonal Placemat 0")
    lamp0 = wake("Lamp 0")
    throwPillow4 = wake("Throw Pillow 4")
    tinfoil = wake("Tinfoil")

    establishCommunication(bentMetalStraw, straightMetalStraw)
    
    foodScale = wake("Food Scale")
    thirdCupMeasuringCup = wake("Third Cup Measuring Cup")
    seasonalPlacemat1 = wake("Seasonal Placemat 1")
    lamp1 = wake("Lamp 1")
    chair2 = wake("Chair 2")

    negativeInteraction(plant, house)
    
    gallonZiplockBags = wake("Gallon Ziplock Bags")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    saranWrap = wake("Saran Wrap")
    tomatoKnife = wake("Tomato Knife")
    knives.append(tomatoKnife)
    
    establishCommunication(GTAVXboxGame, battlefield4XboxGame)
    
    placemat0 = wake("Placemat 0")
    halfTeaspoon = wake("Half Teaspoon")
    bakingSheet0 = wake("Baking Sheet 0")
    sandwichZiplockBags = wake("Sandwich Ziplock Bags")
    kitchenTrashcan = wake("Kitchen Trashcan")
    seasonalPlacemat2 = wake("Seasonal Placemat 2")
    coffeePodBasket = wake("Coffee Pod Basket")
    forks = []
    largeFork0 = wake("Large Fork 0")
    forks.append(largeFork0)
    steakKnife0 = wake("Steak Knife 0")
    knives.append(steakKnife0)
    dunkinDonutsCoffeePod0 = wake("Dunkin' Donuts Coffee Pod 0")
    smallCup0 = wake("Small Cup 0")
    cups.append(smallCup0)

    positiveInteraction(dog, fish)

    dunkinDonutsCoffeePod1 = wake("Dunkin' Donuts Coffee Pod 1")
    steakKnife1 = wake("Steak Knife 1")
    knives.append(steakKnife1)
    plates = []
    smallPlate0 = wake("Small Plate 0")
    plates.append(smallPlate0)
    sideTable1 = wake("Side Table 1")
    largeFork1 = wake("Large Fork 1")
    forks.append(largeFork1)
    knife0 = wake("Knife 0")
    knives.append(knife0)
    dunkinDonutsCoffeePod2 = wake("Dunkin' Donuts Coffee Pod 2")
    steakKnife2 = wake("Steak Knife 2")
    knives.append(steakKnife2)
    dunkinDonutsCoffeePod3 = wake("Dunkin' Donuts Coffee Pod 3")
    largeFork2 = wake("Large Fork 2")

    negativeInteraction(phone, computer)

    forks.append(largeFork2)
    tallCup1 = wake("Tall Cup 1")
    cups.append(tallCup1)
    smallPlate1 = wake("Small Plate 1")
    plates.append(smallPlate1)
    seasonalPlacemat3 = wake("Seasonal Placemat 3")
    largeFork3 = wake("Large Fork 3")
    forks.append(largeFork3)
    smallCup1 = wake("Small Cup 1")
    cups.append(smallCup1)
    dunkinDonutsCoffeePod4 = wake("Dunkin' Donuts Coffee Pod 4")
    quarterTeaspoon = wake("Quarter Teaspoon")

    establishCommunication(tv, callOfDutyMW3XboxGame)
    
    dunkinDonutsCoffeePod5 = wake("Dunkin' Donuts Coffee Pod 5")
    largeFork4 = wake("Large Fork 4")
    forks.append(largeFork4)
    largeSpoon0 = wake("Large Spoon 0")
    spoons.append(largeSpoon0)
    smallFork0 = wake("Small Fork 0")
    forks.append(smallFork0)

    positiveInteraction(dog, fish)

    largePlate1 = wake("Large Plate 1")
    plates.append(largePlate1)
    steakKnife3 = wake("Steak Knife 3")
    knives.append(steakKnife3)
    dunkinDonutsCoffeePod6 = wake("Dunkin' Donuts Coffee Pod 6")
    largeFork5 = wake("Large Fork 5")
    placemat1 = wake("Placemat 1")
    bakingSheet1 = wake("Baking Sheet 1")
    forks.append(largeFork5)
    paringKnife = wake("Paring Knife")
    smallFork1 = wake("Small Fork 1")
    
    establishCommunication(tv, fallout4XboxGame)
    
    forks.append(smallFork1)
    knife1 = wake("Knife 1")
    knives.append(knife1)
    chair3 = wake("Chair 3")
    largeFork6 = wake("Large Fork 6")
    forks.append(largeFork6)

    positiveInteraction(phone, computer)
    
    utilityKnife = wake("Utility Knife")
    smallFork2 = wake("Small Fork 2")
    forks.append(smallFork2)
    dunkinDonutsCoffeePod7 = wake("Dunkin' Donuts Coffee Pod 7")
    largeFork7 = wake("Large Fork 7")
    forks.append(largeFork7)
    placemat2 = wake("Placemat 2")
    tallCup0 = wake("Tall Cup 0")
    cups.append(tallCup0)
    
    establishCommunication(tv, maddenXboxGame)
    
    largeSpoon1 = wake("Large Spoon 1")
    spoons.append(largeSpoon1)
    dunkinDonutsCoffeePod8 = wake("Dunkin' Donuts Coffee Pod 8")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    largeFork8 = wake("Large Fork 8")
    placemat3 = wake("Placemat 3")
    forks.append(largeFork8)
    largeSpoon2 = wake("Large Spoon 2")
    spoons.append(largeSpoon2)
    dunkinDonutsCoffeePod9 = wake("Dunkin' Donuts Coffee Pod 9")
    steakKnife4 = wake("Steak Knife 4")
    knives.append(steakKnife4)
    bowl0 = wake("Bowl 0")
    bowls.append(bowl0)
    
    establishCommunication(tv, halo5XboxGame)
    
    largeSpoon3 = wake("Large Spoon 3")
    spoons.append(largeSpoon3)
    largeFork9 = wake("Large Fork 9")
    forks.append(largeFork9)
    dunkinDonutsCoffeePod10 = wake("Dunkin' Donuts Coffee Pod 10")
    steakKnife5 = wake("Steak Knife 5")
    knives.append(steakKnife5)
    knife2 = wake("Knife 2")
    knives.append(knife2)
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    canOpener = wake("Can Opener")
    steakKnife6 = wake("Steak Knife 6")
    knives.append(steakKnife6)
    strawBrush = wake("Straw Brush")
    
    establishCommunication(tv, callOfDutyModernWarfare2XboxGame)
    
    dunkinDonutsCoffeePod11 = wake("Dunkin' Donuts Coffee Pod 11")
    smallSpoon1 = wake("Small Spoon 1")
    spoons.append(smallSpoon1)

    positiveInteraction(dog, fish)

    dunkinDonutsCoffeePod12 = wake("Dunkin' Donuts Coffee Pod 12")
    bowl2 = wake("Bowl 2")
    bowls.append(bowl2)
    
    establishCommunication(tv, seaofThievesXboxGame)
    
    steakKnife7 = wake("Steak Knife 7")
    knives.append(steakKnife7)
    smallFork3 = wake("Small Fork 3")
    forks.append(smallFork3)
    dunkinDonutsCoffeePod13 = wake("Dunkin' Donuts Coffee Pod 13")
    knife3 = wake("Knife 3")
    knives.append(knife3)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    smallFork4 = wake("Small Fork 4")
    forks.append(smallFork4)
    
    establishCommunication(tv, callOfDutyAdvancedWarfareXboxGame)
    
    dunkinDonutsCoffeePod14 = wake("Dunkin' Donuts Coffee Pod 14")
    smallFork5 = wake("Small Fork 5")
    forks.append(smallFork5)
    bowl1 = wake("Bowl 1")
    bowls.append(bowl1)

    positiveInteraction(phone, computer)

    dunkinDonutsCoffeePod15 = wake("Dunkin' Donuts Coffee Pod 15")
    smallFork6 = wake("Small Fork 6")
    forks.append(smallFork6)
    sideTable0 = wake("Side Table 0")
    smallFork7 = wake("Small Fork 7")
    forks.append(smallFork7)
    smallFork8 = wake("Small Fork 8")
    forks.append(smallFork8)
    
    negativeInteraction(plant, house)
    
    dunkinDonutsCoffeePod16 = wake("Dunkin' Donuts Coffee Pod 16")
    smallFork9 = wake("Small Fork 9")
    forks.append(smallFork9)
    
    establishCommunication(tv, legoStarWarsIIXboxGame)
    
    dunkinDonutsCoffeePod17 = wake("Dunkin' Donuts Coffee Pod 17")
    smallPlate2 = wake("Small Plate 2")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    plates.append(smallPlate2)
    knife4 = wake("Knife 4")
    knives.append(knife4)
    dunkinDonutsCoffeePod18 = wake("Dunkin' Donuts Coffee Pod 18")
    knife5 = wake("Knife 5")
    knives.append(knife5)
    knife6 = wake("Knife 6")
    knives.append(knife6)
    dunkinDonutsCoffeePod19 = wake("Dunkin' Donuts Coffee Pod 19")
    knife7 = wake("Knife 7")
    knives.append(knife7)
    knife8 = wake("Knife 8")
    knives.append(knife8)
   
    establishCommunication(tv, battlefield4XboxGame)
    
    dunkinDonutsCoffeePod20 = wake("Dunkin' Donuts Coffee Pod 20")

    positiveInteraction(fish, dog)
    
    knife9 = wake("Knife 9")
    knives.append(knife9)
    dunkinDonutsCoffeePod21 = wake("Dunkin' Donuts Coffee Pod 21")
    dunkinDonutsCoffeePod22 = wake("Dunkin' Donuts Coffee Pod 22")
    dunkinDonutsCoffeePod23 = wake("Dunkin' Donuts Coffee Pod 23")
    largeSpoon4 = wake("Large Spoon 4")
    spoons.append(largeSpoon4)
    largeSpoon5 = wake("Large Spoon 5")
    spoons.append(largeSpoon5)
    largeSpoon6 = wake("Large Spoon 6")
    spoons.append(largeSpoon6)
    largeSpoon7 = wake("Large Spoon 7")
    spoons.append(largeSpoon7)
    largeSpoon8 = wake("Large Spoon 8")
    spoons.append(largeSpoon8)
    dunkinDonutsCoffeePod24 = wake("Dunkin' Donuts Coffee Pod 24")
    largeSpoon9 = wake("Large Spoon 9")
    spoons.append(largeSpoon9)
    dunkinDonutsCoffeePod25 = wake("Dunkin' Donuts Coffee Pod 25")
    smallSpoon0 = wake("Small Spoon 0")
    spoons.append(smallSpoon0)
    dunkinDonutsCoffeePod26 = wake("Dunkin' Donuts Coffee Pod 26")
    smallSpoon2 = wake("Small Spoon 2")
    spoons.append(smallSpoon2)
    dunkinDonutsCoffeePod27 = wake("Dunkin' Donuts Coffee Pod 27")
    dunkinDonutsCoffeePod28 = wake("Dunkin' Donuts Coffee Pod 28")
    smallSpoon3 = wake("Small Spoon 3")
    spoons.append(smallSpoon3)
    smallSpoon4 = wake("Small Spoon 4")
    spoons.append(smallSpoon4)
    dunkinDonutsCoffeePod29 = wake("Dunkin' Donuts Coffee Pod 29")
    
    positiveInteraction(dog, fish)
    
    smallSpoon5 = wake("Small Spoon 5")
    spoons.append(smallSpoon5)
    dunkinDonutsCoffeePod30 = wake("Dunkin' Donuts Coffee Pod 30")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    smallSpoon6 = wake("Small Spoon 6")
    spoons.append(smallSpoon6)
    smallSpoon7 = wake("Small Spoon 7")
    spoons.append(smallSpoon7)
    dunkinDonutsCoffeePod31 = wake("Dunkin' Donuts Coffee Pod 31")
    smallSpoon8 = wake("Small Spoon 8")
    spoons.append(smallSpoon8)

    positiveInteraction(computer, phone)

    dunkinDonutsCoffeePod32 = wake("Dunkin' Donuts Coffee Pod 32")
    smallSpoon9 = wake("Small Spoon 9")
    spoons.append(smallSpoon9)
    dunkinDonutsCoffeePod33 = wake("Dunkin' Donuts Coffee Pod 33")
    smallCup2 = wake("Small Cup 2")
    cups.append(smallCup2)
    smallCup3 = wake("Small Cup 3")
    cups.append(smallCup3)
    
    negativeInteraction(plant, house)
    
    dunkinDonutsCoffeePod34 = wake("Dunkin' Donuts Coffee Pod 34")
    tallCup2 = wake("Tall Cup 2")
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    cups.append(tallCup2)
    tallCup3 = wake("Tall Cup 2")
    cups.append(tallCup3)
    dunkinDonutsCoffeePod35 = wake("Dunkin' Donuts Coffee Pod 35")
    smallPlate3 = wake("Small Plate 3")
    plates.append(smallPlate3)
    smallPlate4 = wake("Small Plate 4")
    plates.append(smallPlate4)
    dunkinDonutsCoffeePod37 = wake("Dunkin' Donuts Coffee Pod 37")
    largePlate0 = wake("Large Plate 0")
    plates.append(largePlate0)
    largePlate2 = wake("Large Plate 2")
    plates.append(largePlate2)
    
    positiveInteraction(fish, dog)
    
    positiveInteraction(dog, fish)
    dunkinDonutsCoffeePod38 = wake("Dunkin' Donuts Coffee Pod 38")
    largePlate3 = wake("Large Plate 3")
    plates.append(largePlate3)

    positiveInteraction(dog, fish)
    positiveInteraction(computer, phone)

    dunkinDonutsCoffeePod39 = wake("Dunkin' Donuts Coffee Pod 39")
    largePlate4 = wake("Large Plate 4")
    
    positiveInteraction(wineGlass1, wineGlass0)

    plates.append(largePlate4)
    bowl3 = wake("Bowl 3")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    bowls.append(bowl3)
    bowl4 = wake("Bowl 4")
    bowls.append(bowl4)
    positiveInteraction(fish, dog)
    dunkinDonutsCoffeePod40 = wake("Dunkin' Donuts Coffee Pod 40")

    print("\n\nRELATIONSHIPS:")
    for being in state["beings"]:
        if being.connections == {}:
            continue
        print(being.name + "'s connections: ")
        for connection in being.connections:
            relationship = being.connections[connection]["relationship"]
            if relationship == "FRIEND" or relationship == "ENEMY":
                relationship += "\t"        # for alignment purposes
            print("\t" + relationship + "\t" + str(being.connections[connection]["level"]) + "\t" + connection.name)

    print("\n\nCOMMUNITIES:")
    if len(state) > 1:
        for community in state:
            if community == "beings":
                continue
            print(community + "'s members:")
            for being in state[community]:
                print("\t" + being.name)

if __name__ == '__main__':
    main()