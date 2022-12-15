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

# dETERMINE ROLL STRENGTH
DEFAULT_ROLL_STRENGTH = 10
def Roll_Strength( current_roll, sides ):
    roll_strength = ( DEFAULT_ROLL_STRENGTH * current_roll ) / sides
    return roll_strength


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
Heal = './video/Heal.mp4'
Heal_6 = './video/Heal/6.mp4'
Heal_7 = './video/Heal/7.mp4'
Heal_8 = './video/Heal/8.mp4'
Heal_9 = './video/Heal/9.mp4'
Heal_10 = './video/Damage/10.mp4'

Clown = './video/Clown.mp4'
Taunt = './video/Taunt.mp4'

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

def attack_emote( name, op_name, Roll_Strength ):
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
    print( "|\n| " + str( name ) + " @xxxx[{:::::::::::::::::::::::::::::>  " + str( op_name ) + "\n|" )

def potion_emote( Symbol ):
    if( Symbol == "S" ):
        play_animation( Strength_Potion )
    elif( Symbol == "H" ):
        #play_animation( Heal )
        pass
    elif( Symbol == "HP" ):
        Symbol == "H"
        play_animation( Healing_Potion )
    potion = "|\n|  |~~~|\n|  |   |\n| .' " + str( Symbol )+ " '.\n| '.___.'\n|"
    print( potion )

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
    potion_emote( "H" )

def print_stats( Player1, Player2 ):

    print(f"| > Name:\t{ Player1.name }\t| > Name:\t{ Player2.name }")
    print(f"| > Health:\t{ Player1.health }\t| > Health:\t{ Player2.health }")
    print(f"| > Max Hit:\t{ Player1.max_hit }\t| > Max Hit:\t{ Player2.max_hit }")
    print(f"| > Max Heal:\t{ Player1.max_heal }\t| > Max Heal:\t{ Player2.max_heal }")
    if( Player1.prayer > 0 or Player2.prayer > 0 ):
        print(f"| > Prayer:\t{ Player1.prayer }\t| > Prayer:\t{ Player2.prayer }")

def battle_stats( Creatures ):

    name = [str( Creature.name ) for Creature in Creatures]
    health = [str( Creature.health ) for Creature in Creatures]
    max_hit = [str( Creature.max_hit ) for Creature in Creatures]
    max_heal = [str( Creature.max_heal ) for Creature in Creatures]

    print("| > Name:\t\t" + "\t\t| > Name:\t\t".join( name ))
    print("| > Health:\t\t" + "\t\t| > Health:\t\t".join( health ))
    print("| > Max_Hit:\t\t" + "\t\t| > Max_Hit:\t\t".join( max_hit ))
    print("| > Max_Heal:\t\t" + "\t\t| > Max_Heal:\t\t".join( max_heal ))

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
        print(f"|\n| {self.name} attacks {other_creature.name} and deals {temp_roll} damage")
        attack_emote( self.name, other_creature.name, roll_strength )

    def make_noise(self):
        print(f"{ self.name } the { self.species }:\t{self.noise}")

    def greet(self, message):
        print(f"{message}, I am { self.name } and I am a { self.species }")

class Troll(Creature):
  def __init__(self, name, prey):
    super().__init__(name, 40, 10, 0, "Troll", "Rooaaarrrr")
    self.prey = prey

  def hunt(self):
    print(f"{self.name} the { self.species } is hunting {self.prey.name}.")
    if( self.prey.health <= 0 ):
        print(f"{self.prey.name} has already been killed!!!")
    else:
        if( roll( 2 ) % 2 == 0 ):
            pass
            #self.prey.runs(  )
        else:
            self.attack( self.prey )
            if( self.prey.health <= 0 ):
                print(f"{self.name} the { self.species } killedd {self.prey.name}.")

class Deer(Creature):
  def __init__(self, name):
    super().__init__( name, 10, 0, 0, "Deer", "Aaaahhhhhh")

  def runs(self):
    print(f"{ self.name } the { self.species } is running fast away")
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
DEFAULT_STRENGTH_POT = 6
DEFAULT_HEALING_POT = 4

