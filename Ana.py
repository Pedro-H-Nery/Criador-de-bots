import ReconhecimentoVoz as rv
import pyautogui
import time
from pynput import mouse, keyboard
import win32api

class Ana:
    def __init__(self):
        self.nome="Ana"
        self.movimentos=[]

    def criarBot(self):
        win32api.MessageBox(0, 'Clique nos lugares que deseja que o bot clique.\nNo final clique na tecla ESC para encerrar a aprendizagemo.', 'Aprendizagem do bot', 0x00001000)
        self.movimentos=[]
        self.mouse_listener = mouse.Listener(on_click=self.clicarMouse, on_scroll=self.scrollMouse)
        self.keyboard_Listener=keyboard.Listener(on_press=self.pressionarTeclado, on_release=self.soltarTecla)
        self.mouse_listener.start()
        self.keyboard_Listener.start()
        self.mouse_listener.join()
        self.keyboard_Listener.join()

    def clicarMouse(self, x, y, button, pressed):
        if(pressed):
            self.movimentos.append(f'Clique({x},{y})')

    def scrollMouse(self,x, y, dx, dy):
        self.movimentos.append(f'Scroll({x},{y},{dx},{dy})')

    def pressionarTeclado(self, key):
        self.movimentos.append(f'Tecla({key})')

    def soltarTecla(self,key):
        if key == keyboard.Key.esc:
            self.mouse_listener.stop()
            self.keyboard_Listener.stop()
            self.ativarBot(self.movimentos)
    
    def criarComando(self):
        pass

    def reconhecimentoVoz(self):
        pass

    def ativarBot(self, movimentos):
        win32api.MessageBox(0, 'Agora o bot repetirá os cliques.', 'Iniciação do bot', 0x00001000)
        for mov in movimentos:
            if(mov[0]=="C"):
                time.sleep(2)
                pyautogui.click(int(mov[7:mov.find(",")]),int(mov[mov.find(",")+1:mov.find(")")]))
            elif(mov[0]=="T"):
                time.sleep(2)
                pyautogui.press(mov[7:mov.find(")")-1])
        time.sleep(1)
        win32api.MessageBox(0, 'O bot terminou sua tarefa.', 'Finalização do bot', 0x00001000)

if __name__ == '__main__':
    teste = Ana()
    teste.criarBot()