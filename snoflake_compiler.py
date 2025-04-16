import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os
import re

# Transpiler logic (no external import needed now)
KEYWORDS = {
    'truefalse': 'bool',
    'integer': 'int',
    'character': 'char',
    'nonchanging': 'const',
    'stoploop': 'break',
    'option': 'case',
    'none': 'void'
}

def tokenize(code):
    return re.findall(r'".*?"|\'.*?\'|\w+|[^\s\w]', code)

def transpile(tokens):
    return ' '.join(KEYWORDS.get(token, token) for token in tokens)

def extract_main_function(code):
    match = re.search(r'none\s+main\s*\([^)]*\)\s*\{(?:[^{}]*|\{[^{}]*\})*\}', code, re.DOTALL)
    if not match:
        return code, None
    main = match.group()
    return code.replace(main, '').strip(), main.strip()

def convert_code(code):
    code_wo_main, main_func = extract_main_function(code)
    tokens = tokenize(code_wo_main)
    transpiled = transpile(tokens)
    if main_func:
        main_tokens = tokenize(main_func)
        transpiled += "\n\n" + transpile(main_tokens)
    return transpiled

# Tkinter IDE
class SnoFlakeIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("SnoFlake IDE ❄️")
        self.root.geometry("900x650")

        self.editor = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12))
        self.editor.pack(fill=tk.BOTH, expand=True)

        run_btn = tk.Button(root, text="▶ Run", command=self.run_snoflake, bg="#87CEEB")
        run_btn.pack(fill=tk.X)

        self.console = scrolledtext.ScrolledText(root, height=10, state='disabled', bg="#1e1e1e", fg="#00FF00", font=("Consolas", 10))
        self.console.pack(fill=tk.BOTH)

    def log(self, text):
        self.console.config(state='normal')
        self.console.insert(tk.END, text + "\n")
        self.console.see(tk.END)
        self.console.config(state='disabled')

    def run_snoflake(self):
        code = self.editor.get("1.0", tk.END).strip()
        cpp_code = convert_code(code)

        with open("temp.cpp", "w") as f:
            f.write(cpp_code)

        try:
            compile = subprocess.run(["g++", "temp.cpp", "-o", "sno_program"], capture_output=True, text=True)
            if compile.returncode != 0:
                self.log("[❌] Compilation Error:\n" + compile.stderr)
                return

            self.log("[✅] Compilation successful.")
            result = subprocess.run(["sno_program"], capture_output=True, text=True, shell=True)
            self.log("[💬] Program Output:\n" + result.stdout + result.stderr)

        except Exception as e:
            self.log(f"[❌] Error: {e}")

# Launch
if __name__ == "__main__":
    root = tk.Tk()
    app = SnoFlakeIDE(root)
    root.mainloop()
