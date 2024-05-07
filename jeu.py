# Nuit du c0de 2023

import pyxel
import random
import time

class Alian:
    def __init__(self,pos):
        self.pos = pos
        self.affiche = False
        self.balle_pos = [0,0] 
    
    def affc(self):
        try:
            self.pos = self.pos
            self.pos[0] = (self.pos[0] + random.randint(-1,1)) % 128
        except:
            
            self.pos = [random.randint(0,128),random.randint(1,50)]
        
        pyxel.blt(self.pos[0],self.pos[1] ,0,16,0,8,7)
        
    
    
        
            
class Space:
    def __init__(self):
        pyxel.init(128,128, title="NDC 2023")
        pyxel.load('1.pyxres')
        pyxel.run(self.update,self.draw)
        self.liste_ennemis = [Alian() for k in range(10)]
        self.pyxelcnul = True
        self.w = 0
    
    def affiche_ennemi(self):
        try:
            self.pyxelcnul = self.pyxelcnul
        except: 
            self.pyxelcnul = True
        
        if self.pyxelcnul:
            try:
                for k in self.liste_ennemis:
                    k.affc()
            except:
                self.liste_ennemis = [Alian((random.randint(0,100),random.randint(0,50))) for k in range(8)]
            
            for k in self.liste_ennemis:
                k.affc()
                
            
            for k in self.liste_ennemis:
                pyxel.blt(k.balle_pos[0],k.balle_pos[1], 0,24,33,1,1)
                
                k.balle_pos[0] = k.pos[0]
                if k.balle_pos[1] < k.pos[1]:
                   k.balle_pos[1] = k.pos[1]
                k.balle_pos[1] = ((k.balle_pos[1] + 1)%(128))
                tv = 16
                if (
                    k.balle_pos[0] <= (pyxel.mouse_x+tv)%(128) and k.balle_pos[0] >= (pyxel.mouse_x)%(128) and
                    k.balle_pos[1] <= (pyxel.mouse_y+tv)%(128) and k.balle_pos[1] >= (pyxel.mouse_y)%(128)
                    ):
                    self.pyxelcnul = False
                
                if (
                    k.pos[0] <= (pyxel.mouse_x+tv)%(128) and k.pos[0] >= (pyxel.mouse_x)%(128) and
                    k.pos[1] <= (pyxel.mouse_y+tv)%(128) and k.pos[1] >= (pyxel.mouse_y)%(128)
                    ):
                    self.pyxelcnul = False
            
        else:
            pyxel.text(50,64,"Game over !",7)
            
            
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(pyxel.mouse_x%(128-15),pyxel.mouse_y%(128-15),0,0,32,16,16)
        try:
            self.w = self.w
            if self.pyxelcnul:
                self.w += 1
            pyxel.text(1,1,str(self.w) + " pts",7)
        except:
            self.w = 0
        
            
        try:
            self.affiche_ennemi()
        except:
            pass
        
Space()