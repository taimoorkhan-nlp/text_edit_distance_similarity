# Analyzing Text Similarity Using Edit Distance

[![Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/taimoorkhan-nlp/text_edit_distance_similarity/HEAD?labpath=text_edit_distance_similarity.ipynb)

---
## Description
This method calculates edit distance between two texts to estimate how similar or dissimilar two texts representing two dialects of language, definitions of similar concepts across different disciplines or same news from two media sources are. Additionally the method also helps to distor text (using insertion, deletion, substitution and transposition operations) with personal information.
The method offers 3 edit distance variants (__Simple edit distance__, __Levenshtein edit distance__ and __Damerau-levenshtein edit distance__) and has the following operations:

- __Simple edit distance__ between two texts (at word or character level)
- __Levenshtein edit distance__ (with substitution cost 2) between two texts (at the word or character level)
- Damerau-levenshtein edit distance between two texts (at the word or character level)
- Distorting or randomizing text for a given number of spins of randomly picked operations (insertion, deletion, substitution and transposition)

- **[How to Use](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/how_to_use.md):** Detailed instructions for setting up the environment, configuring the method, and running the script.
- **[Reproducibility](https://github.com/taimoorkhan-nlp/text_edit_distance_similarity/blob/main/reproducibility.md):** The method is not installing any packages or resources. It only uses the basic string and random packages usually already included.

The methods are defined in `utils.py` and are called on sample tweets from the notebook `text_edit_distance.ipynb`

The method in plain python without any package installation and therefore, preserving the environment or the `requirements.txt` file is not required. Random seeds are defined to have predictable random numbers for reproducibility.

## Use cases
- __Comparing Textual Similarity Across Different Domains:__ This method can be used to compare how similar or different definitions, phrases, or terminology are across different domains or contexts. For example, a social scientist could use the __Simple edit distance__ or Levenshtein Edit Distance (at the word level) to compare the terminology used in different areas of research, such as "transparency" in public policy vs. "transparency" in computer science. This can help identify variations in the usage or meaning of terms across various fields.
- Analyzing Dialects or Variants of Language: You can apply these methods to compare texts in different dialects of the same language or different stylistic variations of writing. For instance, comparing tweets or social media posts from different geographic regions using __Damerau-levenshtein edit distance__ might help identify subtle differences that also consider character transpositions in informal writing.

- __Evaluating Media Reporting on the Same Topic:__ Use edit distance to compare how two media outlets report on the same news story. If you're working with two different versions of the same article or report, the __Levenshtein edit distance__ (Word Level) could highlight the differences in word choice and structure.

- __Text Distortion for Privacy or Anonymization:__ You can use this method to distort sensitive text data (like tweets or user-generated content) by applying random operations. This can help anonymize or distort text while maintaining its structural integrity for analysis.

## Keywords
Edit distance, text dissimilarity, Levenshtein edit distance, Damerau-levenshtein edit distance

### Contact Details
Taimoor Khan (taimoor.khan@gesis.org)
