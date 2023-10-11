import numpy as np


def jaccard_similarity(set1, set2):
    """Compute the Jaccard similarity between two sets"""
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0


# other similarity metrics for the text comparison
def cosine_similarity(set1, set2):
    """Compute the cosine similarity between two sets"""
    intersection = len(set1 & set2)
    return intersection / (len(set1) * len(set2))


def sorensen_dice_similarity(set1, set2):
    """Compute the Sorensen-Dice similarity between two sets"""
    intersection = len(set1 & set2)
    return 2 * intersection / (len(set1) + len(set2))

def overlap_similarity(set1, set2):
    """Compute the overlap similarity between two sets"""
    intersection = len(set1 & set2)
    return intersection / min(len(set1), len(set2))


def tversky_similarity(set1, set2, alpha=0.5):
    """Compute the Tversky similarity between two sets"""
    intersection = len(set1 & set2)
    return intersection / (
        intersection
        + alpha * (len(set1) - intersection)
        + (1 - alpha) * (len(set2) - intersection)
    )


def _jaro_similarity(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    match_distance = max(len_s1, len_s2) // 2 - 1

    common_chars_s1 = []
    common_chars_s2 = []

    for i, char in enumerate(s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)

        if char in s2[start:end]:
            common_chars_s1.append(char)
            common_chars_s2.append(s2[start:end][s2[start:end].index(char)])

    m = len(common_chars_s1)
    if m == 0:
        return 0.0

    transpositions = sum(c1 != c2 for c1, c2 in zip(common_chars_s1, common_chars_s2)) // 2
    jaro_similarity = (m / len_s1 + m / len_s2 + (m - transpositions) / m) / 3
    return jaro_similarity


def jaro_winkler_similarity(s1, s2, p=0.1):
    jaro_sim = _jaro_similarity(s1, s2)
    common_prefix_len = 0

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 == c2:
            common_prefix_len += 1
        else:
            break

    jaro_winkler_sim = jaro_sim + (common_prefix_len * p * (1 - jaro_sim))
    return jaro_winkler_sim



def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
 
    matrix = np.zeros ((size_x, size_y)) 
 
    for x in range(size_x):
        matrix [x, 0] = x # row aray with elements of x
    for y in range(size_y):
        matrix [0, y] = y # column array with elements of y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]: # if the alphabets at the postion is same
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
 
            else:         # if the alphabbets at the position are different
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
 
    # returning the levenshtein distance
    return (matrix[size_x - 1, size_y - 1])