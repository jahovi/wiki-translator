# Wiki-tranlator

Quickly tranlate technical terms and jargon  from english to german using the power of Wikipedia. Just `Ctrl-C` a term to your clipboard and run `wiki-translator.py`. If there is both an english and a german wikipedia page for the term, the german page will open in your default browser.

To streamline the process on windows, you can create a .bat file with the following content:

```
@python Drive:\Path\to\wiki_translator.py %*
```

Assuming python is on your path, double-clicking the bat will execute the script.

## Requirements

- Python 3
- beautifulsoup4
- pyperclip
- requests

Simply install with `pip install -r Drive:\Path\to\requirements.txt`