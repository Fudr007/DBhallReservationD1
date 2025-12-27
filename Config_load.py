import configparser
import os

class ConfigError(Exception):
    pass

def load_config(path="config.ini"):
    if not os.path.isfile(path):
        raise ConfigError(f"Config file '{path}' not found.")

    config = configparser.ConfigParser()
    config.read(path)

    if "database" not in config:
        raise ConfigError("Missing [database] section in config file.")

    db = config["database"]

    required = ["user", "password", "host", "port", "service", "encoding"]
    for field in required:
        if field not in db or not db[field].strip():
            raise ConfigError(f"Missing or empty '{field}' in config file.")

    try:
        port = int(db["port"])
        if port <= 0 or port > 65535:
            raise ValueError
    except ValueError:
        raise ConfigError("Port must be a positive integer.")

    dsn = f"{db['host']}:{port}/{db['service']}"

    return {
        "user": db["user"],
        "password": db["password"],
        "dsn": dsn,
        "encoding": db["encoding"]
    }