from faq_data import FAQ_DB
from config import Config
from chatbot_app import ChatbotApp

def main():
    app = ChatbotApp(FAQ_DB, Config)
    app.start()

if __name__ == "__main__":
    main()