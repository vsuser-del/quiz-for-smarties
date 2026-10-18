# 🧠 The Impossible Python Quiz Game

A challenging command-line quiz application written in Python that tests your pattern recognition, logic, and math skills. It starts easy, but the questions quickly scale in difficulty.

---

## 🚀 Prerequisites

To run this game, **you need Python installed on your computer**. 

If you do not have Python yet:
1. Download it from the official [python.org](https://python.org) website.
2. **Important:** During installation on Windows, make sure to check the box that says **"Add Python to PATH"**.

---

## 💻 How to Play

### Method 1: The Quick Way (Default)
1. Locate your quiz script file (e.g., `quiz.py`) in your file explorer.
2. **Double-click** the file. 
3. If prompted, select **Python (default)** as the program to open it.

### Method 2: From the Terminal / Command Prompt (Recommended)
If you want to ensure you see your final score without the window accidentally disappearing, run it via the terminal:

1. Open your Terminal (Mac/Linux) or Command Prompt (Windows).
2. Navigate to the folder where you saved the file:
   ```bash
   cd path/to/your/quiz-folder
   ```
3. Run the quiz:
   ```bash
   python quiz.py
   ```
   *(Note: On macOS or Linux, use `python3 quiz.py` instead).*

---

## 🎮 Game Features & Rules

* **6 Brain-Teasing Questions:** Test your wits against geometric sequences, factorials, word algebra, and mathematical constants.
* **No Decimals for Pi:** For Question 5, make sure to enter the digits without the decimal point (e.g., `3141`).
* **Input Validation:** The game checks if your answer is a valid number and gives you a cheeky response if you type text instead.
* **Live Scoring:** Tracks your correct answers and calculates your final accuracy percentage at the end of the run.
* **Anti-Instant Close:** The game ends with a script pause, requiring you to press `ENTER` before the terminal window exits.

---

## 🛠️ Troubleshooting

* **The window closes instantly at the end:** The script uses an `input()` prompt at the very end to keep the screen open. If it still closes too fast, use **Method 2** to run it directly inside a permanent terminal window.
* **"Python is not recognized" error:** You need to reinstall Python and make sure to check the **"Add Python to PATH"** checkbox during the setup process.

