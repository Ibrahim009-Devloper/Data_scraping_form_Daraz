import logging
import datetime
import os

folder_name = "logs"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

log_path = os.path.join(folder_name,"Daraz_scraping.log")


class log_maker():
    @staticmethod
    def log_gen():
        logging.basicConfig(filename= log_path,level=logging.INFO,format="'%(asctime)s | %(levelname)s | %(name)s | %(message)s",datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger("Daraz screper informations")
        logger.setLevel(logging.INFO)
        return logger