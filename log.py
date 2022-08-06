#import
import logging
import os
import sys
from datetime import datetime

#função principal de log
def get_logger(logger_name):

    #verifica a existência da pasta log
    if not os.path.exists(sys.path[1] + '/logs'):
        os.mkdir(sys.path[1] + '/logs')

    #define nome do arquivo
    path_file_log = f'{sys.path[1]}/logs/log_{datetime.now().strftime("%Y%m%d")}.log'

    logging.basicConfig(
        filename = path_file_log
        ,level = logging.INFO
        ,datefmt = '%Y-%m-%d %H:%M:%S'
        ,format = "'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).funcName)s(%(lineno)d) - %(message)s'"
    )

    logger = logging.getLogger(logger_name)
    Stream_Handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    Stream_Handler.setFormatter(formatter)
    logger.addHandler(Stream_Handler)

    return logger