import tensorflow_hub as hub
from scipy import spatial


class GoogleSentenceEncoder:
    threshold = 0.75

    def __init__(self):
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model = hub.load(module_url)
        print("module %s loaded" % module_url)

    def embed(self, user_input):
        return self.model([user_input.lower()])[0]

    def similarity(self, sentence_1, sentence_2):
        encoding_1 = self.embed(sentence_1)
        encoding_2 = self.embed(sentence_2)
        return 1 - spatial.distance.cosine(encoding_1, encoding_2)


if __name__ == '__main__':
    encoder = GoogleSentenceEncoder()
    print(encoder.similarity("how are you", "how are you doing"))   # 0.847
    print(encoder.similarity("what is your favorite subject?", "WHAT is the best subject in school?"))  # 0.798
    print(encoder.similarity("what is your favorite subject?", "how are you"))  # 0.285
