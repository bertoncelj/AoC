
file = open("submarine_movements.txt", "r")
lines = file.readlines()
commands = list(map(lambda s: tuple(s.strip().split(" ")), lines))
test = [("forward","5"),
        ("down","5"),
        ("forward","8"),
        ("up","3"),
        ("down","8"),
        ("forward","2")
       ]

# print(commands)
def get_hor_ver(cmds_log):
    horizontal = 0
    vertical = 0
    for cmd_txt in cmds_log:
        if cmd_txt[0] == "forward":
            horizontal = horizontal + int(cmd_txt[1])
        elif cmd_txt[0] == "down":
            vertical = vertical + int(cmd_txt[1])
        elif cmd_txt[0] == "up":
            vertical = vertical - int(cmd_txt[1])
        else:
            raise "Unkown name"
    return (horizontal, vertical)

def get_hor_ver_aim(cmds_log):
    horizontal = 0
    vertical = 0
    aim = 0
    for cmd_txt in cmds_log:
        if cmd_txt[0] == "forward":
            horizontal = horizontal + int(cmd_txt[1])
            vertical = vertical + int(cmd_txt[1])*aim
            print("forward", horizontal, vertical, aim)
        elif cmd_txt[0] == "down":
            # vertical = vertical + int(cmd_txt[1])
            aim = aim + int(cmd_txt[1])
            print("down", horizontal, vertical, aim)
        elif cmd_txt[0] == "up":
            # vertical = vertical - int(cmd_txt[1])
            aim = aim - int(cmd_txt[1])
            print("up", horizontal, vertical, aim)
        else:
            raise "Unkown name"
    return (horizontal, vertical)

hor, ver = get_hor_ver(commands)
print(hor*ver)
hor, ver = get_hor_ver_aim(commands)
print(hor*ver)

