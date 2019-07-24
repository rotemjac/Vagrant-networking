import os,subprocess
#import vagrant

from vagrantfile_builder.builder import VagrantManager
from configuration.manager import ConfigManager

config = ConfigManager().get_configuration()
VagrantManager.generate_vagrantfile(config)

# os.chdir("./vagrantfile_builder")
# subprocess.run("vagrant up")

#v = vagrant.Vagrant()
#v.up()