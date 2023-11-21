from PokemonConstants import *

allPokemonList = {  
    'Bulbasaur': [GRASS, POISON],
    'Ivysaur': [GRASS, POISON],
    'Venusaur': [GRASS, POISON],
    'Charmander': [FIRE],
    'Charmeleon': [FIRE],
    'Charizard': [FIRE, FLYING],
    'Squirtle': [WATER],
    'Wartortle': [WATER],
    'Blastoise': [WATER],
    'Caterpie': [BUG],
    'Metapod': [BUG],
    'Butterfree': [BUG, FLYING],
    'Weedle': [BUG, POISON],
    'Kakuna': [BUG, POISON],
    'Beedrill': [BUG, POISON],
    'Pidgey': [NORMAL, FLYING],
    'Pidgeotto': [NORMAL, FLYING],
    'Pidgeot': [NORMAL, FLYING],
    'Rattata': [NORMAL],
    'Raticate': [NORMAL],
    'Spearow': [NORMAL, FLYING],
    'Fearow': [NORMAL, FLYING],
    'Ekans': [POISON],
    'Arbok': [POISON],
    'Pikachu': [ELECTRIC],
    'Raichu': [ELECTRIC],
    'Sandshrew': [GROUND],
    'Sandslash': [GROUND],
    'Nidoran♀': [POISON],
    'Nidorina': [POISON],
    'Nidoqueen': [POISON, GROUND],
    'Nidoran♂': [POISON],
    'Nidorino': [POISON],
    'Nidoking': [POISON, GROUND],
    'Clefairy': [NORMAL],
    'Clefable': [NORMAL],
    'Vulpix': [FIRE],
    'Ninetales': [FIRE],
    'Jigglypuff': [NORMAL],
    'Wigglytuff': [NORMAL],
    'Zubat': [POISON, FLYING],
    'Golbat': [POISON, FLYING],
    'Oddish': [GRASS, POISON],
    'Gloom': [GRASS, POISON],
    'Vileplume': [GRASS, POISON],
    'Paras': [BUG, GRASS],
    'Parasect': [BUG, GRASS],
    'Venonat': [BUG, POISON],
    'Venomoth': [BUG, POISON],
    'Diglett': [GROUND],
    'Dugtrio': [GROUND],
    'Meowth': [NORMAL],
    'Persian': [NORMAL],
    'Psyduck': [WATER],
    'Golduck': [WATER],
    'Mankey': [FIGHTING],
    'Primeape': [FIGHTING],
    'Growlithe': [FIRE],
    'Arcanine': [FIRE],
    'Poliwag': [WATER],
    'Poliwhirl': [WATER],
    'Poliwrath': [WATER, FIGHTING],
    'Abra': [PSYCHIC],
    'Kadabra': [PSYCHIC],
    'Alakazam': [PSYCHIC],
    'Machop': [FIGHTING],
    'Machoke': [FIGHTING],
    'Machamp': [FIGHTING],
    'Bellsprout': [GRASS, POISON],
    'Weepinbell': [GRASS, POISON],
    'Victreebel': [GRASS, POISON],
    'Tentacool': [WATER, POISON],
    'Tentacruel': [WATER, POISON],
    'Geodude': [ROCK, GROUND],
    'Graveler': [ROCK, GROUND],
    'Golem': [ROCK, GROUND],
    'Ponyta': [FIRE],
    'Rapidash': [FIRE],
    'Slowpoke': [WATER, PSYCHIC],
    'Slowbro': [WATER, PSYCHIC],
    'Magnemite': [ELECTRIC, STEEL],
    'Magneton': [ELECTRIC, STEEL],
    'Farfetch\'d': [NORMAL, FLYING],
    'Doduo': [NORMAL, FLYING],
    'Dodrio': [NORMAL, FLYING],
    'Seel': [WATER],
    'Dewgong': [WATER, ICE],
    'Grimer': [POISON],
    'Muk': [POISON],
    'Shellder': [WATER],
    'Cloyster': [WATER, ICE],
    'Gastly': [GHOST, POISON],
    'Haunter': [GHOST, POISON],
    'Gengar': [GHOST, POISON],
    'Onix': [ROCK, GROUND],
    'Drowzee': [PSYCHIC],
    'Hypno': [PSYCHIC],
    'Krabby': [WATER],
    'Kingler': [WATER],
    'Voltorb': [ELECTRIC],
    'Electrode': [ELECTRIC],
    'Exeggcute': [GRASS, PSYCHIC],
    'Exeggutor': [GRASS, PSYCHIC],
    'Cubone': [GROUND],
    'Marowak': [GROUND],
    'Hitmonlee': [FIGHTING],
    'Hitmonchan': [FIGHTING],
    'Lickitung': [NORMAL],
    'Koffing': [POISON],
    'Weezing': [POISON],
    'Rhyhorn': [GROUND, ROCK],
    'Rhydon': [GROUND, ROCK],
    'Chansey': [NORMAL],
    'Tangela': [GRASS],
    'Kangaskhan': [NORMAL],
    'Horsea': [WATER],
    'Seadra': [WATER],
    'Goldeen': [WATER],
    'Seaking': [WATER],
    'Staryu': [WATER],
    'Starmie': [WATER, PSYCHIC],
    'Mr. Mime': [PSYCHIC],
    'Scyther': [BUG, FLYING],
    'Jynx': [ICE, PSYCHIC],
    'Electabuzz': [ELECTRIC],
    'Magmar': [FIRE],
    'Pinsir': [BUG],
    'Tauros': [NORMAL],
    'Magikarp': [WATER],
    'Gyarados': [WATER, FLYING],
    'Lapras': [WATER, ICE],
    'Ditto': [NORMAL],
    'Eevee': [NORMAL],
    'Vaporeon': [WATER],
    'Jolteon': [ELECTRIC],
    'Flareon': [FIRE],
    'Porygon': [NORMAL],
    'Omanyte': [ROCK, WATER],
    'Omastar': [ROCK, WATER],
    'Kabuto': [ROCK, WATER],
    'Kabutops': [ROCK, WATER],
    'Aerodactyl': [ROCK, FLYING],
    'Snorlax': [NORMAL],
    'Articuno': [ICE, FLYING],
    'Zapdos': [ELECTRIC, FLYING],
    'Moltres': [FIRE, FLYING],
    'Dratini': [DRAGON],
    'Dragonair': [DRAGON],
    'Dragonite': [DRAGON, FLYING],
    'Mewtwo': [PSYCHIC],
    'Mew': [PSYCHIC],
    'Chikorita': [GRASS],
    'Bayleef': [GRASS],
    'Meganium': [GRASS],
    'Cyndaquil': [FIRE],
    'Quilava': [FIRE],
    'Typhlosion': [FIRE],
    'Totodile': [WATER],
    'Croconaw': [WATER],
    'Feraligatr': [WATER],
    'Sentret': [NORMAL],
    'Furret': [NORMAL],
    'Hoothoot': [NORMAL, FLYING],
    'Noctowl': [NORMAL, FLYING],
    'Ledyba': [BUG, FLYING],
    'Ledian': [BUG, FLYING],
    'Spinarak': [BUG, POISON],
    'Ariados': [BUG, POISON],
    'Crobat': [POISON, FLYING],
    'Chinchou': [WATER, ELECTRIC],
    'Lanturn': [WATER, ELECTRIC],
    'Pichu': [ELECTRIC],
    'Cleffa': [NORMAL],
    'Igglybuff': [NORMAL],
    'Togepi': [NORMAL],
    'Togetic': [NORMAL, FLYING],
    'Natu': [PSYCHIC, FLYING],
    'Xatu': [PSYCHIC, FLYING],
    'Mareep': [ELECTRIC],
    'Flaaffy': [ELECTRIC],
    'Ampharos': [ELECTRIC],
    'Bellossom': [GRASS],
    'Marill': [WATER],
    'Azumarill': [WATER],
    'Sudowoodo': [ROCK],
    'Politoed': [WATER],
    'Hoppip': [GRASS, FLYING],
    'Skiploom': [GRASS, FLYING],
    'Jumpluff': [GRASS, FLYING],
    'Aipom': [NORMAL],
    'Sunkern': [GRASS],
    'Sunflora': [GRASS],
    'Yanma': [BUG, FLYING],
    'Wooper': [WATER, GROUND],
    'Quagsire': [WATER, GROUND],
    'Espeon': [PSYCHIC],
    'Umbreon': [DARK],
    'Murkrow': [DARK, FLYING],
    'Slowking': [WATER, PSYCHIC],
    'Misdreavous': [GHOST],
    'Unown': [PSYCHIC],
    'Wobbuffet': [PSYCHIC],
    'Girafarig': [NORMAL, PSYCHIC],
    'Pineco': [BUG],
    'Forretress': [BUG, STEEL],
    'Dunsparce': [NORMAL],
    'Gligar': [GROUND, FLYING],
    'Steelix': [STEEL, GROUND],
    'Snubbull': [NORMAL],
    'Granbull': [NORMAL],
    'Qwilfish': [WATER, POISON],
    'Scizor': [BUG, STEEL],
    'Shuckle': [BUG, ROCK],
    'Heracross': [BUG, FIGHTING],
    'Sneasel': [DARK, ICE],
    'Teddiursa': [NORMAL],
    'Ursaring': [NORMAL],
    'Slugma': [FIRE],
    'Magcargo': [FIRE, ROCK],
    'Swinub': [ICE, GROUND],
    'Piloswine': [ICE, GROUND],
    'Corsola': [WATER, ROCK],
    'Remoraid': [WATER],
    'Octillery': [WATER],
    'Delibird': [ICE, FLYING],
    'Mantine': [WATER, FLYING],
    'Skarmory': [STEEL, FLYING],
    'Houndour': [DARK, FIRE],
    'Houndoom': [DARK, FIRE],
    'Kingdra': [WATER, DRAGON],
    'Phanpy': [GROUND],
    'Donphan': [GROUND],
    'Porygon2': [NORMAL],
    'Stantler': [NORMAL],
    'Smeargle': [NORMAL],
    'Tyrogue': [FIGHTING],
    'Hitmontop': [FIGHTING],
    'Smoochum': [ICE, PSYCHIC],
    'Elekid': [ELECTRIC],
    'Magby': [FIRE],
    'Miltank': [NORMAL],
    'Blissey': [NORMAL],
    'Raikou': [ELECTRIC],
    'Entei': [FIRE],
    'Suicune': [WATER],
    'Larvitar': [ROCK, GROUND],
    'Pupitar': [ROCK, GROUND],
    'Tyranitar': [ROCK, DARK],
    'Lugia': [PSYCHIC, FLYING],
    'Ho-Oh': [FIRE, FLYING],
    'Celebi': [PSYCHIC, GRASS],
    'Treecko': [GRASS],
    'Grovyle': [GRASS],
    'Sceptile': [GRASS],
    'Torchic': [FIRE],
    'Combusken': [FIRE, FIGHTING],
    'Blaziken': [FIRE, FIGHTING],
    'Mudkip': [WATER],
    'Marshtomp': [WATER, GROUND],
    'Swampert': [WATER, GROUND],
    'Poochyena': [DARK],
    'Mightyena': [DARK],
    'Zigzagoon': [NORMAL],
    'Linoone': [NORMAL],
    'Wurmple': [BUG],
    'Silcoon': [BUG],
    'Beautifly': [BUG, FLYING],
    'Cascoon': [BUG],
    'Dustox': [BUG, POISON],
    'Lotad': [WATER, GRASS],
    'Lombre': [WATER, GRASS],
    'Ludicolo': [WATER, GRASS],
    'Seedot': [GRASS],
    'Nuzleaf': [GRASS, DARK],
    'Shiftry': [GRASS, DARK],
    'Taillow': [NORMAL, FLYING],
    'Swellow': [NORMAL, FLYING],
    'Wingull': [WATER, FLYING],
    'Pelipper': [WATER, FLYING],
    'Ralts': [PSYCHIC],
    'Kirlia': [PSYCHIC],
    'Gardevoir': [PSYCHIC],
    'Surskit': [BUG, WATER],
    'Masquerain': [BUG, FLYING],
    'Shroomish': [GRASS],
    'Breloom': [GRASS, FIGHTING],
    'Slakoth': [NORMAL],
    'Vigoroth': [NORMAL],
    'Slaking': [NORMAL],
    'Nincada': [BUG, GROUND],
    'Ninjask': [BUG, FLYING],
    'Shedinja': [BUG, GHOST],
    'Whismur': [NORMAL],
    'Loudred': [NORMAL],
    'Exploud': [NORMAL],
    'Makuhita': [FIGHTING],
    'Hariyama': [FIGHTING],
    'Azurill': [NORMAL],
    'Nosepass': [ROCK],
    'Skitty': [NORMAL],
    'Delcatty': [NORMAL],
    'Sableye': [DARK, GHOST],
    'Mawile': [STEEL],
    'Aron': [STEEL, ROCK],
    'Lairon': [STEEL, ROCK],
    'Aggron': [STEEL, ROCK],
    'Meditite': [FIGHTING, PSYCHIC],
    'Medicham': [FIGHTING, PSYCHIC],
    'Electrike': [ELECTRIC],
    'Manectric': [ELECTRIC],
    'Plusle': [ELECTRIC],
    'Minun': [ELECTRIC],
    'Volbeat': [BUG],
    'Illumise': [BUG],
    'Roselia': [GRASS, POISON],
    'Gulpin': [POISON],
    'Swalot': [POISON],
    'Carvanha': [WATER, DARK],
    'Sharpedo': [WATER, DARK],
    'Wailmer': [WATER],
    'Wailord': [WATER],
    'Numel': [FIRE, GROUND],
    'Camerupt': [FIRE, GROUND],
    'Torkoal': [FIRE],
    'Spoink': [PSYCHIC],
    'Grumpig': [PSYCHIC],
    'Spinda': [NORMAL],
    'Trapinch': [GROUND],
    'Vibrava': [GROUND, DRAGON],
    'Flygon': [GROUND, DRAGON],
    'Cacnea': [GRASS],
    'Cacturne': [GRASS, DARK],
    'Swablu': [NORMAL, FLYING],
    'Altaria': [DRAGON, FLYING],
    'Zangoose': [NORMAL],
    'Seviper': [POISON],
    'Lunatone': [ROCK, PSYCHIC],
    'Solrock': [ROCK, PSYCHIC],
    'Barboach': [WATER, GROUND],
    'Whiscash': [WATER, GROUND],
    'Corphish': [WATER],
    'Crawdaunt': [WATER, DARK],
    'Baltoy': [GROUND, PSYCHIC],
    'Claydol': [GROUND, PSYCHIC],
    'Lileep': [ROCK, GRASS],
    'Cradily': [ROCK, GRASS],
    'Anorith': [ROCK, BUG],
    'Armaldo': [ROCK, BUG],
    'Feebas': [WATER],
    'Milotic': [WATER],
    'Castform': [NORMAL],
    'Kecleon': [NORMAL],
    'Shuppet': [GHOST],
    'Banette': [GHOST],
    'Duskull': [GHOST],
    'Dusclops': [GHOST],
    'Tropius': [GRASS, FLYING],
    'Chimecho': [PSYCHIC],
    'Absol': [DARK],
    'Wynaut': [PSYCHIC],
    'Snorunt': [ICE],
    'Glalie': [ICE],
    'Spheal': [ICE, WATER],
    'Sealeo': [ICE, WATER],
    'Walrein': [ICE, WATER],
    'Clamperl': [WATER],
    'Huntail': [WATER],
    'Gorebyss': [WATER],
    'Relicanth': [WATER, ROCK],
    'Luvdisc': [WATER],
    'Bagon': [DRAGON],
    'Shelgon': [DRAGON],
    'Salamence': [DRAGON, FLYING],
    'Beldum': [STEEL, PSYCHIC],
    'Metang': [STEEL, PSYCHIC],
    'Metagross': [STEEL, PSYCHIC],
    'Regirock': [ROCK],
    'Regice': [ICE],
    'Registeel': [STEEL],
    'Latias': [DRAGON, PSYCHIC],
    'Latios': [DRAGON, PSYCHIC],
    'Kyogre': [WATER],
    'Groudon': [GROUND],
    'Rayquaza': [DRAGON, FLYING],
    'Jirachi': [STEEL, PSYCHIC],
    'Deoxys': [PSYCHIC],
    'Turtwig': [GRASS],
    'Grotle': [GRASS],
    'Torterra': [GRASS, GROUND],
    'Chimchar': [FIRE],
    'Monferno': [FIRE, FIGHTING],
    'Infernape': [FIRE, FIGHTING],
    'Piplup': [WATER],
    'Prinplup': [WATER],
    'Empoleon': [WATER, STEEL],
    'Starly': [NORMAL, FLYING],
    'Staravia': [NORMAL, FLYING],
    'Staraptor': [NORMAL, FLYING],
    'Bidoof': [NORMAL],
    'Bibarel': [NORMAL, WATER],
    'Kricketot': [BUG],
    'Kricketune': [BUG],
    'Shinx': [ELECTRIC],
    'Luxio': [ELECTRIC],
    'Luxray': [ELECTRIC],
    'Budew': [GRASS, POISON],
    'Roserade': [GRASS, POISON],
    'Cranidos': [ROCK],
    'Rampardos': [ROCK],
    'Shieldon': [ROCK, STEEL],
    'Bastiodon': [ROCK, STEEL],
    'Burmy': [BUG],
    'Wormadam_Plant': [BUG, GRASS],
    'Wormadam_Sandy': [BUG, GROUND],
    'Wormadam_Trash': [BUG, STEEL],
    'Mothim': [BUG, FLYING],
    'Combee': [BUG, FLYING],
    'Vespiquen': [BUG, FLYING],
    'Pachirisu': [ELECTRIC],
    'Buizel': [WATER],
    'Floatzel': [WATER],
    'Cherubi': [GRASS],
    'Cherrim': [GRASS],
    'Shellos': [WATER],
    'Gastrodon': [WATER, GROUND],
    'Ambipom': [NORMAL],
    'Drifloon': [GHOST, FLYING],
    'Drifblim': [GHOST, FLYING],
    'Buneary': [NORMAL],
    'Lopunny': [NORMAL, FIGHTING],
    'Mismagius': [GHOST],
    'Honchkrow': [DARK, FLYING],
    'Glameow': [NORMAL],
    'Purugly': [NORMAL],
    'Chingling': [PSYCHIC],
    'Stunky': [POISON, DARK],
    'Skuntank': [POISON, DARK],
    'Bronzor': [STEEL, PSYCHIC],
    'Bronzong': [STEEL, PSYCHIC],
    'Bonsly': [ROCK],
    'Mime Jr.': [PSYCHIC],
    'Happiny': [NORMAL],
    'Chatot': [NORMAL, FLYING],
    'Spiritomb': [GHOST, DARK],
    'Gible': [DRAGON, GROUND],
    'Gabite': [DRAGON, GROUND],
    'Garchomp': [DRAGON, GROUND],
    'Munchlax': [NORMAL],
    'Riolu': [FIGHTING],
    'Lucario': [FIGHTING, STEEL],
    'Hippopotas': [GROUND],
    'Hippowdon': [GROUND],
    'Skorupi': [POISON, BUG],
    'Drapion': [POISON, DARK],
    'Croagunk': [POISON, FIGHTING],
    'Toxicroak': [POISON, FIGHTING],
    'Carnivine': [GRASS],
    'Finneon': [WATER],
    'Lumineon': [WATER],
    'Mantyke': [WATER, FLYING],
    'Snover': [ICE, GRASS],
    'Abomasnow': [ICE, GRASS],
    'Weavile': [DARK, ICE],
    'Magnezone': [ELECTRIC, STEEL],
    'Lickilicky': [NORMAL],
    'Rhyperior': [GROUND, ROCK],
    'Tangrowth': [GRASS],
    'Electivire': [ELECTRIC],
    'Magmortar': [FIRE],
    'Togekiss': [NORMAL, FLYING],
    'Yanmega': [BUG, FLYING],
    'Leafeon': [GRASS],
    'Glaceon': [ICE],
    'Gliscor': [GROUND, FLYING],
    'Mamoswine': [ICE, GROUND],
    'Porygon-Z': [NORMAL],
    'Gallade': [PSYCHIC, FIGHTING],
    'Probopass': [ROCK, STEEL],
    'Dusknoir': [GHOST],
    'Froslass': [ICE, GHOST],
    'Rotom': [ELECTRIC, GHOST],
    'Rotom_Heat': [FIRE, GHOST],
    'Rotom_Wash': [WATER, GHOST],
    'Rotom_Frost': [ICE, GHOST],
    'Rotom_Fan': [FLYING, GHOST],
    'Rotom_Mow': [GRASS, GHOST],
    'Uxie': [PSYCHIC],
    'Mesprit': [PSYCHIC],
    'Azelf': [PSYCHIC],
    'Dialga': [STEEL, DRAGON],
    'Palkia': [WATER, DRAGON],
    'Heatran': [FIRE, STEEL],
    'Regigigas': [NORMAL],
    'Giratina': [GHOST, DRAGON],
    'Cresselia': [PSYCHIC],
    'Phione': [WATER],
    'Manaphy': [WATER],
    'Darkrai': [DARK],
    'Shaymin_Land': [GRASS],
    'Shaymin_Sky':[GRASS, FLYING],
    'Arceus': [NORMAL],
    'Victini': [PSYCHIC, FIRE],
    'Snivy': [GRASS],
    'Servine': [GRASS],
    'Serperior': [GRASS],
    'Tepig': [FIRE],
    'Pignite': [FIRE, FIGHTING],
    'Emboar': [FIRE, FIGHTING],
    'Oshawott': [WATER],
    'Dewott': [WATER],
    'Samurott': [WATER],
    'Patrat': [NORMAL],
    'Watchog': [NORMAL],
    'Lillipup': [NORMAL],
    'Herdier': [NORMAL],
    'Stoutland': [NORMAL],
    'Purrloin': [DARK],
    'Liepard': [DARK],
    'Pansage': [GRASS],
    'Simisage': [GRASS],
    'Pansear': [FIRE],
    'Simisear': [FIRE],
    'Panpour': [WATER],
    'Simipour': [WATER],
    'Munna': [PSYCHIC],
    'Musharna': [PSYCHIC],
    'Pidove': [NORMAL, FLYING],
    'Tranquill': [NORMAL, FLYING],
    'Unfezant': [NORMAL, FLYING],
    'Blitzle': [ELECTRIC],
    'Zebstrika': [ELECTRIC],
    'Roggenrola': [ROCK],
    'Boldore': [ROCK],
    'Gigalith': [ROCK],
    'Woobat': [PSYCHIC, FLYING],
    'Swoobat': [PSYCHIC, FLYING],
    'Drilbur': [GROUND],
    'Excadrill': [GROUND, STEEL],
    'Audino': [NORMAL],
    'Timburr': [FIGHTING],
    'Gurdurr': [FIGHTING],
    'Conkeldurr': [FIGHTING],
    'Tympole': [WATER],
    'Palpitoad': [WATER, GROUND],
    'Seismitoad': [WATER, GROUND],
    'Throh': [FIGHTING],
    'Sawk': [FIGHTING],
    'Sewaddle': [BUG, GRASS],
    'Swadloon': [BUG, GRASS],
    'Leavanny': [BUG, GRASS],
    'Venipede': [BUG, POISON],
    'Whirlipede': [BUG, POISON],
    'Scolipede': [BUG, POISON],
    'Cottonee': [GRASS],
    'Whimsicott': [GRASS],
    'Petilil': [GRASS],
    'Lilligant': [GRASS],
    'Basculin': [WATER],
    'Sandile': [GROUND, DARK],
    'Krokorok': [GROUND, DARK],
    'Krookodile': [GROUND, DARK],
    'Darumaka': [FIRE],
    'Darmanitan': [FIRE],
    'Darmanitan_Zen': [FIRE, PSYCHIC],
    'Maractus': [GRASS],
    'Dwebble': [BUG, ROCK],
    'Crustle': [BUG, ROCK],
    'Scraggy': [DARK, FIGHTING],
    'Scrafty': [DARK, FIGHTING],
    'Sigilyph': [PSYCHIC, FLYING],
    'Yamask': [GHOST],
    'Cofagrigus': [GHOST],
    'Tirtouga': [WATER, ROCK],
    'Carracosta': [WATER, ROCK],
    'Archen': [ROCK, FLYING],
    'Archeops': [ROCK, FLYING],
    'Trubbish': [POISON],
    'Garbodor': [POISON],
    'Zorua': [DARK],
    'Zoroark': [DARK],
    'Minccino': [NORMAL],
    'Cinccino': [NORMAL],
    'Gothita': [PSYCHIC],
    'Gothorita': [PSYCHIC],
    'Gothitelle': [PSYCHIC],
    'Solosis': [PSYCHIC],
    'Duosion': [PSYCHIC],
    'Reuniclus': [PSYCHIC],
    'Ducklett': [WATER, FLYING],
    'Swanna': [WATER, FLYING],
    'Vanillite': [ICE],
    'Vanillish': [ICE],
    'Vanilluxe': [ICE],
    'Deerling': [NORMAL, GRASS],
    'Sawsbuck': [NORMAL, GRASS],
    'Emolga': [ELECTRIC, FLYING],
    'Karrablast': [BUG],
    'Escavalier': [BUG, STEEL],
    'Foongus': [GRASS, POISON],
    'Amoonguss': [GRASS, POISON],
    'Frillish': [WATER, GHOST],
    'Jellicent': [WATER, GHOST],
    'Alomomola': [WATER],
    'Joltik': [BUG, ELECTRIC],
    'Galvantula': [BUG, ELECTRIC],
    'Ferroseed': [GRASS, STEEL],
    'Ferrothorn': [GRASS, STEEL],
    'Klink': [STEEL],
    'Klang': [STEEL],
    'Klinklang': [STEEL],
    'Tynamo': [ELECTRIC],
    'Eelektrik': [ELECTRIC],
    'Eelektross': [ELECTRIC],
    'Elgyem': [PSYCHIC],
    'Beheeyem': [PSYCHIC],
    'Litwick': [GHOST, FIRE],
    'Lampent': [GHOST, FIRE],
    'Chandelure': [GHOST, FIRE],
    'Axew': [DRAGON],
    'Fraxure': [DRAGON],
    'Haxorus': [DRAGON],
    'Cubchoo': [ICE],
    'Beartic': [ICE],
    'Cryogonal': [ICE],
    'Shelmet': [BUG],
    'Accelgor': [BUG],
    'Stunfisk': [GROUND, ELECTRIC],
    'Mienfoo': [FIGHTING],
    'Mienshao': [FIGHTING],
    'Druddigon': [DRAGON],
    'Golett': [GROUND, GHOST],
    'Golurk': [GROUND, GHOST],
    'Pawniard': [DARK, STEEL],
    'Bisharp': [DARK, STEEL],
    'Bouffalant': [NORMAL],
    'Rufflet': [NORMAL, FLYING],
    'Braviary': [NORMAL, FLYING],
    'Vullaby': [DARK, FLYING],
    'Mandibuzz': [DARK, FLYING],
    'Heatmor': [FIRE],
    'Durant': [BUG, STEEL],
    'Deino': [DARK, DRAGON],
    'Zweilous': [DARK, DRAGON],
    'Hydreigon': [DARK, DRAGON],
    'Larvesta': [BUG, FIRE],
    'Volcarona': [BUG, FIRE],
    'Cobalion': [STEEL, FIGHTING],
    'Terrakion': [ROCK, FIGHTING],
    'Virizion': [GRASS, FIGHTING],
    'Tornadus': [FLYING],
    'Thundurus': [ELECTRIC, FLYING],
    'Reshiram': [DRAGON, FIRE],
    'Zekrom': [DRAGON, ELECTRIC],
    'Landorus': [GROUND, FLYING],
    'Kyurem': [DRAGON, ICE],
    'Keldeo': [WATER, FIGHTING],
    'Meloetta_Aria': [NORMAL, PSYCHIC],
    'Meloetta_Pirouette': [NORMAL, FIGHTING],
    'Genesect': [BUG, STEEL]
}