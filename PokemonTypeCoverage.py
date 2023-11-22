import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pyvenn.venn as venn

from PokemonConstants import *
from PokemonList import allPokemonList

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
    userTypeWeakPokemonList = []
    typeIndex = 0
    for type in userTypes:
        userTypeWeakPokemonList.append(set())
        for pokemon in allPokemonList:
            if isWeakToAttack(type, pokemon) is True:
                userTypeWeakPokemonList[typeIndex].add(pokemon)
        typeIndex += 1
    return userTypeWeakPokemonList

def isWeakToAttack(attackType, pokemon):
    pokemonTypes = allPokemonList.get(pokemon)
    if len(pokemonTypes) == 1:
        if pokemonTypes[0] in SUPER_EFFECTIVE.get(attackType):
            return True
    elif len(pokemonTypes) == 2:
        if (pokemonTypes[0] not in INEFFECTIVE.get(attackType) and pokemonTypes[0] not in NO_EFFECT.get(attackType) and 
            pokemonTypes[1] not in INEFFECTIVE.get(attackType) and pokemonTypes[1] not in NO_EFFECT.get(attackType)):
            return True
    return False

def isImmuneToAttack(attackType, pokemon):
    pokemonTypes = allPokemonList.get(pokemon)
    if len(pokemonTypes) == 1:
        if pokemonTypes[0] in NO_EFFECT.get(attackType):
            return True
    elif len(pokemonTypes) == 2:
        if pokemonTypes[0] in NO_EFFECT.get(attackType) or pokemonTypes[1] in NO_EFFECT.get(attackType):
            return True
    return False

# def isResistantToAttack(attackType, pokemon):
#     pokemonTypes = allPokemonList.get(pokemon)
#     if len(pokemonTypes) == 1:
#         if pokemonTypes[0] in INEFFECTIVE.get(attackType):
#             return True
#     elif len(pokemonTypes) == 2:
#         if (pokemonTypes[0] not in SUPER_EFFECTIVE.get(attackType) and pokemonTypes[0] not in EFFECTIVE.get(attackType) and 
#             pokemonTypes[1] not in INEFFECTIVE.get(attackType) and pokemonTypes[1] not in NO_EFFECT.get(attackType)):
#             return True
#     return False

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