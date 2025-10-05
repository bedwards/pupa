import sys
import os
import subprocess

data_dir = "../pupa_data/Zhang Henshui - The Story of a Noble Family"
output_dir = f"{data_dir}/chapters_english_01"
model = "llama3.3:70b"

notes_translation = ("Translate from Chinese to English and rewrite in the style of "
    "Colson Whitehead without naming him. No meta-level commentary, just tranlated "
    "content. Take liberty to make it read like a Colson Whitehead novel. Do not "
    "attempt to create a strict translation. Create something that today's reader "
    "who enjoys Colson Whitehead would also enjoy.")

def translate(prompt, output_file):
    print(f"Translating to: {output_file}")
    print(f"Prompt preview: {prompt[:67]}...")
    
    # Run ollama and capture output
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True
    )
    
    # Save translation to output file
    os.makedirs(output_dir, exist_ok=True)
    with open(output_file, "wb") as f:
        f.write(result.stdout)
    
    print(f"Translation saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pupa_04.py <input_filepath>")
        print("Example: python pupa_04.py ../pupa_data/Zhang\\ Henshui\\ -\\ The\\ Story\\ of\\ a\\ Noble\\ Family/chapters_chinese/000_prologue.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    # Read the Chinese text
    with open(input_file, "r", encoding="utf-8") as f:
        chinese_text = f.read()
    
    # Determine if it's prologue or chapter based on filename
    filename = os.path.basename(input_file)
    
    if "prologue" in filename:
        prompt = (
            f"{notes_translation}\n\n"
            f"Translate the Prologue (楔子) into English in the style of Colson Whitehead:\n\n"
            f"{chinese_text}"
        )
        output_filename = "00_prologue_en.txt"
    else:
        # Extract chapter number from filename (e.g., "01_chapter.txt" -> "1")
        chapter_num = filename.split("_")[0].lstrip("0") or "1"
        prompt = (
            f"{notes_translation}\n\n"
            f"Translate Chapter {chapter_num} into English in the style of Colson Whitehead:\n\n"
            f"{chinese_text}"
        )
        output_filename = f"{filename.split('_')[0]}_chapter_en.txt"
    
    output_file = f"{output_dir}/{output_filename}"
    translate(prompt, output_file)
