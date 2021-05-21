class ExactMatch:

    def __init__(self):
        pass

    def similarity(self, sentence_1, sentence_2):
        pass


if __name__ == '__main__':
    encoder = ExactMatch()
    print(encoder.similarity("how are you", "how are you doing"))  # 0.0
    print(encoder.similarity("How are you", "how are you"))  # 1.0
    print(encoder.similarity("what is your favorite subject?", "WHAT is the best subject in school?"))  # 0.0
    print(encoder.similarity("what is your favorite subject?", "how are you"))  # 0.0
