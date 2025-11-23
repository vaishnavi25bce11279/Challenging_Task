class ChatManager:
    #Manages chat operations and FAQ retrieval
    def __init__(self, faq_database):
        self.faq_db = faq_database
        
    def get_categories(self):
        #Return list of all FAQ categories
        return list(self.faq_db.keys())
    
    def get_questions(self, category):
        #Return list of questions for a given category
        if category in self.faq_db:
            return list(self.faq_db[category].keys())
        return []
    
    def get_answer(self, category, question):
        #Retrieve answer for a specific question
        if category in self.faq_db and question in self.faq_db[category]:
            return self.faq_db[category][question]
        return "💀This question killed my last brain cell."
    
    def validate_selection(self, category, question):
        #Validate if category and question are selected
        return bool(category and question)