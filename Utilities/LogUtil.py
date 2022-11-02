import logging
import time

class logger():

    def __init__(self,logger,file_level=logging.INFO):
        self.logger =logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - %(levelname)s - %(message)s')

        curr_time =time.strftime("%Y-%m-%d")
        self.LogFileName = 'C:\\Users\\megha\\PycharmProjects\\PageObjectModelFramework\\Logs\\log' + curr_time +'.txt'
        # 'a' to append the logs in the same file, 'w' to generate new logs and delete old logs
        fh = logging.FileHandler(self.LogFileName, mode='w')
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
