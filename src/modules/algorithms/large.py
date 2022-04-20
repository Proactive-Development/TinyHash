"""
1) HelloWorld
2) 48656c6c6f576f726c64
Final: 3046f74
"""

def generate(text):
    raw = text
    text = text.encode("utf-8").hex()
    output = str(len(raw)+len(text))+text[0]+text[round(len(text)/4)]+text[round(len(text)/2)]+text[-round(len(text)/4)]+text[-1]
    return output
