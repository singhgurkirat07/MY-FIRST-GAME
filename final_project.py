import boss as b
import fight as f 

a=input('ARE YOU READY TO BEGIN YOUR GAME(Y or N):').upper()
if a=='Y':    
    print('GAME INTIATED,LETS BEGIN THIS BLODDY JOURNEY.....')
    print("Your health=100\n")
    c=input('DO YOU WANNA GO FOR BOSS [YES OR NO]:').upper()
    if c=='YES':
        b.boss_encounter()
        f.fight()
        if f.won==True:
            print('\n======================================\n   CONGRATS YOU HAVE COMPLETED GAME\n======================================\n')
        elif f.won==False:
            print('\n=====================\n   NOT LUCKY ENOUGH\n=====================y\n')
    else:
        print('invalid input') 
    
elif a=='N':
    print("YOU FUCKIN' LOSER, SCARDY CAT")
else:
    print("INVALID ENTRY")







   




