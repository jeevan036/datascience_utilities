import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary data
nltk.download('punkt')

def tokenize_text(text):
    sentences = sent_tokenize(text)  # Sentence tokenization
    words = word_tokenize(text)  # Word tokenization
    return sentences, words

# Example usage
if __name__ == "__main__":
    sample_text = "Hello! How are you? This is an example sentence."
    sentences, words = tokenize_text(sample_text)
    print("Sentences:", sentences)
    print("Words:", words)
