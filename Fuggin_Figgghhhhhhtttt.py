# Import the random module to use the randint() function
import random

from termcolor import colored

# This function returns a random integer between 1 and 20, inclusive
# It also adds the roll to a ledger of previous rolls
def roll( sides ):
  roll = random.randint(1, int( sides ) )
  #print( "| Rolled:\t" + str( roll ) )
  return roll

import sys
import cv2

Animation_Mode = False
if( "-a" in sys.argv ):
    Animation_Mode = True
Descriptions_Mode = False
if( "-d" in sys.argv ):
    Descriptions_Mode = True

# dETERMINE ROLL STRENGTH
DEFAULT_ROLL_STRENGTH = 10

DEFAULT_STRENGTH_POT = 5
DEFAULT_HEALING_POT = 4

BASE_ADVENTURE_ROLL = 100

# PLAYER DEFAULTS
DEFAULT_HEALTH = 75
"""
DEFAULT_STRENGTH_POT = 3
DEFAULT_HEALING_POT = 4

	0	1	2	3	4	5
X4	7	11 	15 	19	21	25	29
X3	9	12	15	18	21  24	27				

	0	1	2	3	4	5	
x5	7	12	17	22	27	32	37
x4	11	15	19	23	27	31	35
"""

# Load the video
Waft_Success = './video/Waft_Success.mp4'
Failed_Waft = './video/Failed_Waft.mp4'
New_Champ = './video/New_Champ.mp4'
Old_Champ = './video/Old_Champ.mp4'
Prayer = './video/Prayer.mp4'
Healing_Potion = './video/Healing_Potion.mp4'
Strength_Potion = './video/Strength_Potion.mp4'
Heal = './video/Heal.mp4'
Damage_1 = './video/Damage/1.mp4'
Damage_2 = './video/Damage/2.mp4'
Damage_3 = './video/Damage/3.mp4'
Damage_4 = './video/Damage/4.mp4'
Damage_5 = './video/Damage/5.mp4'
Damage = './video/Damage.mp4'
Damage_6 = './video/Damage/6.mp4'
Damage_7 = './video/Damage/7.mp4'
Damage_8 = './video/Damage/8.mp4'
Damage_9 = './video/Damage/9.mp4'
Damage_10 = './video/Damage/10.mp4'

Heal_1 = './video/Heal/1.mp4'
Heal_2 = './video/Heal/2.mp4'
Heal_3 = './video/Heal/3.mp4'
Heal_4 = './video/Heal/4.mp4'
Heal_5 = './video/Heal/5.mp4'
Heal_6 = './video/Heal/6.mp4'
Heal_7 = './video/Heal/7.mp4'
Heal_8 = './video/Heal/8.mp4'
Heal_9 = './video/Heal/9.mp4'
Heal_10 = './video/Damage/10.mp4'

Clown = './video/Clown.mp4'
Taunt = './video/Taunt.mp4'

def Roll_Strength( current_roll, sides ):
    roll_strength = ( DEFAULT_ROLL_STRENGTH * current_roll ) / sides
    return roll_strength

def play_animation( Animation ):
    #if( Animation_Mode ):
    if( Animation_Mode or Animation == Waft_Success or Animation == Failed_Waft ): # Silly edit

        Animation_Temp = cv2.VideoCapture( Animation )
        # Loop through each frame of the video
        while True:
            # Read the next frame from the video
            success, frame = Animation_Temp.read()

            # If there are no more frames left, break the loop
            if not success:
                break

            # Show the frame
            cv2.imshow('Video', frame)

            # Wait for a key press
            key = cv2.waitKey(30)
            if key == 27:  # Esc key
                break
        Animation_Temp.release(  )
        cv2.destroyAllWindows(  )


def Start_Adventure_Greeting(  ):
    print( """|
|        .'(   )\.---.     /`-.      /`-.  )\    /(      .-,.-.,-.    /`-.     /`-.        .-.   )\.---.   .')       )\.---.     /`-.    )\.--.  
|    ,') \  ) (   ,-._(  ,' _  \   ,' _  \ \ (_.' /      ) ,, ,. (  ,' _  \  ,' _  \   ,'  /  ) (   ,-._( ( /       (   ,-._(  ,' _  \  (   ._.' 
|   (  /(/ /   \  '-,   (  '-' (  (  '-' (  )  _.'       \( |(  )/ (  '-' ( (  '-' (  (  ) | (   \  '-,    ))        \  '-,   (  '-' (   `-.`.   
|    )    (     ) ,-`    )   _  )  ) ,_ .'  / /             ) \     ) ,_ .'  )   _  )  ) './ /    ) ,-`    )'._.-.    ) ,-`    ) ,_ .'  ,_ (  \  
|   (  .'\ \   (  ``-.  (  ,' ) \ (  ' ) \ (  \             \ (    (  ' ) \ (  ,' ) \ (  ,  (    (  ``-.  (       )  (  ``-.  (  ' ) \ (  '.)  ) 
|    )/   )/    )..-.(   )/    )/  )/   )/  ).'              )/     )/   )/  )/    )/  )/..'      )..-.(   )/,__.'    )..-.(   )/   )/  '._,_.'  
|    """)

def Fuggin_Figgghhhhhhtttt(  ):
    print( """|
|\t    ______                  _      
|\t   / ____/_  ______ _____ _(_)___  
|\t  / /_  / / / / __ `/ __ `/ / __ \ 
|\t / __/ / /_/ / /_/ / /_/ / / / / / 
|\t/_/    \__,_/\__, /\__, /_/_/ /_/  
|\t            /____//____/          
|\t    _______                   __    __    __    __    __    __    __  __  __  __  __
|\t   / ____(_)___ _____ _____ _/ /_  / /_  / /_  / /_  / /_  / /_  / /_/ /_/ /_/ /_/ /
|\t  / /_  / / __ `/ __ `/ __ `/ __ \/ __ \/ __ \/ __ \/ __ \/ __ \/ __/ __/ __/ __/ / 
|\t / __/ / / /_/ / /_/ / /_/ / / / / / / / / / / / / / / / / / / / /_/ /_/ /_/ /_/_/  
|\t/_/   /_/\__, /\__, /\__, /_/ /_/_/ /_/_/ /_/_/ /_/_/ /_/_/ /_/\__/\__/\__/\__(_)   
|\t        /____/____//____/           
|""")

