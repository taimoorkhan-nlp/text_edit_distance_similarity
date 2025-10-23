import random
import string


# 1. Simple Edit distance
def simple_edit_distance(text1, text2, level="c"):
    if level == "w":
        text1 = text1.split(" ")
        text2 = text2.split(" ")
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


# 2. Levenstein edit distance
def levenshtein_edit_distance(text1, text2, level="c"):
    if level == "w":
        text1 = text1.split(" ")
        text2 = text2.split(" ")
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                substitution_cost = 2
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + substitution_cost,  # Substitution
                )

    return dp[m][n]


# 3. Damerau Levenstein edit distance
def damerau_levenshtein_distance(text1, text2, level="c"):
    if level == "w":
        text1 = text1.split(" ")
        text2 = text2.split(" ")

    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Populate the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if text1[i - 1] == text2[j - 1] else 1

            # Minimum cost of insertion, deletion, substitution
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion
                dp[i][j - 1] + 1,  # Insertion
                dp[i - 1][j - 1] + cost,  # Substitution
            )

            # Check for transpositions
            if (
                i > 1
                and j > 1
                and text1[i - 1] == text2[j - 2]
                and text1[i - 2] == text2[j - 1]
            ):
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost)  # Transposition

    return dp[m][n]
