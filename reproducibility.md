The method provides three edit distance implementations:
- Simple edit distance: involves 3 operations (insert, delete and subsitute), all having cost 1
- Levenshtein edit distance: involves 3 operations where (insert and delete) have cost 1, while substitute have cost 2. It is also equivalent to saying that the method allows only insertion and deletion and not substitution.
- Damerau-levenshtein edit distance: involves 4 operations (insert, delete, substitute and transposition), all having equal cost

It is a language agnostic method that compares symbols for edit distance. In this implementation, the symbols can either be character or word for English.

The edit distance working involves, starting from one of the two inputs as source and using the operations available (depending on the edit distance version), it finds out the minimum cost or edit distance to reach the other input i.e., target. 

The following figure shows working of the method, where the optimum path (with least cost) is along the diagonal.
![alt semantic search design](semantic-search-design.png)