def taunt_emote(  ):
    play_animation( Taunt )
    print( "|                      /´¯/)\n|                    ,/¯  /\n|                   /    /\n|             /´¯/'   '/´¯¯`·¸\n|          /'/   /    /       /¨¯\\\n|        ('(   ´   ´     ¯~/'   ')\n|         \\                 '     /\n|          ''   \\           _ ·´\n|            \\              ( \n|              \\             \\   " )

def clown_emote(  ):
    play_animation( Clown )
    print( """|
|                   >>>>>\\|/<<<<<
|                  >>>\\\\\\\\v////<<<
|                 >>>\\\\\\\\vvv////<<<    
|                >>>( vvvvvvvvv )<<<
|                >>>>) (.)_(.) (<<<<
|                >>>/    (_)    \<<<
|                >( (._      _.) )<
|                  \    `---'   /
|                    "'--._.--'" 
|               .--.____| u |____.--.
|              /___| |__\___/__| |___\\
|              |___|_|_________|_|___|
|    """ )

def prayer_emote(  ):
    play_animation( Prayer )
    #print("        ________        \n     _|--      --|_     \n   _|-_||_        -|_   \n  |- -  _-    _---- -|  \n |-    |||    _|_    -| \n |      -     -|-     | \n |                    | \n |  ||_  ----__       | \n -| | |   _____      |- \n  -|- ---- ___-    _|-  \n   |      -|     _|-    \n   |_     -|___|--      \n    -------             \n" )
    print( """|
|      P  PP PP P
|      P P   PP   P    P PP
|      P PPP  PP   PP   PP P
|      PPPP PP   PP  PP  P  P
|      P  P  PP   P   P   P PP
|      P   P   P   PP  PP   P  P
|      PP   PP  PP   P    P     P
|      PP  PP P   P              PP
|       P   P P                   P
|        P     P                  P
|         P     P                 P
|         PP    PP                P 
|          P     PP                PP
|           P     PP              PPPPP
|         PPP       PPP          PPPPPPPP
|        PPPPPP         PPP    PPPPPPPPP
|        PPPPPP      PPPPP   PPPPPPPPPPP
|           PPPPPPPPPPP      PPPPPPPP
|    """)


def look_emote(  ):
    print( "|              _ \n|         .-'    `-.\n|       .'           `.\n|     ;               ;`\\\n|     ;               ; |\n|      \\.           .' /\n|        `-._____.-_.'\n|         / /`/\n|        / / /\n|       / / /\n|       \\/_/\n|")

def waft_emote(  ):
    play_animation( Waft_Success )
    waft = "|  _\n| | Y~.         --_-_-_-_---\n| | r.|              -_-_-_\n|  Y ||   _            -_-_-\n|  | t_\_/ _)           -__-\n|   \  `. /             _-_\n|     `-._/)          _-\n|        (,db          -_\n|          Yb.        _-_\n| "
    print(waft)

def Clean_Message( Message ):
    if( len( Message ) > 40 ):
        Clean_Message_Long( Message )
        return
    print( "|\t  ______________________________________________" )
    print( "|\t /                                              \\ " )
    print( "|\t|                                               |" )
    print( "|\t|\t"+ str( Message ) ) 
    print( "|\t|                                               |" )
    print( "|\t\\_______________________________________________/" )

def Clean_Message_Long( Message ):
    print( "|\t  ____________________________________________________________________________________________" )
    print( "|\t /                                                                                            \\ " )
    print( "|\t|                                                                                              |" )
    print( "|\t|\t"+ str( Message ) ) 
    print( "|\t|                                                                                              |" )
    print( "|\t\\______________________________________________________________________________________________/" )

def Prompt_User_Adventure_Base( Group_Name ):
    print( "|\t  ____________________________________________________________________________________________" )
    print( "|\t /                                                                                            \\ " )
    print( "|\t|                                                                                              |" )
    print( "|\t|\t"+ str( Group_Name ) + ", when you are ready, press 'k' to blaze forward, or 'e' to exit?" )
    print( "|\t|\t", end="" )
    Choice = input(":" )
    print( "|\t\\______________________________________________________________________________________________/" )
    return Choice

def Prompt_User( Player ):
    print( "|\t  ____________________________________________________________________________________________" )
    print( "|\t /                                                                                            \\ " )
    print( "|\t|                                                                                              |" )
    print( "|\t|\t"+ str( Player ) + ", do you want to attack, heal, waft sand, or look around? a, h, w, or l?" )
    print( "|\t|\t", end="" )
    Choice = input(":" )
    print( "|\t\\______________________________________________________________________________________________/" )
    return Choice

def Prompt_User_With_Prayer( Player ):
    print( "|\t  ____________________________________________________________________________________________" )
    print( "|\t /                                                                                            \\ " )
    print( "|\t|                                                                                              |" )
    print( "|\t|\t"+ str( Player ) + ", do you want to attack, heal, waft sand, look around, or pray? a, h, w, l, or p?" )
    print( "|\t|\t", end="" )
    Choice = input(":" )
    print( "|\t\\______________________________________________________________________________________________/" )
    return Choice

