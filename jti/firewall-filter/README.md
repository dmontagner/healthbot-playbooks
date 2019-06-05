# How to install (option #1)

1- Upload `generic-bytes-to-bps.py` to `/var/local/healthbot/input`
2- Load the rule file via import rule in the HealthBot UI
3- Load the playbook file via import playbook in the HealthBot UI


# How to install (option #2)

1- Upload `generic-bytes-to-bps.py` to `/var/local/healthbot/input`

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

