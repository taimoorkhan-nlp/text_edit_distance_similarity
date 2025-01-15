# Analyzing Text Similarity Using Edit Distance

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/taimoorkhan-nlp/text_edit_distance_similarity/HEAD?labpath=text_edit_distance_similarity.ipynb)


## Description
This method calculates the edit distance between two texts to estimate how similar or dissimilar they are. The two texts may represent two dialects of the language, definitions of similar concepts across different disciplines, or the same news from two media sources. Additionally, the method also helps to distort text (using insertion, deletion, substitution, and transposition operations) with personal information.
The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__ and __Damerau-Levenshtein edit distance__) between two texts both at character and word level, and has the following operations:

- __Simple edit distance__ i.e., having insertion, deletion and substitution operations, all having cost 1.
- [__Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S0010482523001142) i.e., having insertion and deletion with cost 1 and subsitution with cost 2 (it is also equivalent to saying no subsitution allowed)
- [__Damerau-Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S1319157821001828) i.e., having insertion, deletion, substitution and transposition, all having equal cost 1.
*The method is reproducible as it offers vanilla implementation wihtout requiring any packages or resources to be installed. It only uses the basic (string and random) packages usually already included. It gives full control to update costs and scale as needed be. Random seeds are defined to have predictable random numbers for reproducibility.*

## Keywords
Edit distance, text similarity, Levenshtein edit distance, Damerau-Levenshtein edit distance

## Use Case(s)
- Identifying different mentions of entities (e.g. names like "Donald Trump", "D. Trump", and "Trump")
- Finding tweets/social media posts similar to a certain tweet, sentence, or claim.

## Repo Structure
- [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb)
- [utils.py](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/utils.py)

The methods are defined in [utils.py](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/utils.py) and are called on sample tweets from the notebook [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb).

## Environment Setup
No setup is needed.

## Input Data
Provide the input texts directly in the notebook. The method is directly applicable to textual digital behavioral data from social media and other digital platform.

## Sample Input and Output
Provide two posts/strings as input directly in the in the notebook [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb) to compare.
  
For example, we want to measure the dissimilarity (edit distance) between the two tweets sharing the same news:
```
tweet1 = "Excited to share our latest research on AI and its impact on social sciences! Leveraging data for better insights"
tweet2 = "Thrilled about our new findings on how AI transforms social science research. Innovation meets impact!"
```
After running the script, the method prints output to the screen as string.
The output string has the following information
  - `Edit distance version used` from the available implementation versions.
  - `at word/character level` showing whether the method is applied at word or character level
  - `score (as integer value)` representing the edit distance or cost between the texts, usually interpretted as the minimum edits needed to transform source text to target text using the available operations and their costs.

The two sample outputs for tweet1 and tweet2 given in the input above. First using levenshtein edit distance at the word level while second using simple edit distance at the character level.
Levenshtein edit distance (at word level) is 26 i.e., tweet1 and tweet2 are 26 word changes apart using Levenshtein edit distance.
Simple edit distance (at character level) is 71 i.e., tweet1 and tweet2 are 71 character changes apart using simple edit distance.
```
levenshtein edit distance (at word level): 26
simple edit distance (at character level): 71
```

## How to Use
- run `pip install jupyter` or `conda install jupyter`, if not installed already
- run jupyter using the command `jupyter lab` or `jupyter notebook`
- Open and execute all cells in [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb).
- execute the notebook cells to call all methods defined in [utils.py](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/utils.py) on same texts

## Contact Details
Taimoor Khan (<a href=mailto:taimoor.khan@gesis.org>taimoor.khan@gesis.org</a>)

## Publications
1. Hossain, E., Rana, R., Higgins, N., Soar, J., Barua, P. D., Pisani, A. R., & Turner, K. (2023). Natural language processing in electronic health records in relation to healthcare decision-making: a systematic review. Computers in biology and medicine, 155, 106649.
2. Chaabi, Y., & Allah, F. A. (2022). Amazigh spell checker using Damerau-Levenshtein algorithm and N-gram. Journal of King Saud University-Computer and Information Sciences, 34(8), 6116-6124.
