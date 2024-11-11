import os
import fitz  # PyMuPDF for reading PDF files
import re
import spacy
from textblob import TextBlob
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk

# Initialize spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Sample lists for skills and job titles
skills_list = ["python", "java", "data analysis", "machine learning", "c++", "sql", "web development"]
job_titles = ["software engineer", "data scientist", "frontend developer", "data analyst"]

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text")
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading PDF: {e}")
        return ""

# Function to clean the extracted text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Function to analyze skills and experience from text
def analyze_skills_experience(text):
    text = text.lower()
    found_skills = [skill for skill in skills_list if skill in text]
    found_titles = [job for job in job_titles if job in text]
    return found_skills, found_titles

# Function to predict personality traits based on text sentiment
def predict_personality_traits(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.3:
        return "Positive, Likely to be Agreeable"
    elif sentiment < -0.3:
        return "Negative, Likely to be Less Agreeable"
    else:
        return "Neutral"

# Function to score a candidate based on extracted features
def score_candidate(skills, titles, personality):
    score = 0
    score += len(skills) * 5
    score += len(titles) * 3
    if "Positive" in personality:
        score += 5
    elif "Negative" in personality:
        score -= 5
    return score

# Enhanced feedback on resume strength
def resume_feedback(score):
    if score >= 30:
        return "Excellent Resume!"
    elif score >= 20:
        return "Good Resume, but could use more specific skills."
    elif score >= 10:
        return "Average Resume, add more relevant projects and skills."
    else:
        return "Needs improvement, add relevant skills and experience."

# Function to process the selected PDFs and display results
def process_pdfs():
    pdf_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if not pdf_paths:
        return
    
    all_results = []
    
    for pdf_path in pdf_paths:
        raw_text = extract_text_from_pdf(pdf_path)
        cleaned_text = clean_text(raw_text)
        
        skills, titles = analyze_skills_experience(cleaned_text)
        personality = predict_personality_traits(cleaned_text)
        candidate_score = score_candidate(skills, titles, personality)
        
        result = {
            'file': pdf_path,
            'skills': skills,
            'titles': titles,
            'personality': personality,
            'score': candidate_score,
            'feedback': resume_feedback(candidate_score)
        }
        all_results.append(result)
    
    display_comparison_results(all_results)

# Function to display comparison results and the best CV
def display_comparison_results(results):
    result_text.delete(1.0, tk.END)
    
    highest_score = -1
    best_cv = None
    
    for result in results:
        result_text.insert(tk.END, f"Resume: {result['file']}\n")
        result_text.insert(tk.END, f"Skills found: {result['skills']}\n")
        result_text.insert(tk.END, f"Job titles found: {result['titles']}\n")
        result_text.insert(tk.END, f"Predicted personality traits: {result['personality']}\n")
        result_text.insert(tk.END, f"Candidate score: {result['score']}\n")
        result_text.insert(tk.END, f"Feedback: {result['feedback']}\n")
        result_text.insert(tk.END, "-"*50 + "\n")
        
        # Check if this resume has the highest score
        if result['score'] > highest_score:
            highest_score = result['score']
            best_cv = result['file']
    
    # Display the best CV based on the highest score
    if best_cv:
        result_text.insert(tk.END, f"\nBest Resume: {best_cv}\n")
        result_text.insert(tk.END, f"Highest Score: {highest_score}\n")
        result_text.insert(tk.END, "This CV stands out among the selected resumes.\n")

# GUI setup
root = ThemedTk(theme="breeze")
root.title("Personality Prediction System")
root.geometry("600x600")

# Style and theme enhancements
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 10))

# Title label
title_label = ttk.Label(root, text="Resume Comparison & Skill Analyzer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Button to select PDFs and process
select_button = ttk.Button(root, text="Select and Compare Resumes", command=process_pdfs)
select_button.pack(pady=10)

# Text box to display results
result_text = tk.Text(root, wrap="word", font=("Arial", 10), width=70, height=15)
result_text.pack(pady=10)

# Start the GUI main loop
root.mainloop()
