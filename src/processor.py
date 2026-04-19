import pandas as pd
import re

class HRDataProcessor:
    def __init__(self, employee_csv):
        self.df = pd.read_csv(employee_csv)

    def clean_text(self, text):
        """Standardizes text for NLP tasks."""
        text = re.sub(r'[^a-zA-Z0-9\s]', '', str(text))
        return text.strip().lower()

    def get_employee_record(self, name):
        """Simulates a database lookup for the Agent to use."""
        record = self.df[self.df['name'].str.lower() == name.lower()]
        if not record.empty:
            return record.to_dict('records')[0]
        return None