# Interactive Map for RPG

## The Why

I play RPG (Donjon de Naheulbeuk) and I am always fighting with printing
the map, I do not have good figurine for player and at the end of the days
the battle are a mess to follow.

Last time we played we where in ski holiday so no printing facilities
(but plenty of computing facilities) and I had a computer and a TV screen.

The idea : display the map on the TV set, then display the player and move them
on the map (there are usually 6 players).

The problem: I could not find any application suitable for that.

The Solution: this application :-)

## The What

   * a PyGame application
   * runs on a raspberry Pi
   * simple to use
   * can load three maps, and rotate the display between them
   * as many players are you want
   * a "group" icon for group action
   * easy toggle between group and individuals

## The How

### Installation

   * installe Python and PyGame
   * put the maps in the Background folder
   * put the players in the Players folder
   * run it

images can be JPEG, GIF or PNG. They are loaded in alphabetical order, this means
that namming them with 0xxxx, 1yyyy will help (see usage).

GIF,PNG is recommended for players image if you want transparency support.



### Usage
   * 1,2,3 keys switch between the maps (1 in the first in alphabetical order, 2 the second, etc..)
   * G toggle between group and players icon, group icon is the first file in alphabetical order, go better name this file _group.gif)
   * ESC to quit

