protocol = input().split(":")

if protocol[0] == "" and protocol[1] == "":
    protocol = protocol[1:]

if protocol[len(protocol)-1] == "" and protocol[len(protocol)-2] == "":
    protocol = protocol[:-1]

if len(protocol) != 8:
    idx_0 = protocol.index("")
    protocol = protocol[:idx_0+1] + [""]*(8-len(protocol)) + protocol[idx_0+1:]

for idx, item in enumerate(protocol):
    if len(item) != 4:
        num_0 = 4-len(item)
        protocol[idx] = "0"*num_0 + item
    
print(":".join(protocol))