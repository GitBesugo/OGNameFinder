import time
from pathlib import Path
from typing import Optional

import requests
from faker import Faker


OUTPUT_FILE = Path("output.txt")
INVALID_CHARS = {"-", " ", "'"}


def load_saved_words(path: Path) -> set[str]:
    if not path.exists():
        return set()

    return {
        line.strip().lower()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def is_valid_word(word: Optional[str]) -> bool:
    if word is None:
        return False

    return not any(char in word for char in INVALID_CHARS) and 3 < len(word) < 16


def main():
    checked_words = load_saved_words(OUTPUT_FILE)
    fake = Faker(locale="en_US")

    with requests.Session() as session, OUTPUT_FILE.open(
        "a",
        encoding="utf-8",
        buffering=1,
    ) as output_file:
        while True:
            word = fake.word()
            if not is_valid_word(word):
                continue

            word = word.lower()
            if word in checked_words:
                continue

            try:
                response = session.get(
                    f"https://api.mojang.com/users/profiles/minecraft/{word}",
                    timeout=10,
                )
            except requests.RequestException as error:
                print(f"{word}: request failed ({error})")
                time.sleep(5)
                continue

            print(f"{word}: {response.status_code}")

            if response.status_code == 429:
                print("Rate limited! Sleeping for 5 seconds...")
                time.sleep(5)
                continue

            checked_words.add(word)
            if response.status_code != 404:
                continue

            print(f"AVAILABLE: {word}")
            output_file.write(word + "\n")


if __name__ == "__main__":
    main()