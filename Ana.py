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
        win32api.MessageBox(0, 'Clique nos lugares que deseja que o bot clique.\nNo final clique no canto inferior direito para encerrar a aprendizagem.', 'Aprendizagem do bot', 0x00001000)
        self.movimentos=[]
        with mouse.Listener(on_click=self.clicarMouse) as listener:
            listener.join()

        listener = mouse.Listener(on_click=self.clicarMouse)
        listener.start()
        listener.stop()
        self.ativarBot(self.movimentos)

    def clicarMouse(self, x, y, button, pressed):
        if(x>1200 and y>600):
            return False
        if(pressed):
            self.movimentos.append(f'Clique({x},{y})')
    
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
        time.sleep(1)
        win32api.MessageBox(0, 'O bot terminou sua tarefa.', 'Finalização do bot', 0x00001000)

if __name__ == '__main__':
    teste = Ana()
    teste.criarBot()