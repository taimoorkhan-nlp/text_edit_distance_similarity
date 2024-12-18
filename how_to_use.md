## How to use

## Prerequisites
The method does not need any specific setup or installation and only uses basic packages i.e., string and random.

## Steps to execute
### 1. Environment setup
No setup is needed.

### 2. Run in Jupyter
- run `pip install jupyter` or `conda install jupyter`, if not installed already
- run jupyter using the command `jupyter lab` or `jupyter notebook`
- Open and execute all cells in [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb).
- execute the notebook cells to call all methods defined in `utils.py` on same texts
### 3. Update Inputs
Provide the input texts directly in the notebook.

### 4. View Outputs
The method prints the output as the word or character level edit distance between two texts, depending on the function used.

### Input and Output Specification (With sample)
#### Input
- **Input Query:** Provide two posts/strings as input directly in the in the notebook [text_edit_distance_similarity.ipynb](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/text_edit_distance.ipynb) to compare.
  
For example, we want to measure the dissimilarity (edit distance) between the two tweets sharing the same news:
```
tweet1 = "Excited to share our latest research on AI and its impact on social sciences! Leveraging data for better insights"
tweet2 = "Thrilled about our new findings on how AI transforms social science research. Innovation meets impact!"
```
#### Output
- **Output format**:
After running the script, the method prints output to the screen as string.
- **Structure of Output**:
The output string has the following information
  - `Edit distance version used` from the available implementation versions.
  - `at word/character level` showing whether the method is applied at word or character level
  - `score (as integer value)` representing the edit distance or cost between the texts, usually interpretted as the minimum edits needed to transform source text to target text using the available operations and their costs.
- **Sample Output**:
The two sample outputs for tweet1 and tweet2 given in the input above. First using levenshtein edit distance at the word level while second using simple edit distance at the character level.

Levenshtein edit distance (at word level) is 26 i.e., tweet1 and tweet2 are 26 word changes apart using Levenshtein edit distance.
Simple edit distance (at character level) is 71 i.e., tweet1 and tweet2 are 71 character changes apart using simple edit distance.
```
levenshtein edit distance (at word level): 26
simple edit distance (at character level): 71
```

