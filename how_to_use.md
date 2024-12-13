## How to use
- Start the notebook in jupyter and provide the two input strings to find the edit distance between them.

## Prerequisites
The method does not need any speicific setup or installation and is only using basic packages i.e., string and random.

## Steps to execute
### 1. Environment setup
No setup needed.

### 2. Run in Jupyter
- run jupyter using command `jupyter lab` or `jupyter notebook`
- Open and execute all cells in text_edit_distance_similarity.ipynb.
- execute the notebook cells to call all methods defined in `utils.py` on same texts
### 3. Update Inputs
Provide the input posts directly in the notebook

### 4. View Outputs
The methods prints the output as the word or character level edit distance, depending on the function used.

### Input and Output Specification (With sample)
#### Input
- **Input Query:** Provide two posts/strings as input directly in the notebook to compare.
  
For example we want to measure the dissimilarity (edit distance) between the two tweets sharing the same news.
```
tweet1 = "Excited to share our latest research on AI and its impact on social sciences! Leveraging data for better insights"
tweet2 = "Thrilled about our new findings on how AI transforms social science research. Innovation meets impact!"
```
#### Output
- **Output format**: After running the script, the method displays the output as;
For example for calculating the levenshtein edit distance at word level and simple edit distance at the character level are;
```
levenshtein edit distance (at word level): 26
simple edit distance (at character level): 71
```

