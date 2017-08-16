from keyhac import *
import itertools

# 修飾キーの組み合わせを全種類文字列の配列として作る
mods = ["Shift-", "Ctrl-", "Alt-", "Cmd-","Fn-"]
m = mods[:]

for i in range(2,len(mods)+1):
    for mod in itertools.combinations(mods,i):
        m.append(''.join(mod))

m.append('')


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    # かなkeyを新しく修飾キーとして登録
    keymap.defineModifier(104, "User0")

    # 代わりに英数キーでかな/英数をtoggleできるようにする。
    keymap_global["102"] = "Alt-Ctrl-Space"

    # かなり趣味の領域のキー配置
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

# 他の修飾キーを考慮して右左のような動作をするように全種類登録
def keyMap(gl, usr , key, alt):
    for mod in m:
        gl[mod + usr + "-" + key] = mod + alt
