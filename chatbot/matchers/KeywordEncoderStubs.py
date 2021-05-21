import math
import re
from collections import Counter


def get_cosine(encoding_1, encoding_2):
    intersection = set(encoding_1.keys()) & set(encoding_2.keys())
    numerator = sum([encoding_1[x] * encoding_2[x] for x in intersection])
    sum1 = sum([encoding_1[x] ** 2 for x in list(encoding_1.keys())])
    sum2 = sum([encoding_2[x] ** 2 for x in list(encoding_2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator or denominator == 0:
        return 0.0
    else:
        return float(numerator) / denominator


class KeywordEncoder:

    def __init__(self):
        self.word = re.compile(r"\w+")

    def embed(self, text):
        pass

    def similarity(self, sentence_1, sentence_2):
        pass

if __name__ == '__main__':
    encoder = KeywordEncoder()
    print(encoder.similarity("how are you", "how are you doing"))  # 0.866
    print(encoder.similarity("what is your favorite subject?", "WHAT is the best subject in school?"))  # 0.507
    print(encoder.similarity("what is your favorite subject?", "how are you"))  # 0.0