def attack_emote( name, op_name, Roll_Strength, temp_roll ):
    if( Descriptions_Mode ):
        Clean_Message( f"{name} attacks {op_name} and deals {temp_roll} damage" )
    print(f"""|
|\t\t{name}\t\t\t\t\t\t{int(temp_roll)}
|\t                           ___
|\t                          ( ((
|\t                           ) ))
|\t  .::.                    / /(
|\t 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
|\t(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
|\t `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
|\t  `::'                    \ \(
|\t                           ) ))
|\t                          (_((
|\t\t\t\t\t\t\t\t\t{op_name} 
|\t    """)

    #Roll_Strength = 20 # Remove with more animations
    if( int( Roll_Strength ) == 1 ):
        play_animation( Damage_1 )
    elif( int( Roll_Strength ) == 2 ):
        play_animation( Damage_2 )
    elif( int( Roll_Strength ) == 3 ):
        play_animation( Damage_3 )
    elif( int( Roll_Strength ) == 4 ):
        play_animation( Damage_4 )
    elif( int( Roll_Strength ) == 5 ):
        play_animation( Damage_5 )
    elif( int( Roll_Strength ) == 6 ):
        play_animation( Damage_6 )
    elif( int( Roll_Strength ) == 7 ):
        play_animation( Damage_7 )
    elif( int( Roll_Strength ) == 8 ):
        play_animation( Damage_8 )
    elif( int( Roll_Strength ) == 9 ):
        play_animation( Damage_9 )
    elif( int( Roll_Strength ) == 10 ):
        play_animation( Damage_10 )

def strength_potion_emote():
    Clean_Message( "Strength_Potion" )
    play_animation( Strength_Potion )
    print( f"""|
|\t       _/  `.  :                          
|\t    .-' `-.     `+._._                    
|\t  .'       ``-  '  `-.`.                  
|\t /              \     `.\                 
|\t:                \      \:                
|\t:    .-'         .L      ;            ._  
|\t \ .'   \      /`) `.    |\         /`\ \ 
|\t |       :.   : '    ;   ; \       : :'  ;
|\t | :     | `--J     / ._/   ;    .-' /'-';
|\t :  \    :_.-'    .'    :`. L_.-'    _.-' 
|\t  \   -.-'   /   / |`.  |  /  _.'  .'     
|\t   ;           .'  :  \ :        .'       
|\t   |      .' .'   /    / \    .-'         
|\t   :    .'.-'`-- : -' :   `.-'            
|\t    \ _.-'       |    |                   
|\t     "  | \           |                   
|\t        ;  ;     c   :|                   
|   """)

def health_potion_emote(  ):
    
    play_animation( Healing_Potion )
    
    print( f"""|
|\t
|\t                        //
|\t                       //
|\t                      //
|\t                     //
|\t              _______||
|\t         ,-'''       ||`-.
|\t        (            ||   )
|\t        |`-..._______,..-'|
|\t        |            ||   |
|\t        |     _______||   |
|\t        |,-'''_ _  ~ ||`-.|
|\t        |  ~ / `-.\ ,-'\ ~|
|\t        |`-...___/___,..-'|
|\t        |    `-./-'_ \/_| |
|\t        | -'  ~~     || -.|
|\t        (   ~      ~   ~~ )
|\t         `-..._______,..-'
|   """ )
    Clean_Message( "Health Potion" )

def super_health_potion_emote(  ):
    print( f"""|
|\t
|\t                        //
|\t                       //
|\t                      //
|\t                     //
|\t              _______||
|\t         ,-'''       ||`-.
|\t        (            ||   )
|\t        |`-..._______,..-'|
|\t        | Super      ||   |
|\t        |  Health____||   |
|\t        |,-'''_ _  ~ ||`-.|
|\t        |  ~ / `-.\ ,-'\ ~|
|\t        |`-...___/___,..-'|
|\t        |    `-./-'_ \/_| |
|\t        | -'  ~~     || -.|
|\t        (   ~      ~   ~~ )
|\t         `-..._______,..-'
|   """ )
    
def heal_emote( Roll_Strength ):
    if( int( Roll_Strength ) == 1 ):
        play_animation( Heal_1 )
    elif( int( Roll_Strength ) == 2 ):
        play_animation( Heal_2 )
    elif( int( Roll_Strength ) == 3 ):
        play_animation( Heal_3 )
    elif( int( Roll_Strength ) == 4 ):
        play_animation( Heal_4 )
    elif( int( Roll_Strength ) == 5 ):
        play_animation( Heal_5 )
    elif( int( Roll_Strength ) == 6 ):
        play_animation( Heal_6 )
    elif( int( Roll_Strength ) == 7 ):
        play_animation( Heal_7 )
    elif( int( Roll_Strength ) == 8 ):
        play_animation( Heal_8 )
    elif( int( Roll_Strength ) == 9 ):
        play_animation( Heal_9 )
    elif( int( Roll_Strength ) == 10 ):
        play_animation( Heal_10 )
    else:
        play_animation( Heal )
    
    print( """|
|\t          |  \ \ | |/ /
|\t          |  |\ `' ' /
|\t          |  ;'aorta \      / , pulmonary
|\t          | ;    _,   |    / / ,  arteries
|\t superior | |   (  `-.;_,-' '-' ,
|\tvena cava | `,   `-._       _,-'_
|\t          |,-`.    `.)    ,<_,-'_, pulmonary
|\t         ,'    `.   /   ,'  `;-' _,  veins
|\t        ;        `./   /`,    \-'
|\t        | right   /   |  ;\   |\\
|\t        | atrium ;_,._|_,  `, ' \\
|\t        |        \    \ `       `,
|\t        `      __ `    \   left  ;,
|\t         \   ,'  `      \,  ventricle
|\t          \_(            ;,      ;;
|\t          |  \           `;,     ;;
|\t inferior |  |`.          `;;,   ;'
|\tvena cava |  |  `-.        ;;;;,;' FL
|\t          |  |    |`-.._  ,;;;;;'
|\t          |  |    |   | ``';;;'
|\t                  aorta
|""")

def Nose_Honking_Clown( name ):
    print( f"|    " )
    print( f"|      While { name } is walking past a group of age appropriote people" )
    print( f"|    { name } overhears the people talking about how they would never date { name } ")
    print( f"|      How they find { name } unattractive" )
    print(  )
    print( f"|    One of the people calls { name } a NOSE HONKING CLOWN" )
    print( f"|    Another makes fun of { name }'s shirt" )
    print( f"|    " )
    print( f"|    The people didn't mean for { name } to hear but it hurts nontheless..." )
    print( f"|    { name } loses 2 hp and is bummed about the whole thing" )
    print( f"|    " )

