#upon encounter with boss
import random as r
boss_dialogues1=['Hahahahaha','AGAIN A WEAKING HAS COME','LETS SEE WHAT ARE YOU WORTH','COME ON YOU WEAKING']
boss_health=80
damage=[30,50,60,30,40,50,30,50,20,40,30,20,20,30]
def boss_encounter():
    print('============================\n       BOSS ENCOUNTER\n============================') 

    print('BOSS:'+r.choices(boss_dialogues1)[0])#this [0]helps us return one of boss dialouges without []
    print(f'\nBOSS HEALTH:{boss_health}')
    



