import PySimpleGUI as sg

def LogIn():
    sg.theme('Black')
    layout = [[sg.Text('account_sid'), sg.Input(size=(25,5), key='account_sid')],
        [sg.Text('Auth_token'), sg.Input(size=(25,5), key='auth_token')],
        [sg.Text('Meu_num'), sg.Input(size=(25, 5), key='numero')], # Ex.: +55899999999
        [sg.Text('Num_Twilio'), sg.Input(size=(25, 5), key='num_twilio')], # Ex.: +19799999999
        [sg.Button('Log-in')]]

    #  Gerar Janela
    janela = sg.Window('Log-in', layout)
    button, values = janela.Read()

    #  Armazenando valores
    email = values['account_sid']
    Pass = values['auth_token']
    tel = values['numero']
    tel_twilio = values['num_twilio']

    #  Condicionais
    if len(Pass) < 30:
        print('Senha deve conter 30 ou mais caracteres!')
    else:
        with open('bcdds.txt', 'w', encoding='utf-8') as file:
            for c in (email,'\n',Pass,'\n',tel,'\n',tel_twilio):
                file.write(c)
            print(file)
    return [email,Pass,tel,tel_twilio]

with open('bcdds.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    if len(content) > 0:
        login_assistente = [linha.rstrip('\n') for linha in content]
        print(content)
    else:
        login_assistente = LogIn()
