from collections import Counter
import re

def detect_trends(data):
    all_texts = ' '.join(post['text'] for post in data)
    words = re.findall(r'\w+', all_texts.lower())
    word_freq = Counter(words)
    return word_freq.most_common(10)