# define the Player class
class Player:
    def __init__(self, name, health, max_hit, max_heal):
        self.name = name
        self.health = health
        self.max_hit = max_hit
        self.max_heal = max_heal
        self.stun = 0
        self.prayer = 0
        self.items = [  ]

    def attack(self, other_player):
        # subtract the max_hit of the attacking player from the health of the other player
        temp_roll = roll( self.max_hit )
        roll_strength = Roll_Strength( temp_roll, self.max_hit )
        print(f"|\n| {self.name} attacks {other_player.name} and deals {temp_roll} damage")
        attack_emote( self.name, other_player.name, roll_strength )

    def heal(self):
        # add some amount of health to the player's current health
        temp_roll = roll( self.max_heal )
        roll_strength = Roll_Strength( temp_roll, self.max_heal )
        self.health += temp_roll
        heal_emote( roll_strength )
        print(f"| {self.name} heals for {temp_roll} health points")

    def buff_max_health(self, buff):
        # add some amount of health to the player's current health
        self.max_heal += buff
        print(f"| { self.name } has added { buff } to max heals its now { self.max_heal }")

    def buff_max_hit(self, buff):
        # add some amount of health to the player's current health
        self.max_hit += buff
        print(f"| { self.name } has buffed max hp by { buff } its now { self.max_hit }")

    def waft_sand(self, Target):

        if( roll( 4 ) == 1 ):
            print(f"| Success!!\n| {self.name} wafts sand right into {Target.name}'s face! Ouch!")
            Target.add_stun( 3 )
            waft_emote(  )
            print(f"| {Target.name} is stunned for { Target.stun } turns")
        else:
            play_animation( Failed_Waft )
            print(f"| What are you doing {self.name}? Wafting sand... ? You're a FREAK!!!")

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
            print( f"|    " )
            print( f"|      While { self.name } is walking past a group of age appropriote girls" )
            print( f"|    { self.name } overhears the girls talking about how they would never date { self.name } and how they find { self.name } unattractive" )
            print( f"|    One of the girls calls { self.name } a NOSE HONKING CLOWN" )
            print( f"|    Another makes fun of { self.name }'s shirt" )
            print( f"|    " )
            print( f"|    The girls didn't mean for { self.name } to hear but it hurts nontheless..." )
            print( f"|    { self.name } loses 2 hp and is bummed about the whole thing" )
            print( f"|    " )
            clown_emote(  )
            self.dec_hp( 2 )
        elif( look == 7 ):
            seperator(  )
            print(f"|       {self.name} starts to look around. But...              " )
            print(f"|       In { self.name }'s time away drift away and ponder..." )
            print(f"|    ____________________________________________________" )
            print(f"|   |    What is this world? What happens when it ends?  |" )
            print(f"|   |    Is there beautiful heaven? Or black oblivian?    |" )
            print(f"|   |                   I Sleep                          |" )
            print(f"|   |____________________________________________________|" )
            print(f"|       " )
            print(f"|       { self.name } suddently realises they are still fighting...              " )
            print(f"|       They have also find no items but gain a unique perspective..." )
            print(f"|       " )
            print(f"|       { self.name } gain some prayer" )
            prayer_emote(  )
            self.add_prayer( 7 ) # Default 7
        elif( look >= 14 and look < 17 ):
            # Found Strength Potion
            print(f"| You found your inner strength! \n|   You're persistant I'll give you that {self.name}")
            potion_emote( "S" )
            self.buff_max_hit( DEFAULT_STRENGTH_POT ) # Default 10
        elif( look >= 18 ):
            # Found healing Potion
            print(f"| wait... what... thats broken...")
            potion_emote( "HP" )
            self.buff_max_health( DEFAULT_HEALING_POT ) # Default 15
        else: # 1 - 12
            print(f"| Looking for what?! {self.name}... You're the worst!!!")
            # Found Nothing

def Player_Choice( Player, Target ):
    if( Player.stun > 0 ):
        print(f"|\n| {Player.name} Missed their turn because they are stunned...\n|")
        Player.dec_stun( 1 )
        return
    while( True ):
        player_choice = input(f"|\n| {Player.name}, do you want to attack, heal, waft sand, or look around? a, h, w, or l?: ")
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
def seperator(  ):
    print( "| -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+" )

player1 = input( "Champ:      " )
player2 = input( "Chalenger:  " )

Default_Healing = 8
Default_Hitpoints = 10
Default_Health = 75
Default_Stunned = 0

# create two player objects
player1 = Player( str( player1 ), Default_Health, Default_Hitpoints, Default_Healing)
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
print( "\nFuggin Figgghhhhhhtttt!\n" )
while player1.health > 0 and player2.health > 0:
    seperator(  )

    #battle_stats( [ player1, player2 ] )
    print_stats( player1, player2 )
    print( "| Round #" + str( Round_Count ) + ":\t" )
    if( Round_Count % 2 == 0 ):
        Player_Choice( player1, player2 )
    else:
        Player_Choice( player2, player1 )
    Round_Count += 1

print( "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
if player2.health > player1.health:
    play_animation( New_Champ )
    print( "!!\tA New Champ is Crowned" )
    print( "!!\t" + str( player2.name ) + " Wins" )
else:
    play_animation( Old_Champ )
    print( "!!\t" + ( player1.name ) + " Wins!! " )
print( "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
print( "!!!!!!!!!!!!  Game Over !!!!!!!!!!!!!!!!!" )
print( "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" )
