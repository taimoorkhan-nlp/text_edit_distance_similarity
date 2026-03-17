---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Analyzing Text Similarity Using Edit Distance


## Description

This method calculates the edit distance between text pairs to estimate their similarity or dissimilarity. The edit distance measures how many operations — such as insertion, deletion, or substitution — are needed to transform one text into another with minimum cost. For instance, Simple edit distance between *"cut"* and *"cat"* is 1 (both at the word and character level), as only one substitution is needed. Similarly, Simple distance between *"cat"* and *"at"* is also 1 at the character level, as only one deletion suffices. In its simplest form, edit distance assigns an equal cost to all operations — insertions, deletions, and substitutions. Variants of the method allow for different cost structures, making it adaptable to various applications. For example, this method can be used to compare texts like dialects of a language, definitions of similar concepts across disciplines, or even versions of the same news article from different media sources. 


## Use Cases

- Identifying spelling errors in entities (e.g., "Association of Language Testers in Europe" and "Association of Language Testers of Europe")
- Finding tweets/social media posts similar to a certain tweet, sentence, or claim.


## Input Data

The method reads a CSV file without header and two columns, containing text pairs to be compared. See [data/input_text_pairs.csv](data/input_text_pairs.csv) for an example:

|       |      |
|:-----:|:----:|
| The sun rises in the east |	The sun sets in the west |
| He likes to play football |	He loves to play soccer |
| She made a cup of tea	| She prepared a cup of coffee |
| They visited the museum	| They toured the art gallery |
| Reading helps improve vocabulary	| Reading enhances language skills |

<!-- #region -->
## Input Data

The method reads a CSV file without header and two columns, containing text pairs to be compared. See [data/input_text_pairs.csv](data/input_text_pairs.csv) for an example:


| Original Sentence                     | Modified Sentence                     |
|:------------------------------------:|:------------------------------------:|
| She enjoys reading books             | She enjoys reading many books        |
| He plays the guitar on the weekends  | He plays the guitar                  |
| The cat sat on the mat               | The dog sat on the mat               |
| She quickly finished her work        | She finished quickly her work        |

<!-- #endregion -->

## Output Data

The method writes an output CSV file with the result for three different edit distance variants computed for each input pair (see technical details). See [data/output_scores.csv](data/output_scores.csv) for the output for the example input file:

| Index | Sentence 1                          | Sentence 2                          | Damerau |
|:-----:|------------------------------------|------------------------------------|:-------:|
| 0     | She enjoys reading books           | She enjoys reading many books      | 1       |
| 1     | He plays the guitar on the weekends| He plays the guitar                | 3       |
| 2     | The cat sat on the mat             | The dog sat on the mat             | 1       |
| 3     | She quickly finished her work      | She finished quickly her work      | 1       |


## Hardware

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).


## Environment Setup

Execute the following command to install the required packages

`pip install -r requirements.txt`

```python
!pip install ipynb==0.5.1, jupyterlab-quarto==0.3.5, zstandard==0.23.0, jupytext==1.19.1, markdown-it-py==4.0.0, mdit-py-plugins==0.5.0, mdurl==0.1.2, pandas==3.0
```

## How to Use

- Run Jupyter using the command `jupyter lab` or `jupyter notebook`
- Open and execute all cells in [text_edit_distance_similarity.ipynb](text_edit_distance.ipynb) using the methods defined in [utils.py](utils.py).
- It reads the input as text pairs from `data/input_text_pairs.csv` and writes the output to `data/output_scores.csv` having text pairs along with the edit distances.
- *Optional:* Provide specific method (simple, levenshtein, damerau, default is all) and level (c for character level, w for word level) in the method `batch_edit_distance(csv_path='data/input_text_pairs.csv', method='all', level='c')`

Alternative: execute as Python script
```
jupyter nbconvert --to script text_edit_distance.ipynb # convert the notebook to script `text_edit_distance.py`
python text_edit_distance.py
cat data/output_scores.csv # show result
```


```python
from functions import (simple_edit_distance,
            levenshtein_edit_distance, damerau_levenshtein_distance)
import csv
import pandas as pd
import os
```

The method offers three variants of edit distance 
- Simple edit distance
- Levenshtein edit distance
- Damerau Levenshtein edit distance

The method can be applied to the text pairs in 2 levels
- At word level
- At character level


