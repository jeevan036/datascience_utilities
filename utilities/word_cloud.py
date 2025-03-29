from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    """
    Generates and displays a word cloud from the given text.
    
    Parameters:
        text (str): Input text for generating the word cloud.
    
    Returns:
        None
    """
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Example usage:
if __name__ == "__main__":
    sample_text = "Data Science Machine Learning Deep Learning Artificial Intelligence"
    generate_word_cloud(sample_text)
