import pyautogui
import pyperclip
from typing import List
import time
import random

class Roubo:
    def __init__(self, nome: str, estamina: int, poderDeRoubo: int, recompensa: int):
        self.__nome = nome
        self.__estamina = estamina
        self.__poderDeRoubo = poderDeRoubo
        self.__recompensa = recompensa

    def __str__(self) -> str:
        nome = f"Nome: {self.__nome}"
        estamina = f"Estamina: {self.__estamina}"
        poderDeRoubo = f"Poder de Roubo: {self.__poderDeRoubo}"
        recompensa = f"Recompensa: {self.__recompensa}"
        return  nome + "\n" + estamina + "\n" + poderDeRoubo + "\n" + recompensa

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def estamina(self):
        return self.__estamina
    
    @estamina.setter
    def estamina(self, estamina: int):
        self.__estamina = estamina

    @property
    def poderDeRoubo(self):
        return self.__poderDeRoubo
    
    @poderDeRoubo.setter
    def poderDeRoubo(self, poderDeRoubo: int):
        self.__poderDeRoubo = poderDeRoubo

    @property
    def recompensa(self):
        return self.__recompensa
    
    @recompensa.setter
    def recompensa(self, recompensa: int):
        self.__recompensa = recompensa

class Coordenadas:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

# Menus
coordMenuRoubar = Coordenadas(-1570, 415)           # 1° Menu
coordMenuVidaNoturna = Coordenadas(-1450, 415)      # 2° Menu
coordMenuHospital = Coordenadas(-1330, 415)         # 3° Menu
coordMenuMercadoNegro = Coordenadas(-1210, 415)     # 4° Menu

# Títulos
coordTituloPadrao = Coordenadas(-1600, 490)
coordTituloFestasRave = Coordenadas(x=-1590, y=370)


# Mansão ou Festas
coordsMansaoOuFestas: List[Coordenadas] = []
coordsMansaoOuFestas.append(Coordenadas(-1575, 810))
coordsMansaoOuFestas.append(Coordenadas(-1250, 810))
coordsMansaoOuFestas.append(Coordenadas(-930, 810))
coordsMansaoOuFestas.append(Coordenadas(-600, 810))
coordsMansaoOuFestas.append(Coordenadas(-1575, 900))
coordsMansaoOuFestas.append(Coordenadas(-1250, 900))
coordsMansaoOuFestas.append(Coordenadas(-930, 900))
coordsMansaoOuFestas.append(Coordenadas(-600, 900))

# Poder De Roubo Solo
coordPoderDeRouboSoloInicio = Coordenadas(-890, 190)
coordPoderDeRouboSoloFim = Coordenadas(-845, 190)

# Seleção Roubo
coordSelecaoRoubo = Coordenadas(-1300, 655)

# Quantidade de Tickets
coordQuantidadeTickets = Coordenadas(-1367, 264)

# Botões
coordBotaoRoubar: Coordenadas = Coordenadas(-1290, 745)

coordBotaoReabastecer: Coordenadas = Coordenadas(-1510, 570)

coordsBotaoEntrarVidaNoturna: List[Coordenadas] = []
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-1460, 840))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-1130, 840))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-800, 840))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-480, 840))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-1460, 935))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-1130, 935))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-800, 935))
coordsBotaoEntrarVidaNoturna.append(Coordenadas(-480, 935))

coordBotaoComprarDroga: Coordenadas = Coordenadas(-970, 760)

coordsBotaoSairFestaRave: List[Coordenadas] = []
coordsBotaoSairFestaRave.append(Coordenadas(-1400, 845))
coordsBotaoSairFestaRave.append(Coordenadas(-970, 845))
coordsBotaoSairFestaRave.append(Coordenadas(-540, 845))

coordBotaoDetox = Coordenadas(-1450, 600)

coordBotaoArmas = Coordenadas(x=-1225, y=545)

