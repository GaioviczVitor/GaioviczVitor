# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:25:13 2022

@author: Vitor Gaiovicz
"""

palavra_secreta = 'programar'
digitadas = []
chances = 5



while True:
    if chances <= 0:
        print('looser')
        break
    
    letra = input('Digite uma letra:')
    
    if len(letra)> 1:
        print('Somente uma letra.')
        continue
    
    digitadas.append(letra)
    
    if letra in palavra_secreta:
        print(f'Boa! a letra"{letra}" existe na palavra.')
    else:
        print(f'Ixi! A letra"{letra}" não conta na palavra. Tente novamente.')
        digitadas.pop()
        
    if letra not in palavra_secreta:
        chances -=1
    print(f'você ainda tem {chances} chances.')  
    
    if chances == 0 : 
        print('game over')
    
    secreto_temporario = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario +='*'
    
        
    print(secreto_temporario)
            
    if secreto_temporario == palavra_secreta:
        print('Parabéns, você coseguiu!')    
        break
    