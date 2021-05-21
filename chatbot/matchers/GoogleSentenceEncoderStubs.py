import tensorflow_hub as hub
from scipy import spatial


class GoogleSentenceEncoder:
    threshold = 0.75

    def __init__(self):
        module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model = hub.load(module_url)
        print("module %s loaded" % module_url)

    def embed(self, user_input):
        pass

    def similarity(self, sentence_1, sentence_2):
        pass


if __name__ == '__main__':
    encoder = GoogleSentenceEncoder()
    print(encoder.similarity("how are you", "how are you doing"))   # 0.847
    print(encoder.similarity("what is your favorite subject?", "WHAT is the best subject in school?"))  # 0.798
    print(encoder.similarity("what is your favorite subject?", "how are you"))  # 0.285