```python
def _pair_texts(sent1, sent2, method, level):
    dist = {'sentence1':sent1, 'sentence2': sent2}

    if method=='simple':
        dist['simple'] = simple_edit_distance(sent1, sent2, level=level)
    elif method=='levenshtein':
        dist['levenshtein'] = levenshtein_edit_distance(sent1, sent2, level=level)
    elif method=='damerau':
        dist['damerau'] = damerau_levenshtein_distance(sent1, sent2, level=level)
    elif method=='all':
        dist['simple'] = simple_edit_distance(sent1, sent2, level=level)
        dist['levenshtein'] = levenshtein_edit_distance(sent1, sent2, level=level)
        dist['damerau'] = damerau_levenshtein_distance(sent1, sent2, level=level)
    return dist


def edit_distance(sentences_set1, sentences_set2, texts=None, method='all', level='w'):
    """
    Calculate edit distances for the corresponding sentences in sentence_set1 and sentence_set2.
    
    Args:
        sentences_set1: List of set 1 sentences
        sentences_set2: List of set 2 sentences
        method (str): Type of edit distance method as 'simple', 'levenshtein', 'damerau', or 'all' (default).
        level (str): Level of comparison with 'c' for character level comparison and 'w' for word level comparison (default 'c').
        
    Returns:
        results (dictionary): Containing pairs of sentences and the edit distance score(s) by chosen method and level.
    """
    output = []
    if len(sentences_set1) == len(sentences_set2):
        for index in range(len(sentences_set1)):
            output.append(_pair_texts(sentences_set1[index], sentences_set2[index], method, level))
            
    return output 

```

- The first sentence pair covers the insertion scenario
- The second setence pair covers the deletion scenario
- The third sentence pair covers the substitution scenario
- The fourth sentence pair covers the transposition scenario 

```python

    
# Example usage:
path_set1 = 'data/sentences_set1.txt'
path_set2 = 'data/sentences_set2.txt'

if os.path.exists(path_set1) and os.access(path_set1, os.F_OK) and os.path.exists(path_set2) and os.access(path_set2, os.F_OK):
    with open(path_set1, 'r') as file1:
        sentences_set1 = file1.read().split('\n')
    with open(path_set2, 'r') as file2:
        sentences_set2 = file2.read().split('\n')
else:
    sentences_set1 = ['She enjoys reading books', 'He plays the guitar on the weekends', 'The cat sat on the mat', 'She quickly finished her work']
    sentences_set2 = ['She enjoys reading many books', 'He plays the guitar', 'The dog sat on the mat', 'She finished quickly her work']


```

```python
results = edit_distance(sentences_set1, sentences_set2, method='damerau', level='w')
df = pd.DataFrame(results)
print(df)

```

```python
output_filepath = 'data/output_scores.csv'

if os.access(output_filepath.split('/')[0], os.W_OK):
    with open(outputfile_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Text1', 'Text2', 'Simple', 'Levenshtein', 'Damerau-Levenshtein'])     # Write header
        writer.writerows(results) 
```

## Technical Details

The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__, and __Damerau-Levenshtein edit distance__) between two texts, both at character and word level, and has the following operations:

- __Simple edit distance__, i.e., having insertion, deletion, and substitution operations, all having cost 1.
- [__Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S0010482523001142) i.e., having insertion and deletion with cost 1 and substitution with cost 2 (it is also equivalent to saying no substitution allowed)
- [__Damerau-Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S1319157821001828) i.e., having insertion, deletion, substitution, and *transposition*, all having equal cost 1.
 
The method is reproducible as it offers the vanilla implementation without requiring any packages or resources to be installed. It gives full control to update costs and scale as needed. However, for big data processing, there are more efficient libraries e.g., [https://pypi.org/project/editdistance/](https://pypi.org/project/editdistance/) that are much faster.



## Publications

1. Hossain, E., Rana, R., Higgins, N., Soar, J., Barua, P. D., Pisani, A. R., & Turner, K. (2023). Natural language processing in electronic health records in relation to healthcare decision-making: a systematic review. Computers in biology and medicine, 155, 106649.
2. Chaabi, Y., & Allah, F. A. (2022). Amazigh spell checker using the Damerau-Levenshtein algorithm and N-gram. Journal of King Saud University-Computer and Information Sciences, 34(8), 6116-6124.


## Contact Details

Taimoor Khan <taimoor.khan@gesis.org>


```python

```
