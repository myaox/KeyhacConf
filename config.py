from keyhac import *
import itertools

mods = ["Shift-", "Ctrl-", "Alt-", "Cmd-","Fn-"]
m = mods[:]

for i in range(2,len(mods)+1):
    for mod in itertools.combinations(mods,i):
        m.append(''.join(mod))

m.append('')


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()
    keymap.defineModifier(104, "User0")
    #keymap.replaceKey("RCmd", 104)

    keymap_global["102"] = "Alt-Ctrl-Space"
    maps = [
                ["J", "Left"],
                ["K", "Down"],
                ["I", "Up"],
                ["L", "Right"],
                ["U", "Home"],
                ["O", "End"],
                ["P", "Back"],
                ["Atmark", "Delete"],
                ["M", "PageUp"],
                ["Period", "PageDown"]
            ]
    
    for map in maps:
        keyMap(keymap_global, "User0", map[0], map[1])

def keyMap(gl, usr , key, alt):
    for mod in m:
        gl[mod + usr + "-" + key] = mod + alt
