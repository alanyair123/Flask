network_config_2 = {
    "0001": {
        "ip": "192.168.0.2",
        "device": "Switch",
        "policy": "Deny All",
        "status": False,
        "lista":[1,3,7,8,9]
    },
    "0002": {
        "ip": "192.168.0.1",
        "device": "Firewall",
        "policy": "Avoid .2 .3 .4",
        "status": True
    },
    "0003": {
        "ip": "192.168.0.5",
        "device": "Router",
        "policy": "Allow All",
        "status": True
    },
    "0004": {
        "ip": "192.168.0.6",
        "device": "Access Point",
        "policy": "Allow Local",
        "status": True
    },
    "0005": {
        "ip": "192.168.0.7",
        "device": "Server",
        "policy": "Restricted",
        "status": "False"
    }
}
print(network_config_2.get("0001").get("lista")[2])