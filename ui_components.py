import tkinter as tk
from tkinter import ttk, scrolledtext
class ChatDisplay: #Chat display component 
    def __init__(self, parent, config):
        self.config = config
        self.widget = scrolledtext.ScrolledText(
            parent, 
            wrap=tk.WORD, 
            font=config.FONT_CHAT,
            bg=config.BG_CHAT, 
            fg=config.FG_PRIMARY,
            height=20, 
            insertbackground="white"
        )
        self.widget.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.add_message(config.WELCOME_MSG, is_bot=True, show_separator=False)
        self.widget.config(state=tk.DISABLED)
    
    def add_message(self, message, is_bot=False, show_separator=True):
        #Add a message to chat display
        self.widget.config(state=tk.NORMAL)
        self.widget.insert(tk.END, f"\n{message}\n")
        if is_bot and show_separator:
            self.widget.insert(tk.END, self.config.SEPARATOR + "\n")
        self.widget.see(tk.END)
        self.widget.config(state=tk.DISABLED)
    
    def clear(self):
        #Clear chat display
        self.widget.config(state=tk.NORMAL)
        self.widget.delete(1.0, tk.END)
        self.add_message(self.config.WELCOME_MSG, is_bot=True, show_separator=False)
        self.widget.config(state=tk.DISABLED)


class ControlPanel:#Control panel with dropdowns and buttons
    
    def __init__(self, parent, config, on_category_change, on_ask, on_clear):
        self.config = config
        self.frame = tk.Frame(parent, bg=config.BG_SECONDARY)
        self.frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Category
        tk.Label(
            self.frame, text="Category:", 
            bg=config.BG_SECONDARY, fg=config.FG_PRIMARY, 
            font=config.FONT_LABEL
        ).grid(row=0, column=0, padx=5, sticky="w")
        
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            self.frame, textvariable=self.category_var,
            state="readonly", width=35, font=config.FONT_COMBO
        )
        self.category_combo.grid(row=0, column=1, padx=5, pady=5)
        self.category_combo.bind("<<ComboboxSelected>>", on_category_change)
        
        # Question
        tk.Label(
            self.frame, text="Question:", 
            bg=config.BG_SECONDARY, fg=config.FG_PRIMARY,
            font=config.FONT_LABEL
        ).grid(row=1, column=0, padx=5, sticky="w")
        
        self.question_var = tk.StringVar()
        self.question_combo = ttk.Combobox(
            self.frame, textvariable=self.question_var,
            state="readonly", width=60, font=config.FONT_COMBO
        )
        self.question_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Buttons
        btn_frame = tk.Frame(self.frame, bg=config.BG_SECONDARY)
        btn_frame.grid(row=0, column=2, rowspan=2, padx=10)
        
        tk.Button(
            btn_frame, text="Ask", command=on_ask,
            bg=config.BTN_ASK, fg="white", font=config.FONT_BTN,
            padx=20, pady=5, cursor="hand2", relief=tk.FLAT
        ).pack(pady=2)
        
        tk.Button(
            btn_frame, text="Clear", command=on_clear,
            bg=config.BTN_CLEAR, fg=config.BTN_CLEAR_FG, 
            font=config.FONT_BTN_SMALL,
            padx=18, cursor="hand2", relief=tk.FLAT
        ).pack(pady=2)
    
    def set_categories(self, categories):
        #Set category dropdown values
        self.category_combo['values'] = categories
    
    def set_questions(self, questions):
        #Set question dropdown values
        self.question_combo['values'] = questions
        self.question_combo.set('')
    
    def get_selected_category(self):
        #Get selected category
        return self.category_var.get()
    
    def get_selected_question(self):
        #Get selected question
        return self.question_var.get()