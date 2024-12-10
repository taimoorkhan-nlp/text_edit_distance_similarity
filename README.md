# Edit distance toolkit 
## Description
Edit distance is a sequence comparison method that can be used to compare two text samples for their similarity or dissimilarity. It operates on the principle of minimum edits (changes) needed to transform source text into target text. It can be used for finding edit distance between two text samples representing the same message in two dialects, languages, same news across different posts on social media or definitions of the same/similar terms across different disciplines. 

The method offers 3 edit distance variants i.e., Simple edit distance, Levenshtein edit distance and Damerau-levenshtein edit distance. It uses insertion, deletion, substitution and transposition operations depending on the variant used. The method operates at both word and character levels.

- Simple edit distance between two texts (at word and char level)
- Levenshtein edit distance between two texts (at word and char level)
- Damerau-levenshtein edit distance between two texts (at word and char level)
- *Bonus:* Distorting or randomizing text for given number of spins of randomly picked operations (insertion, deletion, substitution and transposition)

The methods are defined in `utils.py` and are called on sample tweets from the notebook `text_edit_distance.ipynb`

The method in plain python without any package installation and therefore, preserving the environment or the `requirements.txt` file is not required. Random seeds are defined to have predictable random numbers for reproducibility.

## Keywords
edit distance, randomizing text, levenshtein edit distance

## Use cases
- Social science researcher interested in finding the edit distance between a toxic post and its detoxified version
- social science researcher interested in finding the edit distance among the definitions of terms reproducibility, replicability, reusability, transparency across different science disciplines


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
