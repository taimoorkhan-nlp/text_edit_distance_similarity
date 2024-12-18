# Analyzing Text Similarity Using Edit Distance

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/taimoorkhan-nlp/text_edit_distance_similarity/HEAD?labpath=text_edit_distance_similarity.ipynb)


## Description
This method calculates the edit distance between two texts to estimate how similar or dissimilar they are. The two texts may represent two dialects of the language, definitions of similar concepts across different disciplines, or the same news from two media sources. Additionally, the method also helps to distort text (using insertion, deletion, substitution, and transposition operations) with personal information.
The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__ and __Damerau-levenshtein edit distance__) and has the following operations:

- __Simple edit distance__ between two texts (at the word or character level)
- [__Levenshtein edit distance__](https://www.sciencedirect.com/topics/computer-science/levenshtein-distance) with substitution cost 2 between two texts (at the word or character level)
- [__Damerau-levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S1319157821001828) between two texts (at the word or character level)

**[How to Use]([#how-to-use](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/how_to_use.md)):** Detailed instructions for setting up the environment, configuring the method, and running the script.

**Reproducibility:** The method does not install any packages or resources. It only uses the basic string and random packages usually already included.

The methods are defined in `utils.py` and are called on sample tweets from the notebook `text_edit_distance.ipynb`

The method in plain Python without any package installation and therefore, preserving the environment or the `requirements.txt` file is not required. Random seeds are defined to have predictable random numbers for reproducibility.

## Use cases
- Identifying different mentions of entities (e.g. names like "Donald Trump", "D. Trump", and "Trump")
- Finding tweets/social media posts similar to a certain tweet, sentence, or claim.

## Keywords
Edit distance, text similarity, Levenshtein edit distance, Damerau-Levenshtein edit distance

## How to use

## Prerequisites
The method does not need any specific setup or installation and only uses basic packages i.e., string and random.

## Steps to execute

### 1. Environment setup

No setup is needed.

### 2. Run in Jupyter
- run jupyter using the command `jupyter lab` or `jupyter notebook`.
- Open and execute all cells in text_edit_distance_similarity.ipynb.
- execute the notebook cells to call all methods defined in `utils.py` on same texts.
- 
### 3. Update Inputs
Provide the input texts directly in the notebook.

### 4. View Outputs
The method prints the output as the word or character level edit distance, depending on the function used.

### Input and Output Specification (With sample)
#### Input
- **Input Query:** Provide two posts/strings as input directly in the notebook to compare.
  
For example, we want to measure the dissimilarity (edit distance) between the two tweets sharing the same news:
```
tweet1 = "Excited to share our latest research on AI and its impact on social sciences! Leveraging data for better insights"
tweet2 = "Thrilled about our new findings on how AI transforms social science research. Innovation meets impact!"
```

#### Output
- **Output format**: After running the script, the method displays the output as;
Levenshtein edit distance (at word level) is 26 i.e., tweet1 and tweet2 are 26 word changes apart using Levenshtein edit distance.
Simple edit distance (at character level) is 71 i.e., tweet1 and tweet2 are 71 character changes apart using simple edit distance.
```
levenshtein edit distance (at word level): 26
simple edit distance (at character level): 71
```


### Contact Details
Taimoor Khan (taimoor.khan@gesis.org)