# Roubos
roubos: List[Roubo] = list()
roubos.append(Roubo("Loja de 1,99", 5, 2, 5))                   # 0
roubos.append(Roubo("Velhinha na rua", 10, 8, 40))              # 1
roubos.append(Roubo("R\u00e1dio de carro", 10, 16, 82))         # 2
roubos.append(Roubo("Taxi", 10, 40, 246))                       # 3
roubos.append(Roubo("Roubar uma casa", 10, 80, 615))            # 4
roubos.append(Roubo("Posto de gasolina", 10, 160, 1847))        # 5
roubos.append(Roubo("Tabacaria", 10, 400, 4102))                # 6
roubos.append(Roubo("Sequestro", 20, 720, 13840))               # 7
roubos.append(Roubo("Joalheria", 20, 1360, 25949))              # 8
roubos.append(Roubo("Banco Pequeno", 20, 2400, 51897))          # 9
roubos.append(Roubo("Moroccan Harbour", 50, 9000, 112500))      # 10
roubos.append(Roubo("Pharmacy", 50, 10000, 113750))             # 11
roubos.append(Roubo("Ambulance", 50, 11000, 116250))            # 12
roubos.append(Roubo("Local Dealer", 50, 25000, 412500))         # 13
roubos.append(Roubo("Drug Factory", 50, 18000, 562500))         # 14
roubos.append(Roubo("Rave Party", 50, 15000, 225000))           # 15
roubos.append(Roubo("Hardware Store", 50, 22000, 250000))       # 16
roubos.append(Roubo("Hospital", 50, 37000, 437500))             # 17
roubos.append(Roubo("Local Pusher", 50, 50000, 437500))         # 18
roubos.append(Roubo("Taliban Squad", 50, 25000, 437500))        # 19
roubos.append(Roubo("Latin Kings", 50, 30000, 437500))          # 20
roubos.append(Roubo("Jamaican Crew", 50, 15000, 437500))        # 21
roubos.append(Roubo("The Rednecks Crew", 50, 15000, 437500))    # 22
roubos.append(Roubo("Voodoo Priest", 50, 15000, 437500))        # 23

# Parâmetros do Jogo
nivelVicioAtual = 31
nivelVicioMax = 70
rouboSelecionado: Roubo = roubos[14]

roubo_apto = Roubo = roubos[14]

boolContinuarExecucao = True
boolReabastecimento = True
boolPrimeiroRouboComReabastecimento = True

# TESTADO
def verificarSeMouseMexeu(coordenada: Coordenadas):
    global boolContinuarExecucao

    time.sleep(0.1)
    mousePosicao = pyautogui.position()
    if (coordenada.x != mousePosicao.x or coordenada.y != mousePosicao.y):
        boolContinuarExecucao = False

# TESTADO
def timoutRequisicao(tempoMinimo:float, multiplicador: int = 1):
    min = tempoMinimo
    max = tempoMinimo + (0.2 * multiplicador)
    time.sleep(random.uniform(min, max))

# TESTADO
def isMenuCorreto(coordTitulo: Coordenadas, titulo: str):
    global boolContinuarExecucao
    
    time.sleep(0.3)
    pyautogui.click(coordTitulo.x, coordTitulo.y, clicks=3)
    pyautogui.hotkey("ctrl", "c")
    tituloCopiado = pyperclip.paste().strip()

    boolContinuarExecucao = titulo == tituloCopiado

# TESTADO
def getPoderDeRouboSolo():
    pyautogui.moveTo(coordPoderDeRouboSoloInicio.x, coordPoderDeRouboSoloInicio.y)
    
    verificarSeMouseMexeu(coordPoderDeRouboSoloInicio)
    if (not boolContinuarExecucao):
        return

    pyautogui.mouseDown(button='left')

    pyautogui.moveTo(coordPoderDeRouboSoloFim.x, coordPoderDeRouboSoloFim.y)
    
    verificarSeMouseMexeu(coordPoderDeRouboSoloFim)
    if (not boolContinuarExecucao):
        return

    pyautogui.hotkey("ctrl", "c")
    pyautogui.mouseUp(button='left')
    return int(pyperclip.paste())

