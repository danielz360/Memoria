import pygame
import os.path
from MayCBoton import MayCBoton
from MayCLabel import MayCLabel

class MayCCuadroMs(object):
    def __init__(self,p_Interface_Padre,p_Mensaje,p_Posicion,p_Dir_Iconos):
        #Inicializo SubMódulos de Pygame
        pygame.init()
        #Propiedades
        self.Interface_Padre=p_Interface_Padre
        self.Tamano=(100,100)
        self.Mensaje=p_Mensaje
        self.Posicion_Actual=p_Posicion
        self.Interface=pygame.Surface(self.Tamano,0,32)
        self.Interface.fill((255,255,255))
        self.Dir_Iconos=p_Dir_Iconos    
        #Creacion Items 
        self.SubMenus=[]
        #Boton en Juego (Que esta Interactuando con los eventos =>MOUSEMOTION)
        self.Boton_NJuego=None
        self.GUI()

    def GUI(self):
        self.lblMensaje=MayCLabel(self.Interface,self.Mensaje,'lblM',(10,10),"Blanco")
        self.lblMensaje.Insertar()
        self.btnSi = MayCBoton(self.Interface,"btnSi","Si.png",self.Dir_Iconos,p_Coordenadas=(10,40),p_Tamano=(30,30))
        self.btnSi.Insertar()
        self.btnNo = MayCBoton(self.Interface,"btnNo","No.png",self.Dir_Iconos,p_Coordenadas=(10,40),p_Tamano=(30,30))
        self.btnNo.Insertar()
        
                                
    def InsertarInterface(self):
        self.Interface_Padre.blit(self.Interface,self.Posicion_Actual)                    
        #self.InsertarMensajesAyuda()        