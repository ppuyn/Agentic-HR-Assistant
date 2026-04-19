import pandas as pd
import re

class HRDataProcessor:
    def __init__(self, employee_csv):
        self.df = pd.read_csv(employee_csv)

    def clean_text(self, text):
        """Standardizes text for NLP tasks."""
        # Convert to string and lowercase first
        text = str(text).lower()
        # Remove special characters but keep basic punctuation if needed
        text = re.sub(r'[^a-z0-9\s]', '', text)
        # Remove extra internal whitespace
        return " ".join(text.split())

    def get_employee_record(self, name):
        """Simulates a database lookup for the Agent to use."""
        record = self.df[self.df['name'].str.lower() == name.lower()]
        if not record.empty:
            return record.to_dict('records')[0]
        return None