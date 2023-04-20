import re

with open('test.txt') as f:
    lines = f.read()

lines = re.sub(r'\/\*[\s\S]*?\*\/', '', lines)
lines = re.sub(r'//.*\n', '\n', lines)
lines = lines.replace('    ', '').replace('\n', ' ').replace('  ', ' ')

print(lines)