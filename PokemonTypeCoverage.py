import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pyvenn.venn as venn

from PokemonConstants import *


ALL_TYPES = {POISON, BUG, GRASS, PSYCHIC, DARK, FIRE, ELECTRIC, 
             STEEL, GROUND, FLYING, ROCK, FIGHTING, WATER, ICE, 
             NORMAL, DRAGON, GHOST}

SUPER_EFFECTIVE = {
    POISON: {GRASS},
    BUG: {GRASS, PSYCHIC, DARK},
    GRASS: {WATER, GROUND, ROCK},
    PSYCHIC: (FIGHTING, POISON),
    DARK: {PSYCHIC, GHOST},
    FIRE: {GRASS, ICE, BUG, STEEL},
    ELECTRIC: {WATER, FLYING},
    STEEL: {ICE, ROCK},
    GROUND: {FIRE, ELECTRIC, POISON, ROCK, STEEL},
    FLYING: {GRASS, FIGHTING, BUG},
    ROCK: {FIRE, ICE, FLYING, BUG},
    FIGHTING: {NORMAL, ICE, ROCK, DARK, STEEL},
    WATER: {FIRE, GROUND, ROCK},
    ICE: {GRASS, GROUND, FLYING, DRAGON},
    NORMAL: set(),
    DRAGON: {DRAGON},
    GHOST: {PSYCHIC, GHOST}
}

INEFFECTIVE = {
    POISON: {POISON, GROUND, ROCK, GHOST},
    BUG: {FIRE, FIGHTING, POISON, FLYING, GHOST, STEEL},
    GRASS: {FIRE, GRASS, POISON, FLYING, BUG, DRAGON, STEEL},
    PSYCHIC: {PSYCHIC, STEEL},
    DARK: {FIGHTING, DARK, STEEL},
    FIRE: {FIRE, WATER, ROCK, DRAGON},
    ELECTRIC: {ELECTRIC, GRASS, DRAGON},
    STEEL: {FIRE, WATER, ELECTRIC, STEEL},
    GROUND: {GRASS, BUG},
    FLYING: {ELECTRIC, ROCK, STEEL},
    ROCK: {FIGHTING, GROUND, STEEL},
    FIGHTING: {POISON, FLYING, PSYCHIC, BUG},
    WATER: {WATER, GRASS, DRAGON},
    ICE: {FIRE, WATER, ICE, STEEL},
    NORMAL: {ROCK, STEEL},
    DRAGON: {STEEL},
    GHOST: {DARK, STEEL}
}

NO_EFFECT = {
    POISON: {STEEL},
    BUG: set(),
    GRASS: set(),
    PSYCHIC: {DARK},
    DARK: set(),
    FIRE: set(),
    ELECTRIC: {GROUND},
    STEEL: set(),
    GROUND: {FLYING},
    FLYING: set(),
    ROCK: set(),
    FIGHTING: {GHOST},
    WATER: set(),
    ICE: set(),
    NORMAL: {GHOST},
    DRAGON: set(),
    GHOST: {NORMAL}
}

COLOURS_TYPE = {
    POISON: "#E791FD",
    BUG: "#A5CD8E",
    GRASS: "#94F187",
    PSYCHIC: "#F352B1",
    DARK: "#958C8A",
    FIRE: "#FF9437",
    ELECTRIC: "#E5E906",
    STEEL: "#BDBDD5",
    GROUND: "#D5C42E",
    FLYING: "#83C4D4",
    ROCK: "#D1A54E",
    FIGHTING: "#FA7677",
    WATER: "#679BFC",
    ICE: "#31DED5",
    NORMAL: "#BBBAAB",
    DRAGON: "#BE84B2",
    GHOST: "#AB75F9"
}

EFFECTIVE = dict()

def calcEffectiveTypes():
    for type in ALL_TYPES:
        EFFECTIVE[type] = ALL_TYPES.difference(SUPER_EFFECTIVE[type]).difference(INEFFECTIVE[type]).difference(NO_EFFECT[type])

def inputUserTypes():

    types = []
    i = 0

    print("Enter in the move types, up to four. If you have less than four, enter in 'stop'")

    while(i < 4):

        print("Enter in type", i+1, ": ", end="")
        type = input().replace(" ", "")

        if type.lower() == "stop":
            break
        elif type.upper() not in ALL_TYPES:
            print("Invalid type, please try again.")
        else:
            types.append(type.upper())
            i += 1

    return types

def confirmUserTypes(userTypes):

    print("Your types are: ", end="")
    for type in userTypes:
        print(type, end=" ")
    print()

    while True:

        userTypeConfirm = input("Confirm these types? (y/n): ")

        if userTypeConfirm == "y":
            return True
        elif userTypeConfirm == "n":
            return False
        
