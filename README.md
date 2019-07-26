# Vagrant-networking
Exploring VirtualBox network modes with vagrant.

1. All configuration are under configuration/config_files.

Network configuration:
Currently supported network modes:
bridge
bridge_with_default_interface
internal
host_only


2. To change the scripts that are running on host / guests go to vagrantfile_builder/scripts.

3. The output of all scripts will be under:
vagrantfile_builder/outputs

4. In order to start / destory Vms use the scirpt_start / script_destroy

5. In order not to mix the jinja2 template expressions ( {{}} ) with the ruby template expressions ( #{} ) I only used jinja2 expressions in very few places - just to assign the value from the config files and make it available via ruby.
Notice that for any other case then a simple string configuration, we have a mismatch between python data types and ruby.
As a walkaround, I'm wrapping the ruby configuration with "" (make it a simple string, no matter which data structure) and esacping using the "safe" filter.