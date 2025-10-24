"""Program: Name Analyzer
This program reads a person's full name and displays:
- The name in uppercase letters
- The name in lowercase letters
- The total number of letters (excluding spaces)
- The number of letters in the first name
"""

# === HEADER ===
print("=" * 45)
print("=== WELCOME TO THE NAME ANALYZER PROGRAM ===")
print("=" * 45)

# === INPUT ===
full_name = input("\nPlease enter your full name: ").strip()

# === PROCESSING ===
upper_name = full_name.upper()
lower_name = full_name.lower()
total_letters = len(full_name.replace(" ", ""))  # removes spaces before counting
first_name = full_name.split()[0]
first_name_length = len(first_name)

# === OUTPUT ===
print("\n--- RESULTS ---")
print(f"Your name in uppercase letters: {upper_name}")
print(f"Your name in lowercase letters: {lower_name}")
print(f"Total number of letters (excluding spaces): {total_letters}")
print(f"Your first name is '{first_name}' and it has {first_name_length} letters.")
print("=" * 45)
print("Thank you for using the Name Analyzer!")
print("=" * 45)
