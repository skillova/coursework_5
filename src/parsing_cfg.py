from configparser import ConfigParser


def get_cfg(filename=None, section=None) -> dict:
    """Чтение конфигурационного файла *.ini"""
    parser = ConfigParser()
    parser.read(filename)
    cfg = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            cfg[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")
    return cfg
