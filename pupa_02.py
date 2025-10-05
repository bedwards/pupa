import re
import subprocess

data_dir = "../pupa_data/Zhang Henshui - The Story of a Noble Family"
input_file = f"{data_dir}/Chinese - Zhang Henshui - The Story of a Noble Family.txt"
model = "llama3.3:70b"

notes_translation = ("Translate from Chinese to English and rewrite in the style of "
    "Colson Whitehead without naming him. No meta-level commentary, just tranlated "
    "content. Take liberty to make it read like a Colson Whitehead novel. Do not "
    "attempt to create a strict translation. Create something that today's reader "
    "who enjoys Colson Whitehead would also enjoy.")

def translate(prompt):
    print(f"Sending prompt: {prompt[:67]}")
    subprocess.run(
        [
            "ollama",
            "run",
            model,
        ],
        input=prompt.encode()
    )


txt = open(input_file, encoding="utf-8").read()
parts = re.split(r'第.+?回', txt)

translate(
    f"{notes_translation}\n\nTranslate the Prologue (楔子) into English in the style of Colson Whitehead:\n\n{parts[0]}"
)

for i, ch in enumerate(parts[1:13], 1):
    prompt = (
        f"{notes_translation}\n\nTranslate Chapter {i} into English in the style of Colson Whitehead:\n\n{ch}"
    )
    translate(prompt)
