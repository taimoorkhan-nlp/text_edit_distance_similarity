# Analyzing Text Similarity Using Edit Distance

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/taimoorkhan-nlp/text_edit_distance_similarity/HEAD?labpath=text_edit_distance_similarity.ipynb)

## Description
This method calculates the edit distance between two texts to estimate how similar or dissimilar they are. The two texts may represent two dialects of the language, definitions of similar concepts across different disciplines, or the same news from two media sources. Additionally, the method also helps to distort text (using insertion, deletion, substitution, and transposition operations) with personal information.
The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__ and __Damerau-levenshtein edit distance__) and has the following operations:

- __Simple edit distance__ between two texts (at the word or character level)
- [__Levenshtein edit distance__](https://www.sciencedirect.com/topics/computer-science/levenshtein-distance) with substitution cost 2 between two texts (at the word or character level)
- [__Damerau-levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S1319157821001828) between two texts (at the word or character level)

**[How to Use](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/how_to_use.md):** Detailed instructions for setting up the environment, configuring the method, and running the script.

**Reproducibility:** The method does not install any packages or resources. It only uses the basic string and random packages usually already included.

The methods are defined in `utils.py` and are called on sample tweets from the notebook `text_edit_distance.ipynb`

The method in plain Python without any package installation and therefore, preserving the environment or the `requirements.txt` file is not required. Random seeds are defined to have predictable random numbers for reproducibility.

## Use cases
- Identifying different mentions of entities (e.g. names like "Donald Trump", "D. Trump", and "Trump")
- Finding tweets/social media posts similar to a certain tweet, sentence, or claim.

## Keywords
Edit distance, text similarity, Levenshtein edit distance, Damerau-Levenshtein edit distance

### Contact Details
Taimoor Khan (taimoor.khan@gesis.org)
