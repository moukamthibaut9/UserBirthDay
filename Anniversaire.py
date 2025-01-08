import pygame,sys,random

pygame.init()

(screen_w,screen_h)=(pygame.display.Info().current_w,pygame.display.Info().current_h)
ncx=135
ncy=70
dcx=screen_w//ncx
dcy=screen_h//ncy
window_w=ncx*dcx
window_h=ncy*dcy
surface=(window_w,window_h)
frame_sec=pygame.time.Clock()

# Parametres de personnalisation du programme
user_name1 = "BELINGA" # Premier nom de l'utilisateur conserné
user_name2 = "TRAORE" # Deuxieme nom de l'utilisateur conserné
user_name3 = "Jislain" # Troisieme nom de l'utilisateur conserné
user_name1_offset_value = 17.5*dcx # Valeur du décalage par rapport à la gauche du premier nom 
user_name2_offset_value = 19*dcx # Valeur du décalage par rapport à la gauche du deuxieme nom 
user_name3_offset_value = 17.5*dcx # Valeur du décalage par rapport à la gauche du troisieme nom 
window_title = f"JOURNEE SPECIALE {user_name1}" # Titre de la fenetre
# Fin parametrage


window=pygame.display.set_mode(surface,pygame.RESIZABLE)
pygame.display.set_caption(window_title)

def message_screen_printing(font,message,rectangle,couleur):
    if font==1:
        font=pygame.font.SysFont("arial",2*dcx,False)
    elif font==2:
        font=pygame.font.SysFont("calibri",5*dcx,False,True)
    elif font==3:
        font=pygame.font.SysFont("freemono",9*dcx,True,False)
    elif font==4:
        font=pygame.font.SysFont("algerian",14*dcx,True,False)
    elif font==5:
        font=pygame.font.SysFont("liberation serif",20*dcx,True,False)
    message=font.render(message,True,couleur)
    window.blit(message,rectangle)
def grille():
    for i in range(0,ncx):
        for j in range(0,ncy):
            rect=pygame.Rect(i*dcx,j*dcy,dcx,dcy)
            pygame.draw.rect(window,(192,192,192),rect,1)

class Happy_Birthday:  
    def __init__(self):
        self.mots_anniversaire=[
            ["J","O","Y","E","U","X"," ","A","N","N","I","V","E","R","S","A","I","R","E"],
            ["H","A","P","P","Y"," ","B","I","R","T","H","D","A","Y"],
            ["H","E","R","Z","L","I","C","H","E","N"," ","G","L","U","C","K","W","U","N","S","C","H"]
        ]
        self.image=pygame.image.load("gateau.png")
        self.rect_part1=pygame.Rect(37*dcx,-60*dcy,30*dcx,60*dcy)
        self.rect_part2=pygame.Rect(67*dcx,70*dcy,30*dcx,60*dcy)
        self.direction=0
        # Defini si la premiere partie de l'animation est terminée ou pas (Actuellement à pas terminé)
        self.first_part_ended=False 
    def icon_moving_printing(self):
        rect_img1=pygame.Rect(0,0,112,224)
        image1=self.image.subsurface(rect_img1)
        image1=pygame.transform.scale(image1,(30*dcx,60*dcy))
        window.blit(image1,self.rect_part1)
        self.rect_part1.y+=self.direction
        rect_img2=pygame.Rect(112,0,112,224)
        image2=self.image.subsurface(rect_img2)
        image2=pygame.transform.scale(image2,(30*dcx,60*dcy))
        window.blit(image2,self.rect_part2)
        self.rect_part2.y-=self.direction
        if self.rect_part1.y==self.rect_part2.y:self.direction=0
    def anniversaire(self):
        letter_width=7*dcx
        letter_height=8*dcy
        for i in range(0,len(self.mots_anniversaire)):
            indexes_mots_anniversaire=[]
            for k in range(0,len(self.mots_anniversaire[i])):
                # Pendant la premiere partie de l'animation, on verifie si l'utilisateur
                # clique sur le bouton de fermeture de la fenetre pour arreter le programme
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                #########################################################################
                j=random.randint(0,len(self.mots_anniversaire[i])-1)
                if j in indexes_mots_anniversaire:
                    while j in indexes_mots_anniversaire:
                        j=random.randint(0,len(self.mots_anniversaire[i])-1)
                indexes_mots_anniversaire.append(j)
                if i==0: 
                    message_screen_printing(
                        3,
                        self.mots_anniversaire[i][j],
                        (letter_width*(j+0.2),1*dcy,letter_width,letter_height),
                        (random.choice([0,255]),random.choice([0,255]),random.choice([0,255]))
                    )
                elif i==1:
                    message_screen_printing(
                        3,
                        self.mots_anniversaire[i][j],
                        (letter_width*(j+3),24*dcy,letter_width,letter_height),
                        (random.choice([0,255]),random.choice([0,255]),random.choice([0,255]))
                    )
                else:
                    letter_width=6*dcx
                    message_screen_printing(
                        3,
                        self.mots_anniversaire[i][j],
                        (letter_width*(j+0.2),46*dcy,letter_width, letter_height),
                        (random.choice([0,255]),random.choice([0,255]),random.choice([0,255]))
                    )
                pygame.time.delay(500)
                pygame.display.flip()
            if i==0:
                message_screen_printing(5,user_name1,(user_name1_offset_value,6*dcy,50*dcx,15*dcy),(0,255,0))
            elif i==1:
                message_screen_printing(5,user_name2,(user_name2_offset_value,28*dcy,50*dcx,15*dcy),(255,0,0))
            else:
                message_screen_printing(5,user_name3,(user_name3_offset_value,51*dcy,50*dcx,15*dcy),(255,255,0))
            pygame.display.flip()
        self.first_part_ended=True
        pygame.time.delay(1000)
            

birthday_song=pygame.mixer.Sound("birthday_son.mp3")
background_image=pygame.transform.scale(pygame.image.load('fond3.jpeg'),(window_w,window_h))
birthday_song.play()

pygame.time.set_timer(pygame.USEREVENT,200)
running = True

happy_birthday=Happy_Birthday()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.USEREVENT:
            if happy_birthday.rect_part1.bottom==happy_birthday.rect_part2.bottom:
                happy_birthday.direction=0
            else: 
                happy_birthday.direction=5
            
    window.blit(background_image,(0,0,window_w,window_h))
    #window.fill(pygame.Color((112,112,112)))  
    #grille()    
    if not happy_birthday.first_part_ended: # Pour la premiere partie de l'animation
        happy_birthday.anniversaire()
    else: # Pour la seconde partie de l'animation
        message_screen_printing(3,"MORE SUCCESS",(35*dcx,0.5*dcy,window_w,15*dcy),(0,0,255))
        message_screen_printing(3,"IN YOUR LIFE",(35*dcx,61.5*dcy,window_w,15*dcy),(0,0,255))
        happy_birthday.icon_moving_printing()
    pygame.display.flip()
    pygame.display.update()
    frame_sec.tick(60)
pygame.quit()
sys.exit()
