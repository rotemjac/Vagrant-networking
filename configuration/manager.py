
from configuration.config_files import (
    box,
    servers,
    network
)


class ConfigManager:
    def __init__(self):
        self.config = {
            'box': box.box_config,
            'servers': servers.servers_config,
            'network': network.network_config
        }


    def get_configuration(self):
        return self.config

