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

def Roll_Strength( current_roll, sides ):
    roll_strength = ( DEFAULT_ROLL_STRENGTH * current_roll ) / sides
    return roll_strength

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
    print( "|                      /´¯/)\n|                    ,/¯  /\n|                   /    /\n|             /´¯/'   '/´¯¯`·¸\n|          /'/   /    /       /¨¯\\\n|        ('(   ´   ´     ¯~/'   ')\n|         \\                 '     /\n|          ''   \\           _ ·´\n|            \\              ( \n|              \\             \\   " )

def clown_emote(  ):
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

def strength_potion_emote():
    Clean_Message( "Strength_Potion" )
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
        # heal_emote( roll_strength )
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
        print( "|      f = fight                                |" )
        print( "|      e = exit                                 |" )
        print( "|                                               |" )
    #    print( "    s = settings" ) # Edits a JSON FILE
        Game = input( "| :" )
        if( Game == "f" ):

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
 
