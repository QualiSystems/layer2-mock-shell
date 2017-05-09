from cloudshell.shell.core.driver_context import *
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface
import cloudshell.api.cloudshell_api
import cloudshell.helpers.scripts.cloudshell_dev_helpers
import drivercontext
import os
import json


class NewL2Driver(ResourceDriverInterface, NetworkingResourceDriverInterface):
    def health_check(self, context):
        raise NotImplementedError()

    def shutdown(self, context):
        raise NotImplementedError()

    def orchestration_restore(self, context, saved_artifact_info, custom_params):
        raise NotImplementedError()

    def save(self, context, folder_path, configuration_type, vrf_management_name):
        raise NotImplementedError()

    def run_custom_command(self, context, custom_command):
        raise NotImplementedError()

    def restore(self, context, path, configuration_type, restore_method, vrf_management_name):
        raise NotImplementedError()

    def run_custom_config_command(self, context, custom_command):
        raise NotImplementedError()

    def orchestration_save(self, context, mode, custom_params):
        raise NotImplementedError()

    def __init__(self):
        pass

    # Initialize the driver session, this function is called everytime a new instance of the driver is created
    # This is a good place to load and cache the driver configuration, initiate sessions etc.
    def initialize(self, context):
        """
        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """
        return 'Finished initializing'

    # Destroy the driver session, this function is called everytime a driver instance is destroyed
    # This is a good place to close any open sessions, finish writing to log files
    def cleanup(self):
        pass

    def remove_vlan(self, context, ports, VLAN_Ranges, VLAN_Mode, additional_info='', qnq='', ctag=''):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        raise NotImplementedError()

    def add_vlan(self, context, ports, VLAN_Ranges, VLAN_Mode, additional_info='', qnq='', ctag=''):
        """
        :param cloudshell.shell.core.driver_context.ResourceRemoteCommandContext context: context information object
         created on execution by cloudshell
        """

        raise NotImplementedError()

    def get_inventory(self, context):
        """
        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        """
        #  # example autoload return results
        # resources = [AutoLoadResource('Generic Chassis', 'Chassis 1', '1'),
        #              AutoLoadResource('Generic Module', 'Module 1', '1/1'),
        #              AutoLoadResource('Generic Port', 'Port 1', '1/1/1')]
        #
        # attributes = [
        #       AutoLoadAttribute('', 'Location', 'Santa Clara Lab'),
        #       AutoLoadAttribute('', 'Model', 'Catalyst 3850'),
        #       AutoLoadAttribute('', 'Vendor', 'Cisco'),
        #       AutoLoadAttribute('1', 'Serial Number', 'JAE053002JD'),
        #       AutoLoadAttribute('1', 'Model', 'WS-X4232-GB-RJ'),
        #       AutoLoadAttribute('1/1', 'Model', 'WS-X4233-GB-EJ'),
        #       AutoLoadAttribute('1/1', 'Serial Number', 'RVE056702UD'),
        #       AutoLoadAttribute('1/1/1', 'IPv4 Address', '192.168.10.7')
        # ]
        #
        # result = AutoLoadDetails(resources, attributes)
        # return result
        raise NotImplementedError()

    def ApplyConnectivityChanges(self, context, request):
        """
        :type context: drivercontext.ResourceCommandContext
        :type json: str
        """
        session_cloud = cloudshell.api.cloudshell_api. \
            CloudShellAPISession(context.connectivity.server_address,
                                 token_id=context.connectivity.admin_auth_token, domain=context.reservation.domain)

        # Write request
        requestJson = json.loads(request)
        session_cloud.WriteMessageToReservationOutput(context.reservation.reservation_id,
                                                      json.dumps(requestJson, indent=4, sort_keys=True))
        session_cloud.WriteMessageToReservationOutput(context.reservation.reservation_id,
                                                      "-------------------------------------")

        ##Build Response
        response = {"driverResponse": {"actionResults": []}}

        for actionResult in requestJson['driverRequest']['actions']:
            actionResultTemplate = {"actionId": None, "type": None, "infoMessage": "", "errorMessage": "",
                                    "success": "True", "updatedInterface": "None"}
            actionResultTemplate['type'] = str(actionResult['type'])
            actionResultTemplate['actionId'] = str(actionResult['actionId'])
            response["driverResponse"]["actionResults"].append(actionResultTemplate)

        session_cloud.WriteMessageToReservationOutput(context.reservation.reservation_id,
                                                      "Response \n" + json.dumps(response, indent=4, sort_keys=True))
        return 'command_json_result=' + str(response) + '=command_json_result_end'

    def load_firmware(self, context, remote_host, file_path):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        """
        raise NotImplementedError()

    def apply_connectivity_changes(self, context, connectivity_json):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        """
        raise NotImplementedError()

    def send_custom_command(self, context, command):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        """
        raise NotImplementedError()

    def update_firmware(self, context, remote_host, file_path):
        raise NotImplementedError()
