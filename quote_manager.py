import json
import os

class QuoteManager:
    def __init__(self,filename="quotes.json"):
        self.filename=filename
        self.quotes=[]
        self.load_quotes()

    def load_quotes(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = f.read().strip()
                    if not data:
                        return []
                    return json.loads(data)
            except json.JSONDecodeError:
                print("⚠️ Warning: quotes.json is invalid JSON. Starting fresh.")
                return []
            return []
        else:
            self.quotes = []
        
    def save_quotes(self):
        with open("quotes.json", "w") as f:
            json.dump(self.quotes, f, indent=2)
    def add_quote(self,author,quote):
        self.quotes.append({
            "author":author,
            "quote":quote
        })
        self.save_quotes()
    def get_all_quotes(self):
        return self.quotes
    
    def delete_quote(self,index):
        if 0 <= index < len(self.quotes):
            self.quotes.pop(index)
            self.save_quotes()