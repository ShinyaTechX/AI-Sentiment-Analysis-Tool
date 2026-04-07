# re = regular expressions
# Used for: searching text, replacing patterns

import re

def clean_text(text: str) -> str:   # text: str -> input must be a string, -> str -> function returns a string
    text = text.lower()   # Turns all letters into lowercase
    text = re.sub(r"http\S+", "", text)   # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)   # Remove special characters
    return text.strip()   # Remove extra spaces(edges)
