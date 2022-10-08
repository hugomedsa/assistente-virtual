# Dedicado a ligações
from twilio.rest import Client
import pyautogui, Login
from datetime import datetime, timedelta

account_sid,auth_token,meu_numero, numero_twilio = Login.login_assistente

client = Client(account_sid, auth_token)

def avisar():
    pyautogui.hotkey('alt', 'tab')
    ligacao = client.calls.create(to=meu_numero,
                                  from_=numero_twilio,
                                  twiml='<Response><Say language="pt-BR">Você tem novas tarefas!</Say></Response>')
    print(f'Tarefa ou correção detectada. Entrando em contato...{datetime.utcnow() - timedelta(hours=3, minutes=0)}')


