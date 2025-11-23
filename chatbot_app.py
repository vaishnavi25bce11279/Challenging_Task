from chat_manager import ChatManager
from ui_components import DisplayManager


class ChatbotApp:
    #Main application controller
    
    def __init__(self, faq_database, config):
        self.config = config
        self.chat_manager = ChatManager(faq_database)
        self.display = DisplayManager(config)
        self.running = True
    
    def start(self):
        #Start the chatbot application
        self.display.clear_screen()
        self.display.print_header()
        print(self.config.WELCOME_MSG)
        
        while self.running:
            self.display.print_menu()
            choice = input("\n👉🕵️‍♂️ Agent,input your mission number: ").strip()
            
            if choice == self.config.MENU_VIEW_CATEGORIES:
                self.browse_categories()
            elif choice == self.config.MENU_SEARCH:
                self.search_questions()
            elif choice == self.config.MENU_EXIT:
                self.exit_app()
            else:
                print("\n❌🕵️‍♂️ Detective says:That choice has no evidence.Try again!")
    
    def browse_categories(self):
        #Browse categories and questions
        categories = self.chat_manager.get_categories()
        
        while True:
            self.display.print_categories(categories)
            choice = input("\n👉👻 Pick a category number… or press 0 to ghost the menu!: ").strip()
            
            if choice == '0':
                break
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(categories):
                    category = categories[idx]
                    self.browse_questions(category)
                else:
                    print("\n❌ 🐒 Oops! That number slipped on a banana peel. Try again.!")
            except ValueError:
                print("\n 🧮 Math is crying. Enter a valid number to make it smile again.")
    
    def browse_questions(self, category):
        """Browse questions in a category"""
        questions = self.chat_manager.get_questions(category)
        
        while True:
            self.display.print_questions(category, questions)
            choice = input("\n👉 Select question number (or 0 to go back): ").strip()
            
            if choice == '0':
                break
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(questions):
                    question = questions[idx]
                    answer = self.chat_manager.get_answer(category, question)
                    self.display.print_answer(question, answer)
                    input("\n📌 Press enter to unlock the next level...")
                else:
                    print("\n❌ Invalid question!Even Sherlock couldn't find it!")
            except ValueError:
                print("\n❌ Please enter a valid number!")
    
    def search_questions(self):
        """Search for questions by keyword"""
        keyword = input("\n🔍 Enter search keyword: ").strip()
        
        if not keyword:
            print("\n❌ Please enter a keyword!")
            return
        
        results = self.chat_manager.search_questions(keyword)
        
        if not results:
            print(f"\n❌ No questions found containing '{keyword}'")
            return
        
        self.display.print_search_results(results)
        
        choice = input("\n👉 Enter the result number to reveal the secrets… or 0 to teleport back: ").strip()
        
        if choice == '0':
            return
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(results):
                category, question = results[idx]
                answer = self.chat_manager.get_answer(category, question)
                self.display.print_answer(question, answer)
                input("\n📌 Press enter to unlock the next level...")
            else:
                print("\n❌ Error:That number doesn't live here!")
        except ValueError:
            print("\n❌ Please enter a valid number!")
    
    def exit_app(self):
        #Exit the application
        print("\n👋 VAISHBOT signing off! Remember me when I’m famous. Goodbye!!")
        self.running = False