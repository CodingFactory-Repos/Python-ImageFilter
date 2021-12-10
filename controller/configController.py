import configparser

def get_ini():
    write_config = configparser.ConfigParser()

    write_config.add_section("Filters")
    write_config.set("Filters", "content", "--filter grayscale|blur:3|dilate:3")

    cfgfile = open("sample.ini", 'w')
    write_config.write(cfgfile)
    cfgfile.close()

    read_config = configparser.ConfigParser()
    read_config.read("sample.ini")

    name = read_config.get("Filters", "content")

    return name
