positive_words = ["good", "great", "fantastic", "excellent", "happy", "love", "like", "enjoy"]
negative_words = ["bad", "terrible", "awful", "hate", "angry", "sad", "dislike", "worse"]

def analyze_sentiment(text):
    score = 0
    words = text.lower().split()
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return "positive" if score > 0 else "negative" if score < 0 else "neutral"