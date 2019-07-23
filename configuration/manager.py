
from configuration.config_files import (
    box,
    servers,
    network
)


class ConfigManager:
    def __init__(self):
        self.config = dict()
        self.config.update(box.box_config)
        self.config.update(servers.servers_config)
        self.config.update(network.network_config)


    def get_configuration(self):
        return self.config

