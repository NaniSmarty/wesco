# import logging
# from logging.handlers import RotatingFileHandler
# #from log4mongo.handlers import MongoHandler
# from datetime import datetime
# import os, time
# var = datetime.now()
# var1 = var.date()
# s = var1.strftime("%d-%m-%Y")
# ########################ERROR LOG###############################################
# # log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
# # logFile = '/home/sasikumar/PycharmProjects/Pycharm/MylottoHub/lotto/ERRORlog'+str(s)
# # # my_handler = MongoHandler(host="192.168.10.134", port=27017, username="Aryan", password="root@123", database_name="Guest_db", collection="error_log")
# # my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=100*1024*1024, backupCount=50, encoding=None, delay=0)
# # my_handler.setFormatter(log_formatter)
# # my_handler.setLevel(logging.INFO)
# # app_log = logging.getLogger('root')
# # app_log.setLevel(logging.INFO)
# # app_log.addHandler(my_handler)
#
#
# ############################IO LOG###################################################
#
# IO_log_flag = 0    ### 0 - OFF ,,,,1 - ON
#
# IOlog_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
# IOlogFile = '/home/narayanaraju/wesco/wesco_lotto/game/'+str(s)
# # IOmy_handler = MongoHandler(host="192.168.10.134", port=27017, username="Aryan", password="root@123", database_name="Guest_db", collection="IO_log")
# IOmy_handler = RotatingFileHandler(IOlogFile, mode='a', maxBytes=100*1024*1024, backupCount=50, encoding=None, delay=0)
# IOmy_handler.setFormatter(IOlog_formatter)
# IOmy_handler.setLevel(logging.INFO)
# io_log = logging.getLogger('root1')
# io_log.setLevel(logging.INFO)
# io_log.addHandler(IOmy_handler)
#
# ##################################LOG Exterminator######################################
# # ls = []
# # path = r"Logger###path####"
# # now = time.time()
# #
# #
# # for filename in os.listdir(path):
# #     if os.path.getmtime(os.path.join(path, filename)) < now - 60:
# #         if os.path.isfile(os.path.join(path, filename)):
# #             print(filename)
# #             print(type(filename))
# #             os.remove(os.path.join(path, filename))
