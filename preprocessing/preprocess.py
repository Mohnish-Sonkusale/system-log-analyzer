import re 

def preprocess_log_line(line: str) -> str:
    """
    Clean and normalize a single raw system log line.
    """
    line = line.lower()
    line = re.sub(r"\d{4}-\d{2}-\d{2}","", line)  # Remove dates (e.g. 2025-07-01)
    line = re.sub(r"\[[^\]]*\]", "", line) # Remove bracketed sections [module]
    line = re.sub(r"[^\w\s]", "", line)  # Remove punctuation and special chars
    line = re.sub(r"\s+", " ", line).strip()  # Normalize whitespace
    
    return line
