import os, time, pyaudio
import speech_recognition as controladorVoz
recognizer = controladorVoz.Recognizer()

def limpar_tela():
    os.system("cls")
    
def aguarde(segundos):
    time.sleep(segundos)
    
def inicializarBancoDeDados():
    # r - read, w - write, a - append
    try:
        banco = open("base.atitus","r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("base.atitus","w")
    
def escreverDados(listaIdeias):
    # INI - inserindo no arquivo
    banco = open("base.atitus","w")
    for item in listaIdeias:
        banco.write(item + "\n")
    banco.close()
    # END - inserindo no arquivo

def ouvir():
    
    with controladorVoz.Microphone() as source:
        print("Diga algo:")
        print("Fique em silêncio para finalizar!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Voce disse: {texto}")
            return texto
        except controladorVoz.UnknownValueError:  # Corrigido o nome da exceção
            print("Não entendi o que você disse!")
            return ""
        except controladorVoz.RequestError:
            print("Erro ao conectar com o servidor!")
            return ""
