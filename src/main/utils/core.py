from pathlib import Path
import os
import sys
core_lib = os.path.join(str(Path.home()), "apps", "angox", "angox-core-lib")
sys.path.insert(0, core_lib)
sys.path.append('../../../../angox-core-lib/')
sys.path.append('../angox-core-lib/')
from logger import Logger
from utils.file import UtilidadFile
from utils.path import UtilidadPath
from utils.token import generate_token, TypeTokenEnum
from config.config import Config
from config.config_dto import ConfigDTO
from concurrency.thread_pool import ThreadPoolExecutor
from concurrency.task import ITask
from controller import ControllerDataBase
from dto.dto import DTO
from service import ServiceExternal

current_dir = Path(__file__).parent
dir_logger = UtilidadFile.getPathFromResources('logging.conf', current_dir)
loggerx = Logger.getLogger(dir_logger)
config: ConfigDTO = Config(dir_file=current_dir).getConfig()
