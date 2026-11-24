"""Module that writes the make.fun competition entry line.
Demonstrates the agent running npm install 14 times in parallel, spawning 800 background processes,
and politely offering coffee while the CPU melts.
"""

import os

LINE = "My agent ran npm install 14 times in parallel, spawned 800 background processes, and politely asked if I wanted a coffee while CPU utilization hit 999%."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
