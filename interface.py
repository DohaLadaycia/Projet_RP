import time
import pygame
import sys
import os
class Interface:
    pygame.display.init()
    pygame.display.set_caption('*Mancala*')
    screen=pygame.display.set_mode((1074,597))
    def menu(self): 
      img_p=pygame.image.load('menu-01.png').convert()
      fond = pygame.transform.scale(img_p, (1074,597))
      self.screen.blit(fond,(0,0))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONUP:
          pos=pygame.mouse.get_pos()
          posse1=pos
          print(posse1)
          if posse1[1]>285 and posse1[1]<=350:
            return 1
          elif  posse1[1]>380 and posse1[1]<=430:
            return -1
    def draw(self,dict):
       img_p=pygame.image.load('board-01.png').convert()
       fond = pygame.transform.scale(img_p, (1074,597))
       self.screen.blit(fond,(0,0))
       img_0p=pygame.image.load('0.png').convert_alpha()
       img_1p=pygame.image.load('1.png').convert_alpha()
       img_2p=pygame.image.load('2.png').convert_alpha()
       img_3p=pygame.image.load('3.png').convert_alpha()
       img_4p=pygame.image.load('4.png').convert_alpha()
       img_5p=pygame.image.load('5.png').convert_alpha()
       img_6p=pygame.image.load('6.png').convert_alpha()
       img_7p=pygame.image.load('7.png').convert_alpha()
       img_8p=pygame.image.load('8.png').convert_alpha()
       img_9p=pygame.image.load('9.png').convert_alpha()
       img_10p=pygame.image.load('10.png').convert_alpha()
       img_11p=pygame.image.load('11.png').convert_alpha()
       img_12p=pygame.image.load('12.png').convert_alpha()
       img_13p=pygame.image.load('13.png').convert_alpha()
       img_14p=pygame.image.load('14.png').convert_alpha()
       img_15p=pygame.image.load('15.png').convert_alpha()
       img_16p=pygame.image.load('16.png').convert_alpha()
       img_17p=pygame.image.load('17.png').convert_alpha()
       img_18p=pygame.image.load('18.png').convert_alpha()
       img_19p=pygame.image.load('19.png').convert_alpha()
       img_20p=pygame.image.load('20.png').convert_alpha()
       img_21p=pygame.image.load('21.png').convert_alpha()
       img_22p=pygame.image.load('22.png').convert_alpha()
       img_23p=pygame.image.load('23.png').convert_alpha()
       img_24p=pygame.image.load('24.png').convert_alpha()
       img_25p=pygame.image.load('25.png').convert_alpha()
       img_26p=pygame.image.load('26.png').convert_alpha()
       img_27p=pygame.image.load('27.png').convert_alpha()
       img_28p=pygame.image.load('28.png').convert_alpha()
       img_29p=pygame.image.load('29.png').convert_alpha()
       img_30p=pygame.image.load('30.png').convert_alpha()
       img_31p=pygame.image.load('31.png').convert_alpha()
       img_32p=pygame.image.load('32.png').convert_alpha()
       img_33p=pygame.image.load('33.png').convert_alpha()
       img_34p=pygame.image.load('34.png').convert_alpha()
       img_35p=pygame.image.load('35.png').convert_alpha()
       img_36p=pygame.image.load('36.png').convert_alpha()
       img_37p=pygame.image.load('37.png').convert_alpha()
       img_38p=pygame.image.load('38.png').convert_alpha()
       img_39p=pygame.image.load('39.png').convert_alpha()
       img_40p=pygame.image.load('40.png').convert_alpha()
       img_41p=pygame.image.load('41.png').convert_alpha()
       img_42p=pygame.image.load('42.png').convert_alpha()
       img_43p=pygame.image.load('43.png').convert_alpha()
       img_44p=pygame.image.load('44.png').convert_alpha()
       img_45p=pygame.image.load('45.png').convert_alpha()
       img_46p=pygame.image.load('46.png').convert_alpha()
       img_47p=pygame.image.load('47.png').convert_alpha()
       img_48p=pygame.image.load('48.png').convert_alpha()
       img_p=pygame.image.load('1_p.png').convert_alpha()
       player1=pygame.image.load('player1.png').convert_alpha()
       player2=pygame.image.load('player2.png').convert_alpha()
       img_p = pygame.transform.scale(img_p, (25,25))
       images={0:img_0p,1:img_1p,2:img_2p,3:img_3p,4:img_4p,5:img_5p,6:img_6p,7:img_7p,8:img_8p,9:img_9p,10:img_10p,11:img_11p,12:img_12p,13:img_13p,14:img_14p,15:img_15p,16:img_16p,17:img_17p,18:img_18p,19:img_19p,20:img_20p,21:img_21p,22:img_22p,23:img_23p,24:img_24p,25:img_25p,26:img_26p,27:img_27p,28:img_28p,29:img_29p,30:img_30p,31:img_31p,32:img_32p,33:img_33p,34:img_34p,35:img_35p,36:img_36p,37:img_37p,38:img_38p,39:img_39p,40:img_40p,41:img_41p,42:img_42p,43:img_43p,44:img_44p,45:img_45p,46:img_46p,47:img_47p,48:img_48p}
       d={'A':(145,220),'B':(280,220),'C':(420,220),'D':(550,220),'E':(690,220),'F':(820,220),'M1':(960,250),'G':(145,90),'H':(280,90),'I':(420,90),'J':(550,90),'K':(690,90),'L':(820,90),'M2':(50,250)}
       for key in d:
          for i in range(1,dict[key]+1):
            if i==9:
              self.screen.blit(img_p,(d[key][0]+(int(i/4)*25),d[key][1]-(int(i/4)*25)))
            if i==8:
              self.screen.blit(img_p,(d[key][0]+(i/8*25),d[key][1]-(i/4*25)))
            if i==7:
              self.screen.blit(img_p,(d[key][0],d[key][1]-(int(i/3)*25)))
            if i==6:
              self.screen.blit(img_p,(d[key][0]+(i/3*25),d[key][1]-(i/6*25)))
            if i==5:
              self.screen.blit(img_p,(d[key][0]+(int(i/2)*25),d[key][1])) 
            if i==4:
              self.screen.blit(img_p,(d[key][0]+(i/4*25),d[key][1]-(i/4*25)))
            if i==3:
                self.screen.blit(img_p,(d[key][0],d[key][1]-(i/3*25)))
            if i==2:
                self.screen.blit(img_p,(d[key][0]+(i/2*25),d[key][1]))    
            if i==1:
                self.screen.blit(img_p,(d[key][0],d[key][1]))   
            if i>9 :
                self.screen.blit(img_p,(d[key][0]+(i/(i-2)*25),d[key][1]-(i/(i-2)*25)))
          self.screen.blit(pygame.transform.scale(images[dict[key]], (50,50)),(d[key][0]+25,d[key][1]+30))
          self.screen.blit(pygame.transform.scale(player2,(150,50)),(10,20) )
          self.screen.blit(pygame.transform.scale(player1,(150,50)),(920,20))
       pygame.display.flip()
       time.sleep(1)
    def human(self):
      d={'A':(145,220),'B':(280,220),'C':(420,220),'D':(550,220),'E':(690,220),'F':(820,220),'M1':(960,250),'G':(145,90),'H':(280,90),'I':(420,90),'J':(550,90),'K':(690,90),'L':(820,90),'M2':(50,250)}
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
          pos=pygame.mouse.get_pos()
          posse=pos
          print(posse)
          if (posse[0]>=100 and posse[0]<=240 and posse[1]>=200 and posse[1]<=280):
            return 'A'
          elif(posse[0]>=100 and posse[0]<=240 and posse[1]>=85 and posse[1]<=170):
            return'G'
          if (posse[0]>=250 and posse[0]<=380 and posse[1]>=150 and posse[1]<=280):
            return 'B'
          elif(posse[0]>=250 and posse[0]<=380 and posse[1]>=85 and posse[1]<=170):
            return 'H'
          if (posse[0]>=390 and posse[0]<=520 and posse[1]>=150 and posse[1]<=280):
            return 'C'
          elif(posse[0]>=390 and posse[0]<=520 and posse[1]>=85 and posse[1]<=170):
            return'I'
          if (posse[0]>=530 and posse[0]<=660 and posse[1]>=150 and posse[1]<=280):
            return 'D'
          elif(posse[0]>=530 and posse[0]<=660 and posse[1]>=85 and posse[1]<=170):
            return 'J'
          if (posse[0]>=670 and posse[0]<=790 and posse[1]>=150 and posse[1]<=280):
            return 'E'
          elif(posse[0]>=670 and posse[0]<=790 and posse[1]>=85 and posse[1]<=170):
            return 'K'
          if (posse[0]>=800 and posse[0]<=920 and posse[1]>=150 and posse[1]<=280):
            return 'F'
          elif(posse[0]>=800 and posse[0]<=920 and posse[1]>=85 and posse[1]<=170):
            return 'L'
    def win(self,winner):
      if winner==1:
        img_p=pygame.image.load('player1_won-01.png').convert()
        fond = pygame.transform.scale(img_p, (1074,597))
        self.screen.blit(fond,(0,0))
      else:
        img_p=pygame.image.load('player2_won-01-01.png').convert()
        fond = pygame.transform.scale(img_p, (1074,597))
        self.screen.blit(fond,(0,0))
      pygame.display.flip()
