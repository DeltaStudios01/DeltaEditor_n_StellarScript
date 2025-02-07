import customtkinter as ctk ; import tkinter as tk; from tkinter import filedialog, messagebox as msgbox, simpledialog, font, Toplevel ; import json; import uuid ; import zipfile
import qrcode, qrcode.constants ; from io import BytesIO ; from PIL import Image, ImageTk ; import base64 as bs64 ; import subprocess
import sys, os, re, io ; from threading import Thread ; import shutil
import urllib.parse, webbrowser, requests, socket, webview, speedtest
import math, pygame, time, abc, random, typing, turtle, turtledemo, pandas, numpy, tempfile
import matplotlib.pyplot as plt

# loading the config file
stellar_config = {
    "windows_title": "DeltaEditor - Stellar Script Editor & Executor",
    "version" : "1.0",
    "anable_secret": True,
    "debug_mode": False,
    "networkutil": {
        "speedtest_max_attemps": 10
    }
}

__version__ = stellar_config["version"]
# __icon__ = os.path.join(os.path.dirname(__file__), 'DeltaEditor.ico')

if stellar_config["debug_mode"]: 
    print("-----------------------Debug Terminal-----------------------")
    print(f"DeltaEditor and StellarScript is at version: {__version__}")
    print(f"Now running at {time.strftime("%d-%m-%Y %H:%M:%S")}")
    print("------------------------------------------------------------")

def keyboardshortcut(): 
    script = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keyboard Shortcut</title>
    <style>
        body {
            font-family: Consolas, sans-serif;
            background-color: #2e2e2e;
            color: white;
            margin: 0;
            padding: 20px;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #bbbbbb;
        }
        ul {
            font-family: Arial, Helvetica, sans-serif;
            padding-left: 20px;
        }
        h1, h2 {
            color: #39c1d5;
        }
        pre {
            background-color: #3a3a3a;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
            position: relative;
        }
        .keyword {
            color: #ffbc00;
        }
        .category {
            margin: 20px 0 10px;
            font-size: 1.2em;
            color: #4bd5d5;
            font-weight: bold;
        }
        .copy-button {
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 5px 10px;
            background-color: #39c1d5;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 0.9em;
        }
        .copy-button:hover {
            background-color: #2aa0b3;
        }
    </style>
</head>
<body>
    <h1>Keyboard Shortcut</h1>
    <ul>
        <li><span class="keyword">F5</span>: Run Code</li>
        <li><span class="keyword">Ctrl+S</span>: Save File</li>
        <li><span class="keyword">Ctrl+O</span>: Open File</li>
        <li><span class="keyword">Shift+F5</span>: Error Lenses</li>
        <li><span class="keyword">Alt+F5</span>: Format Code</li>
        <li><span class="keyword">Ctrl+Z</span>: Undo</li>
        <li><span class="keyword">Ctrl+Y</span>: Redo</li>
        <li><span class="keyword">Alt+Q</span>: Generate QR</li>
        <li><span class="keyword">Ctrl+F5</span>: Open Command Prompt</li>
        <li><span class="keyword">Ctrl+R</span>: Search and Replace</li>
    </ul>
    <footer>
        <p>&copy; 2024 Delta Studios. All rights reserved.</p>
    </footer>
</body>
</html>
"""

    webview.create_window("StellarScript Keyboard Shortcuts", html=script, width=500, height=440)
    webview.start()

def stellarKeywordWiki():
    script = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stellar Script - Language Reference</title>
    <link rel="icon" href="StellarScript.ico" type="image/x-icon">
    <style>
        body {
            font-family: Consolas, sans-serif;
            background-color: #2e2e2e;
            color: white;
            margin: 0;
            padding: 20px;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #bbbbbb;
        }
        ul {
            font-family: Arial, Helvetica, sans-serif;
            padding-left: 20px;
            user-select: text;
        }
        h1, h2 {
            color: #39c1d5;
        }
        pre {
            background-color: #3a3a3a;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
            position: relative;
            user-select: text;
        }
        .keyword {
            color: #ffbc00;
            user-select: text;
        }
        .category {
            margin: 20px 0 10px;
            font-size: 1.2em;
            color: #4bd5d5;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Stellar Script - Language Reference</h1>

    <h2>Core Keywords and Constructs</h2>

    <div class="category">Built-in Functions</div>
    <ul>
        <li><span class="keyword">include</span> &lt;stlmain.stlcore&gt; - Import core modules.</li>
        <li><span class="keyword">let</span> - Declare a variable.</li>
        <li><span class="keyword">func</span> - Define a function.</li>
        <li><span class="keyword">display()</span> - Output to the console.</li>
        <li><span class="keyword">if</span>, <span class="keyword">else</span>, <span class="keyword">elif</span> - Conditional statements.</li>
        <li><span class="keyword">for</span>, <span class="keyword">while</span> - Looping constructs.</li>
        <li><span class="keyword">return</span> - Return a value from a function.</li>
        <li><span class="keyword">true</span>, <span class="keyword">false</span>, <span class="keyword">none</span> - Boolean and null values.</li>
    </ul>

    <div class="category">Encoding</div>
    <ul>
        <li><span class="keyword">base32</span> - Base32 Encoding >> <span class="keyword">.encode ; .decode</span></li>
        <li><span class="keyword">base64</span> - Base64 Encoding >> <span class="keyword">.encode ; .decode</span></li>
        <li><span class="keyword">base128</span> - Base128 Encoding >> <span class="keyword">.encode ; .decode</span></li>
    </ul>

    <div class="category">Utilities</div>
    <ul>
        <li><span class="keyword">NetworkUtil</span> >> <span class="keyword">.check_connection() ; .run_speedtest() ; .get_public_ip() ; .search_on_google() ; .open_link() ; .get_http_status_code() ; .ping_host() ; .is_valid_url() ; .download_file() ; .get_dns_info() ; .get_geo_location() ; .get_headers()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">MathUtil</span> >> <span class="keyword">.factorial() ; .is_prime() ; .fibonacci() ; .square_root() ; .calculate_logarithm() ; .calculate_combinations() ; .calculate_permutations()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">GraphicUtil</span> >> <span class="keyword">.create_line_plot() ; .create_bar_plot()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">TimeUtil</span> >> <span class="keyword">.get_current_time() ; .measure_execution_time()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">SystemUtil</span> >> <span class="keyword">.get_system_info() ; .check_disk_space()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">FileUtil</span> >> <span class="keyword">.list_files_in_directory() ; .read_file() ; .write_file()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">GameUtil</span> >> <span class="keyword"> .setup() ; .draw_text() ; .load_image() ; .play_sound() ; .stop_sound() ; .handle_events() ; .fill_screen() ; .draw_rect() ; .draw_circle() ; .draw_line() ; .draw_polygon() ; .detect_collision() ; .update_screen()</span></li>
        <span class="keyword">---------------------------------------------------------------------------------------------------------------------------------<span>
        <li><span class="keyword">Stellar</span> >> <span class="keyword"> .displayMessage() ; base64 ; base32 ; base128</span></li>
    </ul>

    <h2>Examples</h2>
    <p>Here are some examples of Stellar Script code:</p>

    <h3>Random Number Generation</h3>
    <pre>
include &lt;stlmain.stlcore&gt;
include &lt;random&gt; as r

min_num = 1
max_num = 10

display(r.randint(min_num, max_num))
    </pre>

    <h3>Date and Time</h3>
    <pre>
include &lt;stlmain.stlcore&gt;
include &lt;datetime&gt; as dt

current_time = dt.get_current_time("%Y-%m-%d %H:%M:%S")
display("Current Time: " + current_time)
    </pre>

    <h3>Measure Execution Time</h3>
    <pre>
include &lt;stlmain.stlcore&gt;

func example():
    result = 0
    for i in range(1000000):
        result += i
    return result

execution_time = TimeUtil.measure_execution_time(example)
display("Execution Time: " + execution_time)
    </pre>

    <h3>Advanced Math</h3>
    <pre>
include &lt;stlmain.stlcore&gt;

number = 25
display("Square Root: " + MathUtil.square_root(number))
display("Logarithm: " + MathUtil.calculate_logarithm(100, 10))
    </pre>

    <h3>System Information</h3>
    <pre>
include &lt;stlmain.stlcore&gt;

info = SystemUtil.get_system_info()
display("System Info: " + str(info))
    </pre>

    <h3>DNS Info</h3>
    <pre>
include &lt;stlmain.stlcore&gt;

dns_info = NetworkUtil.get_dns_info("example.com")
display("DNS Info: " + str(dns_info))
    </pre>

    <h3>Bar Plot</h3>
    <pre>
include &lt;stlmain.stlcore&gt;

labels = ["A", "B", "C"]
values = [10, 20, 30]
GraphicUtil.create_bar_plot(labels, values)
    </pre>
    
    <h3>Run SpeedTest</h3>
    <pre>
include &lt;stlmain.stlcore&gt

test = NetworkUtil.run_speedtest()
display(test)
    </pre>c

    <h2>Special Notes</h2>
    <p>Make sure to include the core module <span class="keyword">include &lt;stlmain.stlcore&gt;</span> at the beginning of your code. Otherwise, the code may not run as expected.</p>

    <footer>
        <p>&copy; 2024 Delta Studios. All rights reserved.</p>
    </footer>
</body>
</html>
    """
   
    webview.create_window("StellarScript Keywords and Examples", html=script, resizable=False)
    webview.start()

