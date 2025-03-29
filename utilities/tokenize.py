import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK resources (run this once)
nltk.download('punkt')

def tokenize_text(text):
    # Tokenize into sentences
    sentences = sent_tokenize(text)
    print("Sentences:")
    print(sentences)
    
    # Tokenize into words
    words = word_tokenize(text)
    print("\nWords:")
    print(words)

if __name__ == "__main__":
    # Example text to tokenize
    sample_text = """Hello! This is a simple text to demonstrate tokenization using NLTK.
                     Tokenization splits the text into sentences and words."""

    # Tokenize the text
    tokenize_text(sample_text)
