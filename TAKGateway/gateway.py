#
#     ______   ______   ______   ____
#    /_  __/  / ____/  / ____/  / __ \
#     / /    / __/    / /      / /_/ /
#    / /    / /___   / /___   / ____/
#   /_/    /_____/   \____/  /_/
#
# Gateway is responsible for feeding node-red with meshtastic events. Does not work standalone.

# import meshtastic

import sys
import meshtastic.node
import meshtastic.node
import meshtastic.serial_interface
from google.protobuf.json_format import MessageToJson
from meshtastic.util import stripnl, remove_keys_from_dict, convert_mac_addr


# TODO: Receive messages from meshtastic - Send to SQLite for processing by node-red


def getnodeinfo(self, file=sys.stdout):  # pylint: disable=W0613
    myinfo = ''
    if self.myInfo:
        myinfo = f"{stripnl(MessageToJson(self.myInfo))}"

    nodes = ""
    if self.nodes:
        for n in self.nodes.values():
            # when the TBeam is first booted, it sometimes shows the raw data
            # so, we will just remove any raw keys
            keys_to_remove = ('raw','payload')
            n2 = remove_keys_from_dict(keys_to_remove, n)

            # if we have 'macaddr', re-format it
            if 'macaddr' in n2['user']:
                val = n2['user']['macaddr']
                # decode the base64 value
                addr = convert_mac_addr(val)
                n2['user']['macaddr'] = addr

            nodes = nodes + f"{stripnl(n2)}"
    # infos = myinfo +  nodes
    print("MyInfo:")
    print(myinfo)
    print("Nodes")
    print(nodes)
    return myinfo, nodes


def fetchserial():
    fartmachine = meshtastic.serial_interface.SerialInterface()
    fartmachine.close()
    return fartmachine


#Will literally shit itself if it receive non answers to location
getnodeinfo(fetchserial())


