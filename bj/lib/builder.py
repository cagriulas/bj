from jira import JIRA
import stashy
import configparser
from pathlib import Path

config_path = Path.home() / ".config/bj.ini"


def get_configs():
    config = configparser.ConfigParser()
    if config.read(config_path) == []:
        raise Exception(str("Type `bj help config` for details about config creation."))
    return config

def save_configs(**kw):
    config = configparser.ConfigParser()

    config["bitbucket"] = {}
    config["bitbucket"]["url"] = kw["bb-url"]
    config["bitbucket"]["username"] = kw["bb-username"]
    config["bitbucket"]["password"] = kw["bb-pw"]

    config["jira"] = {}
    config["jira"]["url"] = kw["jira-url"]
    config["jira"]["username"] = kw["jira-username"]
    config["jira"]["password"] = kw["jira-pw"]

    with open(config_path, "w") as cfg:
        config.write(cfg)

    return config_path


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

class Builder(Singleton):

    _instances = {
        "jira": None,
        "bb": None
    }

    def __init__(self):
        pass

    def build_jira(self):
        if self._instances["jira"] is None:
            cfg = get_configs()["jira"]

            self._instances["jira"] = JIRA(
                {
                    'server': cfg["url"]
                }, 
                basic_auth=(cfg["username"], cfg["password"])
            )

        return self._instances["jira"]
    
    def build_bb(self):
        if self._instances["bb"] is None:
            cfg = get_configs()["bitbucket"]
            
            self._instances["bb"] = stashy.connect(cfg["url"], cfg["username"], cfg["password"])

        return self._instances["bb"]
