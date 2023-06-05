# FireFly - Spell Check and Word Analysis Website

FireFly is a spell checking website that provides a range of language-related features, including synonym and antonym finding, spelling checking, auto-correction, word resemblance checking, and part-of-speech identification. The backend of the website is built using Python, while the frontend is developed using HTML and CSS. This project was completed within a remarkable timeframe of just 24 days by Yasir.

## Features

1. **Spell Checker**: FireFly enables users to check the spelling of words. It highlights misspelled words and offers suggestions for potential corrections.

2. **Auto Corrector**: The website incorporates an auto-correct feature that automatically rectifies misspelled words, providing users with the correct spellings.

3. **Synonym and Antonym Finder**: Users can search for synonyms and antonyms of specific words. This functionality assists in broadening vocabulary and finding suitable words for diverse contexts.

4. **Word Resemblance Checker**: FireFly includes a word resemblance checker that allows users to assess the similarity between two words. It provides a measure of how closely related the two words are.

5. **Part-of-Speech Finder**: This feature aids in identifying the part of speech (e.g., noun, verb, adjective) for a given word. It facilitates users in understanding the grammatical role of a word within a sentence.

## Getting Started

To run FireFly locally, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/<username>/<repository>.git
```

2. Install the required dependencies. Ensure that Python is installed on your system.

```bash
pip install -r requirements.txt
```

3. Start the backend server:

```bash
python app.py
```

4. Open a web browser and navigate to `http://localhost:8000` to access the FireFly website.

## Project Structure

The project structure is organized as follows:

- `app.py`: The primary entry point for the backend server.
- `templates/`: Contains HTML templates for the website.
- `static/`: Includes CSS and JavaScript files for styling and interactive features.
- `spell_check.py`: Implements the spell checking functionality.
- `auto_correct.py`: Implements the auto-correct feature.
- `synonym_antonym.py`: Provides synonym and antonym searching capabilities.
- `word_resemblance.py`: Calculates the word resemblance between two words.
- `part_of_speech.py`: Determines the part of speech for a given word.

## Contributing

Contributions to FireFly are highly appreciated. If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## Author

This project was developed by Yasir. If you have any questions or feedback, feel free to reach out to me via email at [your-email@example.com](mailto:your-email@example.com).

## License

FireFly is licensed under the [MIT License](LICENSE).