def Life_Is_Pain( name ):
    print(f"|       {name} starts to look around. But...              " )
    print(f"|       In { name }'s time away drift away and ponder..." )
    print(f"|    ____________________________________________________" )
    print(f"|   |    What is this world? What happens when it ends?  |" )
    print(f"|   |    Is there beautiful heaven? Or black oblivian?    |" )
    print(f"|   |                   I Sleep                          |" )
    print(f"|   |____________________________________________________|" )
    print(f"|       " )
    print(f"|       { name } suddently realises they are still fighting...              " )
    print(f"|       They have also find no items but gain a unique perspective..." )
    print(f"|       " )
    print(f"|       { name } gain some prayer" )

def print_stats( Player1, Player2 ):

    print(f"| > Name:\t{ Player1.name }\t| > Name:\t{ Player2.name }")
    print(f"| > Health:\t{ Player1.health }\t| > Health:\t{ Player2.health }")
    print(f"| > Max Hit:\t{ Player1.max_hit }\t| > Max Hit:\t{ Player2.max_hit }")
    print(f"| > Max Heal:\t{ Player1.max_heal }\t| > Max Heal:\t{ Player2.max_heal }")
    if( Player1.prayer > 0 or Player2.prayer > 0 ):
        print(f"| > Prayer:\t{ Player1.prayer }\t| > Prayer:\t{ Player2.prayer }")

live_stats = [ "Name", "Health", "Max Hit", "Max Heal", "Prayer", "Wins" ]

def fetch_stat( Creatures, stat ):
    results = []

    

    for Creature in Creatures:
        try:
            #print( "fetching:\t" + str( stat ) + " for " + str( Creature.name ) + ":\t" + str( getattr(Creature, stat) ) )
            results.append( str( getattr(Creature, stat) ) )
        except:
            results.append( 0 )

    return results

def Num_Tabs( STAT ):
    #print( len( STAT ) )
    if( len( STAT ) == 0):
        return "\t\t\t\t"
        
    elif( len( STAT ) < 4):
        return "\t\t\t"
    if( len( STAT ) > 8):
        return "\t"
    else:
        return "\t\t"



def print_stat( stat ):
    
    STAT = str( stat['stat'] ).capitalize(  ).replace( "_", " " )
    print("|\t| > " + STAT + ":" + str( Num_Tabs( STAT ) ), end="" )
    print( ( "\t\t|\t| > " + STAT + ":" + str( Num_Tabs( STAT ) ) ).join( stat['value'] ), end="\t" )
    print( "\t|")
    #print("|\t| " + str( stat['stat'] ) + ":\t\t" + "\t|\t| > " + str( stat['stat'] ) + ":\t\t".join( stat['value'] ) + "\t|")

def b_top( Creatures ):
    print( "|\t", end="" )
    for box in range(len(Creatures)):
        print( " ______________________________________ \t ", end="" )
    print()
    print( "|\t", end="" )
    for box in range(len(Creatures)):
        print( "/\t\t\t\t\t\\\t", end="" )
    print()

def b_bot( Creatures ):
    print( "|\t", end="" )
    for box in range(len(Creatures)):
        print( "\\______________________________________/\t ", end="" )
    print(  )
    
def Is_Empty_Stat( PLAYER_STATS ):
    try:
        for stat in PLAYER_STATS:
            if( int( stat ) > 0):
                return False
        return True
    except:
        return False

def battle_stats( Creatures, active ):
    stats = [  ]
    b_top( Creatures )
    for stat in live_stats:
        #print( stat.lower().replace( " ", "_" ) )
        PLAYER_STATS = fetch_stat( Creatures, stat.lower().replace( " ", "_" ) )
        if( Is_Empty_Stat( PLAYER_STATS ) ):
            pass
        else:
            stats.append( { "value": PLAYER_STATS , "stat": stat.lower().replace( " ", "_" ) } )

    """
    name = [str( Creature.name ) for Creature in Creatures]
    health = [str( Creature.health ) for Creature in Creatures]
    max_hit = [str( Creature.max_hit ) for Creature in Creatures]
    max_heal = [str( Creature.max_heal ) for Creature in Creatures]
    prayer_int = [int( Creature.prayer ) for Creature in Creatures]
    prayer = [str( Creature.prayer ) for Creature in Creatures]
    wins = [str( Creature.wins ) for Creature in Creatures]
    wins_int = [int( Creature.wins ) for Creature in Creatures]
        

    """
    for stat in stats:
        #print( stat )
        print_stat( stat )
    """
    print("|\t| Name     :\t\t" + "\t|\t| > Name     :\t\t".join( name ) + "\t|")
    print("|\t| Health   :\t\t" + "\t|\t| > Health   :\t\t".join( health ) + "\t|")
    print("|\t| Max_Hit  :\t\t" + "\t|\t| > Max_Hit  :\t\t".join( max_hit ) + "\t|")
    print("|\t| Max_Heal :\t\t" + "\t|\t| > Max_Heal :\t\t".join( max_heal ) + "\t|")
    if( sum( prayer_int ) > 0 ):
        print("|\t| Prayer   :\t\t" + "\t|\t| > Prayer   :\t\t".join( prayer ) + "\t|")
    if( sum( wins_int ) > 0 ):
        print("|\t| Wins     :\t\t" + "\t|\t| > Wins     :\t\t".join( wins ) + "\t|")
    """
    b_bot( Creatures )

""" PRINTING ABOVE """
class Creature:
    def __init__(self, name, health, max_hit, max_heal, species, noise):
        self.name = name
        self.health = health
        self.max_hit = max_hit
        self.max_heal = max_heal
        self.noise = noise
        self.species = species
        self.stun = 0
    
    def attack(self, other_creature):
        print( "BM Attack" )
        print( self.max_hit )
        # subtract the max_hit of the attacking player from the health of the other player
        temp_roll = roll( self.max_hit )
        print( "BM Attack 2" )
        roll_strength = Roll_Strength( temp_roll, self.max_hit )
        print( "BM Attack 3" )
        other_creature.health -= temp_roll
        print( "BM Attack 4" )
        Clean_Message(f"{self.name} attacks {other_creature.name} and deals {temp_roll} damage")
        attack_emote( self.name, other_creature.name, roll_strength, temp_roll )
        print( other_creature.health )
        if( other_creature.health <= 0 ):
            return "dead"
        else:
            return "not dead"

    def make_noise(self):
        Clean_Message(f"{ self.name } the { self.species }:\t{self.noise}")

    def greet(self, message):
        Clean_Message(f"{message}, I am { self.name } and I am a { self.species }")


