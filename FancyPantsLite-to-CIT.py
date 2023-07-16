from PIL import Image
import sys
import os

def quit_with_error(error:str):
    from time import sleep
    print(error)
    sleep(4)
    quit()

def main():
    if len(sys.argv) != 3: quit_with_error("Select both of the FancyPantsLite textures and drag them onto this .py file")
    _, fpl1_path, fpl2_path = sys.argv
    if fpl1_path[-5] == '2': fpl1_path, fpl2_path = fpl2_path, fpl1_path
    if fpl1_path[-5] != '1' or fpl2_path[-5] != '2': quit_with_error("Select the FancyPantsLite textures leather_layer_1 and leather_layer_2")

    fpl1 = Image.open(fpl1_path)
    fpl2 = Image.open(fpl2_path)

    textures1 = create_files(fpl1)
    textures2 = create_files(fpl2)

    save_properties(list(textures1), list(textures2), fpl1_path)
    for color, img in textures1.items():
        save_image(color, img, fpl1_path)
    for color, img in textures2.items():
        save_image(color, img, fpl2_path)

    fpl1.close()
    fpl2.close()

    basepath = fpl1_path.replace('\\\\', '/').replace('\\', '/').removesuffix("textures/models/armor/leather_layer_1.png")+"optifine/cit/fancypantslite"
    with open(basepath+"/base_leather_armor.properties", 'w') as file:
        for line in create_base_properties():
            file.write(line+'\n')
    
    with open(basepath+"/base_leather_armor_1.png", 'wb') as file:
        file.writelines([b'\x89PNG\r\n', b'\x1a\n', b'\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00 \x08\x06\x00\x00\x00\xa2\x9d~\x84\x00\x00\x01\xefIDATh\xde\xe5\x99Qn\x840\x0cD\xb9\xff\r\xf8\xe6\x9b\x1bp\x06\xbeV\xbd\xce\xae\xbc\xd2T\xaf#cv\xab6M\t\x92%B\xbc\x8b=\xb1\xc7q\x98\xa6\x93kY\x96\xfb<\xcfO\x89{\x89\x9eMW\xbf\xc2\xd9\x8f\xdb\xed\x8b\xec\xfb\xfe\x94\x98\x1b\x06\x80u]\xef\xdb\xb6}\xca0\x00D\x98\x07\x00\xe1t\x80 \x89\xf1\x90\x00(\xfcC\x86\xe0\x80p2\x9cu\x00\x02\x94a8@N+\xf7E\x86\xc3T\x81\xaa\x14^\xd6Aw\xf6\x0c\x88j\xbe\xd2\xed\xaa\xce\x93\xe0\xc4\xf2"A=\x93\x04\x1f\xc8\x19\xa5\x06\xf9A\x1c\xe1\xfb\x08\xeav\xc1!Y\x99\x8b{\xe5\xf8\xd1\x8ar\xae\xfa\xbd\x00 p"\xd3n\x00\xa0aY(W\xbfu\x80\x08\x02\x01\xe2\x1e\x82\xf3\xddq\xc0O\x00\xeay\x9e\xed!\x86*\xa3\x02\xc1\xf9a\x882\xca\xc8\xb8T\xf9\x1c\xe6rv\xef\x85\xb3\x9aE\x12\xfb\x80^\x00 \x8f\xfc\xfa\x0b\xb9A\xea\x01\x00\x96\xd5&\x00\xf8\x16\xb6\x07\x00(\xdd\xf6\x12U\xee\xbe\xab_\xf5\x1aU\x0f\xd3\x04 \xe5\xa4\xb6\xb6\x1a\xd3)\x9d)p\xde\xc7n\xb8o\xa5\xb3\xde\xe2l\xdc\x04\x00\xf6\x024\x9e\xbd\x04\x1dv\xfd\xac\x19\xd3\xbc\xf7\x12l\xbe\x08\x90\xfa\x0c\xfd\x1f\xc7M"@/\xa4\xc1"M:\xe6\x06;@$[\xf6%G\x0ef\xff\xf7\'\x00\xb0\xbd%\x00*\x9d>\x9f\xe9{\xab\xcd\x88\xe1!l5&\x00\xcd\xaa\x04\x9b\x1d\x19\xe4Ght\xd8\xf5\t\x88\x0bI\xed\xac5\xff6\t\xbe\xcb\xaa\xd93?@\x91\x03Y\x04d\xfa\xbe\xfaM\xdbegQ\x92X\xc6\xaa\xd98;!\xe2\x07\x149\x9c\xe9\x130\x9e:5;0Q\x08\x92d\xdc\xe0l\x85\xa9\xefQ\xa1\x15\xe4\xd7$\x86\xbc\xeb\xfb\xea7\xfd\xf0"\x12q\x96fNsE\xa8\x7fd\xa0t\x08D\x15\xceY\xfa5\xdb\xe5i\x85=\xe4=g9\xafqedw[\xd6W\x0f*2\xd6\xad\x98\xf8\xbf\xb7\xfb\x0f\xfe\x8a\xe1F\xecE\xe2\x7f\x00\x00\x00\x00IEND\xaeB`\x82'])
    with open(basepath+"/base_leather_armor_1_overlay.png", 'wb') as file:
        file.writelines([b'\x89PNG\r\n', b'\x1a\n', b'\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00 \x08\x06\x00\x00\x00\xa2\x9d~\x84\x00\x00\x00\x7fIDATh\xde\xed\x97!\x0e\x800\x10\x04\xfb\x0c\xe4Y\x12$\x02Q\x81F"\x91H\xfe\xef\x0f\xd6a\x01Uv&\xd9\x07t\xda\xee\xb5\xa5<`\x19\xbaT\x8a+\xdb\x14\xa9 \xc0\x95\xbdF*\xb6\x02\x8e\xb9O\x05\x01\x08\xa0\x03\x10\xf0\x86u\x8cTl\xc7`\xf3\'H\xaf\xc0/\x02\xe8\x90k\xf7\xed\xa7\x08%Z\xf9K\xf8\n', b"h\xb6\xf9\xef\xb1\x14\xa0\xf2\xd2\xd1\xb5\x15\xa0\xc5\xab\xbcl\x05X_\x01\x00\x00\x00\x00\x00\xf8%'\n", b'\xd0W\xc8\xae\xab\xaf\xf4\x00\x00\x00\x00IEND\xaeB`\x82'])
    with open(basepath+"/base_leather_armor_2.png", 'wb') as file:
        file.writelines([b'\x89PNG\r\n', b'\x1a\n', b'\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00 \x08\x06\x00\x00\x00\xa2\x9d~\x84\x00\x00\x01\tIDATh\xde\xedV\xc1\t\xc30\x10\xcb\xfeK\xe4\x9f\xbfG\xc8\x0cy\x86L\x92\xa2\x80\x8a8\xaeN?-\xe4,\x81\x89\x8d\xafP\xc9:\xd9\xd3d\x18\x86a\x18\x86a\x18\x86a\x18\xc6\xf0X\x96\xe5\xc4\x98\xe7\xf9\xfa\x0e)\xc0\xb1\xef\xe7\xb6m\x97\x08\xc3\t\x00\xd2 \xdfZ\x1bW\x00\x1d\xc3\xf4<\xfb\x9e\xbd\xaf9\xf0i\xaf\x84@ \x03\xbb\xaf\xeb\xfa&\x88y\xb6&y\xcc\xcb\xb4\x08HP\x00\x12D\x06`\xf0\xa4\xb9\xe6\xa9c\xce\xfa\x12\x0e\xd0\x13\x06\xc1\x9e\x03T\x902\x02\xe8\t\xab\xc5\xd5\xf2$\x1c\x05)\xd5\x02\x14\x00km\x81L\x10\xae\xcb\xb4\x00\t\xc5w\x80:@\x05\xa2`\xe52\x80\x04U\x90\x18\x921#z\xd7d\xbcR\xf5\xab\xfb\xd9\xde_\x04\xce\xee\xfb\xbb\xb7A\xac\xe1\xd3Y\xd7\x1c\xcc\x97\xb8\xaf\x8e\xd2z\xfd\xcd#ZL[\x86\x02\x81\x04]B7\xa9c\xbe\xad\x7f\x84\x00\xd9C\x8a\x04\x95\x8c^\xa3JPC6\xd6?"cbf\xdceJ\x961\xbd\xfa_\xff\xff\x17\xd2\xd0d\xd5\xbc\xcf15\x00\x00\x00\x00IEND\xaeB`\x82'])
    with open(basepath+"/base_leather_armor_2_overlay.png", 'wb') as file:
        file.writelines([b'\x89PNG\r\n', b'\x1a\n', b'\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00 \x08\x03\x00\x00\x00\x95C\x8e\xb6\x00\x00\x00\x15PLTE\x00\x00\x00J,\x18R4 Z8 b< j@)sH)\xd7lI\t\x00\x00\x00\x01tRNS\x00@\xe6\xd8f\x00\x00\x00NIDATH\r\xed\xc11\n', b'C1\x10CA\xed\xd3*\xf7?rb\x93"\xa5\xc1\x04~\xb13\x1ac\x8c\xf18\xb6\xae\xf8\x15\xeb\x86\x13\xeb\x8a\xad\xe7\xe0\xa3\xd8\n', b'(\xbet\x8a\x04\xb24\xa4!\x1b:UnH/\xd0\xaeJ/\xe8\x14P\xc5\x0fo\xe8_\xde7\xa6\x01:\x1d\x8c\xa6]\x00\x00\x00\x00IEND\xaeB`\x82'])
    with open(basepath+"/empty.png", 'wb') as file:
        file.writelines([b'\x89PNG\r\n', b'\x1a\n', b'\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00 \x08\x06\x00\x00\x00\xa2\x9d~\x84\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00\tpHYs\x00\x00\x0e\xc3\x00\x00\x0e\xc3\x01\xc7o\xa8d\x00\x00\x00MIDAThC\xed\xd01\x01\x000\x0c\x80\xb0n\xfe=\xb7\x0f. \x0f?ow\xc7\xecS\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xad\x06P\xa9\x99\x03#\xa2\x03=\xd8\xfa`\x19\x00\x00\x00\x00IEND\xaeB`\x82'])


