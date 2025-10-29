import re
from urllib.parse import urlparse

def is_valid_url(url):
    """Check if a string is a valid URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def format_message(message, max_length=4000):
    """Format message to ensure it doesn't exceed Telegram's message length limit"""
    if len(message) <= max_length:
        return message
    
    # Truncate and add ellipsis
    return message[:max_length-3] + "..."

def extract_urls(text):
    """Extract URLs from text"""
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    return url_pattern.findall(text)

def clean_text(text):
    """Clean text by removing extra whitespace and normalizing line breaks"""
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Replace multiple newlines with a double newline
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()