from main import DIR, ENVIRON
import yaml


class YamlRead:
    @staticmethod
    def env_config():
        with open(file=f'{DIR}/config/env/{ENVIRON}/config.yml', mode='r', encoding='urf-8') as f:
            return yaml.load(f, loader=yaml.FullLoader)

    @staticmethod
    def data_config():
        with open(file=f'{DIR}/config/env/{ENVIRON}/config.yml', mode='r', encoding='urf-8') as f:
            return yaml.load(f, loader=yaml.FullLoader)
