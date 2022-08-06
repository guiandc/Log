def main():
    #EM SEGUIDA ADICIONE LOGS EM CADA UMA DAS FUNÇÕES DO PROJETO
    try:
        print('Hello World')
        log.info("-------SUCCESSFUL PRINTING!") #<=== MENSAGEM DE SUCESSO
    except:
        log.error("===> ERROR: DURING MESSAGE PRINTING. :( ") #<=== MENSAGEM DE ERRO

if __name__ == '__main__':
    #ADICIONE AS DUAS LINHAS DE CÓDIGO A SEGUIR EM CADA UM DOS ARQUIVOS .py DO PROJETO
    import log                          #<=== 1
    log = log.get_logger(__name__)      #<=== 2
    main()