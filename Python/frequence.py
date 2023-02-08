def frequency(phrase):
    words = phrase.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(frequency("You already know who I am, My name is Topher and I think Olivia"))

