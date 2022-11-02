from configparser import ConfigParser


# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locators","username"))
# print(config.get("basic info","testsiteurl"))

def readConfig(section, key):
    config = ConfigParser()
    config.read("C:\\Users\\megha\\PycharmProjects\\PageObjectModelFramework\\ConfigurationData\\conf.ini")
    return config.get(section, key)

# print(readConfig("locators","cartitle_XPATH"))
