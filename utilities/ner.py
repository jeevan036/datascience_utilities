import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    """Extracts named entities from the given text."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
if __name__ == "__main__":
    sample_text = "Apple Inc. was founded by Steve Jobs in California."
    entities = extract_named_entities(sample_text)
    print("Named Entities:", entities)
