# task_automation.py
# Automate small tasks: move JPGs, extract emails, scrape webpage title

import os
import shutil
import re
import requests


def move_jpg_files():
    print("\n=== Move all .jpg files to a new folder ===")
    source = input("Enter source folder path: ").strip()
    dest = input("Enter destination folder path: ").strip()

    if not os.path.isdir(source):
        print("Source folder does not exist.")
        return

    if not os.path.isdir(dest):
        print("Destination folder does not exist. Creating it...")
        os.makedirs(dest, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source):
        if filename.lower().endswith(".jpg"):
            src_path = os.path.join(source, filename)
            dest_path = os.path.join(dest, filename)
            shutil.move(src_path, dest_path)
            moved_count += 1

    print(f"✅ Moved {moved_count} .jpg file(s) from '{source}' to '{dest}'.")


def extract_emails():
    print("\n=== Extract all email addresses from a .txt file ===")
    input_file = input("Enter input .txt file path: ").strip()
    output_file = input("Enter output file path to save emails: ").strip()

    if not os.path.isfile(input_file):
        print("Input file does not exist.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Simple email regex
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    unique_emails = sorted(set(emails))

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"✅ Found {len(unique_emails)} unique email(s). Saved to '{output_file}'.")


def scrape_title():
    print("\n=== Scrape title of a webpage and save it ===")
    url = input("Enter webpage URL (e.g., https://www.example.com): ").strip()
    output_file = input("Enter output file path to save title: ").strip()

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("Error fetching the page:", e)
        return

    html = response.text

    # Simple way to find <title>...</title>
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
    else:
        title = "No title found"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\n")
        f.write(f"Title: {title}\n")

    print(f"✅ Page title saved to '{output_file}'.")
    print("Title:", title)


def main():
    while True:
        print("\n====== TASK AUTOMATION MENU ======")
        print("1. Move all .jpg files from one folder to another")
        print("2. Extract all email addresses from a .txt file")
        print("3. Scrape the title of a webpage and save it")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_title()
        elif choice == "4":
            print("Exiting Task Automation script. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