def setUserTypes():
    while True:
        userTypes = inputUserTypes()
        if confirmUserTypes(userTypes) is True:
            return userTypes

def inputMenu(userTypes):
    selection = input("Enter a selection ('help' for menu): ").lower()
    if selection == "help":
        print("\nMENU\n**********")
        print("Change Attack Types")
        print("View Attack Types")
        print("Defender Type Weakness Counts")
        print("Type Coverage Venn")
        print("Pokemon Coverage Venn")
        print()
    elif selection == "change attack types":
        return {"flag": "CHANGE_USER_TYPES", "data": setUserTypes()}
    elif selection == "view attack types":
        printUserTypes(userTypes)
    elif selection == "defender type weakness counts":
        getDefenderTypeWeaknessCounts(userTypes)
    elif selection == "type coverage venn":
        createTypeCoverageVennDiagram(userTypes)
    elif selection == "pokemon coverage venn":
        createPokemonCoverageVennDiagram(userTypes)
    else:
        print("Unknown prompt, please try again.")

def getDefenderTypeWeaknessCounts(userTypes):
    for type in ALL_TYPES:
        weaknessCount = 0
        for userType in userTypes:
            if type in SUPER_EFFECTIVE.get(userType):
                weaknessCount += 1
        print(type, ": ", weaknessCount)

def printUserTypes(userTypes):
    for type in userTypes:
        print(type, end=" ")
    print()

def createTypeCoverageVennDiagram(userTypes):
    superEffectiveList = []
    notSuperEffectiveList = ALL_TYPES.copy()
    for type in userTypes:
        superEffectiveList.append(SUPER_EFFECTIVE[type])

    for typeSet in superEffectiveList:
        notSuperEffectiveList.difference_update(typeSet)

    labels = venn.get_labels(superEffectiveList, fill=['types'])
    if len(userTypes) == 1:
        fig, ax = venn.venn(labels, names=[userTypes[0]])
    elif len(userTypes) == 2:
        fig, ax = venn.venn2(labels, names=[userTypes[0], userTypes[1]])
    elif len(userTypes) == 3:
        fig, ax = venn.venn3(labels, names=[userTypes[0], userTypes[1], userTypes[2]])
    elif len(userTypes) == 4:
        fig, ax = venn.venn4(labels, names=[userTypes[0], userTypes[1], userTypes[2], userTypes[3]])
    fig.savefig('TypeCoverageVennDiagram.png', bbox_inches='tight')
    plt.close()

    print("\nThese types are not weak to your attacks:")
    for i, type in enumerate(notSuperEffectiveList):
        if i % 3 == 0 and i != 0: 
            print("\n" + type + " ", end="")
        else:
            print(type + " ", end="")
    print("\n")

def createPokemonCoverageVennDiagram(userTypes):
    superEffectivePokemonList = getWeakPokemon(userTypes)
    labels = venn.get_labels(superEffectivePokemonList, fill=['number'])
    fig, ax = venn.venn4(labels, names=[userTypes[0], userTypes[1], userTypes[2], userTypes[3]])
    fig.savefig('PokemonCoverageVennDiagram.png', bbox_inches='tight')
    plt.close()

def getWeakPokemon(userTypes):
    from PokemonList import allPokemonList
    userTypeWeakPokemonList = []
    typeIndex = 0
    for type in userTypes:
        userTypeWeakPokemonList.append(set())
        for pokemon in allPokemonList:
            if isWeak(type, pokemon) is True:
                userTypeWeakPokemonList[typeIndex].add(pokemon)
        typeIndex += 1
    return userTypeWeakPokemonList

def isWeak(attackType, pokemon):
    from PokemonList import allPokemonList
    pokemonTypes = allPokemonList.get(pokemon)
    if len(pokemonTypes) == 1:
        if pokemonTypes[0] in SUPER_EFFECTIVE.get(attackType):
            return True
    elif len(pokemonTypes) == 2:
        if (pokemonTypes[0] not in INEFFECTIVE.get(attackType) and pokemonTypes[0] not in NO_EFFECT.get(attackType) and 
            pokemonTypes[1] not in INEFFECTIVE.get(attackType) and pokemonTypes[1] not in NO_EFFECT.get(attackType)):
            return True
    return False

def main():
    print("Welcome!")
    calcEffectiveTypes()
    userTypes = setUserTypes()

    while True:
        retData = inputMenu(userTypes)
        if type(retData) == dict:
            if retData["flag"] == "CHANGE_USER_TYPES":
                userTypes = retData["data"]
    


main()