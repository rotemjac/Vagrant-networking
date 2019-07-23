from vagrantfile_builder.builder import VagrantManager
from configuration.manager import ConfigManager

config = ConfigManager().get_configuration()
VagrantManager.generate_vagrantfile(config)

