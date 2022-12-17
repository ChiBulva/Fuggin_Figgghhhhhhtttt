# Import the random module to use the randint() function
import random

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

DEFAULT_STRENGTH_POT = 6
DEFAULT_HEALING_POT = 4

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
"""
Clown = './video/Clown.mp4'
Taunt = './video/Taunt.mp4'

def Roll_Strength( current_roll, sides ):
    roll_strength = ( DEFAULT_ROLL_STRENGTH * current_roll ) / sides
    return roll_strength

def play_animation( Animation ):
    
    if( Animation_Mode ):

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

def Prompt_User( Player ):
    print( "|\t  ____________________________________________________________________________________________" )
    print( "|\t /                                                                                            \\ " )
    print( "|\t|                                                                                              |" )
    print( "|\t|\t"+ str( Player ) + ", do you want to attack, heal, waft sand, or look around? a, h, w, or l?" )
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
    print( f"|      While { name } is walking past a group of age appropriote girls" )
    print( f"|    { name } overhears the girls talking about how they would never date { name } ")
    print( f"|      How they find { name } unattractive" )
    print(  )
    print( f"|    One of the girls calls { name } a NOSE HONKING CLOWN" )
    print( f"|    Another makes fun of { name }'s shirt" )
    print( f"|    " )
    print( f"|    The girls didn't mean for { name } to hear but it hurts nontheless..." )
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

def battle_stats( Creatures, active ):
    name = [str( Creature.name ) for Creature in Creatures]
    health = [str( Creature.health ) for Creature in Creatures]
    max_hit = [str( Creature.max_hit ) for Creature in Creatures]
    max_heal = [str( Creature.max_heal ) for Creature in Creatures]
    prayer_int = [int( Creature.prayer ) for Creature in Creatures]
    prayer = [str( Creature.prayer ) for Creature in Creatures]
    wins = [str( Creature.wins ) for Creature in Creatures]
    wins_int = [int( Creature.wins ) for Creature in Creatures]
    
    print( "|\t", end="" )
    for box in range(len(name)):
        print( " ______________________________ \t ", end="" )
    print()
    print( "|\t", end="" )
    for box in range(len(name)):
        print( "/\t\t\t\t\\\t", end="" )
    print()
    print("|\t| Name     :\t\t" + "\t|\t| > Name     :\t\t".join( name ) + "\t|")
    print("|\t| Health   :\t\t" + "\t|\t| > Health   :\t\t".join( health ) + "\t|")
    print("|\t| Max_Hit  :\t\t" + "\t|\t| > Max_Hit  :\t\t".join( max_hit ) + "\t|")
    print("|\t| Max_Heal :\t\t" + "\t|\t| > Max_Heal :\t\t".join( max_heal ) + "\t|")
    if( sum( prayer_int ) > 0 ):
        print("|\t| Prayer   :\t\t" + "\t|\t| > Prayer   :\t\t".join( prayer ) + "\t|")
    if( sum( wins_int ) > 0 ):
        print("|\t| Wins     :\t\t" + "\t|\t| > Wins     :\t\t".join( wins ) + "\t|")

    print( "|\t", end="" )
    for box in range(len(name)):
        print( "\\______________________________/\t ", end="" )
    print()

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
        # subtract the max_hit of the attacking player from the health of the other player
        temp_roll = roll( self.max_hit )
        roll_strength = Roll_Strength( temp_roll, self.max_hit )
        other_creature.health -= temp_roll
        Clean_Message(f"{self.name} attacks {other_creature.name} and deals {temp_roll} damage")
        attack_emote( self.name, other_creature.name, temp_roll )

    def make_noise(self):
        Clean_Message(f"{ self.name } the { self.species }:\t{self.noise}")

    def greet(self, message):
        Clean_Message(f"{message}, I am { self.name } and I am a { self.species }")

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
        Clean_Message(f"{ self.name } has added { buff } to max heals its now { self.max_heal }")

    def buff_max_hit(self, buff):
        # add some amount of health to the player's current health
        self.max_hit += buff
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
        look_emote(  )
        # add some amount of health to the player's current health
        look = roll( 20 + luck )
        if( look == 3 ):
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

def Player_Choice( Player, Target ):
    while( True ):
        print(f"|")
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
            # if player 1 makes an invalid choice, Try again
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

def Figgghhhhhttt( Champ, wins ):
    print( "   - -  -   -    -     -      -       -        -         -          -           -            -             -              -               -                ---->" )
    print( " /" )
    print( "|" )

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

    Default_Healing = 8
    Default_Health = 75
    Default_Hitpoints = 10
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
        print( "\\" )
        print( "   - -  -   -    -     -      -       -        -         -          -           -            -             -              -               -                ---->" )
    
        return

    else:
        winner.add_wins( 1 )
        print( "\\" )
        print( "   - -  -   -    -     -      -       -        -         -          -           -            -             -              -               -                ---->" )
        Figgghhhhhttt( winner, winner.wins )


def Game_Over( player1, player2 ):

    
    winner = player1
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

def Run_Adventure( Players ):
    Round_Count = 1

    round_stats( "" )
    battle_stats( Players, "Kevin" )
    round_stats( "" )

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
    DEF_ADV_HEALTH = 75
    return Player( str( Player_Name ), DEF_ADV_HEALTH, DEF_ADV_MAX_HIT, DEF_ADV_MAX_HEAL)

def Adventure(  ):
    Players = []
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
