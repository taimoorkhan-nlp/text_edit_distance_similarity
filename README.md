# text-randomizer (adding noise using Edit distance variants) 
### Description
This method aims to introduce noise or corruption into a given text by modifying it using the concept of edit distance. It has 3 implementations of edit distance i.e., simple edit distance, Levenshtein edit distance and Damerau-Levenshtein edit distance. Originally the method measures the difference between two strings by counting the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.

The method takes a text string as input, which can be a sentence, paragraph, or any other textual data. The user specifies which method to use and how many randomization operations to perform, which determines the degree of noise to be introduced into the text. The method randomly selects a combination of edit operations (insertions, deletions, or substitutions) based on the specified corruption level. For each edit operation, the method randomly selects a character position within the input text string.
The selected edit operations are applied to the chosen character positions in the input text string. The operations are insertion, deletion, substitution and transposition.
The method returns the corrupted text string, which now contains the introduced noise.

The edit distance metric ensures that the corrupted text remains relatively similar to the original text, while introducing a controlled level of noise. The method can be customized by adjusting the corruption level, the types of edit operations allowed, and the character selection strategy to suit specific use cases or requirements.

### Use cases
This text corruption method can be useful in various applications, such as:

**Data Augmentation:** Introducing controlled noise into text data can help improve the robustness and generalization of machine learning models, particularly in natural language processing tasks like text classification, machine translation, or speech recognition.

**Simulating Noisy Data:** The method can be used to simulate real-world scenarios where text data may be corrupted or contain errors, such as text from social media platforms containing personal/sensitive details.

**Privacy Preservation:** By corrupting text data with a controlled level of noise, this method can potentially be used as a privacy-preserving technique, making it more difficult to recover the original text from the corrupted version.

### Repository Structure

### Keywords
edit distance, randomizing text, levenshtein edit distance

### Environmental Setup
The method has vanilla implementation of the edit distance types mentioned without requiring any additional resources.

### Sample Input
### Sample Output

### How to Use

### Contact Details
Taimoor Khan (taimoor.nlp@gmail.com)
