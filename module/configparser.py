import ConfigParser

CONF_FILE = "configparser.conf"
DEBUG = False

cp = ConfigParser.SafeConfigParser()
cp.read(CONF_FILE)

sectionName = "production" if not DEBUG else "development"

print(cp.get(sectionName, "key1"))
print(cp.get(sectionName, "key2"))