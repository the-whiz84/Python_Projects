print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You arrive at the edge of a lake. You can see a small island in the middle of the lake.\nYou should find a way to cross it, so you decide to follow it\'s shore.\n")
decision1 = input("Which way do you go? Type 'left' or 'right': ").lower()


if decision1 == "left":
    print("You went left. After walking for several minutes along the shore, you see a boat in the distance.\nYou arrive next to it and notice there is only one paddle.\n")
    decision2 = input("Do you want to take the boat and struggle with only one paddle? Or do you want to swim to the island?\nType 'boat' or 'swim': ").lower()
    if decision2 == "boat":
        print("You decide to take the boat as you do not know what might lurk in the water. It takes you more than 1 hour to reach the island with only one paddle.\n")
        print("Your arrive on the island and look around while you catch your breath. In the middle of the island is a ruined temple, barely visible from the overgrown vegetation.\nYou walk toward it and enter inside. You stand in front of 3 doors.")
        decision3 = input("Which one do you choose to go through? Type 'red', 'yellow' or 'blue': ").lower()
        if decision3 == "red":
          print("You go through the red door. You fall through a trap door into a pit full of spikes and die.\nGAME OVER!")
          print('''
      .... NO! ...                  ... MNO! ...
    ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
         ''')
        elif decision3 == "blue":
          print("You go through the blue door. Flames start shooting out of every wall and you have a most gruesome death.\nGAME OVER!")
          print('''
                      (  .      )
       )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          ''')
        elif decision3 == "yellow":
          print("You choose the yellow door. Congratulations, you found the treasure chest!\nYOU WIN!")
          print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
          ''')
        else:
          print("That door does not exist. A giant boulder falls on your head. GAME OVER!")
    else:
        print(
            "You decide to swim than struggling with one paddle. You are confident that your swimming skills will get you there faster.\nUnfortunately, that was a bad decision as the water is infested with alligators and you become their lunch.\nGAME OVER!"
        )
        print('''
                  .-._   _ _ _ _ _ _ _ _
      .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
      '_ '    .   .--_'-' '-' '-' _'-' '._
      V: V 'vv-'   '_   '.       .'  _..' '.'.
      '  =.____.=_.--'   :_.__.__:_   '.   : :
                 (((____.-'        '-.  /   : :
        snd                         (((-'\ .' /
                                 _____..'  .'
                                '-._____.-'
    ''')
else:
    print(
        "You go right and walk along the shore for several minutes.\nSuddenly, a giant bear that was fishing attacks and you die!\nGAME OVER!"
    )
    print('''
     :"'._..---.._.'";
     `.             .'
     .'    ^   ^    `.
    :      a   a      :                 __....._
    :     _.-0-._     :---'""'"-....--'"        '.
     :  .'   :   `.  :                          `,`.
      `.: '--'--' :.'                             ; ;
       : `._`-'_.'                                ;.'
       `.   '"'                                   ;
        `.               '                        ;
         `.     `        :           `            ;
          .`.    ;       ;           :           ;
        .'    `-.'      ;            :          ;`.
    __.'      .'      .'              :        ;   `.
  .'      __.'      .'`--..__      _._.'      ;      ;
  `......'        .'         `'""'`.'        ;......-'
 jgs    `.......-'                 `........'

  ''')