# TESTADO
def selecionarRoubo(nomeRoubo: str):
    pyautogui.click(coordSelecaoRoubo.x, coordSelecaoRoubo.y)
    
    verificarSeMouseMexeu(coordSelecaoRoubo)
    if (not boolContinuarExecucao):
        return

    pyautogui.write(nomeRoubo)
    
    verificarSeMouseMexeu(coordSelecaoRoubo)
    if (not boolContinuarExecucao):
        return
    
    pyautogui.press("enter")

# TESTADO
def getPoderDeRouboNecessario(poderDeRouboSolo: int):
    return int((poderDeRouboSolo / 0.98))

# TESTADO
def getRouboApto(poderDeRouboNecessario: int):
    for roubo in reversed(roubos):
        if (roubo.poderDeRoubo <= poderDeRouboNecessario):
            return roubo

# TESTADO
def roubar():
    global rouboSelecionado

    timoutRequisicao(1)

    if (boolPrimeiroRouboComReabastecimento and boolReabastecimento):
        pyautogui.click(x=coordMenuRoubar.x, y=coordMenuRoubar.y)
        isMenuCorreto(coordTituloPadrao, "Roubar")
        
        if boolContinuarExecucao:
            verificarSeMouseMexeu(coordTituloPadrao)
    else:
        verificarSeMouseMexeu(coordBotaoReabastecer)

    if (not boolContinuarExecucao):
        return

    poderDeRouboSolo = getPoderDeRouboSolo()

    if (not boolContinuarExecucao):
        return

    poderDeRouboNecessario = getPoderDeRouboNecessario(poderDeRouboSolo)
    
    # rouboApto: Roubo = getRouboApto(poderDeRouboNecessario)

    if roubo_apto.nome != rouboSelecionado.nome:
        selecionarRoubo(roubo_apto.nome)

        if (not boolContinuarExecucao):
            return

        rouboSelecionado = roubo_apto
        time.sleep(0.3)

    timoutRequisicao(0)
    pyautogui.click(coordBotaoRoubar.x, coordBotaoRoubar.y)

    verificarSeMouseMexeu(coordBotaoRoubar)
    if (not boolContinuarExecucao):
        return

# TESTADO
def obterIndexFestaRave():
    global coordsMansaoOuFestas

    indexFestaRave = -1

    for idx, mansaoOuFesta in enumerate(coordsMansaoOuFestas):
        pyautogui.click(mansaoOuFesta.x, mansaoOuFesta.y, clicks=2)
        pyautogui.hotkey("ctrl", "c")
        tipoVidaNoturna = pyperclip.paste()
        
        verificarSeMouseMexeu(mansaoOuFesta)
        if (not boolContinuarExecucao):
            break

        if "festas".lower() in tipoVidaNoturna.lower():
            indexFestaRave = idx
            break

    return indexFestaRave

# TESTADO
def recuperarEstamina():
    timoutRequisicao(1)
    pyautogui.click(coordMenuVidaNoturna.x, coordMenuVidaNoturna.y)
    
    isMenuCorreto(coordTituloPadrao, "Vida Noturna")

    if boolContinuarExecucao:
        verificarSeMouseMexeu(coordTituloPadrao)

    if (not boolContinuarExecucao):
        return

    indexFestaRave = obterIndexFestaRave()

    if (not boolContinuarExecucao):
        return

    if indexFestaRave != -1:
        coordEntrar = coordsBotaoEntrarVidaNoturna[indexFestaRave]

        pyautogui.click(coordEntrar.x, coordEntrar.y)

        time.sleep(1)

        isMenuCorreto(coordTituloFestasRave, "Festas Rave")

        if boolContinuarExecucao:
            verificarSeMouseMexeu(coordTituloFestasRave)

        if (not boolContinuarExecucao):
            return

        pyautogui.click(coordBotaoComprarDroga.x, coordBotaoComprarDroga.y)

        time.sleep(1)

        verificarSeMouseMexeu(coordBotaoComprarDroga)
        if (not boolContinuarExecucao):
            return

        for botaoSair in coordsBotaoSairFestaRave:
            pyautogui.click(botaoSair.x, botaoSair.y)

            verificarSeMouseMexeu(botaoSair)
            if (not boolContinuarExecucao):
                return
    else:
        pyautogui.click(coordMenuRoubar.x, coordMenuRoubar.y)

        verificarSeMouseMexeu(coordMenuRoubar)
        if (not boolContinuarExecucao):
            return

        recuperarEstamina()

