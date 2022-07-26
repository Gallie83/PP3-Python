# **_Battleship_**

Live Website:<a href="https://pp3-battleship-kg.herokuapp.com/" target="_blank" rel="noopener">Battleship</a> 
Github Repository: <a href="https://github.com/Gallie83/PP3-Python" target="_blank" rel="noopener">Github</a> 

# Contents
* [**About**](<#about>)
* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
* [Design Choices](<#design-choices>)
* [**Existing Features**](<#existing-features>)
    * [How To Play](<#how-to-play>)
    * [Future Features](<#future-features>)
* [**Bugs**](<#bugs>)
    *  [Resolved Bugs](<#resolved-bugs>)
    *  [Unresolved Bugs](<#unresolved-bugs>)
* [Testing](#testing)
* [Technologies Used](#technologies)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    *  [Content](<#content>)
*  [**Acknowledgements**](<#acknowledgements>)
# About
This battleship game is based on the classic board game- "Battleship".
This is designed to be a one player game where 4 single space ships are randomly spawned onto a 6 x 6 grid. The player then chooses the difficulty they would like to play on, and then they are given a certain amount of chances to find all the ships.

# User Experience (UX)

## User Stories

* As a user I want to clearly see how the board is layed out.
* As a user I want to see which coordinates I have already selected.
* As a user I want to be able to select the difficulty.
* As a user I want to have all the neccessary game information easily visible.

[Back to top](<#contents>)

# Design Choices

* I chose to have the x-axis of the grid as letters and the y-axis as numbers, as having a coordinate system with two letters could easily lead to confusion. I also ensured that there was a space inbetween each column to stop the board from looking too narrow or unlegible.

[Back to top](<#contents>)

# Existing Features  
  * ## How to Play

    * When the game is loaded up, the board is presented to the player. 
    
    * The player is then asked to choose the difficulty they would like to play on, this determines how many shots the player will be allowed to take while looking for the 4 hidden ships. The player is then asked to give a coordinate to shoot at in the form of A3. A message then appears informing the player whether they missed or hit a battleship. 
    
    * The board is then updated and printed to the console showing where the player shot. An exclamation mark "!"  reveals where a player shot and missed, and an "X" shows where they hit a ship. They player is then shown how many shots they have left and is asked to shoot again. 
    
    * Once the player either wins or runs out of lives, a winning or losing message appears and asks if they would like to play again.

  * ## Future Features

    * An input at the beginning asking what size of board the player would like to play on. 
    * Mulitple lengths of ship that would be placed both horizontally and vertically on the board.
    * A score counter, keeping track of how many games the player has lost or won. 
    * The board shows where the remaining ships are if player loses the game.

[Back to top](<#contents>)

# Bugs

# Resolved Bugs
* When changing the board to display where the player had taken previous shots, I had trouble stopping the row of letters at the top of the board from being changeable. After many trials and errors, I managed to write this function.

![Check row function image](readmeimg/check_row.png)

* This ensures that the numerical value from the players guess has to be on the board and below the x-axis of letters.

## Unresolved Bugs
* I tried to add a score counter, keeping track of the players amount of games won and lost. I had a variable for wins and another for losses, both set to zero. A function would then be called at the end of each round to increment the appropriate variable and diplay how many wins and losses the player had. However, a long list of error messages would pop up at the end of each round and I was unable to figure out a way of making these score counters work. 

# Testing

* Python code was tested using the <a href="http://pep8online.com/" target="_blank" rel="noopener">Pep8 Website</a> 
![Pep8 image](readmeimg/pep8.png)

* Runable heroku page was tested using lighthouse.
![Lighthouse testing image](readmeimg/lighthouse.png)

## Technologies Used

### Languages Used

- [Python](https://www.python.org/)

- [Git](https://git-scm.com/) - Git was used for version control.
- [GitPod](https://www.gitpod.io/) - GitPod, through GitHub, hosted the IDE used for the entirety of this project.
- [Github](https://github.com/) - GitHub is used to host the project files.
- [Heroku](https://www.heroku.com/) - Heroku is used to deploy the application.

[Back to top](<#contents>)


## Deployment

    - To prep the application for deployment to Heroku I had to add a newline (\n) 
    character at the end of every input field for proper display.
    - I then went to Heroku itself and added the PORT: 8000 Config Var.
    - The buildpacks used for this application are Python and NodeJS, in that order.

[Back to top](<#contents>)

### Build Log From Heroku

-----> Building on the Heroku-20 stack

-----> Using buildpacks:
       1. heroku/python
       2. heroku/nodejs
-----> Python app detected

-----> No Python version was specified. Using the same version as the last build: python-3.9.7

       To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes

-----> No change in requirements detected, installing from cache

-----> Using cached install of python-3.9.7

-----> Installing pip 20.2.4, setuptools 47.1.1 and wheel 0.36.2

-----> Installing SQLite3

-----> Installing requirements with pip

-----> Node.js app detected
       
-----> Creating runtime environment
       
       NPM_CONFIG_LOGLEVEL=error
       NODE_VERBOSE=false
       NODE_ENV=production
       NODE_MODULES_CACHE=true
       
-----> Installing binaries
       engines.node (package.json):  unspecified
       engines.npm (package.json):   unspecified (use default)
       
       Resolving node version 14.x...
       Downloading and installing node 14.17.6...
       Using default npm version: 6.14.15
       
-----> Restoring cache
       - node_modules
       
-----> Installing dependencies
       Installing node modules (package.json)
       audited 9 packages in 0.33s
       found 4 vulnerabilities (3 low, 1 high)
         run `npm audit fix` to fix them, or `npm audit` for details
       
-----> Build
       
-----> Caching build
       - node_modules
       
-----> Pruning devDependencies
       audited 9 packages in 0.346s
       found 4 vulnerabilities (3 low, 1 high)
         run `npm audit fix` to fix them, or `npm audit` for details
       
-----> Build succeeded!
-----> Discovering process types
       Procfile declares types -> web
-----> Compressing...
       Done: 84.7M
-----> Launching...
       Released v7
       https://battleship-project3.herokuapp.com/ deployed to Heroku

[Back to top](<#contents>)

# Credits
## Content

* The random library was imported into python to generate random number for the ships positions.
* All code, except where otherwise specified, was written by me - Kevin Gallagher

# Acknowledgements
The site was completed as a Portfolio 3 Project piece for the Full Stack Software Developer Diploma at the [Code Institute](https://codeinstitute.net/). As such I would like to thank my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/), the Slack community, and all at the Code Institute for their help and support.

Kevin Gallagher 2022.

[Back to top](<#contents>)