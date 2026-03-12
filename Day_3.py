#I had alot of life stuff come up so day three took longer than a day but I learned alot
print(r'''

                                                        \  /
                  __                                     \/
     _   ---===##===---_________________________--------------  _
    [ ~~~=================###=###=###=###=###=================~~ ]
    /  ||  | |~\  ;;;;     PKP    ;;;  ET22-689  ;;;;  /~| |  ||  \
   /___||__| |  \ ;;;;            [_]            ;;;; /  | |__||___\
   [\        |__| ;;;;  ;;;; ;;;; ;;; ;;;; ;;;;  ;;;; |__|        /]
  (=|    ____[-]_______________________________________[-]____Kraq|=)
  /  /___/|#(__)=o########o=(__)#||___|#(__)=o#########o=(__)#|\___\
 _________-=\__/=--=\__/=--=\__/=-_____-=\__/=--=\__/=--=\__/=-______

''')
print("Welcome to walk in the park.")
print("Your mission is to survive.")
choice1= input('you\'re comeing to a trail head Turn type "left" or "right".\n').lower()
#choice3= input(print('you enter a liminal space and there are two door one on the "left" and "right"'
                     #'which door do you pick".')).lower()
if choice1 == "left":
    choice2= input('you come to rail road crossing there is a train coming '
          'do you "wait" or "cross".\n').lower()
    if choice2 == "wait":
        choice3 = input('you enter a liminal space and there are 3 door "red" and "yellow" and black'
                              ' which door do you pick".\n').lower()
        if choice3 == "red":
            print("you entered a Level 3 death floor, Game Over ")
        elif choice3 == "yellow":
            print("You found the level 0, you survive ")
        elif choice3 == "black":
            print("you entered endless void of the level 9999999999999999 you lose, Game Over ")
    else:
        print("you got hit but a train game over")
else:
    print("you trip in a goffer hole and break your neck , game over")
