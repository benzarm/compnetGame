Welcome to Matt & Trent's Wild [text] Fighter!

In this game, you'll find yourself pitted against a worthy opponent in one of 4
randomly generated environments...

SETUP is simple:
1)  Start up the server using wildServer.py, giving the IP and PORT as command 
	line arguments, in that order. 
		Example: $ python3 wildServer.py 192.168.0.107 46000

	You should get a message saying "waiting to accept first player..." This 
	means you're ready to accept the fighters!

2)  In a new window, connect to the server using wildClient.py, also giving the
	same command line arguments as the server. 
   		Example: $ python3 wildClient.py 192.168.0.107 46000

3)  Do the same thing for the second player!

4)  You are ready to FIGHT! Follow the instructions displayed on the client and
	be sure not to enter any commands unless prompted. This could screw things
	up a bit. 

GAMEPLAY is as follows:
1)  Both players will first enter their names, one after the other. 

2)  Then, each will pick a class. There are three classes, each with a slight 
	edge over exactly one other class. 
	Fighter > Ranger
	Ranger > Mage
	Mage > Fighter
	Attacks by those with an advantage will do slightly more damage than usual.

3)  Now you are ready to FIGHT! What follows is what we call the "attack loop."
	Each player will choose an attack one after the other. Attacks will be 
	sent to the server, processed, and the damage each does will be sent back
	to each client. The clients will display the healths of each fighter after
	every time through the attack loop. 

	The attacks are as follows:

	  /| ____________________________
	O|===|* >___FIGHTER__________________>
	      \|

	    SLASH: 			Basic and trusty slice from a longsword. Consistent and 
	    				effective.
	    BLOCK: 			Nullifies the opponent's attack with a strong shield block. 
	    CHARGE: 		Powerful but risky, this attack throws your whole weight
	    				into the enemy and has the potential to dish out serious 
	    				damage. 

	>>>>>>>_____RANGER__________\`-._
	>>>>>>>                     /.-'
		
		BASIC ARROW: 	Tried and true steel-tipped arrow from a longbow cuts
						straight through armor and cloaks alike. 
		DODGE: 			Evades the enemy's attack with some quick footwork.
		FIRE ARROW:		Dishes out HEAVY fire damage if it succeeds, but is 
						incredibly risky due to its explosive and unpredictable 
						nature.

	                                     ______,....-///,  ~~~~~~~~
	\=========================""""""""""""       ___,..-'  ~~~~~~~~
	/===========WIZARD===========----------""""""

		ATTACK SPELL:	The first spell every wizard masters, the basic attack
						spell is consistent and painful to whoever lays on the 
						other side.
		HEALING SPELL:  Mends some of your ailments with a unique healing tome.
		CURSE SPELL: 	Turns the enemy against themselves with a powerful 
						curse that makes the enemies attack weaker and does damage
						to them in return.

4)  Once one player drops to 0 health, the game will be over and a victor will
	be crowned! Who will conquer? Who will come out on top?

IMPORTANT NOTES:
 - Standard width terminal (80) is ideal.
 - Make sure to download all the files in the GitHub repo, including the music
   files, and keep them in the same folder as the client python file. 
 - Make sure to install the mixer python library before playing for peak 
   game quality (the music really makes it). Use this command: 
   		python3 -m pip install -U pygame --user