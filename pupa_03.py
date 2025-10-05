import re
import os

data_dir = "../pupa_data/Zhang Henshui - The Story of a Noble Family"
input_file = f"{data_dir}/Chinese - Zhang Henshui - The Story of a Noble Family.txt"
output_dir = f"{data_dir}/chapters_chinese"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the Chinese text
txt = open(input_file, encoding="utf-8").read()

# Split by chapter markers (第...回)
parts = re.split(r'第.+?回', txt)

# Save prologue (楔子)
prologue_path = f"{output_dir}/000_prologue.txt"
with open(prologue_path, "w", encoding="utf-8") as f:
    f.write(parts[0])
print(f"Saved: {prologue_path}")

# Save each chapter
for i, ch in enumerate(parts[1:], 1):
    chapter_path = f"{output_dir}/{i:03d}_chapter.txt"
    with open(chapter_path, "w", encoding="utf-8") as f:
        f.write(ch)
    print(f"Saved: {chapter_path}")

print(f"\nTotal files created: 1 prologue + {len(parts)-1} chapters = {len(parts)} files")
