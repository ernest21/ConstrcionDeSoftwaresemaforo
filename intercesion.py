import threading
import semaforo
import pygame

class intercession(pygame.sprite.Sprite):
  """docstring for intercession"""
  def __init__(self, x,y,sizeX, sizeY):
    super(intercession, self).__init__()

    self.x = x
    self.y = y
    self.rect=pygame.Rect(x, y, sizeX, sizeY)
    eventoX = threading.Event()
    eventoY = threading.Event()
    self.semaforo = semaforo.Semaforo(eventoX, eventoY)
    self.semaforo.iniciar()