def stellarScriptWiki():
    script = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stellar Script</title>
    <link rel="icon" href="StellarScript.ico" type="image/x-icon">
    <style>
        /* Default Light Mode Styles */
        body {
            font-family: "Consolas", sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            transition: background-color 0.3s, color 0.3s;
        }
        h1, h2 {
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .feature-list {
            list-style-type: none;
            padding-left: 20px;
        }
        .feature-list li {
            margin-bottom: 15px;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 12px;
            color: #777;
        }
        
        body.dark-mode {
            background-color: #121212;
            color: #e0e0e0;
        }
        .dark-mode .container {
            background-color: #1e1e1e;
            color: #e0e0e0;
        }
        .dark-mode footer {
            color: #bbb;
        }
        .dark-mode h1, .dark-mode h2 {
            color: #fff; /* Change header text color to white in dark mode */
        }
        .mode-toggle {
            position: absolute;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .mode-toggle:hover {
            background-color: #555;
        }
        .dark-mode .mode-toggle {
            background-color: #e0e0e0;
            color: #333;
        }
        .dark-mode .mode-toggle:hover {
            background-color: #bbb;
        }
        pre {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            margin-top: 20px;
        }
        .dark-mode pre {
            background-color: #2c2c2c;
            color: #e0e0e0;
        }
    </style>
</head>
<body>
    <button class="mode-toggle" onclick="toggleMode()">Switch to Dark Mode</button>

    <div class="container">
        <h1>Stellar Script</h1>
        <p><strong>Stellar Script</strong> is a new, specialized programming language designed to make development simpler, faster, and more efficient. With an emphasis on clarity and ease of use, Stellar Script brings powerful features to developers of all levels.</p>
        <p><strong>File Extension for StellarScript</strong> : *.slr *.stl *.stellar *.sx *.stx *.ssf</p>
        <p><strong>Core Extension for StellarScript</strong> : *.stlcore *.stlxcore</p>

        <h2>Key Features of Stellar Script</h2>
        <ul class="feature-list">
            <li><strong>Simplified Syntax</strong> – Stellar Script offers a clean and minimalistic syntax, perfect for both beginners and experienced developers. No unnecessary boilerplate code, just focus on writing logic.</li>
            <li><strong>Rich Standard Library</strong> – The language comes with an extensive set of libraries for handling common tasks like file I/O, networking, data structures, and more.</li>
            <li><strong>Better Error Handling</strong> – Robust error handling mechanisms such as try-catch blocks, clear error messages, and built-in suggestions to ensure smoother debugging.</li>
            <li><strong>Advanced Data Handling</strong> – Stellar Script provides built-in support for complex data types such as maps, sets, and custom classes, making data manipulation simpler and more powerful.</li>
            <li><strong>Concurrency and Asynchronous Programming</strong> – Native support for asynchronous tasks and concurrency, enabling fast, non-blocking code execution for modern applications.</li>
            <li><strong>Integrated Debugging & Profiling</strong> – Stellar Script integrates debugging and profiling directly into the development environment, giving you real-time feedback and ensuring your code runs efficiently.</li>
            <li><strong>Interoperability</strong> – Stellar Script allows integration with other languages (like Python), making it easy to reuse existing tools and libraries.</li>
            <li><strong>Optimized Execution</strong> – Stellar Script ensures fast execution with optimized bytecode compilation for various platforms.</li>
            <li><strong>User Friendly</strong> - Stellar Script is intuitive and beginner-friendly, featuring a GUI with syntax highlighting, autocompletion, and error detection. It offers extensive documentation, interactive tutorials, and strong community support, making coding accessible and efficient for users of all levels.</li>
            <li><strong>Customizable and Extensible</strong> – You can extend Stellar Script with custom modules and even write new built-in functions.</li>
        </ul>

        <h2>Run Stellar Script in DeltaEditor</h2>
        <p>Stellar Script is fully supported in <strong>DeltaEditor</strong>, a powerful and intuitive development environment designed specifically for Stellar Script and other languages. DeltaEditor provides a smooth user experience for writing, testing, and debugging Stellar code.</p>
        <p>Key features in DeltaEditor include:</p>
        <ul class="feature-list">
            <li>Syntax highlighting for Stellar Script, making code easier to read and understand.</li>
            <li>Real-time error checking and suggestions for faster coding and fewer bugs.</li>
            <li>Easy-to-use interface for running and debugging Stellar Script code directly within the editor.</li>
            <li>Built-in tools such as code formatting, search & replace, and file management to streamline the development process.</li>
            <li>Support for creating and executing Stellar Script projects with minimal setup.</li>
        </ul>

        <footer>
            <p>&copy; 2024 Delta Studios. All rights reserved.</p>
        </footer>
    </div>

    <script>
        function toggleMode() {
            var body = document.body;
            var modeToggleButton = document.querySelector('.mode-toggle');
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                modeToggleButton.textContent = 'Switch to Light Mode'; } else {
                modeToggleButton.textContent = 'Switch to Dark Mode'; }
        }
    </script>
</body>
</html>
    """
    
    webview.create_window("StellarScript Wiki", html=script)
    webview.start()

class AutoFill:
    def __init__(self, text_area):
        self.text_area = text_area
        self.suggestions_box = None
        self.keywords = self.keywords = [
            "input", "include", "let", "func", "display", "if", "else", "elif", 
            "for", "while", "return", "true", "false", "none",
            "FileUtil", "GameUtil", "MathUtil", "TimeUtil", 
            "SystemUtil", "GraphicUtil", "NetworkUtil", "switch", 
            "case", "default", "break", "continue", "try", 
            "except", "finally", "with", "as", "lambda", 
            "yield", "assert", "pass", "class", "self", 
            "super", "is", "not", "or", "and", "in", 
            "from", "raise", "global", "nonlocal", "del", 
            "async", "await", "str", "int", "float", "bool", 
            "list", "dict", "set", "tuple", "range", "len",
            "map", "filter", "reduce", "zip", "enumerate", 
            "all", "any", "max", "min", "sorted", "reversed",
            "abs", "sum", "pow", "round", "slice", "open", 
            "write", "read", "def","return", 
            "nonlocal", "breakpoint", 
            "exec", "compile", "eval", "type"]
        self.text_area.bind("<KeyRelease>", self.show_suggestions)

    def show_suggestions(self, event=None):
        word = self.get_current_word()
        if not word:
            self.destroy_suggestions_box()
            return

        suggestions = [kw for kw in self.keywords if kw.startswith(word)]
        if not suggestions:
            self.destroy_suggestions_box()
            return

        if not self.suggestions_box:
            self.create_suggestions_box()

        self.suggestions_box.delete(0, "end")
        for suggestion in suggestions:
            self.suggestions_box.insert("end", suggestion)

    def get_current_word(self):
        cursor_index = self.text_area.index("insert")
        line, column = map(int, cursor_index.split("."))
        line_text = self.text_area.get(f"{line}.0", f"{line}.end")
        word = line_text[:column].split()[-1] if line_text else ""
        return word.strip()

    def create_suggestions_box(self):
        x, y, _, _ = self.text_area.bbox("insert")
        abs_x = self.text_area.winfo_rootx() + x
        abs_y = self.text_area.winfo_rooty() + y + 20

        self.suggestions_box = tk.Listbox(self.text_area, height=5, bg="lightgray", selectbackground="blue")
        self.suggestions_box.place(x=abs_x, y=abs_y, anchor="nw")
        self.suggestions_box.bind("<ButtonRelease-1>", self.insert_suggestion)

    def insert_suggestion(self, event=None):
        if not self.suggestions_box:
            return
        selected = self.suggestions_box.get("active")
        cursor_index = self.text_area.index("insert")
        line, column = map(int, cursor_index.split("."))
        line_text = self.text_area.get(f"{line}.0", f"{line}.end")
        start = line_text[:column].rfind(" ") + 1
        self.text_area.delete(f"{line}.{start}", cursor_index)
        self.text_area.insert(cursor_index, selected)
        self.destroy_suggestions_box()

    def destroy_suggestions_box(self):
        if self.suggestions_box:
            self.suggestions_box.destroy()
            self.suggestions_box = None

class ThemeManager:
    def __init__(self, editor):
        self.editor = editor

    def set_light_theme(self):
        ctk.set_appearance_mode("Light")
        self.editor.text_area.configure(fg_color="white", bg_color="white")
        self.editor.output_area.configure(fg_color="white", bg_color="white")

    def set_dark_theme(self):
        ctk.set_appearance_mode("Dark")
        self.editor.text_area.configure(fg_color="#1d1e1e", bg_color="#1d1e1e")
        self.editor.output_area.configure(fg_color="#1d1e1e", bg_color="#1d1e1e")

    def set_ocean_theme(self):
        ctk.set_appearance_mode("Light")
        self.editor.text_area.configure(fg_color="#ADD8E6", bg_color="#ADD8E6")
        self.editor.output_area.configure(fg_color="#ADD8E6", bg_color="#ADD8E6")

class FontManager:
    def __init__(self, editor, text_area, output_area):
        self.editor = editor
        self.text_area = text_area
        self.output_area = output_area

    HEX_PATTERN = re.compile(r"^#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")
    
    def is_hex_color(self, input_string):
        return bool(self.HEX_PATTERN.match(input_string))

    def changeFont(self):
        accepted_fonts = [
            "ARIAL",
            "COURIER_NEW",
            "HELVETICA",
            "TIMES_NEW_ROMAN",
            "CONSOLAS",
            "COMIC_SANS_MS",
            "VERDANA",
            "TAHOMA",
            "COURIER",
            "LUCIDA_CONSOLE",
            "LUCIDA_SANS",
            "GEORGIA"
        ]

        askFont = simpledialog.askstring("FontManager", f"Accepted Font: {accepted_fonts}\nPlease input font that you want to change:")
        if askFont.upper() in accepted_fonts:
            self.text_area.configure(font=(askFont.replace("_", " ").title(), self.editor.font_size))
            self.output_area.configure(font=(askFont.replace("_", " ").title(), self.editor.font_size))
        else:
            Stellar.displayMessage(Stellar, "FontManager", "Error: \nFont is invalid!")

    def changeTextSize(self): 
        askSize = simpledialog.askinteger("FontManager", "Please type the text size you want to change: ")
        self.text_area.configure(font=(Editor(ctk.CTk()).font_name, askSize))
        self.output_area.configure(font=(Editor(ctk.CTk()).font_name, askSize))

    def changeTextColor(self):
        askColor = simpledialog.askstring("FontManager", "Please type text color or hex code you want to change: ")
        accepted_colors = [
        "red", "green", "blue", "yellow", "black", "white", "gray", "lightgray", 
        "darkblue", "orange", "purple", "pink", "brown", "cyan", "magenta", 
        "lightgreen", "darkgreen", "lightblue", "darkred", "lightyellow", 
        "lightcyan", "darkorange", "darkviolet", "lightpink", "gold", "beige", 
        "lavender", "indigo", "violet", "lightgoldenrod", "salmon", "skyblue", 
        "seashell", "forestgreen", "tomato", "springgreen", "steelblue", 
        "chocolate", "maroon", "slategray", "peachpuff", "mediumvioletred", 
        "mediumpurple", "orchid", "khaki", "plum", "ivory", "lightcoral", 
        "midnightblue", "mediumturquoise", "mediumseagreen", "darkslategray", 
        "mediumslateblue", "mistyrose", "wheat", "aquamarine", "darkseagreen"
        ]

        if askColor:
            askColor = askColor.strip() 

            if askColor.lower() in accepted_colors:
                self.text_area.configure(text_color=askColor.lower())
                self.output_area.configure(text_color=askColor.lower())
            elif self.is_hex_color(askColor):
                self.text_area.configure(text_color=askColor)
                self.output_area.configure(text_color=askColor)
            else:
                self.editor.displayError("Error: Invalid color!")

class Editor:
    def __init__(self, root):
        self.root = root
        self.root.title(stellar_config["windows_title"])
        self.root.geometry("900x600")

        self.text_area_frame = ctk.CTkFrame(root)
        self.text_area_frame.pack(expand=1, fill="both", padx=5, pady=5)

        self.text_area = ctk.CTkTextbox(self.text_area_frame, wrap="word", font=("Consolas", 15))
        self.text_area.pack(side="right", expand=1, fill="both", padx=5, pady=5)
        
        self.line_numbers = tk.Canvas(self.text_area_frame, width=45, background="#2e2e2e", highlightthickness=0)
        self.line_numbers.pack(side="left", fill="both")
        
        self.text_area.bind("<KeyRelease>", self.update_line_numbers)
        self.text_area.bind("<MouseWheel>", self.sync_scroll)
        self.text_area.bind("<Button-1>", self.sync_scroll)
        self.text_area.bind("<KeyRelease>", self.highlight_active_line)

        self.text_area.bind("<Configure>", self.update_line_numbers)

        self.update_line_numbers()
        self.highlight_active_line()

        self.output_frame = ctk.CTkFrame(root)
        self.output_frame.pack(fill="x", padx=5, pady=5)

        self.output_label = ctk.CTkLabel(self.output_frame, text="Output:", anchor="w")
        self.output_label.pack(side="top", fill="x", padx=5, pady=2)

        self.output_area = ctk.CTkTextbox(self.output_frame, height=100, font=("Consolas", 16), state="disabled")
        self.output_area.pack(fill="x", padx=5, pady=5)

        _font = self.text_area.cget("font")
        self.font_name, self.font_size = _font

        self.autofill = AutoFill(self.text_area)
        
        # ctk.set_appearance_mode("Dark")
        # ctk.set_default_color_theme("blue")
        # uncomment if needed

        menubar_font = font.Font(family="Consolas", size=13)
        menubar = tk.Menu(root, font=menubar_font)
        root.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)

        theme_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        theme_manager = ThemeManager(self)
        self.theme_manager = theme_manager
        theme_menu.add_command(label="Dark Theme", command=theme_manager.set_dark_theme)
        theme_menu.add_command(label="Light Theme", command=theme_manager.set_light_theme)
        theme_menu.add_command(label="Ocean Theme", command=theme_manager.set_ocean_theme)
        settings_menu.add_cascade(label="Change Themes", menu=theme_menu)

        font_manager = FontManager(self, self.text_area, self.output_area)
        font_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        font_menu.add_command(label="Change Font", command=font_manager.changeFont)
        font_menu.add_command(label="Change Text Size", command=font_manager.changeTextSize)
        font_menu.add_command(label="Change Text Color", command=font_manager.changeTextColor)
        settings_menu.add_cascade(label="Font Settings", menu=font_menu)

        settings_menu.add_separator()
        settings_menu.add_command(label="Reset to Deafult", command=self.set_deafult)

        import_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        export_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        
        file_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        file_menu.add_command(label="Open             Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save             Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save as          Ctrl+S", command=self.save_as_file)
        file_menu.add_cascade(label="Import", menu=import_menu)
        file_menu.add_cascade(label="Export", menu=export_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit             Alt+F4", command=self.exiteditor)

        tools_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        tools_menu.add_command(label="Error Lens                       Shift+F5", command=self.error_lenses)
        tools_menu.add_command(label="Format Code                        Alt+F5", command=self.format_code)
        tools_menu.add_command(label="Create QR for this code             Alt+Q", command=self.generate_qr)
        tools_menu.add_command(label="Open Command Prompt               Ctrl+F5", command=self.opencmd)
        tools_menu.add_separator()
        tools_menu.add_command(label="Run Code!                              F5", command=self.run_code)
        
        import_menu.add_command(label="Import Python file to StellarScript code", command=self.importpython)
        import_menu.add_command(label="Import JavaScript file to StellarScript code", command=self.importjs)
        
        export_menu.add_command(label="Export to Python file", command=self.exportpython)
        export_menu.add_command(label="Export to JavaScript file", command=self.exportjs)
        
        edit_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        edit_menu.add_command(label="Undo              Ctrl+Z", command=self.undo)
        edit_menu.add_command(label="Redo              Ctrl+Y", command=self.redo)
        edit_menu.add_command(label="Search & Replace  Ctrl+R", command=self.search_replace)

        help_menu = tk.Menu(menubar, tearoff=0, font=menubar_font)
        help_menu.add_command(label="Open StellarScript Wiki", command=stellarScriptWiki)
        help_menu.add_command(label="Open Keywords & Examples", command=stellarKeywordWiki)
        help_menu.add_command(label="Open Keyboard Shortcuts", command=keyboardshortcut)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.file_path = None
        self.undo_stack = [] ; self.redo_stack = []
        self.save_state()
        self.text_area.bind("<KeyRelease>", self.save_state) 
        self.text_area.bind("<KeyPress>", self.save_state) 
        self.debounce_active = False
        self.text_area.bind("<Control-z>", lambda event: self.undo())
        self.text_area.bind("<Control-y>", lambda event: self.redo()) 

        self.text_area.bind("<F5>", lambda event: self.run_code()) ; self.text_area.bind("<Control-s>", lambda event: self.save_file())
        self.text_area.bind("<Control-o>", lambda event: self.open_file()) ; self.text_area.bind("<Shift-F5>", lambda event: self.error_lenses())
        self.text_area.bind("<Alt-F5>", lambda event: self.format_code())
        self.text_area.bind("<Alt-q>", lambda event: self.generate_qr())
        self.text_area.bind("<Control-F5>", lambda event: self.opencmd()) ; self.text_area.bind("<Control-r>", lambda event: self.search_replace())
        self.text_area.bind("Alt-F4", lambda event: self.exiteditor())

    def importpython(self):
        pythonfile = filedialog.askopenfile(defaultextension="*.py", filetypes=[("Python Files", "*.py")])
        if not pythonfile:
            return msgbox.showerror("DeltaEditor", "No file selected!")
        with open(pythonfile.name, "r") as file:
            code = file.read()
        stl_code = self.untranslate(code) 
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", stl_code)
        msgbox.showinfo("DeltaEditor", "Code successfully imported!")

    def importjs(self):
        jsfile = filedialog.askopenfile(defaultextension="*.js", filetypes=[("JavaScript Files", "*.js")])
        if not jsfile:
            return msgbox.showerror("DeltaEditor", "No file selected!")
        with open(jsfile.name, "r") as file:
            code = file.read()
        stl_code = code
        stl_code = re.sub(r'let\s+(\w+)\s*=\s*(.+);', r'let \1 = \2;', stl_code)  # Example, no real change.
        stl_code = stl_code.replace("// include <stlmain.stlcore>", "include <stlmain.stlcore>")
        stl_code = re.sub(r'console\.log\((.+)\);', r'display(\1)', stl_code)
        stl_code = re.sub(r'if\s*\((.+)\)\s*\{', r'if (\1) {', stl_code)
        stl_code = re.sub(r'\}\s*else\s*\{', r'} else {', stl_code)
        stl_code = re.sub(
            r'for\s*\(\s*let\s+(\w+)\s*=\s*(\d+);\s*\1\s*<\s*(\d+);\s*\1\+\+\s*\)\s*\{',
            r'for (let \1 in range(\2, \3)) {', stl_code
        )
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", stl_code)
        msgbox.showinfo("DeltaEditor", "Code successfully converted to StellarScript!")

    def exportjs(self):
        code = self.text_area.get("1.0", "end").strip()
        js_code = re.sub(r'let\s+(\w+)\s*=\s*(.+);', r'let \1 = \2;', code)
        js_code = js_code.replace("include <stlmain.stlcore>", "// include <stlmain.stlcore>")
        js_code = re.sub(r'display\((.+)\)', r'console.log(\1);', js_code)
        js_code = re.sub(r'if\s*\((.+)\)\s*\{', r'if (\1) {', js_code)
        js_code = re.sub(r'\}\s*else\s*\{', r'} else {', js_code)
        js_code = re.sub(
            r'for\s*\(\s*let\s+(\w+)\s+in\s+range\((\d+),\s*(\d+)\)\s*\)\s*\{',
            r'for (let \1 = \2; \1 < \3; \1++) {', js_code
        )
        if code:
            filepath = filedialog.asksaveasfilename(defaultextension="*.js", filetypes=[("JavaScript Files", "*.js")])
            if filepath:
                with open(filepath, "w") as file:
                    file.write(js_code)
                    msgbox.showinfo("DeltaEditor", f"Successfuly create a javascript file!")
            else:
                msgbox.showwarning("DeltaEditor", "File save canceled!")
        else:
            msgbox.showwarning("DeltaEditor", "No code to export!")
        
    def exportpython(self):
        code = self.text_area.get("1.0", "end").strip()
        pythoncode = self.translate(code)
        if code:
            filepath = filedialog.asksaveasfilename(defaultextension="*.py", filetypes=[("Python Files", "*.py")])
            if filepath:
                with open(filepath, "w") as file:
                    file.write(pythoncode)
                    msgbox.showinfo("DeltaEditor", f"Successfuly create a python file!")
            else:
                msgbox.showwarning("DeltaEditor", "File save canceled!")
        else:
            msgbox.showwarning("DeltaEditor", "No code to export!")
    
    def update_line_numbers(self, event=None):  
        self.line_numbers.delete("all")
        i = self.text_area.index("@0,0")
        while True:
            dline_index = self.text_area.dlineinfo(i)
            if dline_index is None:
                break
            y = dline_index[1]
            line_number = f"> {str(i).split(".")[0]} <"
            self.line_numbers.create_text(2, y, anchor="nw", text=line_number, fill="white", font=("Consolas", 10))
            i = self.text_area.index(f"{i}+1line")

    def sync_scroll(self, event=None):
        self.line_numbers.yview_moveto(self.text_area.yview()[0])

    def highlight_active_line(self, event=None):
        self.line_numbers.delete("highlight")
        self.line_numbers.delete("all")

        current_line = self.text_area.index("insert").split(".")[0]

        i = self.text_area.index("@0,0")
        while True:
            dline_index = self.text_area.dlineinfo(i)
            if dline_index is None:
                break
            y = dline_index[1]
            line_number = str(i).split(".")[0]
            display_number = f"> {line_number} <" if line_number == current_line else f"  {line_number}"
            self.line_numbers.create_text(2, y, anchor="nw", text=display_number, fill="white", font=("Consolas", 10))
            i = self.text_area.index(f"{i}+1line")

    def exiteditor(self):
        if self.text_area.get("1.0", "end").strip():
            prompt = msgbox.askyesnocancel("DeltaEditor", "WARNING : Your code is not saved! \nDo you want to save changes in this code?")
            if prompt == False:
                self.root.destroy()
            elif prompt == True:  
                if self.file_path: 
                    if self.save_file(): 
                        self.root.destroy()
                else: 
                    if self.save_as_file(): 
                        self.root.destroy()
            elif prompt == None: 
                pass
        else:
            self.root.destroy()

    def opencmd(self): os.system("start cmd") 

    def set_deafult(self):
        self.theme_manager.set_dark_theme()
        self.text_area.configure(text_color="white", font=("Consolas", 15))
        self.output_area.configure(text_color="white", font=("Consolas", 16))

    def displayError(self, text:str):
        self.output_area.configure(state="normal")
        self.output_area.delete("1.0", "end")
        self.output_area.insert("1.0", text)
        self.output_area.configure(state="disabled")    

    def display(self, text:str):
        self.output_area.configure(state="normal")
        self.output_area.delete("1.0", "end")
        self.output_area.insert("1.0", text)
        self.output_area.configure(state="disabled")

    def error_lenses(self, isForQR=False):
        stellar_code = self.text_area.get("1.0", "end").strip()
        required_module = "include <stlmain.stlcore>"
        errors = []

        if stellar_code.count(required_module) == 0:
            errors.append(f"Error: Missing required Stellar Core module! Please include '{required_module}'.")
        elif stellar_code.count(required_module) > 1:
            errors.append(f"Error: Too many '{required_module}' declarations! Only one is allowed.")

        invalid_keywords = ["def", "print", "import", "help"]
        for keyword in invalid_keywords:
            if invalid_keywords[0] in stellar_code:
                errors.append(f"Error: Keyword '{keyword}' is not defined in StellarScript. Did you mean 'func'?")
            if invalid_keywords[1] in stellar_code:
                errors.append(f"Error: Keyword '{keyword}' is not defined in StellarScript. Did you mean 'display'?")
            if invalid_keywords[2] in stellar_code:
                errors.append(f"Error: Keyword '{keyword}' is not defined in StellarScript. Did you mean 'include'?")
            if invalid_keywords[3] in stellar_code:
                errors.append(f"Error: Keyword '{keyword}' is not defined in StellarScript.")

        if stellar_code.count("(") != stellar_code.count(")"):
            errors.append("Error: Unmatched parentheses. Check your opening and closing parentheses.")
        if stellar_code.count("\"") % 2 != 0 or stellar_code.count("'") % 2 != 0:
            errors.append("Error: Unmatched quotes. Ensure all quotes are properly closed.")

        for line in stellar_code.splitlines():
            line = line.strip()
            if line.startswith("for ") or line.startswith("while "):
                if ":" not in line:
                    errors.append(f"Error: Missing ':' at the end of loop: '{line}'")
            if line.startswith("if ") or line.startswith("elif "):
                if ":" not in line:
                    errors.append(f"Error: Missing ':' at the end of condition: '{line}'")
        if errors:
            error_message = "\n".join(errors)
            if isForQR:
                return "Error"
            msgbox.showerror("DeltaEditor", f"Errors found:\n{error_message}")
            return "Error"
        else:
            if not isForQR:
                msgbox.showinfo("DeltaEditor", "No errors found! Your code looks great!")
            return "NoError"

    def generate_qr(self):
        code = self.text_area.get("1.0", "end").strip()

        if not code:
            return msgbox.showwarning("DeltaEditor", "No code to generate QR.")

        total_lines = len(code.splitlines())
        max_lines = 100  # 59 (L) | 46 (M) | 36 (Q) | 28 (H)

        if total_lines > max_lines:
            return msgbox.showerror("DeltaEditor", f"Code exceeds the maximum limit of {max_lines} lines. Please reduce your code.")
        
        if self.error_lenses(True) == "NoError":
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(f"// Hey, look at this cool Stellar code I made!\n\n{code}")
            qr.make(fit=True)

            theme_colors = {
                "default": ("black", "white"),
                "forest": ("#411900", "lightgreen"),
                "ocean": ("lightblue", "#0066cc"),
                "dark": ("white", "black")
            }

            theme = simpledialog.askstring("QR Code", "Type theme (default, forest, ocean, dark): ")
            fill_color, back_color = theme_colors.get(theme.lower(), theme_colors["default"]) if theme else theme_colors["default"]

            progress_window = ctk.CTkToplevel(self.root)
            progress_window.title("Generating...")
            progress_window.geometry("300x100")
            ctk.set_appearance_mode("dark")  
            ctk.set_default_color_theme("dark-blue") 
            
            progress_label = ctk.CTkLabel(progress_window, text="Generating QR Code, please wait... ( 0% )")
            progress_label.pack(pady=5)
            
            progress = ctk.CTkProgressBar(progress_window, width=250)
            progress.pack(pady=10)
            progress.set(0)
            
            total_steps = 100
            speed = 0.001 * total_lines

            def update_progress(step=0):
                if step <= total_steps:
                    progress.set(step / total_steps)
                    progress_label.configure(text=f"Generating QR Code, please wait... ( {int((step / total_steps) * 100)}% )")
                    progress_window.update_idletasks()
                    self.root.after(int(speed * 1000), update_progress, step + 1)
                else:
                    progress_window.destroy()
                    
                    img = qr.make_image(fill_color=fill_color, back_color=back_color)

                    img = img.resize((700, 700))

                    temp_image = BytesIO()
                    img.save(temp_image, format="PNG")
                    temp_image.seek(0)
                    img_pil = Image.open(temp_image)
                    img_width, img_height = img_pil.size
                    ctk_image = ctk.CTkImage(dark_image=img_pil, size=(img_width, img_height))
                    
                    qr_window = ctk.CTkToplevel(self.root)
                    qr_window.title("QR Code")
                    qr_window.geometry(f"{img_width}x{img_height}")
                    qr_label = ctk.CTkLabel(qr_window, image=ctk_image, text="")
                    qr_label.pack()
                    qr_window.mainloop()

            update_progress()

    def format_code(self):
        code = self.text_area.get("1.0", "end").strip()
        
        if not code:
            msgbox.showwarning("DeltaEditor", "No code to format.")
            return
        
        formatted_code = self.auto_indent(code)
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", formatted_code)

    def auto_indent(self, code):
        lines = code.splitlines()
        indented_code = ""
        indent_level = 0

        for line in lines:
            stripped = line.strip()
            if stripped.endswith(":"):
                indented_code += "    " * indent_level + line.strip() + "\n"
                indent_level += 1
            elif stripped == "":
                indented_code += "\n"
            else:
                indented_code += "    " * indent_level + line.strip() + "\n"

                if indent_level > 0 and stripped.startswith("return"):
                    indent_level -= 1

        return indented_code

    def undo(self):
        if (self.undo_stack):
            current_text = self.text_area.get("1.0", "end-1c")
            self.redo_stack.append(current_text)
            if stellar_config["debug_mode"]: 
                print("Redo Stack After Append:", self.redo_stack)

            last_text = self.undo_stack.pop()
            if stellar_config["debug_mode"]: 
                print("Undo Stack After Pop:", self.undo_stack)

            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", last_text)

    def redo(self):
        if (self.redo_stack):
            current_text = self.text_area.get("1.0", "end-1c")
            self.undo_stack.append(current_text)
            if stellar_config["debug_mode"]: 
                print("Undo Stack After Append:", self.undo_stack)

            next_text = self.redo_stack.pop()
            if stellar_config["debug_mode"]: 
                print("Redo Stack After Pop:", self.redo_stack)

            self.text_area.delete("1.0", "end")
            self.text_area.insert("1.0", next_text)

    def save_state(self, event=None):
        ignored_shortcuts = {
            "F5", "Control-s", "Control-o", "Shift-F5",
            "Alt-F5", "Control-z", "Control-y", "Alt-q",
            "Control-F5", "Control-r", "Alt-F4"
        }
        
        if event:
            keys_pressed = f"{'Control-' if event.state & 4 else ''}" \
                        f"{'Shift-' if event.state & 1 else ''}" \
                        f"{'Alt-' if event.state & 8 else ''}" \
                        f"{event.keysym}"
            if keys_pressed in ignored_shortcuts:
                return
            
        if stellar_config["debug_mode"]:
            print("Redo Stack Before Pop:", self.redo_stack)
            print("Undo Stack Before Append:", self.undo_stack)

        current_text = self.text_area.get("1.0", "end-1c")
        if not self.undo_stack or self.undo_stack[-1] != current_text:
            self.undo_stack.append(current_text)
            self.redo_stack.clear()

    def debounce_off(self):
        self.debounce_active = False

    def search_replace(self):
        search_term = simpledialog.askstring("Search", "Enter text to search:")
        if search_term:
            replace_term = simpledialog.askstring("Replace", f"Replace '{search_term}' with:")
            if replace_term is not None:
                code = self.text_area.get("1.0", "end")
                code = code.replace(search_term, replace_term)
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", code)

    def translate(self, stellar_code: str):
        python_code:str
        python_code = stellar_code.replace("func", "def").replace("display(", "print(")
        python_code = python_code.replace("false", "False").replace("true", "True").replace("none", "None")
        python_code = python_code.replace("// ", "#")
        python_code = python_code.replace("include <stlmain.stlcore>", "# include <stlmain.stlcore>")
        python_code = python_code.replace("--", "-=1").replace("++", "+=1")
        python_code = python_code.replace(";", "")
        python_code = re.sub(r'include\s*<([^>]+)>', r'import \1', python_code)
        if "include <stlmain.stlcore>" not in stellar_code:
            self.displayError("Error:\n CoreMissingError: Missing required Stellar Core module! Please use 'include <stlmain.stlcore>'.\n")
            return ""
        if stellar_config["anable_secret"]:
            if not hasattr(self, 'isSecretLogin'): self.isSecretLogin = False
            if "Stellar.Secret" in stellar_code and not self.isSecretLogin:
                pw = simpledialog.askstring("DeltaEditor", "Oops, I think you are using the secret function! Please insert the password here: ")
                if (pw and str(pw.lower()) == "stellarscript2024") or (pw and str(pw.lower()) == "deltastudios") or (pw and str(pw.lower()) == "deltaeditor&stellarscript") or (pw and str(pw.lower()) == "supersecret") or (pw and str(pw.lower()) == "stellarscriptisthebest"):
                    msgbox.showinfo("Delta Editor", "Password was correct!")
                    self.isSecretLogin = True  
                    msgbox.showinfo("StellarScript", "If you want to see the list of function you can use 'Stellar.Secret.showHelp()'")
                    return python_code
                else:
                    msgbox.showinfo("DeltaEditor", "Password was not correct!")
                    return ""
            if "Secret" in stellar_code and self.isSecretLogin: return python_code  
        if "def" in stellar_code:
            self.displayError("Error:\nName 'def' is not defined.\n")
        elif "print" in stellar_code:
            self.displayError("Error:\nName 'print' is not defined.\n")
        elif "import" in stellar_code:
            self.displayError("Error:\nName 'import' is not defined.\n")
        elif "help" in stellar_code:
            self.displayError("Error:\nName 'help' is not defined.\n")
        else:
            return python_code

    def untranslate(self, python_code):
        stellar_code = python_code.replace("def", "func").replace("print(", "display(")
        stellar_code = stellar_code.replace("# import stlmain.stlcore", "include <stlmain.stlcore>")
        stellar_code = stellar_code.replace("False", "false").replace("True", "true").replace("None", "none")
        stellar_code = stellar_code.replace("#", "// ")
        stellar_code = stellar_code.replace("-=1", "--").replace("+=1", "++")
        stellar_code = re.sub(r'import\s+(\S+)', r'include <\1>', stellar_code)
        
        return stellar_code

    def open_file(self):
        current_content = self.text_area.get("1.0", "end").strip()
        if current_content:
            response = msgbox.askyesnocancel("Unsaved Changes", "Do you want to replace the current content? 'Yes' to replace, 'No' to open in a new window, or 'Cancel' to abort.")
            if response is None: return
            elif not response: new_window = Toplevel(self.root) ; new_editor = Editor(new_window) ; new_window.after(100, new_editor.open_file) ; return
        file_path = filedialog.askopenfilename(filetypes=[("Stellar Script Files", "*.slr *.stl *.stellar *.sx *.stx *.ssf")])
        if file_path:
            try:
                with open(file_path, "r") as file: content = file.read()
                self.text_area.delete("1.0", "end") ; self.text_area.insert("1.0", content) ; self.file_path = file_path ; self.root.title(f"DeltaEditor - Stellar Editor & Executor @ {file_path}")
            except Exception as e: msgbox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get("1.0", "end").strip())
                msgbox.showinfo("Success", "File saved successfully!")
                return True
            except Exception as e:
                msgbox.showerror("Error", f"Could not save file: {e}")
                return False  
        else:
            return self.save_as_file()  
            
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".stl",
                                                filetypes=[("Stellar Script Files", "*.slr *.stl *.stellar *.sx *.stx *.ssf")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get("1.0", "end").strip())
                self.file_path = file_path
                self.root.title(f"Stellar Code Editor - {file_path}")
                msgbox.showinfo("Success", "File saved successfully!")
                return True  
            except Exception as e:
                msgbox.showerror("Error", f"Could not save file: {e}")
                return False  
        return False  

    def run_code(self):
        stellar_code = self.text_area.get("1.0", "end").strip()
        if not stellar_code:
            msgbox.showwarning("Warning", "No code to run!")
            return

        python_code = self.translate(stellar_code)
        if not python_code:
            return

        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        try:
            sys.stdout = stdout_buffer
            sys.stderr = stderr_buffer

            exec(python_code)

            output = stdout_buffer.getvalue()
            error = stderr_buffer.getvalue()

            self.output_area.configure(state="normal")
            self.output_area.delete("1.0", "end")
            if output:
                self.output_area.insert("1.0", output)
            if error:
                self.output_area.insert("end", f"Error:\n{error}")
            self.output_area.configure(state="disabled")

        except Exception as e:
            self.displayError(f"Error:\n{e}\n")

        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

# builtin functions
def input(prompt: object = "", /) -> str:
    answer = simpledialog.askstring("Input", prompt)
    return answer

class NetworkUtil:
    @staticmethod
    def check_connection() -> bool:
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    @staticmethod
    def get_public_ip() -> str:
        try:
            response = requests.get('https://api.ipify.org').text
            return response
        except requests.RequestException:
            return "Could not fetch IP."

    @staticmethod
    def search_on_google(query: str) -> str:
        try:
            search_query = urllib.parse.quote_plus(query) 
            url = f"https://www.google.com/search?q={search_query}"
            return url
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def open_link(url: str) -> None:
        try:
            webbrowser.open(url) 
        except Exception as e:
            Editor.displayError(f"Error opening the link: {str(e)}\n")

    @staticmethod
    def get_http_status_code(url: str) -> int:
        try:
            response = requests.get(url)
            return response.status_code
        except requests.RequestException:
            return -1  # Return -1 if the request fails

    @staticmethod
    def ping_host(host: str) -> bool:
        try:
            # Ping the host to check if it's reachable
            socket.create_connection((host, 80), timeout=5)
            return True
        except (socket.timeout, socket.error):
            return False

    @staticmethod
    def is_valid_url(url: str) -> bool:
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])  
        except ValueError:
            return False
        
    @staticmethod
    def get_dns_info(domain: str) -> dict:
        try:
            # Perform a DNS lookup
            dns_info = socket.gethostbyname_ex(domain)
            return {
                'hostname': dns_info[0],
                'ip_addresses': dns_info[2]
            }
        except socket.gaierror:
            return {"error": "Could not resolve the domain"}

    @staticmethod
    def get_geo_location(ip: str) -> dict:
        try:
            response = requests.get(f"https://ipapi.co/{ip}/json/")
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def get_headers(url: str) -> dict:
        try:
            response = requests.head(url)
            return response.headers
        except requests.RequestException as e:
            return {"error": str(e)}

    @staticmethod
    def run_speedtest():
        attempts = stellar_config['networkutil']['speedtest_max_attemps']
        for attempt in range(attempts):
            try:
                msgbox.showinfo("NetworkUtil - SpeedTest", "Please wait while we run speedtest...")
                test = speedtest.Speedtest()
                test.get_best_server()
                test.download()
                test.upload()
                test.results.share()
                result = test.results.dict()
                down = str(round(result['download'] / 1_000_000, 3)) + " Mbps"
                up = str(round(result['upload'] / 1_000_000, 3)) + " Mbps"
                ping = str(result['ping']) + " ms"
                return f"Download: {down}\nUpload: {up}\nPing: {ping}"
            except speedtest.SpeedtestHTTPError as e:
                if e.code == 403:
                    if attempt < attempts - 1: 
                        msgbox.showwarning("NetworkUtil - SpeedTest", f"Forbidden error. Retrying... ({attempt + 1}/{attempts})")
                        time.sleep(2)  
                    else:
                        msgbox.showerror("NetworkUtil - SpeedTest", "Forbidden error. Maximum retries reached.")
                        return "Speedtest failed due to Forbidden error."
                else:
                    msgbox.showerror("NetworkUtil - SpeedTest", f"HTTP error occurred: {e}")
                    return f"Error: {e}"
            except speedtest.ConfigRetrievalError as e:
                msgbox.showerror("NetworkUtil - SpeedTest", f"Config retrieval error occurred: {e}")
                return f"Error: {e}"
            except Exception as e:
                msgbox.showerror("NetworkUtil - SpeedTest", f"An unexpected error occurred: {e}")
                return f"Unexpected Error: {e}"
        
class MathUtil:
    @staticmethod
    def factorial(n: int) -> int:
        return math.factorial(n)

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(n: int) -> list[int]:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq

    @staticmethod
    def square_root(number: float) -> float:
        return math.sqrt(number)

    @staticmethod
    def calculate_logarithm(number: float, base: float = 10) -> float:
        return math.log(number, base)

    @staticmethod
    def calculate_combinations(n: int, r: int) -> int:
        return math.comb(n, r)

    @staticmethod
    def calculate_permutations(n: int, r: int) -> int:
        return math.perm(n, r)
    
    @staticmethod
    def pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)

class GraphicUtil:
    @staticmethod
    def create_line_plot(x, y):
        plt.plot(x, y)
        plt.title("Line Plot")
        plt.show()

    @staticmethod
    def create_bar_plot(labels, values):
        plt.bar(labels, values)
        plt.title("Bar Plot")
        plt.show()

class FileUtil:
    @staticmethod
    def list_files_in_directory(directory_path: str) -> list[str]:
        try:
            return os.listdir(directory_path)
        except Exception as e:
            return [f"Error: {str(e)}"]

    @staticmethod
    def read_file(file_path: str) -> str:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def write_file(file_path: str, content: str) -> str:
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            return "File written successfully!"
        except Exception as e:
            return f"Error: {str(e)}"

class TimeUtil:
    @staticmethod
    def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> str:
        return time.strftime(format)

    @staticmethod
    def measure_execution_time(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, f"Execution time: {execution_time:.2f} seconds"

class SystemUtil:
    @staticmethod
    def get_system_info() -> dict:
        return {
            "OS": os.name,
            "Platform": sys.platform,
            "StellarScript Version: " : __version__
        }

    @staticmethod
    def check_disk_space() -> str:
        total, used, free = shutil.disk_usage(os.getcwd())
        total_space = total / (1024 ** 3)
        free_space = free / (1024 ** 3)
        return f"Total: {total_space:.2f} GB, Free: {free_space:.2f} GB"
    
class GameUtil:
    @staticmethod
    def setup(width=800, height=600, title=""):
        pygame.init()
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        colors = {
            'WHITE': (255, 255, 255),
            'BLACK': (0, 0, 0),
            'RED': (255, 0, 0),
            'GREEN': (0, 255, 0),
            'BLUE': (0, 0, 255)
        }

        clock = pygame.time.Clock()

        return screen, colors, clock

    @staticmethod
    def draw_text(screen, text, font_size, color, position):
        font = pygame.font.SysFont('Arial', font_size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, position)

    @staticmethod
    def load_image(path, width=None, height=None):
        image = pygame.image.load(path)
        if width and height:
            image = pygame.transform.scale(image, (width, height))
        return image

    @staticmethod
    def play_sound(path, loop=False):
        sound = pygame.mixer.Sound(path)
        if loop:
            sound.play(loops=-1)  
        else:
            sound.play()

    @staticmethod
    def stop_sound():
        pygame.mixer.stop()

    @staticmethod
    def update_screen():
        pygame.display.update()

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    @staticmethod
    def fill_screen(screen, color):
        screen.fill(color)

    @staticmethod
    def draw_rect(screen, x, y, width, height, color):
        pygame.draw.rect(screen, color, (x, y, width, height))

    @staticmethod
    def draw_circle(screen, x, y, radius, color):
        pygame.draw.circle(screen, color, (x, y), radius)

    @staticmethod
    def draw_line(screen, start_pos, end_pos, color, width=1):
        pygame.draw.line(screen, color, start_pos, end_pos, width)

    @staticmethod
    def draw_polygon(screen, points, color):
        pygame.draw.polygon(screen, color, points)

    @staticmethod
    def detect_collision(rect1, rect2):
        return rect1.colliderect(rect2)

    @staticmethod
    def run_game():
        screen, colors, clock = GameUtil.setup()

        while True:
            GameUtil.handle_events()
            GameUtil.fill_screen(screen, colors['WHITE']) 
            GameUtil.update_screen()
            clock.tick(60)  # 60 FPS

# Stellar Core functions
class Stellar:
    def __init__(self):
        self.self = self
        self.outputText = Editor(ctk.CTk()).output_area
        self.inputText = Editor(ctk.CTk()).text_area

    def displayMessage(self, gui_title, gui_text, gui_type = "info"):
        accepted_type = ["info", "warning", "error"]
        if gui_type.lower() in accepted_type:
            if gui_type.lower() == "info":
                msgbox.showinfo(gui_title, gui_text)
            if gui_type.lower() == "warning":
                msgbox.showwarning(gui_title, gui_text)
            if gui_type.lower() == "error":
                msgbox.showerror(gui_title, gui_text)
        else: self.outputText.insert("1.0", f"Error:\n {gui_type} is not accepted type! please use: info, warning, or error")

    class base64:
        @staticmethod
        def encode(data: str) -> str:
            encoded_bytes = bs64.b64encode(data.encode('utf-8'))
            return encoded_bytes.decode('utf-8')

        @staticmethod
        def decode(data: str) -> str:
            decoded_bytes = bs64.b64decode(data.encode('utf-8'))
            return decoded_bytes.decode('utf-8')

    class base32:
        @staticmethod
        def encode(data: str) -> str:
            encoded_bytes = bs64.b32encode(data.encode('utf-8'))
            return encoded_bytes.decode('utf-8')

        @staticmethod
        def decode(data: str) -> str:
            decoded_bytes = bs64.b32decode(data.encode('utf-8'))
            return decoded_bytes.decode('utf-8')

    class base128:
        @staticmethod
        def encode(data: str) -> str:
            data_bytes = data.encode('utf-8')
            encoded = []
            for byte in data_bytes:
                high = byte >> 1
                low = byte & 0x01
                encoded.append(high)
                encoded.append(low)

            return ' '.join(map(str, encoded)).strip()
        
        @staticmethod
        def decode(data: str) -> str:
            data_list = list(map(int, data.split()))
            if len(data_list) % 2 != 0:
                raise ValueError("Input length must be even.")

            decoded = bytearray()
            for i in range(0, len(data_list), 2):
                high = data_list[i] << 1
                low = data_list[i + 1]
                decoded.append(high | low)
   
            return decoded.decode('utf-8')

    if stellar_config["anable_secret"]:
        class Secret:
            def showHelp():
                script = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Secret Class Methods</title>
            <style>
                body {
                    font-family: Consolas, sans-serif;
                    background-color: #2e2e2e;
                    color: white;
                    margin: 0;
                    padding: 20px;
                }
                footer {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 0.9em;
                    color: #bbbbbb;
                }
                ul {
                    font-family: Arial, Helvetica, sans-serif;
                    padding-left: 20px;
                    user-select: text;
                }
                h1, h2 {
                    color: #39c1d5;
                }
                pre {
                    background-color: #3a3a3a;
                    padding: 10px;
                    border-radius: 5px;
                    overflow: auto;
                    position: relative;
                    user-select: text;
                }
                pre {
                    color: #ffbc00;
                    user-select: text;
                }
                .showhelp {
                    color: #ffbc00;
                    user-select: text;
                }
                .category {
                    margin: 20px 0 10px;
                    font-size: 1.2em;
                    color: #4bd5d5;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Secret Class Methods</h1>
            <section class="category">
                <h2>1. Cat</h2>
                <pre>
        Secret.cat()
                </pre>
            </section>
            <section class="category">
                <h2>2. Quote</h2>
                <pre>
        Secret.quote()
                </pre>
            </section>
            <section class="category">
                <h2>3. Surprise Gacha</h2>
                <pre>
        Secret.surprise_gacha()
                </pre>
            </section>
            <section class="category">
                <h2>4. Fortune Cookie</h2>
                <pre>
        Secret.fortune_cookie()
                </pre>
            </section>
            <section class="category">
                <h2>5. Random Web</h2>
                <pre>
        Secret.randomweb()
                </pre>
            </section>
            
            <h2>Special Notes</h2>
            <p>If you want to see this help you can use <span class="showhelp">Stellar.Secret.showHelp()<span></p>

            <footer>
                <p>&copy; 2024 Delta Studios. All rights reserved.</p>
            </footer>
        </body>
        </html>
            """
                webview.create_window("StellarScript Secrets", html=script)
                webview.start()

            def cat():
                print("""
                         meow :3 |\\__/|     (`\\ 
                               _.|o o  |_   ) ) 
                               -(((---(((--------""")
            
            def quote():
                quotes = [
                    "The early bird catches the worm. Unless it’s a cat!",
                    "Be yourself; everyone else is already taken. - Oscar Wilde",
                    "Life is short. Smile while you still have teeth.",
                    "Coding: Turning coffee into code since forever."
                ] ; print(random.choice(quotes))

            def surprise_gacha():
                rewards = [
                    "You win a virtual cookie! 🍪",
                    "Congratulations, you found a secret smile! 😊",
                    "Here’s a virtual high-five! 🙌",
                    "You’ve unlocked the power of imagination. ✨",
                    "Oops, try again! Better luck next time."
                ] ; print(random.choice(rewards))

            def fortune_cookie():
                fortunes = [
                    "You will get 1 Million Dollar soon",
                    "You will find a new opportunity soon.",
                    "Great things are coming your way, be patient!",
                    "A new friendship will brighten your day.",
                    "Your hard work will soon pay off.",
                    "Someone is thinking of you right now!"
                ] ; print(random.choice(fortunes))

            def randomweb():
                links = {
                    "itch.io": "https://www.itch.io",
                    "Twitch": "https://www.twitch.tv",
                    "Steam": "https://www.steampowered.com",
                    "Epic Games Store": "https://www.epicgames.com",
                    "Minecraft": "https://www.minecraft.net",
                    "Roblox": "https://www.roblox.com",
                    "IGN": "https://www.ign.com",
                    "Unity": "https://www.unity.com",
                    "Unreal Engine": "https://www.unrealengine.com",
                    "Chess.com": "https://www.chess.com",
                    "Google": "https://www.google.com",
                    "Wikipedia": "https://www.wikipedia.org",
                    "GitHub": "https://www.github.com",
                    "Stack Overflow": "https://www.stackoverflow.com",
                    "npm": "https://www.npmjs.com",
                    "Python.org": "https://www.python.org",
                    "W3Schools": "https://www.w3schools.com",
                    "Dev.to": "https://dev.to",
                    "CodePen": "https://codepen.io",
                    "Replit": "https://replit.com",
                    "GeeksforGeeks": "https://www.geeksforgeeks.org",
                    "FreeCodeCamp": "https://www.freecodecamp.org",
                    "SoloLearn": "https://www.sololearn.com",
                    "Code.org": "https://www.code.org",
                    "Scratch": "https://scratch.mit.edu",
                    "Pygame": "https://www.pygame.org",
                    "D3.js": "https://d3js.org",
                    "Three.js": "https://threejs.org",
                    "OpenAI": "https://openai.com",
                    "PyTorch": "https://pytorch.org",
                    "Rust Programming": "https://www.rust-lang.org",
                    "Go Programming": "https://go.dev",
                    "OverAPI": "https://overapi.com",
                    "GitLab": "https://about.gitlab.com",
                    "CodeSandbox": "https://codesandbox.io",
                    "Jupyter Notebook": "https://jupyter.org",
                    "Anaconda": "https://www.anaconda.com",
                    "PyPI": "https://pypi.org",
                    "C++ Reference": "https://en.cppreference.com",
                    "Java T Point": "https://www.javatpoint.com",
                    "Oracle Java": "https://www.oracle.com/java",
                    "React": "https://react.dev",
                    "Vue.js": "https://vuejs.org",
                    "TailwindCSS": "https://tailwindcss.com",
                }
                name, picked_link = random.choice(list(links.items()))
                webview.create_window(f"{name} @ {picked_link}", picked_link)
                webview.start()

########################################### - Run The Program - ###########################################

if __name__ == "__main__":
    root = ctk.CTk()
    app = Editor(root)
    root.protocol("WM_DELETE_WINDOW", app.exiteditor) # dialog protocol
    root.mainloop()
    
#  ______  _______      _______ _______     _______ _______ _     _ ______  _____  _____  _______ 
#  |     \ |______ |       |    |_____|     |______    |    |     | |     \   |   |     | |______
#  |_____/ |______ |_____  |    |     |     ______|    |    |_____| |_____/ __|__ |_____| ______|  Software Factory
