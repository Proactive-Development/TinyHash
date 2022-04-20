"""
1) HelloWorld
2) 48656c6c6f576f726c64
Final: 304f4
"""
def generate(text):
    raw = text
    output = str(len(raw)+len(text.encode("utf-8").hex()))+text.encode("utf-8").hex()[0]+text.encode("utf-8").hex()[round(len(text)/2)]+text.encode("utf-8").hex()[-1]
    return output
