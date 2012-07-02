"""Validate a small local-service configuration; never starts the service."""
import configparser
import re


def read_config(text):
    if not isinstance(text, str):
        raise ValueError("Configuration must be text")
    parser = configparser.ConfigParser(interpolation=None, strict=True)
    try:
        parser.read_string(text)
        if set(parser.sections()) != {"service"} or parser.defaults():
            raise ValueError("Use exactly one [service] section and no DEFAULT options")
        section = parser["service"]
        if set(section) != {"name", "port", "debug"}:
            raise ValueError("Service requires exactly name, port, and debug")
        name = section["name"].strip()
        if not re.fullmatch(r"[a-z][a-z0-9-]{0,39}", name):
            raise ValueError("Name must use 1–40 lowercase letters, digits, or hyphens and start with a letter")
        if not re.fullmatch(r"[0-9]{1,5}", section["port"]) or not 1 <= int(section["port"]) <= 65535:
            raise ValueError("Port must be an integer between 1 and 65535")
        return {"name": name, "port": int(section["port"]), "debug": section.getboolean("debug")}
    except (configparser.Error, ValueError) as error:
        raise ValueError("Invalid configuration: " + str(error)) from error