Monsters = [ "Dragon", "BatMonkey", "Troll", "Deer" ]

def spawn_creature( Players ):
    index = random.randint(0, len( Monsters ) - 1)
    print( "Overriding BatMonkey spawn" )
    index = 1
    
    Monster_Name = Monsters[ index ]
    Baby_Monst = globals(  ).get( Monster_Name )( Players ) # Spawn the Monster    

    return Baby_Monst

def Get_Players_Lowest_Health( Players ):
    LH = 10000000
    for Player in Players:
        if( Player.health < LH ):
            LH = Player.health

    return LH

def Get_Players_Max_Health( Players ):
    MS = 0
    for Player in Players:
        MS += Player.max_health

    return MS

def Get_Players_Max_Hit( Players ):
    MS = 0
    for Player in Players:
        MS += Player.max_hit

    return MS

def Inc_Turn( Turn, Num_Players ):
    Turn += 1
    if( Turn >= Num_Players ):
        return 0
    return Turn

# ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - 
# Creature area

class BatMonkey( Creature ):
    def __init__( self, Players ):
        super().__init__("BatMonk", 10, 2, 0, "BatMonkey", "Ooooo Ahhhh ( In Sonar tho )")
        Clean_Message( "Ohh shit what is that.. looks like a F***in BATMONKEY!!!" )
        Clean_Message( "The sight of the BatMonkey makes " + str( Players[ roll( len( Players ) ) - 1 ].name ) + " tremble in fear. How weak." )

        
        MS = Get_Players_Max_Hit( Players )
        print( "Players Max Hit:\t" + str( MS ) )
        self.health = round( MS * 0.66 )  # Will set to 
        print( "BM Health:\t" + str( self.health ) )
        
        LH = Get_Players_Lowest_Health( Players )
        #print( "Players Lowest Health:\t" + str( LH ) )
        self.max_hit = round( LH * 0.1 )  # Will set to 
        if( self.max_hit < 5 ):
            self.max_hit = 5
        print( "BM Max hit:\t" + str( self.max_hit ) )

        self.hit_chance = 1

    def get_wild( self ):
        if( self.hit_chance >= 8 ):
            Clean_Message( "It'll be hard to hit this thing!!" )
        else:
            self.hit_chance += self.hit_chance * 2
            self.max_hit += self.max_hit + 2
            if( self.hit_chance >= 8 ):
                Clean_Message( "The BatMonkey has become wild" )

    def event( self, Players, Group_Name ):

        Num_Players = len( Players )

        round_stats( "Monster: " +str( self.name ) )
        battle_stats( Players, "" )
        battle_stats( [self], "" )
		
        Turn = roll( Num_Players ) - 1

        Clean_Message( "The BatMonkey attacks " + str( Players[ Turn ] ) )
        for attack_hit in range( 3 ):
            
            #try:
            attack_result = self.attack( Players[ Turn ] )
            Clean_Message( "Attack_result:" + str( attack_result ) )
            if( attack_result == "dead" ):
                Clean_Message( str( Players[ Turn ].name ) + " was killed befor the fight.. sad"  )
                break

            #except:
            #    pass

        # remove player from the game here

        while( self.health <= 0  ):
            Players = Purge_Dead( Players )
            Num_Players = len( Players )

            Turn = Inc_Turn( Turn, Num_Players )
            Clean_Message( "It is " + str( Players[ Turn ].name ) + "'s turn..." )

            Turn = Inc_Turn( Turn, Num_Players )


            self.health -= 5 

        Clean_Message( "The BatMonkey was defeated. The " + str( Group_Name ) + " continue their blaze" )

        round_stats( "Monster: " +str( self.name ) )

class Troll(Creature):
  def __init__(self, name, prey):
    super().__init__(name, 40, 10, 0, "Troll", "Rooaaarrrr")
    self.prey = prey

  def hunt(self):
    Clean_Message(f"{self.name} the { self.species } is hunting {self.prey.name}.")
    if( self.prey.health <= 0 ):
        Clean_Message(f"{self.prey.name} has already been killed!!!")
    else:
        if( roll( 2 ) % 2 == 0 ):
            pass
            #self.prey.runs(  )
        else:
            self.attack( self.prey )
            if( self.prey.health <= 0 ):
                Clean_Message(f"{self.name} the { self.species } killedd {self.prey.name}.")

class Deer(Creature):
  def __init__(self, name):
    super().__init__( name, 10, 0, 0, "Deer", "Aaaahhhhhh")

  def runs(self):
    Clean_Message(f"{ self.name } the { self.species } is running fast away")
# End Creature Area
# ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - ! - 

def Purge_Dead( Players ):
    for player in Players:
        if ( player.health >= 0 ):
            Players.remove( player )
    return Players
        

