import pandas as pd

CATEGORY_KEYWORDS = {
    "food": ["restaurant", "grocery", "coffee", "snack"],
    "transport": ["uber", "taxi", "bus", "fuel", "train"],
    "entertainment": ["movie", "game", "concert", "netflix"],
    "utilities": ["electricity", "internet", "water", "rent"],
    "shopping": ["clothes", "amazon", "mall", "store"],
    "health": ["medicine", "doctor", "gym", "hospital"]
}

def categorize_expense(description: str) -> str:
    desc_lower = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in desc_lower for word in keywords):
            return category
    return "other"

def process_csv(file_path: str):
    df = pd.read_csv(file_path)
    df['category'] = df['description'].apply(categorize_expense)
    return df.to_dict(orient="records")
