"""Enum and Type Choice Constrained Decoder.
100% Python Standard Library.
"""

class ConstrainedChoiceDecoder:
    """Filters model logits/choices to valid enumerable tool actions and parameter values."""
    @staticmethod
    def match_choice(raw_output: str, choices: list) -> dict:
        cleaned = raw_output.strip().lower()
        for c in choices:
            if c.lower() == cleaned:
                return {"matched": c, "confidence": 1.0, "match_type": "exact"}

        for c in choices:
            if cleaned.startswith(c.lower()) or c.lower() in cleaned:
                return {"matched": c, "confidence": 0.85, "match_type": "substring"}

        return {"matched": choices[0] if choices else None, "confidence": 0.0, "match_type": "fallback"}