# define the Player class
class Player:
    def __init__(self, name, health, max_hit, max_heal):
        self.name = name
        self.health = health
        self.max_health = 10000
        self.max_hit = max_hit
        self.max_heal = max_heal
        self.stun = 0
        self.prayer = 0
        self.wins = 0
        self.items = [  ]

    def add_wins( self, wins ):
        self.wins += wins

    def set_adventure_round( self, Round_Count ):
        self.max_health = Round_Count * 10

    def attack(self, other_player):
        # subtract the max_hit of the attacking player from the health of the other player
        temp_roll = roll( self.max_hit )
        roll_strength = Roll_Strength( temp_roll, self.max_hit )
        other_player.health -= temp_roll
        
        attack_emote( self.name, other_player.name, roll_strength, temp_roll )
        if( other_player.health <= 0 ):
            return "dead"
        else:
            return "not dead"

    def heal(self):
        # add some amount of health to the player's current health
        temp_roll = roll( self.max_heal )
        roll_strength = Roll_Strength( temp_roll, self.max_heal )
        self.health += temp_roll
        heal_emote( roll_strength )
        Clean_Message( f"{self.name} heals for {temp_roll} health points" )

    def buff_max_health(self, buff):
        # add some amount of health to the player's current health
        self.max_heal += buff
        self.items.append( "Healing_Potion" )
        Clean_Message(f"{ self.name } has added { buff } to max heals its now { self.max_heal }")

    def buff_max_hit(self, buff):
        # add some amount of health to the player's current health
        self.max_hit += buff
        self.items.append( "Strength_Potion" )
        Clean_Message(f"{ self.name } has buffed max hp by { buff } its now { self.max_hit }")

    def waft_sand(self, Target):

        if( roll( 4 ) == 1 ):
            Clean_Message(f"{self.name} wafts sand right into {Target.name}'s face! Ouch!")
            Target.add_stun( 3 )
            waft_emote(  )
            Clean_Message(f"Success!!! {Target.name} is stunned for { Target.stun } turns")
        else:
            play_animation( Failed_Waft )
            Clean_Message(f"Wafting sand {self.name}? You're a FREAK!!!")

    def add_stun( self, stun ):
        # add some amount of health to the player's current health
        self.stun += stun

    def add_prayer( self, count ):
        # add some count to  the player's prayer
        self.prayer += count

    def taunt( self ):
        taunt_emote(  )

    def dec_stun( self, stun ):
        # add some amount of health to the player's current health
        self.stun -= stun
        
    def dec_hp( self, count ):
        self.health -= count

    def look( self, luck ):
        SUPER_POTION_THRESH = int( DEFAULT_HEALTH / 3 )
        ROLL_AMMOUNT = 20

        look_emote(  )
        # add some amount of health to the player's current health
        look = roll( ROLL_AMMOUNT + luck )
        
        if( look == 1 and self.health <= SUPER_POTION_THRESH ):
            Clean_Message( "You're completly hopeless.... Wait...." )
            super_health_potion_emote(  )
            Clean_Message( "A Super Health Potion was found. A real Deus Ex Machina Event. Nice!" )
            self.health = DEFAULT_HEALTH

        elif( look == 3 ):
            Nose_Honking_Clown( self.name )
            clown_emote(  )
            self.dec_hp( 2 )
        elif( look == 7 ):
            Life_Is_Pain( self.name )
            prayer_emote(  )
            self.add_prayer( 7 ) # Default 7
        elif( look >= 14 and look < 17 ):
            # Found Strength Potion
            Clean_Message(f"You're persistant I'll give you that {self.name}")

            strength_potion_emote(  )
            self.buff_max_hit( DEFAULT_STRENGTH_POT ) # Default 10
        elif( look >= 18 ):
            # Found healing Potion
            Clean_Message(f"wait... what... thats broken...")
            health_potion_emote(  )
            self.buff_max_health( DEFAULT_HEALING_POT ) # Default 15
        else: # 1 - 12
            Clean_Message( f" Looking for what?! {self.name}... You're the worst!!!" )
            # Found Nothing

def Battle( Monster, Players ):
    #print( Players.append( Monster ) )
    battle_stats( Players, "" )
    battle_stats( [ Monster ], "" )

    pass

def Monster_Event( Players, Group_Name ):

    Current_Monster = spawn_creature( Players )
    #battle_stats([ Current_Monster ], "")  
    Current_Monster.event( Players, Group_Name )
    # Roll 
    #Monster = spawn_creature(  )
    #Monster_Name = "BatMonkey"
    #creature_class = globals(  ).get( Monster )( Players ) # Spawn the Monster
    pass
    return

def Room_Event( Players, Group_Name ):
    Clean_Message( "Still need to Build Room Events" )
    pass

def Elder_Event( Players, Group_Name ): 
    Clean_Message( "Holy Fuck the elder event... " )
    Clean_Message( "It's gonna be insane... when I get to building it..." )
    pass


def Adventure_Roll( Players, Group_Name ):
    # Game Continued
    print( roll( BASE_ADVENTURE_ROLL ) )
    ADV_ROLL = roll( BASE_ADVENTURE_ROLL )

    if 1 <= ADV_ROLL <= 45: # 45
        print(" !!! Monster_Event !!! ")
        Monster_Event( Players, Group_Name )

    elif  46<= ADV_ROLL <= 70: # 35
        Clean_Message( "Walking timid... another length traveled and nothing seen" )

    elif 71 <= ADV_ROLL <= 99: # 29
        Room_Event( Players, Group_Name )

    elif ADV_ROLL == 100: # 1
        print(" !!! Elder Event !!! ")
        Elder_Event( Players, Group_Name )

    else:
        print("ADV_ROLL is not in any of the specified ranges")



def Player_Choice_Adventure( Group_Name, Players ):
    while( True ):
        print(f"|")
        player_choice = Prompt_User_Adventure_Base( Group_Name )
        print(f"|")
        print( "|\n|" )
        if player_choice == "exit" or player_choice == "e":
            #Player.attack( Target )

            Clean_Message( " Ya know... im not suprised that the " + str( Group_Name ) + " have exited.. makes sense" )
            return False
        elif player_choice == "keep" or player_choice == "k":
            
            Clean_Message( "Once again into the breach! On the " + str( Group_Name )+ " ford." )

            Adventure_Roll( Players, Group_Name )
            return True
        else:
            # if player 1 makes an invalid choice, Try again
            print("| Invalid choice. Try again.")

def Player_Choice( Player, Target ):
    Prayer_Toggle = False
    while( True ):
        Prayer_Toggle = False
        print(f"|")

        if ( Player.prayer > 0 ):
            player_choice = Prompt_User_With_Prayer( Player.name )
            Prayer_Toggle = True
        else:
            player_choice = Prompt_User( Player.name )
        print(f"|")
        print( "|\n|" )
        if player_choice == "attack" or player_choice == "a":
            Player.attack( Target )
            break
        elif player_choice == "heal" or player_choice == "h":
            Player.heal()
            break
        elif player_choice == "waft" or player_choice == "w":
            Player.waft_sand( Target )
            break
        elif player_choice == "look" or player_choice == "l":
            Player.look( 0 )
            break
        elif player_choice == "taunt" or player_choice == "t":
            Player.taunt(  )
            break
        else:
            if( Prayer_Toggle ):
                if player_choice == "pray" or player_choice == "p":
                    print("| " + str( Player.name ) + " prays, but nothing seems to happen...")        
            else: # if player 1 makes an invalid choice, Try again
                print("| Invalid choice. Try again.")

