'''
us random moudule ---->rock,paper,scissors


import random
player1=input("enter the choice:--->rock,paper,scissors")
player2=random.choice(['rock','paper','scissors'])
print("playesr2 selection:",player2)
if player1=='rock' and player2=='paper':
    print("player2 wins")
elif player1=='rock' and player2=='scissors':
    print("player1 wins")
elif player1=='paper' and player2=='rock':
    print("player1 wins")
elif player1=='paper' and player2=='scissors':
    print("player2 wins")
elif player1=='scissors' and player2=='rock':
    print("player2 wins")
elif player1=='scissors' and player2=='paper':
    print("player1 wins")
else:
    print("tie")

#task----->Bulid a game generator sequences----> choice memu
#1---rock paper 
#2---story generator(random choice())---[when,what,who,where----lists[]]
#3otp generate to email
#4 bmi calvulation
'''
import pyqrcode,png
link="https://www.linkedin.com/in/lakshmiprasannabonthala"
qr=pyqrcode.create(link)
print(qr)
qr.png("myqr.png",scale=15)