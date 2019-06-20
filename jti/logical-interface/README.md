# How to install (option #1)

1- Upload `interface-bytes-to-bps.py` to `/var/local/healthbot/input`
2- Load the rule file via import rule in the HealthBot UI
3- Load the playbook file via import playbook in the HealthBot UI


# How to install (option #2)

1- Upload `interface-bytes-to-bps.py` to `/var/local/healthbot/input`

2- Execute `healthbot mgd cli`

3- Execute `request iceberg load`

4- Execute `configure`

5- Execute `load merge terminal relative`

6- Paste the rule configuration

7- Press `<ENTER>`

8- Paste the playbook configuration

9- Press `<Control-D>`

10- Execute `commit and-quit`

11- Execute `request iceberg deploy`


# Configuration required in the router

```
user@router> show configuration services analytics
streaming-server <HEALTHBOT_SERVER> {
    remote-address <HEALTHBOT_SERVER>;
    remote-port <JTI_NATIVE_PORT_CONFIGURED_IN_HEALTHBOT>;
}
export-profile <PROFILE_NAME> {
    local-address <LOCAL_ADDRESS_OF_A_REVENUE_PORT_TOWARDS_HEALTHBOT_SERVER>;
    local-port <JTI_NATIVE_PORT_CONFIGURED_IN_HEALTHBOT>;
    reporting-rate 2;
    format gpb;
    transport udp;
}
sensor firewall-tbt {
    server-name <HEALTHBOT_SERVER>;
    export-name <PROFILE_NAME>;
    resource /junos/system/linecard/interface/logical/usage/;
}
```
