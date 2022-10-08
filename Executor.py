import CallCenter, ImageCenter
from time import sleep

for count in range(57600): # O PROGRAMA ESTARÁ ATIVO DURANTE 16 HORAS
    resultado_pesquisa = ImageCenter.proc_png(ImageCenter.im)
    if resultado_pesquisa == False:
        CallCenter.avisar()
        sleep(0.3)
        ImageCenter.automate_chrome()
        break
        #sleep(28800) #ESPERAR 8 horas PARA RECOMEÇAR O PROGRAMA
    #print(datetime.utcnow() - timedelta(hours=3, minutes=0)) # HORA QUE A TAREFA FOI DETECTADA
    sleep(2)  # TEMPO ENTRE CADA VERIFICAÇÃO SE HÁ TAREFAS NOVAS. QUANTO MENOR O TEMPO, MAIS IRÁ EXIGIR DO PROCESSADOR.