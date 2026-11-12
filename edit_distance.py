def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def jaro_winkler(s1, s2):
    jaro_score = jaro(s1, s2)
    prefix_length = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix_length += 1
        else:
            break
    return jaro_score + (0.1 * prefix_length * (1 - jaro_score))

def jaro(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 == 0 and len_s2 == 0:
        return 1.0
    max_distance = (max(len_s1, len_s2) // 2) - 1
    match_s1 = [False] * len_s1
    match_s2 = [False] * len_s2
    matches = 0
    for i in range(len_s1):
        start = max(0, i - max_distance)
        end = min(i + max_distance + 1, len_s2)
        for j in range(start, end):
            if match_s2[j]:
                continue
            if s1[i] != s2[j]:
                continue
            match_s1[i] = True
            match_s2[j] = True
            matches += 1
            break
    if matches == 0:
        return 0.0
    t = 0
    j = 0
    for i in range(len_s1):
        if match_s1[i]:
            while not match_s2[j]:
                j += 1
            if s1[i] != s2[j]:
                t += 1
            j += 1
    t //= 2
    return (matches / len_s1 + matches / len_s2 + (matches - t) / matches) / 3.0