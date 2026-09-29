from client import ConstrainedChoiceDecoder

choices = ["fetch_url", "run_sql", "write_file"]
res = ConstrainedChoiceDecoder.match_choice("I want to run_sql now", choices)
print("Decoded Action:", res["matched"], f"(Confidence: {res['confidence']})")
