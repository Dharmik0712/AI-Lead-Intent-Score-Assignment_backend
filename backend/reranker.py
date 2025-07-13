KEYWORDS = {
    "urgent": +15,
    "interested": +10,
    "call back": +5,
    "please reach": +5,
    "not interested": -15,
    "unsubscribe": -50,
    "wrong number": -20,
    "no response": -10
}

def apply_reranker(initial_score: float, comment: str) -> int:
    comment = comment.lower()
    adjustment = sum(weight for keyword, weight in KEYWORDS.items() if keyword in comment)
    final_score = initial_score + adjustment
    return int(max(0, min(final_score, 100)))  # Clamp 0–100
