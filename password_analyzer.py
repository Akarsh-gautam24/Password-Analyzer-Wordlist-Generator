import zxcvbn
from zxcvbn import zxcvbn
import itertools

def collect_personal_info():
    print("Enter some personal information to generate wordlist (optional):")
    name = input("Name: ").lower()
    dob = input("Date of Birth (DDMMYYYY): ")
    pet = input("Pet Name: ").lower()
    return [name, dob, pet]

def generate_variations(words):
    leet_dict = {'a': ['@', '4'], 's': ['$', '5'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0']}
    variations = set()
    for word in words:
        variations.add(word)
        variations.add(word[::-1])
        variations.add(word + "123")
        for year in ['2025', '2024', '1999']:
            variations.add(word + year)
        for pattern in itertools.product(*[leet_dict.get(char, [char]) for char in word]):
            variations.add(''.join(pattern))
    return list(variations)

def main():
    password = input("Enter a password to check strength: ")
    result = zxcvbn(password)
    print("\n--- Password Strength Report ---")
    print(f"Score: {result['score']} / 4")
    print(f"Feedback: {result['feedback']['warning'] or 'Strong password!'}")
    print("Suggestions:", ", ".join(result['feedback']['suggestions']))
    personal_data = collect_personal_info()
    raw_words = [word for word in personal_data if word]
    wordlist = generate_variations(raw_words)
    with open("custom_wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    print(f"\n✅ Wordlist generated and saved as 'custom_wordlist.txt' with {len(wordlist)} entries.")

if __name__ == "__main__":
    main()