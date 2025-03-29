from textblob import TextBlob

def analyze_sentiment(text):
    """Returns sentiment polarity (-1 to 1) and subjectivity (0 to 1)."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

# Example usage
if __name__ == "__main__":
    sample_text = "I love this product! It's amazing."
    polarity, subjectivity = analyze_sentiment(sample_text)
    print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")