# TESTADO
def desintoxicar():
    timoutRequisicao(1)
    pyautogui.click(coordMenuHospital.x, coordMenuHospital.y)
    
    isMenuCorreto(coordTituloPadrao, "Hospital")

    if boolContinuarExecucao:
        verificarSeMouseMexeu(coordTituloPadrao)

    if (not boolContinuarExecucao):
        return
    
    pyautogui.hotkey("end")

    time.sleep(0.5)
    
    pyautogui.click(coordBotaoDetox.x, coordBotaoDetox.y)
    
    time.sleep(1)

    verificarSeMouseMexeu(coordBotaoDetox)
    if (not boolContinuarExecucao):
        return
    
    pyautogui.hotkey("home")

def reabastecer():
    timoutRequisicao(1)

    verificarSeMouseMexeu(coordBotaoRoubar)
    if (not boolContinuarExecucao):
        return

    pyautogui.click(x=coordBotaoReabastecer.x, y=coordBotaoReabastecer.y)

    verificarSeMouseMexeu(coordBotaoReabastecer)
    if (not boolContinuarExecucao):
        return

# TESTADO
def ordernarPorPoderDeRouboERecompensaEEstaminaENome():
    global roubos
    roubos = sorted(roubos, key=lambda roubo:(roubo.poderDeRoubo, roubo.recompensa, roubo.estamina, roubo.nome))

# TESTADO
def getQuantidadeTickets():
    pyautogui.click(coordQuantidadeTickets.x, coordQuantidadeTickets.y, clicks=3)
    pyautogui.hotkey("ctrl", "c")
    verificarSeMouseMexeu(coordQuantidadeTickets)
    return int(pyperclip.paste())

def contagemRegressivaInicio():
    print("iniciando em...")

    for x in reversed(range(6)):
        time.sleep(1)
        print(f"{x}")

def automatizarRoubos():
    global nivelVicioAtual
    global boolPrimeiroRouboComReabastecimento
    global coordSelecaoRoubo
    global coordBotaoRoubar
    contagemRegressivaInicio()

    ordernarPorPoderDeRouboERecompensaEEstaminaENome()
    quantidadeTickets = getQuantidadeTickets()

    for ticket in range(quantidadeTickets):
        roubar()
        if (not boolContinuarExecucao):
            break

        time.sleep(1)

        if boolReabastecimento:
            reabastecer()
            
            if boolPrimeiroRouboComReabastecimento:
                coordSelecaoRoubo.y += 215
                coordBotaoRoubar.y += 215
                boolPrimeiroRouboComReabastecimento = False
        else:
            recuperarEstamina()

        quantidadeTickets -= 1
        nivelVicioAtual += 1
        print(f"nivelVicioAtual: {nivelVicioAtual}")

        if (not boolContinuarExecucao):
            break

        if nivelVicioAtual >= nivelVicioMax:
            desintoxicar()
            coordSelecaoRoubo.y -= 215
            coordBotaoRoubar.y -= 215
            boolPrimeiroRouboComReabastecimento = True
        
            if (not boolContinuarExecucao):
                break

            nivelVicioAtual = 0
        
automatizarRoubos()

# def filtrarPorPoderDeRoubo():
#     return list(
#         filter(
#             lambda roubo: roubo.poderDeRoubo < 9,
#             roubos
#         )
#     )

