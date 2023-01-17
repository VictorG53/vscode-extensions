import os
import json

with open('extensions.json', 'r') as f:
    extensions = json.load(f)

for extension in extensions:
    os.system('code --install-extension ' + extension)
