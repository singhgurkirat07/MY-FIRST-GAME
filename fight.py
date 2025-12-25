import random as r
import boss as b
player_attack = [30,40,50,20,60,30,20,40,20,30,40,10,50]
boss_attack=[30,50,60,30,40,50,30,50,20,40,30,20,20,30]
boss_health=b.boss_health
player_health=100
phase=1
won=False
def fight():
    global boss_health, player_health, phase,won
    while boss_health>0 and player_health>0:
        player_attack_onboss=r.choice(player_attack)
        print(f'You did {player_attack_onboss} damage on boss ')
        boss_health-=player_attack_onboss
        if boss_health==0 or boss_health<0:
            print('YOU WON')
            won=True
            break
        boss_attack_on_player=r.choice(boss_attack)
        print(f'BOSS did {boss_attack_on_player} damage on you')
        player_health-=boss_attack_on_player
        if player_health==0 or player_health<0:
           print('YOU DIED')
           break
        
        print(f"YOUR HEALTH={player_health}\nBOSS HEALTH={boss_health}")
        phase+=1
        print(f'\n=============================\nPhase {phase} started\n=============================\n ')
        boss_health+=10
        boss_attack_on_player+=10




        





    
