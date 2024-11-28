# Edit distance toolkit 
## Description
A method offers 3 edit distance variants to find distance (as edits) between two texts. It can be used to estimate how similar or dissimilar two texts representing two dialects of language, definitions of similar concepts across different disciplines or same news from two media sources are. Additionally the method also helps to distor text (using insertion, deletion, substitution and transposition operations) with personal information. It has the following operations:

- simple edit distance between two texts (at word level)
- simple edit distance between two texts (at character level)
- levenshtein edit distance (with substitution cost 2) between two texts (at word level)
- levenshtein edit distance (with submistution cost 2) between two texts (at character level)
- damerau-levenshtein edit distance between two texts (at word level)
- demarau-levenshtein edit distance between two texts (at character level)
- distorting or randomizing text for given number of spins of randomly picked operations (insertion, deletion, substitution and transposition)

The methods are defined in `utils.py` and are called on sample tweets from the notebook `text_edit_distance.ipynb`

The method in plain python without any package installation and therefore, preserving the environment or the `requirements.txt` file is not required. Random seeds are defined to have predictable random numbers for reproducibility.

## Keywords
edit distance, randomizing text, levenshtein edit distance

## Use cases
social science researcher interested in comparing the definitions of terms e.g., reproducibility, transparency etc. across different science disciplines 

## How to use
- run jupyter using command `jupyter lab` or `jupyter notebook`
- execute the notebook cells to call all methods defined in `utils.py` on same texts

## Sample input (For example to tweets)

```
tweet1 = "Excited to share our latest research on AI and its impact on social sciences! Leveraging data for better insights"
tweet2 = "Thrilled about our new findings on how AI transforms social science research. Innovation meets impact!"
```

## Sample output

```
simple edit distance at character 71, at word 16
levenshtein edit distance at character 109, at word 26
...
```

### Contact Details
Taimoor Khan (taimoor.khan@gesis.org)
