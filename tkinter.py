#Importing modules
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as mc
from tkinter import messagebox as mb
from tkinter import ttk
import pygame,random,math,time,sys

pygame.init()
pygame.mixer.init()
root=Tk()
root.title('Attack On Veges')

#Homescreen
def firstscreen():
    global canvas1,pic
    canvas1=Canvas(root,width=1000,height=600)
    canvas1.pack()
    image=Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\AOV.png')
    image=image.resize((1000,600),Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(image)
    canvas1.create_image(0,0,anchor=NW,image=pic)
    
    button1=Button(text='PLAY',command=secondscreen,bg='floral white',fg='black',font=('helvetica',11,'bold'))
    button1.config(height=2,width=23)
    canvas1.create_window(510,370,window=button1)

    button1a = Button(text='RULES', command=rules, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    button1a.config(height=2, width=23)
    canvas1.create_window(510, 430, window=button1a)

    leader = Button(text='SCOREBOARD', command=leaderboardfromfsr, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    leader.config(height=2, width=23)
    canvas1.create_window(510, 490, window=leader)

    endgame = Button(text='QUIT', command=quitgame, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    endgame.config(height=2, width=23)
    canvas1.create_window(510, 550, window=endgame)
    
#playagain screen after gameover    
def playscreen():
    global canvas1,pic,status
    canvas5.pack_forget()
    canvas1=Canvas(root,width=1000,height=600)
    canvas1.pack()
    
    image=Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\AOV.png')
    image=image.resize((1000,600),Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(image)
    canvas1.create_image(0,0,anchor=NW,image=pic)
    status='playagain'
    
    playbutton3=Button(text='PLAY AGAIN',command=game,bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
    playbutton3.config(height=2,width=23)
    canvas1.create_window(510,370,window=playbutton3,tag='play')
    
    button1a = Button(text='RULES', command=rules2, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    button1a.config(height=2, width=23)
    canvas1.create_window(510, 430, window=button1a)

    leader = Button(text='SCOREBOARD', command=leaderboardfroml2, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    leader.config(height=2, width=23)
    canvas1.create_window(510, 490, window=leader)

    endgame = Button(text='QUIT', command=quitgame, bg='floral white', fg='black', font=('helvetica', 11, 'bold'))
    endgame.config(height=2, width=23)
    canvas1.create_window(510, 550, window=endgame)
    canvas1.pack()

#Score screen after gameover
def menuscreen():
    global canvas5,pic,f
    canvas5=Canvas(root,width=1000,height=600)
    canvas5.pack()
    image=Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\gameover.png')
    image=image.resize((1000,600),Image.ANTIALIAS)
    pic=ImageTk.PhotoImage(image)
    canvas5.create_image(0,0,anchor=NW,image=pic)

    conn=mc.connect(host='localhost',user='root',password='Stark3.0',database='project')
    cur=conn.cursor()
    cur.execute("select username,score from aov order by score desc")
    rec=cur.fetchall()
    conn.close()
    for i in rec:
        if i[0]==f:
            score=i[1]
            
    playbutton4=Button(text='MENU',command=playscreen,bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
    playbutton4.config(height=2,width=23)
    canvas5.create_window(510, 490,window=playbutton4)

    sb=Button(text=str(score),bg='azure', fg='black', font=('century schoolbook', 13, 'bold'))
    sb.config(height=2,width=10)
    canvas5.create_window(620,390,window=sb)

#Leaderboard
def leaderboard():
    canvas1.pack_forget()
    global canvas5,origin
    canvas5=Canvas(root,width=1000,height=600)
    
    pic5=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\scoreboard.png').resize((1000,600)))
    bglabel=Label(canvas5,image=pic5)
    bglabel.image=pic5
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    button3 = Button(text='HOME', command=fsrfromleaderboard, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button3.config(height=2, width=13)
    canvas5.create_window(50, 50, window=button3)
    canvas5.pack()

    cols=('Name','Score')
    listbox=ttk.Treeview(root,columns=cols,show='headings')
    listbox.column('#1',anchor='center',width=300)
    listbox.column('#2',anchor='center',width=280)
    listbox.place(x=200,y=200)

    listbox.heading('#0',text='',anchor='center')
    listbox.heading('Name',text='Username',anchor='center')
    listbox.heading('Score',text='Score',anchor='center')

    conn=mc.connect(host='localhost',user='root',password='Stark3.0',database='project')
    cur=conn.cursor()
    cur.execute("select username,score from aov order by score desc")
    rec=cur.fetchall()
    ind=0
    for i in rec:
        listbox.insert('','end',values=i)

def leaderboard2():
    canvas1.pack_forget()
    global canvas5,origin
    canvas5=Canvas(root,width=1000,height=600)
    
    pic5=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\scoreboard.png').resize((1000,600)))
    bglabel=Label(canvas5,image=pic5)
    bglabel.image=pic5
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    button3 = Button(text='HOME', command=playscreen, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button3.config(height=2, width=13)
    canvas5.create_window(50, 50, window=button3)
    canvas5.pack()

    cols=('Name','Score')
    listbox=ttk.Treeview(root,columns=cols,show='headings')
    listbox.column('#1',anchor='center',width=300)
    listbox.column('#2',anchor='center',width=280)
    listbox.place(x=200,y=200)

    listbox.heading('#0',text='',anchor='center')
    listbox.heading('Name',text='Username',anchor='center')
    listbox.heading('Score',text='Score',anchor='center')

    conn=mc.connect(host='localhost',user='root',password='Stark3.0',database='project')
    cur=conn.cursor()
    cur.execute("select username,score from aov order by score desc")
    rec=cur.fetchall()
    
    for i in rec:
        listbox.insert('','end',values=i)
        
#Rules in firstscreen
def rules():
    canvas1.pack_forget()
    global canvas3,button3
    canvas3=Canvas(root,width=1000,height=600)
    pic3=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Woodenbg2.png').resize((1000,600)))
    bglabel=Label(canvas3,image=pic3)
    bglabel.image=pic3
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    button3 = Button(text='HOME', command=fsrfromrules, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button3.config(height=2, width=13)
    canvas3.create_window(50, 50, window=button3)
    canvas3.pack()

#Rules in playagain screen
def rules2():
    canvas1.pack_forget()
    global canvas3,button3
    canvas3=Canvas(root,width=1000,height=600)
    
    pic3=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Woodenbg2.png').resize((1000,600)))
    bglabel=Label(canvas3,image=pic3)
    bglabel.image=pic3
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    button3 = Button(text='HOME', command=psrfromrules, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button3.config(height=2, width=13)
    canvas3.create_window(50, 50, window=button3)
    canvas3.pack()
 
def secondscreen():
    canvas1.pack_forget()
    global canvas2
    canvas2=Canvas(root, width=1000, height=600)
    canvas2.create_text(380,140,text='Attack On Veges',fill='black',font=('century schoolbook',55,'bold'))
    pic3=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\\bgs2.png').resize((1000,600)))
    bglabel=Label(canvas2,image=pic3)
    bglabel.image=pic3
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    canvas2.pack()
    global button2
 
    button2 = Button(text='HOME', command=fsrfromcanvas2, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2, width=13)
    canvas2.create_window(50, 50, window=button2)

    signup = Button(text='SIGN UP', command=signup_entry, bg='azure', fg='black', font=('century  schoolbook',11, 'bold'))
    signup.config(height=2, width=30)
    canvas2.create_window(390,360, window=signup)

    signin = Button(text='SIGN IN', command=signin_entry, bg='azure', fg='black', font=('century  schoolbook',11, 'bold'))
    signin.config(height=2, width=30)
    canvas2.create_window(390,280, window=signin)

    bye = Button(text='QUIT', command=quitgame, bg='azure', fg='black', font=('century  schoolbook', 11, 'bold'))
    bye.config(height=2, width=30)
    canvas2.create_window(390, 440, window=bye)
    
#Establishing connection    
def db(entry1,entry2):
    conn=mc.connect(host='localhost',user='root',password='Stark3.0',database='project')
    cur=conn.cursor(buffered=True)
    global f,p,submit,status
    f=entry1.get()
    p=entry2.get()
    if status=='signup':
        cur.execute("select username from aov")
        rec=cur.fetchall()
        if f!='' and p!='':
            for i in rec:
                if (f,) in rec:
                    mb.showerror('Error','oops...It looks a user of the same name exixts.Enter another username.')
                    signupscreen.delete('invalidpass')
                    break
                else:
                    if p!='':
                        cur.execute("insert into aov(username,password) values ('{}','{}')".format(f,p))
                        cur.execute('commit')
                        mb.showinfo('Game','Yay!You\'re now ready to play. Click Play to Begin.')
                        entry1=Entry(root,state='disabled')
                        entry2 = Entry(root, state='disabled')
                        signupscreen.delete('invaliduser')
                        signupscreen.delete('signupbutton')
                        conn.commit()
                        playbutton1=Button(text='PLAY',command=game,bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
                        playbutton1.config(height=2,width=23)
                        signupscreen.create_window(500,540,window=playbutton1,tag='play')
                        break
        else:
            mb.showinfo('Error','Enter the details')
            
    elif status=='signin':
        cur.execute('select username,password from aov')
        rec=cur.fetchall()
        if f!='' and p!='':
            for i in rec:
                if i[0]==f:
                    if i[1]==p:
                        signinscreen.delete('label4')
                        signinscreen.delete('invalid')
                        mb.showinfo('Game','You\'re Back!...Click Play to Begin')
                        playbutton2=Button(text='PLAY',command=game,bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
                        playbutton2.config(height=2,width=23)
                        signinscreen.create_window(250,540,window=playbutton2,tag='play')
                        break
                    elif i[1]!=p:
                        mb.showerror('Error','The Username does not match the password...\nTry Again or Signup instead')
                        signup = Button(text='SIGN UP', command=signupfromsignin, bg='azure', fg='black',font=('century  schoolbook', 11, 'bold'))
                        signup.config(height=2, width=30)
                        signinscreen.create_window(600, 540, window=signup)
                        break

        else:
            mb.showinfo('Error','Enter the details or signup')
            signup = Button(text='SIGN UP', command=signupfromsignin, bg='azure', fg='black',font=('century  schoolbook', 11, 'bold'))
            signup.config(height=2, width=30)
            signinscreen.create_window(600, 540, window=signup)
            signinscreen.delete('label3')
            signinscreen.delete('label4')            
    conn.close()

#for new user to sign up
def signup_entry():
    global status,signupscreen,button2,entry1,f,p,entry2
    status='signup'
    canvas2.pack_forget()
    signupscreen=Canvas(root, width=1000, height=600)
    signupscreen.pack()
    
    pic3=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\\Woodenbg3.png').resize((1000,600)))
    bglabel=Label(signupscreen,image=pic3)
    bglabel.image=pic3
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    signupscreen.pack()
    
    button2 = Button(text='HOME', command=fsrfromsignup, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2, width=13)
    signupscreen.create_window(50, 50, window=button2)
    
    text=StringVar(value=('Times New Roman 30'))
    entry1=Entry(root,font=text)
    entry2=Entry(root,font=text,show='*')
    
    signupscreen.create_window(500,380,window=entry1)
    signupscreen.create_window(500,450, window=entry2)
    entry1.configure(width=25)
    entry2.configure(width=25)
    
    submit = Button(text='Submit', command=lambda : db(entry1,entry2), bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
    submit.config(height=2, width=23)
    signupscreen.create_window(500, 540,window=submit,tag='submitbutton')
    
    f=entry1.get()
    p=entry2.get()
    signupscreen.pack()
    
#for an existing user to login
def signin_entry():
    global status,signinscreen,button2,entry1,entry2
    status='signin'
    canvas2.pack_forget()
    signinscreen = Canvas(root, width=1000, height=600)
    
    pic3=ImageTk.PhotoImage(Image.open(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\\Woodenbg4.png').resize((1000,600)))
    bglabel=Label(signinscreen,image=pic3)
    bglabel.image=pic3
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    signinscreen.pack()
    
    button2 = Button(text='HOME', command=fsrfromsignin, bg='azure', fg='black', font=('helvetica', 9, 'bold'))
    button2.config(height=2, width=13)
    signinscreen.create_window(50, 50, window=button2)

    text = StringVar(value=('Times New Roman 30'))
    entry1 = Entry(root, font=text)
    entry2 = Entry(root, font=text, show='*')
    entry1.configure(width=25)
    entry2.configure(width=25)
    signinscreen.create_window(300, 380, window=entry1)
    signinscreen.create_window(300, 450, window=entry2)
    
    submit = Button(text='Submit', command=lambda : db(entry1,entry2), bg='azure', fg='black', font=('century schoolbook', 11, 'bold'))
    submit.config(height=2, width=23)
    signinscreen.create_window(250, 540, window=submit)
    
#THE GAME 
def game():
    pygame.init()
    global bullet_state,score_value,status
    #screen
    screen= pygame.display.set_mode((1000,600))

    if status =='signin':
        signinscreen.pack_forget()        
    elif status=='signup':
        signupscreen.pack_forget()       
    elif status=='playagain':
        canvas5.pack_forget()

    #Title
    pygame.display.set_caption('Attack On Veges')
    icon=pygame.image.load('D://Shruti//shruti study//COMPUTERSCIENCE//12thProject_LocknLoad//chef.png')
    pygame.display.set_icon(icon)

    #Time
    time.sleep(2)

    #Background Image
    bg=pygame.image.load('D://Shruti//shruti study//COMPUTERSCIENCE//12thProject_LocknLoad//Background_farm_2.png')

    #Countdown
    def countdown_bg():
        screen= pygame.display.set_mode((1000,600))
        bg=pygame.image.load('D://Shruti//shruti study//COMPUTERSCIENCE//12thProject_LocknLoad//Background_farm_2.png')
        show_score(800,10)
        show_life(800,40)
    def countdown():
        countdown=True

    #Score
    score_value=0
    font=pygame.font.Font('freesansbold.ttf',32)
    textX=800
    textY=10
    def show_score(x,y):
            score=font.render('Score: '+str(score_value),True,(0,0,0))
            screen.blit(score,(x,y))

    #Life
    life_value=3
    life_font=pygame.font.Font('freesansbold.ttf',32)
    lifeX=800
    lifeY=40
    def show_life(x,y):
            life=life_font.render('Lives: '+str(life_value),True,(0,0,0))
            screen.blit(life,(x,y))
    #GAME OVER
    gameover_font=pygame.font.Font('freesansbold.ttf',64)
    def gameover_text():
        conn=mc.connect(host='localhost',user='root',password='Stark3.0',database='project')
        cur=conn.cursor(buffered=True)
        cur.execute("update aov set score={} where username='{}'".format(score_value,f))
        cur.execute('commit')
        conn.close()
        menuscreen()
        pygame.quit()
        sys.exit()
        
    #Player
    playerImg=pygame.image.load('D://Shruti//shruti study//COMPUTERSCIENCE//12thProject_LocknLoad//chef_3.png')
    playerX=100
    playerY=300
    playerX_change=0
    def player(x,y):
        screen.blit(playerImg,(x,y))
        
    #bullet
    bulletImg=pygame.image.load('D://Shruti//shruti study//COMPUTERSCIENCE//12thProject_LocknLoad//bullet.png')
    bulletX=100
    bulletY=100
    bulletX_change=8
    bullet_state='ready'
    def fire_bullet(x,y):
        global bullet_state
        bullet_state='fire'
        screen.blit(bulletImg,(x+150,y+55))
        
    def isCollision(enemyX,bulletX):
        distance=(enemyX-bulletX)
        if distance < 27 and distance > -27:
            return True
        else:
            return False

    #Enemy
    enemyX_change=-7
    enemyX=800
    enemyY=335
    enemy_width=127
    enemy_height=150
    enemy_no=random.randrange(0,3)

    def enemy(x,y,i):
        if enemy_no==0:
            enemyImg=pygame.image.load(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Vege_image - Copy\radish.png')
        elif enemy_no==1:
            enemyImg=pygame.image.load(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Vege_image - Copy\broccoli.png')
        elif enemy_no==2:
            enemyImg=pygame.image.load(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Vege_image - Copy\capsicum.png')
        elif enemy_no==3:
            enemyImg=pygame.image.load(r'D:\Shruti\shruti study\COMPUTERSCIENCE\12thProject_LocknLoad\Vege_image - Copy\chilli.png')
        screen.blit(enemyImg,(x,y))

    def lives(life):
        if enemyX<=(playerX-80):
            return True
        else:
            return False

    #Game Loop
    running=True
    while running: 
        screen.fill((0,0,128)) 
        #bg img
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            #moving player
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    playerX_change=-2
                if event.key==pygame.K_RIGHT:
                    playerX_change=2
                if event.key==pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bulletX=playerX
                        bulletY=playerY
                        fire_bullet(bulletX,bulletY)
            if event.type==pygame.KEYUP:
                  if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_SPACE:
                      playerX_change=0
        
        #Boundry of game
        
        #player
        playerX += playerX_change
        if playerX <=0:
            playerX =0
        elif playerX>=710:
            playerX =710
        #enemy
        enemyX+=enemyX_change
        
        L=lives(life_value)
        #GAME OVER
        if L==True:
            life_value-=1
            enemy_no=random.randrange(0,3)
            enemy(enemyX,enemyY,enemy_no)
            enemyX=800
            enemyY=335
            if life_value==0:
                gameover_text()
                running=False
        #collision
        collision=isCollision(enemyX,bulletX)
        if collision==True:
            bulletX=0
            bullet_state='ready'
            score_value+=1
            enemy_no=random.randrange(0,3)
            enemy(enemyX,enemyY,enemy_no)
            enemyX=800
            enemyY=335
        
        enemy(enemyX,enemyY,enemy_no)
        
        #bullet movement
        if bulletX>=900:
            bulletX=100
            bullet_state= 'ready'
        if bullet_state == 'fire':
            
            fire_bullet(bulletX,bulletY)
            bulletX += bulletX_change
        player(playerX,playerY)
        show_score(textX,textY)
        show_life(lifeX,lifeY)
        pygame.display.update()

    
#Functions for navigating between screens
def fsrfromcanvas2():
    canvas2.pack_forget()
    firstscreen()

def fsrfromrules():
    canvas3.pack_forget()
    firstscreen()
    
def psrfromrules():
    canvas3.pack_forget()
    playscreen()
    
def fsrfromlb():
    canvas5.pack_forget()
    firstscreen()

def fsrfromsignup():
    signupscreen.pack_forget()
    firstscreen()

def fsrfromsignin():
    signinscreen.pack_forget()
    firstscreen()
def signupfromsignin():
    signinscreen.pack_forget()
    signup_entry()

def fsrfromleaderboard():
    canvas5.pack_forget()
    firstscreen()
def leaderboardfroml2():
    canvas5.pack_forget()
    leaderboard2()
    
def leaderboardfromfsr():
    global origin
    canvas1.pack_forget()
    origin='front'
    leaderboard()

def quitgame():
    if mb.askyesno('Quit Game','Do you really want to quit the game?'):
        root.destroy()
        pygame.quit()
        quit()
    
firstscreen()
