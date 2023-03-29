# Game2

Project Proposal
Part 1
* Type: Role-playing
* Overview of the game: The plot of my game will be centered around an astronaut landing on Mars to explore and discovering that instead of Mars being uninhabited, like we all think, it has dinosaurs on it. The dinosaurs have made a cult on mars. The astronaut then has to gain the trust of the dinosaurs, she does this by providing them with soda. She must gain the trust of all the dinosaurs, becoming their cult leader, before they can kill her. 
* Description of your gimmick: There will be thought bubbles that appear over the dinosaurs heads to reflect their trust level of the astronaut. These thoughts will show the progression of the astronaut becoming the cult leader.
* Description of the game mechanics: 
  * The astronaut moves left and right
  * Has pockets in the spacesuit to carry items – this will just be an inventory list on the screen
  * Soda replicator – on the space shuttle produces soda, fueled by mars rocks 
  * Giving the dinosaurs soda – and the dinosaur keeping track of when it has enough to trust the astronaut
  * Dinosaur attacking the astronaut when it doesn’t trust it
*	A list of power-ups, collectibles, or updates:
  * Mars rocks to fuel soda replicator  
  * Some sort of special object (maybe - dinosaur bones/asteroid) that if the astronaut finds the dinosaurs require less soda to trust her
Part 2
*	Outline of Game Architecture: (list of main modules and describe how they interact)
  * Intro screen function with instructions and calls the game loop
  * Game Loop
    -Initialize the background of Mars
    -Call space shuttle class/function
    -Call Astronaut class
    -Generate mars rocks random places
    -Calls dinosaur class 
    -Calls winscreen function
    -Calls losescreen function
  * Space shuttle class/function
    -Puts space shuttle on screen
    -Takes rocks as input and produces soda
    -Has a cool down time after producing soda – or has wait time for soda to be produces (I haven’t decided)
    -Has replicator for astronaut to come and has some sort of trigger for the replicator function
  * Astronaut Class
    -Initialize astronaut 
    -Movement function - take in arrow key presses and move 
    -Pick up function – for picking up rocks and sodas; Adds rocks to rocks group
    -Pocket function - Keeps track of number of rocks and sodas; Updates pocket contents on screen 
 * Dinosaur Sprite Class
  -Creates the dinosaurs
  -Counter to keeps track of how many sodas have been given to the dinosaur
  -thought bubble function to show trust level in astronaut
 	-attack function – I want to try to get this to be distance based, so when the distance between the astronaut and the dinosaur is less than a specific amount the dinosaur attacks and does damage (ideally this could scale with the trust – as the dinosaur trusts you, then you can get closer to it)
 	-create trust group – as the dinosaurs trust the astronaut add them to this group
  * Soda replicator function
   -Intakes rocks
 	 -Produces soda
  * Mars Rocks group
   -Keeps track of how many of the sodas is in the astronauts pockets
   -Add rocks when they are picked up
   -Removes rocks when they are placed in the replicator
  * Win Screen function -Once you gain the trust of all the dinosaurs, triggers an end scene with you as the cult leader
 	* Lose Screen function - If the dinosaurs attack you before you can become the cult leader then trigger cutscene of you dead
*	Overview of the user interface:
  * Movement:
    -The player controls the astronaut by moving them with the keypad
   	-Picking up rocks/soda will be done by standing in front of it and pressing a specific key
  * View:
    -On the screen the player will see the setting, spaceship, dinosaurs, etc.
    -The player will also be able to see their pocket this will have a counter for the rocks and sodas 
*	Potential technical challenges: 
  *	I want to try to get my “attack” feature to be distance based but that may not be feasible – I’m going to have to do some investigating into pygames distance measuring ability and if it can’t then maybe I can use Euclidian/vector distance on the position points
  *	It would be nice to have movement where when I go to the end up the screen the background adjusts – for example entering the space shuttle – I will also have to do some research to figure out that one. I’m sure its possible I’m just not sure how yet.  
  
Part 3 – I am working alone  

Part 4
*	Milestone 1: March 15
 	* Have background
  *	Have Space shuttle with screen movement
  *	Have astronaut moving on screen
*	Milestone 2: March 29
  *	Have rocks on screen
  *	Have the astronaut able to pick up rocks
  *	Have the astronaut placing rocks in the replicator and soda being collected
  *	Have dinosaurs on screen with thought bubbles
  *	Astronaut can give dinosaurs soda
*	Milestone 3: April 12
  *	Win screen
  *	Lose screen
  *	Intro screen
*	Final Game Submission: April 29
  	*Have people playtest between April 12 and this date so I can fix any bugs
  
