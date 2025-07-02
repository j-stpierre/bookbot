def count_words(contents):
    words = contents.split()
    count = len(words)
    return count


def character_count(contents):
    counts = {}
    for char in contents:
        char = char.lower()
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts


def sorted_counts(count_dict):
    sorted = []
    for key in count_dict:
        sorted.append({"char": key, "num": count_dict[key]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


def sort_on(counts):
    return counts["num"]
