from comm import *
from lang import *
from globals import *

DEFAULT_CONFIG = 'conf/conf.json'

@singleton
class Conf():
    data = {}
    conf_file = DEFAULT_CONFIG

    def __init__(self):
        try:
            app_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r'Software\PPServ')
            config_file,type = winreg.QueryValueEx(app_key, "config_file")
            self.conf_file = config_file
        except:
            # 如果没有找到注册表信息则不设置配置文件
            pass
        finally:
            winreg.CloseKey(app_key)

        try:
            self.data = load_json(self.conf_file)
        except:
            logger.debug(Lang().get('load_config_error'))

    def get(self, name = None):
        '''获取配置的数据,如果没有设置key则获取全部'''
        if( name == None ):
            return self.data
        else:
            return self.data[name]

    def set(self, key, value):
        '''设置配置的数据

        只能当前有效，并保存到缓存数据中
        '''
        if key is None and len(value) is 0:
            pass
        else:
            self.data[key] = value
