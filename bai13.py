#bai 13
import re
def chuan_hoa_chuoi(s):
    s = s.strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s([.,])', r'\1 ', s)
    return s

text = """   Quê hương   là  chùm khế  ngọt ."""
print(chuan_hoa_chuoi(text))