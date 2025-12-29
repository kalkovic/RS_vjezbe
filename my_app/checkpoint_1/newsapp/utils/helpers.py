def truncate(text: str, length: int = 100) -> str:
    if not text:
        return ""
    return text if len(text) <= length else text[:length].rstrip() + "..."
