# OGNameFinder

Tool to find available Minecraft usernames (OG names).

## How it works

The script generates random words using the `faker` library and checks them via the Mojang public API. If a name returns a 404 error, it means the name is available and is saved to `output.txt`.

## Requirements

- Python 3.10+
- venv already configured (see `venv/`)

## Installation

```bash
# Activate the virtual environment
.\venv\Scripts\activate.bat

# Install dependencies (if needed)
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Available names are automatically saved to `output.txt`.

## Output

- `output.txt`: list of available Minecraft names found

## Language

To change the language of generated words, modify the locale in `main.py`:

```python
fake = Faker(locale="it_IT")  # Italian
fake = Faker(locale="en_US")  # English (default)
fake = Faker(locale="fr_FR")  # French
fake = Faker(locale="de_DE")  # German
```

## Notes

- The script ignores names with spaces, apostrophes, or hyphens
- Name length: 4-15 characters
- Includes automatic rate limiting to avoid API blocks
