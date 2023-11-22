POISON = "POISON"
BUG = "BUG"
GRASS = "GRASS"
PSYCHIC = "PSYCHIC"
DARK = "DARK"
FIRE = "FIRE"
ELECTRIC = "ELECTRIC"
STEEL = "STEEL"
GROUND = "GROUND"
FLYING = "FLYING"
ROCK = "ROCK"
FIGHTING = "FIGHTING"
WATER = "WATER"
ICE = "ICE"
NORMAL = "NORMAL"
DRAGON = "DRAGON"
GHOST = "GHOST"

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