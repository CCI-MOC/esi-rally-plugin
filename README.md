# esi-rally-plugin
This repository contains custom Rally plugins and task files to test ESI commands using Rally. The plugin is designed to simulate and measure the performance of a particular ESI command. Currently we have plugin for one command that is "esi node network attach" .

## Requirements
    1. pip install rally-openstack
    2. Create db for rally: rally db recreate
    3. Now create a env.yaml file contating auth details of openstack( in our case demo server)
    4. Create a deployment by: rally deployment create --file=env.json --name=env
    5.Finally source the environment by: source ~/.rally/openrc
    6. git clone https://github.com/CCI-MOC/esi-rally-plugin.git
    7. rally --plugin-paths rally/esi_node_network_attach_plugin.py task start rally/esi_node_network_attach_task.yaml 

## Custom Plugin
The esi_node_network_attach_plugin.py file contains the custom Rally plugin. This plugin defines the EsiNodeNetworkAttachScenario class, which implements the benchmarking scenario using the esi_node_network_attach method. For more information on how to write a Scenerio and use it as aPlugin you can visit https://docs.openstack.org/developer/rally/plugins/implementation/scenario_plugin.html

## Task Configuration
Task file allow us to define certain configuration and provide input for the Scenerio that we trying to implement using a Plugin.
https://docs.openstack.org/developer/rally/quick_start/tutorial/step_2_input_task_format.html



