import tkinter as tk
from tkinter import filedialog, messagebox
import re
import PyPDF2

# Define job requirements dictionary for matching
job_requirements = {
    'skills': {'python', 'java', 'sql'},        # Example skills
    'experience': 2,                            # Example experience in years
    'certifications': {'certified developer', 'data analysis'},  # Example certifications
    'personality': 'team player'                # Example personality trait
}

# Function to read PDF content
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to calculate score based on job requirements
def calculate_score(content):
    content = content.lower()
    
    # Extract information using regex and add debug statements
    skills_match = re.search(r'skills(?:\s*[-:]\s*)(.*?)(?:experience|certifications|$)', content, re.DOTALL)
    skills = [skill.strip() for skill in skills_match.group(1).split('\n') if skill.strip()] if skills_match else []
    print("Extracted skills:", skills)  # Debugging

    experience_match = re.search(r'experience(?:\s*[-:]\s*)(\d+)', content)
    experience = int(experience_match.group(1)) if experience_match else 0
    print("Extracted experience:", experience)  # Debugging

    certifications_match = re.search(r'certifications(?:\s*[-:]\s*)(.*?)(?:interests|$)', content, re.DOTALL)
    certifications = [cert.strip() for cert in certifications_match.group(1).split('\n') if cert.strip()] if certifications_match else []
    print("Extracted certifications:", certifications)  # Debugging

    personality_match = re.search(r'personality(?:\s*[-:]\s*)(.*)', content)
    personality = personality_match.group(1).strip() if personality_match else ""
    print("Extracted personality:", personality)  # Debugging

    # Calculate score based on job requirements
    score = 6

    # 1. Skills matching
    skill_match = len(set(skills) & job_requirements['skills'])
    score += (skill_match / len(job_requirements['skills'])) * 4
    print("Skills match score:", score)  # Debugging

    # 2. Experience matching
    if experience >= job_requirements['experience']:
        score += 2
    print("Experience match score:", score)  # Debugging

    # 3. Certifications matching
    cert_match = len(set(certifications) & job_requirements['certifications'])
    score += (cert_match / len(job_requirements['certifications'])) * 2
    print("Certifications match score:", score)  # Debugging

    # 4. Personality match
    if job_requirements['personality'] in personality:
        score += 2
    print("Personality match score:", score)  # Debugging

    # Final score capped at 10
    final_score = min(score, 10)
    print("Final score:", final_score)  # Debugging
    return final_score

# Function to load file and display content in the GUI
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Document files", "*.docx *.pdf")])

    if file_path:
        try:
            if file_path.endswith(".pdf"):
                content = read_pdf(file_path)
            else:
                messagebox.showerror("Error", "Unsupported file format. Please select a .pdf file.")
                return

            # Display content in the text widget
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)

            # Calculate score and display it
            score = calculate_score(content)
            score_label.config(text=f"Score: {score} / 10")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

# Create the Tkinter application window with aesthetic enhancements
root = tk.Tk()
root.title("CV Viewer and Scorer")
root.geometry("700x600")
root.configure(bg="#212121")  # Dark background color

# Title label
title_label = tk.Label(root, text="CV Viewer and Scorer", font=("Helvetica", 16, "bold"), fg="#ffffff", bg="#212121")
title_label.pack(pady=10)

# Load button with styling
load_button = tk.Button(
    root,
    text="Load CV File",
    command=load_file,
    font=("Helvetica", 12, "bold"),
    bg="#1E88E5",  # Button color
    fg="white",
    activebackground="#1976D2",
    padx=20,
    pady=5,
    bd=0,
    relief="flat",
    cursor="hand2"
)
load_button.pack(pady=15)

# Text widget to display file content with scrollbars
text_frame = tk.Frame(root, bg="#212121")
text_frame.pack(fill="both", expand=True, padx=20, pady=10)
text_widget = tk.Text(
    text_frame,
    wrap=tk.WORD,
    font=("Helvetica", 10),
    bg="#424242",  # Darker background for text area
    fg="#ffffff",  # Light text color
    relief="flat",
    bd=1
)
text_widget.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)

# Label to display score with custom styling
score_label = tk.Label(root, text="Score: 0 / 10", font=("Helvetica", 14, "bold"), fg="#ffffff", bg="#212121")
score_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
