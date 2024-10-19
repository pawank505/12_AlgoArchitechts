class Tweet:
    def __init__(self, full_text, polarity):
        self.full_text = full_text
        self.polarity = polarity

    # Add __str__ method to display full_text when printing
    def __str__(self):
        return self.full_text

    # Optional: Add __repr__ method to show tweet info in lists, etc.
    def __repr__(self):
        return f'Tweet(full_text="{self.full_text}", polarity={self.polarity})'
