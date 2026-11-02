import re

# Read the file with utf-8
with open(r'D:\opencode\fake_news_detection-main\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all emoji with ASCII alternatives
replacements = {
    '\u26a0': 'WARNING',  # sun
    '\u2713': 'OK',       # check mark
    '\U0001f50d': '[SEARCH]',  # magnifying glass
    '\U0001f4cb': '[LIST]',    # clipboard
    '\U0001f511': '[KEY]',     # key
    '\U0001f4ca': '[CHART]',   # bar chart
    '\U0001f310': '[GLobe]',   # globe
    '\U0001f3af': '[BUILDING]', # building
    '\u2705': '[OK]',          # check button
    '\u274c': '[X]',           # cross mark
}

for unicode_char, ascii_text in replacements.items():
    # Handle variations with combining marks (like ⚠️ vs ⚠)
    content = content.replace(unicode_char, ascii_text)

# Also handle the specific multi-character emoji sequences
content = content.replace('⚠️', 'WARNING')  # clover/warning

# Write back with utf-8
with open(r'D:\opencode\fake_news_detection-main\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacements done")