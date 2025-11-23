class DisplayManager: #Manages console display and formatting
    
    def __init__(self, config):
        self.config = config
    
    def clear_screen(self):
        #Clear console screen
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):#Print application header
        print("\n" + self.config.SEPARATOR)
        print(f"  {self.config.APP_NAME}")
        print(self.config.SEPARATOR + "\n")
    
    def print_menu(self):#Print main menu
        print("\n🍕 Option Station:")
        print(self.config.LINE)
        print("1.🍿 Explore the Unknown.")
        print("2. 🧠 Sherlock Search Mode.")
        print("3. 😴 Logging Out to Eat Maggi.")
        print(self.config.LINE)
    
    def print_categories(self, categories):
        #Print list of categories
        print("\n📚 CATEGORIES:")
        print(self.config.LINE)
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        print(self.config.LINE)
    
    def print_questions(self, category, questions):
        #Print list of questions for a category
        print(f"\n❓ QUESTIONS IN '{category}':")
        print(self.config.LINE)
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
        print(self.config.LINE)
    
    def print_answer(self, question, answer):
        #Print question and answer
        print("\n" + self.config.SEPARATOR)
        print(f"❓ Question: {question}")
        print(self.config.SEPARATOR)
        print(f"🤖 Answer:\n{answer}")
        print(self.config.SEPARATOR)
    
    def print_search_results(self, results):
        #Print search results
        print(f"\n🔍 SEARCH RESULTS ({len(results)} found):")
        print(self.config.LINE)
        for i, (category, question) in enumerate(results, 1):
            print(f"{i}. [{category}] {question}")
        print(self.config.LINE)
    
    def print_message(self, message):
        #Print a general message
        print(f"\n✨ {message}")