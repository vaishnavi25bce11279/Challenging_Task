import tkinter as tk
from chat_manager import ChatManager
from ui_components import ChatDisplay, ControlPanel

class FAQChatbotApp:
    #Main application controller
    
    def __init__(self, root, faq_database, config):
        self.root = root
        self.config = config
        self.chat_manager = ChatManager(faq_database)
        
        self.setup_window()
        self.create_ui()
        
    def setup_window(self):
        #Configure main window
        self.root.title(self.config.WINDOW_TITLE)
        self.root.geometry(f"{self.config.WINDOW_WIDTH}x{self.config.WINDOW_HEIGHT}")
        self.root.configure(bg=self.config.BG_PRIMARY)
    
    def create_ui(self):
        #Create UI components
        # Header
        header = tk.Label(
            self.root, text="💻 Scholar Sphere",
            font=self.config.FONT_HEADER, 
            bg=self.config.BG_PRIMARY, 
            fg=self.config.FG_ACCENT
        )
        header.pack(pady=15)
        
        # Chat display
        self.chat_display = ChatDisplay(self.root, self.config)
        
        # Control panel
        self.control_panel = ControlPanel(
            self.root, self.config,
            on_category_change=self.handle_category_change,
            on_ask=self.handle_ask,
            on_clear=self.handle_clear
        )
        
        # Initialize categories
        self.control_panel.set_categories(self.chat_manager.get_categories())
    
    def handle_category_change(self, event=None):
        #Handle category selection change
        category = self.control_panel.get_selected_category()
        questions = self.chat_manager.get_questions(category)
        self.control_panel.set_questions(questions)
    
    def handle_ask(self):
        #Handle ask button click
        category = self.control_panel.get_selected_category()
        question = self.control_panel.get_selected_question()
        
        if not self.chat_manager.validate_selection(category, question):
            self.chat_display.add_message(self.config.ERROR_MSG, is_bot=True)
            return
        
        answer = self.chat_manager.get_answer(category, question)
        self.chat_display.add_message(f"👤 You: {question}", is_bot=False)
        self.chat_display.add_message(f"🤖 Siri's Cousin: {answer}", is_bot=True)
    
    def handle_clear(self):
        """Handle clear button click"""
        self.chat_display.clear()