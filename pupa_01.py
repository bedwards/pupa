import re
import subprocess

input_file = "chinese_sample.txt"
# model = "qwen2.5:72b"
model = "llama3.3:70b"

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
    f"Translate the Prologue (楔子) into English in the style of Colson Whitehead:\n{parts[0]}"
)

for i, ch in enumerate(parts[1:13], 1):
    prompt = (
        f"Translate Chapter {i} into English in the style of Colson Whitehead:\n{ch}"
    )
    translate(prompt)
