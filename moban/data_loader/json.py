import json

from lml.plugin import PluginInfo

from moban import constants


@PluginInfo(constants.DATA_LOADER_EXTENSION, tags=["json"])
def open_json(file_name):
    """
    returns json contents as string
    """
    with open(file_name, "r") as json_data:
        data = json.loads(json_data.read())
        return data
