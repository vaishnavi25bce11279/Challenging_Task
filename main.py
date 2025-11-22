# faq_data.py - FAQ Database Module
FAQ_DB = {
    "📚 Course & Subject": {
        "syllabus": "Check college portal under 'Academics'. Python: basics to OOP. Math: calculus & algebra. Physics: mechanics & thermodynamics.",
        "books": "Python: 'Python Crash Course'. Math: B.S. Grewal. Physics: H.C. Verma.",
        "electives": "Consider: career goals, difficulty, professor ratings, placement relevance.",
        "passing": "40% minimum (internal + external separately). Some need 50% combined."
    },
    "📝 Assignments": {
        "format": "Title → Certificate → Abstract → Contents → Introduction → Methodology → Results → Conclusion → References.",
        "ppt": "8-12 slides. Consistent theme. Use bullets (max 6/slide). Add images. Practice timing.",
        "projects": "Calculator, To-Do List, Student System, Weather App, Quiz App, Password Generator.",
        "deadline": "Check portal/emails. Usually 2-3 weeks. Late = penalties."
    },
    "🎓 Exams": {
        "pattern": "Internal: 30-40 marks. External: 60-70. Practicals: 20-30. Assignments: 10-20.",
        "question types": "MCQs (20-30%), Short answers (30-40%), Problems (30-40%).",
        "cgpa": "SGPA = Σ(Grade×Credits)/Total Credits. CGPA = avg of SGPAs. % ≈ (CGPA-0.75)×10",
        "fail": "Reappear in supplementary exam. Pay re-exam fees. May affect CGPA but won't fail year."
    },
    "🏫 College Policies": {
        "attendance": "75% minimum required. Below = detained from exams. Medical cases need certificate.",
        "medical leave": "Submit medical certificate within 3 days to HOD. Get approval before exam.",
        "reexam": "Apply within 7 days. Pay fees. Limited attempts (usually 2-3).",
        "bonafide": "Apply to admin office with ID proof. Takes 2-3 working days."
    },
    "💻 Lab & Practical": {
        "python setup": "Download Python → Install VS Code → Install Python extension → Create .py file.",
        "venv": "Virtual environment isolates project dependencies. Create: python -m venv myenv. Activate: myenv\\Scripts\\activate",
        "lab report": "Title → Aim → Theory → Code → Output → Result → Conclusion. Maintain file properly.",
        "submission": "Proper file binding. Sign all pages. Include code printouts. Submit before deadline."
    },
    "🗂️ Career Guidance": {
        "career options": "Software Dev, Data Science, Web Dev, Cybersecurity, Cloud, AI/ML, Product Management.",
        "certifications": "Python: PCAP, AWS, Azure, Google Cloud, Django, Data Science with Python.",
        "placements": "DSA practice, aptitude, resume building, mock interviews, company research.",
        "internships": "LinkedIn, Internshala, college portal, startup programs, professor references."
    },
    "🤝 Student Help": {
        "time management": "Create schedule. Prioritize tasks. Use Pomodoro (25min focus). Avoid procrastination.",
        "exam stress": "Sleep 7-8hrs. Exercise. Take breaks. Practice meditation. Talk to friends/counselor.",
        "presentation": "Practice multiple times. Maintain eye contact. Speak clearly. Use gestures. Handle Q&A confidently.",
        "study effectively": "Active recall. Spaced repetition. Teach others. Solve problems. Group study."
    }
}

# chatbot_gui.py - Main Application
import tkinter as tk
from tkinter import ttk, scrolledtext

class FAQChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Student FAQ Chatbot")
        self.root.geometry("850x650")
        self.root.configure(bg="#2c3e50")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = tk.Label(self.root, text="🎓 Student FAQ Chatbot", 
                         font=("Arial", 20, "bold"), bg="#2c3e50", fg="white")
        header.pack(pady=15)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Arial", 10), 
            bg="#ecf0f1", fg="#2c3e50", height=20
        )
        self.chat_display.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.chat_display.insert(tk.END, "Bot: Hello! Select a category and question below.\n\n")
        self.chat_display.config(state=tk.DISABLED)
        
        # Controls frame
        control_frame = tk.Frame(self.root, bg="#34495e")
        control_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Category dropdown
        tk.Label(control_frame, text="Category:", bg="#34495e", 
                fg="white", font=("Arial", 10)).grid(row=0, column=0, padx=5, sticky="w")
        
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            control_frame, textvariable=self.category_var, 
            values=list(FAQ_DB.keys()), state="readonly", width=30
        )
        self.category_combo.grid(row=0, column=1, padx=5, pady=5)
        self.category_combo.bind("<<ComboboxSelected>>", self.update_questions)
        
        # Question dropdown
        tk.Label(control_frame, text="Question:", bg="#34495e", 
                fg="white", font=("Arial", 10)).grid(row=1, column=0, padx=5, sticky="w")
        
        self.question_var = tk.StringVar()
        self.question_combo = ttk.Combobox(
            control_frame, textvariable=self.question_var, 
            state="readonly", width=50
        )
        self.question_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Ask button
        ask_btn = tk.Button(control_frame, text="Ask", command=self.ask_question,
                           bg="#27ae60", fg="white", font=("Arial", 11, "bold"),
                           padx=20, cursor="hand2")
        ask_btn.grid(row=1, column=2, padx=10)
        
        # Clear button
        clear_btn = tk.Button(control_frame, text="Clear Chat", command=self.clear_chat,
                             bg="#e74c3c", fg="white", font=("Arial", 10),
                             cursor="hand2")
        clear_btn.grid(row=0, column=2, padx=10)
        
    def update_questions(self, event=None):
        category = self.category_var.get()
        if category:
            questions = list(FAQ_DB[category].keys())
            self.question_combo['values'] = questions
            self.question_combo.set('')
            
    def ask_question(self):
        category = self.category_var.get()
        question = self.question_var.get()
        
        if not category or not question:
            self.add_message("Bot: Please select both category and question!", "bot")
            return
            
        answer = FAQ_DB[category][question]
        self.add_message(f"You: {question}", "user")
        self.add_message(f"Bot: {answer}", "bot")
        
    def add_message(self, message, sender):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"\n{message}\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.insert(tk.END, "Bot: Hello! Select a category and question below.\n\n")
        self.chat_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FAQChatbot(root)
    root.mainloop()
