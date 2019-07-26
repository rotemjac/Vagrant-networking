# Vagrant-networking
Exploring VirtualBox network modes with vagrant.

1. All configuration are under configuration/config_files.

------- Network configuration  -------- 
Currently supported network modes:
bridge
bridge_with_default_interface
internal
host_only


2. To change the scripts that are running on host / guests go to vagrantfile_builder/scripts.

3. The output of all scripts will be under:
vagrantfile_builder/outputs

4. In order to start / destory Vms use the scirpt_start / script_destroy