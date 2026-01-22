from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.103",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)

print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)

# Skip getting full config - it's often too large and causes errors
# Instead, we'll get filtered config directly
print("\n#Skipping full running config retrieval to avoid errors")

# Get filtered native configuration
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
print("\n#Getting filtered native configuration...")
try:
    netconf_reply = m.get_config(source="running", filter=netconf_filter)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
except Exception as e:
    print(f"Error getting config: {e}")

# Configure hostname
netconf_hostname = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CSR1kv</hostname>
    </native>
</config>
"""
print("\n#Configuring hostname...")
try:
    netconf_reply = m.edit_config(target="running", config=netconf_hostname)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
except Exception as e:
    print(f"Error configuring hostname: {e}")

netconf_loopback = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>My NETCONF loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.1.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_newloop = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>2</name>
                <description>My second NETCONF loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>10.2.2.2</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_newloop)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())