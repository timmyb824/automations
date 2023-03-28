# XC Example

## Tasks

### Playbook

Ping all servers in the inventory (ex: tea xc playbook ping).
Inputs: PLAYBOOK

```sh
ansible-playbook -i ../ansible/servers/inventory.ini ../ansible/servers/playbooks/$PLAYBOOK.yaml -K
```
