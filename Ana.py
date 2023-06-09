import ReconhecimentoVoz as rv
import pyautogui
import time
from pynput import mouse, keyboard
from pynput.mouse import Controller
import win32api
import win32con
from tkinter import filedialog

class Ana:
    def __init__(self):
        self.nome="Ana"
        self.time = 1
        self.movimentos=[]

    def criarBot(self):
        resposta = win32api.MessageBox(0, 'Você deseja usar comandos salvos em um arquivo?', 'EscolhaAbrirArquivo', win32con.MB_YESNO)
        if resposta == win32con.IDYES:
            arquivoComandos = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
            try:
                with open(arquivoComandos, 'r') as arquivo:
                    conteudo = arquivo.read()
                    conteudo = conteudo.split('\n')
                    conteudo.pop()
                    self.movimentos = conteudo
                    win32api.MessageBox(0, 'Aprendizado carregado com sucesso.', 'Salvar aprendizado', 0x00001000)
                    self.ativarBot(self.movimentos)
            except FileNotFoundError:
                print(f'O arquivo "{arquivoComandos}" não foi encontrado.')
            except IOError:
                print(f'Ocorreu um erro ao abrir o arquivo "{arquivoComandos}".')
        else:
            win32api.MessageBox(0, 'Clique nos lugares que deseja que o bot clique.\nNo final clique na tecla ESC para encerrar a aprendizagemo.', 'Aprendizagem do bot', 0x00001000)
            self.mouse_listener = mouse.Listener(on_click=self.clicarMouse, on_scroll=self.scrollMouse)
            self.keyboard_Listener=keyboard.Listener(on_press=self.pressionarTeclado, on_release=self.soltarTecla)
            self.mouse_listener.start()
            self.keyboard_Listener.start()
            self.mouse_listener.join()
            self.keyboard_Listener.join()

    def clicarMouse(self, x, y, button, pressed):
        if(pressed):
            button=f'{button}'
            self.movimentos.append(f'Clique(x={x},y={y},b={button[button.find(".")+1:]})')

    def scrollMouse(self,x, y, dx, dy):
        if(len(self.movimentos)==0):
            self.movimentos.append(f'Scroll(x={x},y={y},d={dy},n=1)')
            return
        if(self.movimentos[len(self.movimentos)-1].find(f'Scroll(x={x},y={y},d={dy}')==0):
            ultimaPosicao=self.movimentos[len(self.movimentos)-1]
            numero = int(ultimaPosicao[ultimaPosicao.find("n")+2:ultimaPosicao.find(")")])
            texto = f'Scroll(x={x},y={y},d={dy},n={numero+1})'
            self.movimentos[len(self.movimentos)-1]=texto
        else:
            self.movimentos.append(f'Scroll(x={x},y={y},d={dy},n=1)')

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
        conteudoArquivo=""
        for mov in movimentos:
            if(mov=="Tecla(Key.esc)"):
                break
            conteudoArquivo+=mov+"\n"
            if(mov[0]=="C"):
                time.sleep(self.time)
                if(mov[mov.find("b")+2:mov.find(")")]=="left"):
                    pyautogui.leftClick(int(mov[mov.find("x")+2:mov.find(",")]),int(mov[mov.find("y")+2:mov.find("b")-1]))
                elif(mov[mov.find("b")+2:mov.find(")")]=="right"):
                    pyautogui.rightClick(int(mov[mov.find("x")+2:mov.find(",")]),int(mov[mov.find("y")+2:mov.find("b")-1]))
                elif(mov[mov.find("b")+2:mov.find(")")]=="middle"):
                    pyautogui.middleClick(int(mov[mov.find("x")+2:mov.find(",")]),int(mov[mov.find("y")+2:mov.find("b")-1]))
            elif(mov[0]=="T"):
                time.sleep(self.time)
                if('Key.' in mov):
                    pyautogui.press(mov[mov.find(".")+1:mov.find(")")])
                else:
                    pyautogui.press(mov[7:mov.find(")")-1])
            elif(mov[0]=="S"):
                time.sleep(self.time)
                control = Controller()
                x=int(mov[mov.find("x")+2:mov.find("y")-1])
                y=int(mov[mov.find("y")+2:mov.find("d")-1])
                pyautogui.moveTo(x,y)
                d=int(mov[mov.find("d")+2:mov.find("n")-1])
                n=int(mov[mov.find("n")+2:mov.find(")")])
                control.scroll(0,d*n)
        time.sleep(self.time/2)
        win32api.MessageBox(0, 'O bot terminou sua tarefa.', 'Finalização do bot', 0x00001000)
        resposta = win32api.MessageBox(0, 'Você deseja salvar o aprendizado do bot em arquivo?', 'EscolhaSalvarArquivo', win32con.MB_YESNO)
        if resposta == win32con.IDYES:
            arquivo = open('Resultado.txt', 'w', encoding="utf8")
            arquivo.write(conteudoArquivo)
            arquivo.close()
            win32api.MessageBox(0, 'Aprendizado salvo no arquivo \"Resultado.txt\".', 'Salvar aprendizado', 0x00001000)
        
if __name__ == '__main__':
    teste = Ana()
    teste.criarBot()
