import tkinter as tk
from faq_data import FAQ_DB
from config import Config
from chatbot_app import FAQChatbotApp

def main():
    root = tk.Tk()
    app = FAQChatbotApp(root, FAQ_DB, Config)
    root.mainloop()

if __name__ == "__main__":
    main()