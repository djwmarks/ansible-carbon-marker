#!/usr/bin/python

import socket
import time

def main():
    module = AnsibleModule(
        argument_spec = dict(
            host=dict(required=True),
            port=dict(default=2003, type="int"),
            name=dict(required=True)
        ),
        supports_check_mode = False
    )

    now = int(time.time())
    fd = socket.create_connection((module.params["host"], module.params["port"]))

    name = module.params["name"]
    if isinstance(name, list):
        for name_x in name:
            fd.send("%s %d %d\n" % (name_x, 1, now))
    else:
        fd.send("%s %d %d\n" % (name, 1, now))

    fd.close()
    module.exit_json(changed=False)

from ansible.module_utils.basic import *

if __name__ == "__main__":
    main()
