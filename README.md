# Analyzing Text Similarity Using Edit Distance

## Description

This method calculates the edit distance between two texts to estimate their similarity or dissimilarity. The edit distance measures how many operations — such as inserting, deleting, or substituting characters — are needed to transform one text into another with minimum cost. For instance, Simple edit distance between "cut" and "cat" is 1, as only one substitution is needed. Similarly, Simple distance between "cat" and "at" is also 1, as one deletion suffices. In its simplest form, edit distance assigns an equal cost to all operations — insertions, deletions, and substitutions. Variants of the method allow for different cost structures, making it adaptable to various applications. For example, this method can be used to compare texts like dialects of a language, definitions of similar concepts across disciplines, or even versions of the same news article from different media sources. 

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
  

## Output Data

The method writes an output CSV file with the result for three different edit distance variants computed for each input pair (see technical details). See [data/output_scores.csv](data/output_scores.csv) for the output for the example input file:

| Text 1 | Text 2 | Simple | Levenshtein | Damerau-Levenshtein |
|--------|--------|--------|-------------|---------------------|
| The sun rises in the east	| The sun sets in the west	| 5	| 5	| 5 |
| He likes to play football	| He loves to play soccer	| 9	| 16	| 9 |
| She made a cup of tea	| She prepared a cup of coffee	| 11	| 15	| 11 |
| They visited the museum	| They toured the art gallery	| 15	| 22	| 15 |
| Reading helps improve vocabulary	| Reading enhances language skills	| 22	| 34	| 22 |

## Hardware

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU core, 4 GB RAM, 40GB HDD).

## Environment Setup

Execute the following command to install the required packages

`pip install -r requirements.txt`

## How to Use

- Run Jupyter using the command `jupyter lab` or `jupyter notebook`
- Open and execute all cells in [src/text_edit_distance_similarity.ipynb](src/text_edit_distance.ipynb) using the methods defined in [src/utils.py](src/utils.py).
- It reads the input as text pairs from `data/input_text_pairs.csv` and writes the output to `data/output_scores.csv` having text pairs along with the edit distances.
- *Optional:* Provide specific method (simple, levenshtein, damerau, default is all) and level (c for character level, w for word level) in the method `batch_edit_distance(csv_path='../data/input_text_pairs.csv', method='all', level='c')`

Alternative: execute as Python script
```{python}
cd src
jupyter nbconvert --to script text_edit_distance.ipynb # convert the notebook to script `text_edit_distance.py`
python text_edit_distance.py
cat ../data/output_scores.csv # show result
```

## Technical Details

The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__, and __Damerau-Levenshtein edit distance__) between two texts, both at character and word level, and has the following operations:

- __Simple edit distance__, i.e., having insertion, deletion, and substitution operations, all having cost 1.
- [__Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S0010482523001142) i.e., having insertion and deletion with cost 1 and substitution with cost 2 (it is also equivalent to saying no substitution allowed)
- [__Damerau-Levenshtein edit distance__](https://www.sciencedirect.com/science/article/pii/S1319157821001828) i.e., having insertion, deletion, substitution, and transposition, all having equal cost 1.
 
The method is reproducible as it offers the vanilla implementation without requiring any packages or resources to be installed. It only uses the basic (string and random) packages, usually already included. It gives full control to update costs and scale as needed. Random seeds are defined to have predictable random numbers for reproducibility.
  
## Publications

1. Hossain, E., Rana, R., Higgins, N., Soar, J., Barua, P. D., Pisani, A. R., & Turner, K. (2023). Natural language processing in electronic health records in relation to healthcare decision-making: a systematic review. Computers in biology and medicine, 155, 106649.
2. Chaabi, Y., & Allah, F. A. (2022). Amazigh spell checker using the Damerau-Levenshtein algorithm and N-gram. Journal of King Saud University-Computer and Information Sciences, 34(8), 6116-6124.

## Contact Details

Taimoor Khan (<a href=mailto:taimoor.khan@gesis.org>taimoor.khan@gesis.org</a>)