def Stun_Check( player1, player2, Round_Count ):
    if( player1.stun > 0 ):
        round_stats( str( Round_Count ) )
        Clean_Message( "Get Wafted! Idiot! " + str( player1.stun ) + " more rounds Nerd! " )
        player1.dec_stun( 1 )
    else:
        round_stats( Round_Count )
        if( Round_Count % 2 == 0 ):
            battle_stats( [ player1, player2 ], player1.name ) # Patch for Prayer
        else:
            battle_stats( [ player2, player1 ], player2.name ) # Patch for Prayer
        Player_Choice( player1, player2 )

def round_stats( Round_Count ):


    print( "|" )
    print( "|  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  |" )
    print( "|  \\  /  Round #" + str( Round_Count ) + "  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /  \\  /" )                 
    print( "|  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  |" )
    print( "|" )
    print( "|" )
    
    print( "|" )

def Top_Cap(  ):
    print( "   - -  -   -    -     -      -       -        -         -          -           -            -             -              -               -                ---->" )
    print( " /" )
    print( "|" )

def Bottom_Cap(  ):
    print( "\\" )
    print( "   - -  -   -    -     -      -       -        -         -          -           -            -             -              -               -                ---->" )

def Figgghhhhhttt( Champ, wins ):
    Top_Cap(  )

    """
    print("Spawn Deer")
    Barry = Deer( "Barry" )
    Barry.greet( "Hello" )
    print("Spawn Troll")
    Gruff = Troll( "Gruff", Barry )
    Gruff.greet( Gruff.noise )
    Gruff.hunt(  )

    battle_stats( [ Gruff, Barry ] )
    Gruff.hunt(  )

    battle_stats( [ Gruff, Barry ] )
    Gruff.hunt(  ) 
    """

    Default_Healing = 11
    Default_Health = DEFAULT_HEALTH
    Default_Hitpoints = 9
    Default_Stunned = 0

    if( Champ == "" ):
        player1 = input( "|\tChamp:      " )
        player1 = Player( str( player1 ), Default_Health, Default_Hitpoints, Default_Healing)
    else:
        print( "|\tChamp:      " + str( Champ.name ) )
        player1 = Player( str( Champ.name ), Default_Health, Default_Hitpoints, Default_Healing)
        player1.add_wins( wins )
		
    # create two player objects
    player2 = input( "|\tChallenger: " )
    player2 = Player( str( player2 ), Default_Health, Default_Hitpoints, Default_Healing)
	
	# Troll Event
    #if( roll( 12 ) % 1 == 0 ):
    #    Sean = Troll( "Sean The Troll", Deer( "Cameron the Deer" ) )
    #    Sean.attack( player1 )
    #    Sean.attack( player2 )		
    
	# game loop
    Round_Count = 1
    """
    print( "+++++++" )
    print( "+++++++" )
    print( "+++++++" )
    print( "+++++++" )


    Billy = Player( "Billy", Default_Health, 80, Default_Healing)
    Rikky = Troll( "Rikky", Billy )

    Rikky.hunt(  ) 
    Billy.attack( Rikky )
    Rikky.hunt(  ) 
    Billy.attack( Rikky )
    Rikky.hunt(  ) 

    battle_stats( [ player1, player2, Rikky ] )

    print( "+++++++" )
    print( "+++++++" )
    print( "+++++++" )
    print( "+++++++" )
    """
    Fuggin_Figgghhhhhhtttt(  )
    while player1.health > 0 and player2.health > 0:

        #print_stats( player1, player2 )
        if( Round_Count % 2 == 0 ):
            Stun_Check( player1, player2, Round_Count )
        else:
            Stun_Check( player2, player1, Round_Count )
        Round_Count += 1

    round_stats( Round_Count )
    winner = Game_Over( player1, player2 )

    if( not y_n( "| Do you want to play again?" ) ):
        Bottom_Cap(  )
    
        return

    else:
        winner.add_wins( 1 )
        Bottom_Cap(  )
        
        Figgghhhhhttt( winner, winner.wins )


def Game_Over( player1, player2 ):

    
    winner = player1
    """
    SPs = 0
    HPs = 0
    SP2s = 0
    HP2s = 0
    for item in player1.items:
        if( item == "Strength_Potion" ):
            SPs += 1
        elif( item == "Health_Potion" ):
            HPs += 1

    for item in player2.items:
        if( item == "Strength_Potion" ):
            SP2s += 1
        elif( item == "Health_Potion" ):
            HP2s += 1
    Clean_Message( str( player1.name ) + " had " + str( SPs ) + " Strength_Potions" )
    Clean_Message( str( player1.name ) + " had " + str( HPs ) + " Health_Potions" )
    Clean_Message( str( player2.name ) + " had " + str( SP2s ) + " Strength_Potions" )
    Clean_Message( str( player2.name ) + " had " + str( HP2s ) + " Health_Potions" )
    """
	
    #print( player2.items )
    if player2.health > player1.health:
        winner = player2
        message = "A New Champ is Crowned!!!"
    else:
        winner = player1
        message = "  Aaaaaaand Stilllll!!!  "
    print(f"""|
|             ___________   \t\t\t\t\t\t\t   ___________
|            '._==_==_=_.'  \t\t\t\t\t\t\t  '._==_==_=_.'
|            .-\:      /-.  \t\t\t\t\t\t\t  .-\:      /-.
|           | (|:.     |) | \t\t{message}\t\t | (|:.     |) |
|            '-|:.     |-'  \t\t\t\t\t\t\t  '-|:.     |-'
|              \::.    /    \t\t\t{winner.name}\t\t\t\t    \::.    /
|               '::. .'     \t\t\t\t\t\t\t     '::. .'
|                 ) (       \t\t\t\t\t\t\t       ) (
|               _.' '._     \t\t\t\t\t\t\t     _.' '._
|              `" " " "`    \t\t\t\t\t\t\t    `" " " "`
|
|""")
    
    return winner

