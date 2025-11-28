
from textblob import TextBlob
def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using TextBlob.

    Parameters:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary containing polarity and subjectivity scores.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }
    
# Example usage
if __name__ == "__main__":
    sample_text = "I love programming! It's so much fun and rewarding."
    sentiment_scores = analyze_sentiment(sample_text)
    print(f"Sentiment Analysis:\nPolarity: {sentiment_scores['polarity']}\nSubjectivity: {sentiment_scores['subjectivity']}") 