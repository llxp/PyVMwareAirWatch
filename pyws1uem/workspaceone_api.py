"""WorkspaceOneAPI Client Module

The module handles all basic methods to interact with the API.
Basic HTTP Method calls are defined here (GET, POST, PUT, PATCH, DELETE)
and static methods for error checking, building the client object and constructing header values.

In Case of errors in the response the requests will raise an exception
using the WorkspaceOneAPIError Class.
"""

from __future__ import print_function, absolute_import
import base64
import logging
import requests
from .error import WorkspaceOneAPIError
from .mdm import Devices, Smartgroups, Tags
from .system import Groups, Users, Info
from .mam import Apps
from .client import Client


# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with
# HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 0

# TODO: programing using library should be able to set logging level
# TODO: Implement logging to using config https://docs.python.org/3/howto/logging.html#configuring-logging
# TODO: sett logging correctly for a library https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class WorkspaceOneAPI(object):
    """
    Class for building a WorkspaceONE UEM API Object
    """

    def __init__(self, env: str, apikey: str, username: str, password: str):
        """
        Initialize an AirWatchAPI Client Object.

        :param  env: Base URL of the AirWatch API Service
                apikey: API Key to authorize
                username: Admin username
                password: corresponding pasword
        """
        self.client = Client(env, apikey, username, password)
        self.groups = Groups(self.client)
        self.devices = Devices(self.client)
        self.smartgroups = Smartgroups(self.client)
        self.users = Users(self.client)
        self.info = Info(self.client)
        self.tags = Tags(self.client)
        self.apps = Apps(self.client)
