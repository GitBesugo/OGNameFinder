# OGNameFinder

Tool per trovare username Minecraft disponibili (OG names).

## Funzionamento

Lo script genera nomi casuali usando la libreria `faker` e li controlla tramite l'API pubblica di Mojang. Se un nome restituisce errore 404, significa che il nome e' disponibile e viene salvato in `output.txt`.

## Requisiti

- Python 3.10+
- venv gia' configurato (vedi `venv/`)

## Installazione

```bash
# Attiva il virtual environment
.\venv\Scripts\activate.bat

# Installa le dipendenze (se necessario)
pip install -r requirements.txt
```

## Utilizzo

```bash
python main.py
```

I nomi disponibili vengono salvati automaticamente in `output.txt`.

## Output

- `output.txt`: lista dei nomi Minecraft disponibili trovati

## Lingua

Per cambiare la lingua delle parole generate, modifica il locale in `main.py`:

```python
fake = Faker(locale="it_IT")  # italiano
fake = Faker(locale="en_US")  # inglese (default)
fake = Faker(locale="fr_FR")  # francese
fake = Faker(locale="de_DE")  # tedesco
```

## Note

- Lo script ignora nomi con spazi, apostrafi o trattini
- Lunghezza nomi: 4-15 caratteri
- Include rate limiting automatico per evitare blocchi API
