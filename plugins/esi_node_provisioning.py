from rally_openstack.task.scenario import scenario
from rally import consts
from rally.task import atomic
from rally.task import validation
import subprocess
import time
import os

@validation.add("required_platform", platform="openstack", users=True)
@scenario.configure(name="ScenarioPlugin.esi_node_provisioning")

class EsiNodeProvisioning(scenario.Scenario):
    def esi_node_provisioning(self, image, network, candidate, resource_class='baremetal', ssh_public_key=None):
        """Scenario to test 'openstack esi node provisioning' command."""
        command = f"metalsmith deploy --resource-class {resource_class} --image {image} --network {network} --candidate {candidate}"
        if ssh_public_key:
            command += f" --ssh-public-key {ssh_public_key}"

        start_time = time.time()
        output = os.system(command)
        end_time = time.time()
        execution_time = end_time - start_time

    def run(self, image, network, candidate, resource_class='baremetal', ssh_public_key=None):
        self.esi_node_provisioning(image, network, candidate, resource_class, ssh_public_key)
