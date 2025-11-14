# 🐢✨ Turtle Art & Login System — Combined README

## 📌 Overview

This repository includes two separate Python projects combined in a single documentation file:

1. **Turtle Art Drawing Project** — A detailed and artistic illustration created entirely using Python's `turtle` graphics module. The drawing features complex shapes, curves, character elements, and decorative components. It includes figures resembling Krishna, hair patterns, peacock decorations, and other artistic elements.

2. **Command-Line Login System** — A simple username/password authentication script that includes creative feedback messages and timed loading effects. It demonstrates conditional logic, user input handling, and basic CLI UI behavior.

---

## 🖼️ 1. Turtle Art Drawing Project

### 🎨 Description

This Python script uses the `turtle` module to draw an intricate artwork. It includes:

* Multiple turtles to draw different components
* Precise geometric curves using circles, arcs, and position adjustments
* Layered pen sizes to add depth
* Filled shapes for stylistic effects
* A final decorative frame

The drawing is generated entirely through mathematical movements — no images are used.

### ▶️ How to Run

1. Make sure you have Python installed.
2. Run the script:

```bash
python turtle_art.py
```

3. A window will open and display the full artwork. The drawing may take a moment since it's highly detailed.

---

## 🔐 2. Login System Project

### 🔎 Description

This Python program simulates a basic login system using:

* Hard-coded username and password
* Conditional checks for 4 authentication scenarios
* Creative and unique on-screen messages
* Timed loading animations via `time.sleep()`

**This script is good for learning:**

* Input handling
* Conditionals (`if`, `elif`, `else`)
* Basic user experience feedback
* Delays and loading effects

### ▶️ How to Run

```bash
python login.py
```

When prompted:

* Enter the correct username: `tcm9798`
* Enter the correct password: `tcm123456`

### Possible Outcomes:

**✔️ Correct username & password**  
Displays a full loading sequence and humorous "secret access" messages.

**❌ Wrong password**  
Shows a password-error message.

**❌ Wrong username**  
Shows a username-error message.

**❌ Both wrong**  
Displays a unique message advising the user to recheck both fields.

---

## 📂 Suggested File Structure

```
project/
│
├── turtle_art.py
├── login.py
└── README.md
```

---

## 🛠️ Requirements

Both scripts require only Python's built-in modules:

* `turtle`
* `time`

**No external libraries are needed.**

---

## 📜 License

Feel free to modify, remix, or learn from this project — it's entirely yours to use.