def color_to_hex(color:tuple) -> str:
    int_to_hex = lambda n: str(n) if n < 10 else chr(87+n)
    return (int_to_hex(color[0]%16) + int_to_hex(color[0]>>4)+
            int_to_hex(color[1]%16) + int_to_hex(color[1]>>4)+
            int_to_hex(color[2]%16) + int_to_hex(color[2]>>4))

def color_to_int(color:tuple) -> int:
    return color[0]*2**16 + color[1]*2**8 + color[2]

def save_image(color:tuple, img:Image.Image, fpl_path:str):
    layer = fpl_path[-5]
    path = (fpl_path.replace('\\\\', '/').replace('\\', '/').removesuffix(f'textures/models/armor/leather_layer_{layer}.png')+
            f'optifine/cit/fancypantslite/armor_{color_to_hex(color)}_{layer}.png')
    img.save(path)

def save_properties(colors1:list, colors2:list, fpl_path:str):
    unique = set(colors1 + colors2)
    basepath = fpl_path.replace('\\\\', '/').replace('\\', '/').removesuffix(f'textures/models/armor/leather_layer_{fpl_path[-5]}.png')
    os.makedirs(basepath+"optifine/cit/fancypantslite", exist_ok=True)

    for color in unique:
        path = basepath + f'optifine/cit/fancypantslite/armor_{color_to_hex(color)}.properties'
        properties = [
            "# Generated using https://github.com/PuckiSilver/FancyPantsLite by PuckiSilver", #!
            "type=armor",
            "weight=1"]
        items = []
        if color in colors1:
            properties.append("texture.leather_layer_1=empty")
            properties.append(f'texture.leather_layer_1_overlay=armor_{color_to_hex(color)}_1')
            items.extend(["minecraft:leather_helmet", "minecraft:leather_chestplate"])
        if color in colors2:
            properties.append("texture.leather_layer_2=empty")
            properties.append(f'texture.leather_layer_2_overlay=armor_{color_to_hex(color)}_2')
            items.extend(["minecraft:leather_leggings", "minecraft:leather_boots"])
        properties.append("items="+" ".join(items))
        properties.append(f'nbt.display.color={color_to_int(color)}')

        with open(path, 'w') as file:
            for line in properties:
                file.write(line+'\n')

def create_files(img:Image.Image) -> dict:
    textures = {}
    wx, wy = img.size
    for i in range(wy//32):
        for j in range(wx//64):
            if i == j == 0: continue
            color = img.getpixel((j*64,i*32))
            if color[3] == 0: continue
            textures[color] = img.crop((j*64,i*32,j*64+64,i*32+32))
    return textures

def create_base_properties() -> list[str]:
    return ["# Generated using https://github.com/PuckiSilver/FancyPantsLite by PuckiSilver", #!
            "type=armor",
            "items=minecraft:leather_helmet minecraft:leather_chestplate minecraft:leather_leggings minecraft:leather_boots",
            "texture.leather_layer_1=base_leather_armor_1",
            "texture.leather_layer_2=base_leather_armor_2",
            "texture.leather_layer_1_overlay=base_leather_armor_1_overlay",
            "texture.leather_layer_2_overlay=base_leather_armor_2_overlay",
            "weight=-1"]

if __name__ == '__main__':
    main()
