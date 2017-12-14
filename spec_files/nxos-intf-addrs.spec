---
vars:
  interface:
    name: "{{ item[0].name }}"
    ip: "{{ item[1].ip }}"
    relay: "{{ item[2].relay }}"

keys:
  interfaces:
    value: "{{ interface }}"
    start_block: "^interface [A-z0-9/.-]+$"
    end_block: "^$"
    items:
      - "^interface (?P<name>[A-z0-9/.-]+)"
      - "ip address (?P<ip>[0-9./]+)"
      - "ip dhcp relay address (?P<relay>[0-9./]+)"