def check_integer(x):
    if type(x) is int:
        return True
    else:
        return False

def Run_Adventure( Players, Group_Name ):
    Round_Count = 1
    Top_Cap(  )

    Start_Adventure_Greeting(  )

    round_stats( " PRE GAME LOBBY " )
    battle_stats( Players, "" )

    Clean_Message( "Greetings!!! Enjoy your time in safety, the road ahead is painful and dark." )
    Clean_Message( "You'll see things sthat will make your stomach turn well into old age." )
    Clean_Message( "If you survive that long... Anyways... have a it... I wish you bad luck" )


    Choice = True
    while( len( Players ) != 0 and Choice ):
        round_stats( Round_Count )
        battle_stats( Players, "" )
        Choice = Player_Choice_Adventure( Group_Name, Players )

        # Roll 
        #Monster = spawn_creature(  )
        #Monster_Name = "BatMonkey"
        #creature_class = globals(  ).get( Monster )( Players ) # Spawn the Monster

        #print( "\tSpawn a:\t" + str( creature_class.name ) )

        #print( Adventure_Roll )

        # Narration

        # Event



        # Narration
        Round_Count += 1
    Bottom_Cap()


def y_n( message ):
    answer = input( str( message ) + " | y / n:" )
    if( answer == "y" ):
        return True
    elif( answer == "n" ):
        return False
    else:
        return y_n( message )

def Get_Player_Name( Player_Number ):
    while( True ):
        print("|")
        print( "|\tEnter Player " + str( Player_Number ) + "'s Name?" )
        print("|")
        Player_Name = input( "| : " )
        print("|")
        print( "|\tIs Player " + str( Player_Number ) + "'s Name Correct? \t" + str( Player_Name ) )
        print("|")
        while( True ):
            print("|")
            Correct = input( "| y / n: " )
            print("|")
            if( Correct == "y" ):
                return Player_Name
            elif( Correct == "n" ):
                break
            else:
                print("|")
                print( "|\t!!!Invalid entrheal_emotey, try again... !!!" )
                print("|")

def Spawn_Player( Player_Name ):
    DEF_ADV_MAX_HEAL = 8
    DEF_ADV_MAX_HIT = 10
    DEF_ADV_HEALTH = DEFAULT_HEALTH
    return Player( str( Player_Name ), DEF_ADV_HEALTH, DEF_ADV_MAX_HIT, DEF_ADV_MAX_HEAL)

def Adventure(  ):
    Players = []
    
    Run_Adventure( [ Spawn_Player("Cole"), Spawn_Player("Sam"), Spawn_Player("Sean") ], "RatPackBoiz" )
    return

    print("|")
    print( "|\tHow many player will there be? ( Max: 3 )" )
    print("|")
    while( True ):
        Player_Count = input( "| :" )
        if( int( Player_Count ) == 1 ):
            Players.append(Spawn_Player(Get_Player_Name( 1 )))

            Run_Adventure( Players )

            break
        elif( int( Player_Count ) == 2 ):
            Players.append(Spawn_Player(Get_Player_Name( 1 )))
            Players.append(Spawn_Player(Get_Player_Name( 2 )))
            
            Run_Adventure( Players )
            
            break
        elif( int( Player_Count ) == 3 ):
            Players.append(Spawn_Player(Get_Player_Name( 1 )))
            Players.append(Spawn_Player(Get_Player_Name( 2 )))
            Players.append(Spawn_Player(Get_Player_Name( 3 )))
            
            Run_Adventure( Players )

            break
            

    print( "  ______________________________________________" )
    print( " /                                              \\ " )
    print( "|                                               |" )
    print( "|       Still need to make this....             |") 
    print( "|                                               |" )
    print( "\\_______________________________________________/" )
    print(  )
    print(  )

def Main_Menu(  ):

    print( "  ______________________________________________" )
    print( " /                                              \\ " )
    err_cnt = 0
    while( True ):
        print( "|                                               |" )
        print( "|  Hey Feller! Where would you like to go...    |" )
        print( "|                                               |" )
        print( "|      a = adventure                            |" )
        print( "|      f = fight                                |" )
        print( "|      e = exit                                 |" )
        print( "|                                               |" )
    #    print( "    s = settings" ) # Edits a JSON FILE
        Game = input( "| :" )
        if( Game == "a" ):

            print( "\\_______________________________________________/" )
            print(  )
            print(  )
            Adventure(  )
            print( "  ______________________________________________" )
            print( " /                                              \\ " )
        elif( Game == "f" ):

            print( "\\_______________________________________________/" )
            print(  )
            print(  ) 
            Figgghhhhhttt( "", 0 )        
            print( "  ______________________________________________" )
            print( " /                                              \\ " )
        elif( Game == "e" ):
            break  
        else:
            err_cnt += 1
            print( "|                                               |" )
            print( "|   ____________________________________        |" )
            print( "|  /                                    \       |" )
            if( err_cnt == 1 ):
                print( "| | !!! That wasn't on the list...  !!! |       |")
                print( "| | !!! That wasn't on the list...  !!! |       |")
                print( "| | !!! Please try again...         !!! |       |" )
                
            elif( err_cnt == 2 ):
                print( "| | !!! It's only like 3 things...  !!! |       |")
                print( "| | !!! It's not very hard...       !!! |       |" )
                print( "| | !!! Try again...                !!! |       |" )
            elif( err_cnt == 3 ):
                print( "| | !!! ...                         !!! |       |" )
            elif( err_cnt == 4 ):
                print( "| | !!! Ohh F*** You...  exit()     !!! |       |" )
                print( "|  \\____________________________________/       |" )
                break
            print( "|  \\___________________________________/        |" )
            print( "|                                               |" )
    print( "\\_______________________________________________/" )
    
Main_Menu(  )
 
