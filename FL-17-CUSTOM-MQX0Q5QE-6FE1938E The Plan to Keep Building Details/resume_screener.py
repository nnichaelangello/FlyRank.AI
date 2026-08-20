import os
import glob
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import PyPDF2
import warnings

# Suppress HuggingFace warnings for clean output
warnings.filterwarnings('ignore')

class AIResumeScreener:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        print(f"[SYSTEM] Loading AI Model '{model_name}'...")
        self.model = SentenceTransformer(model_name)
        print("[SYSTEM] Model loaded successfully.")

    def extract_text_from_pdf(self, pdf_path):
        """Extracts text from a single PDF file."""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + " "
        except Exception as e:
            print(f"[ERROR] Could not read {pdf_path}: {e}")
        return text.strip()

    def load_job_description(self, jd_path):
        """Loads the Job Description text."""
        with open(jd_path, 'r', encoding='utf-8') as file:
            return file.read().strip()

    def screen_resumes(self, resumes_dir, jd_path, output_csv=None):
        print(f"\n[SCAN] Reading Job Description from: {jd_path}")
        jd_text = self.load_job_description(jd_path)
        if not jd_text:
            print("[ERROR] Job Description is empty!")
            return

        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)

        pdf_files = glob.glob(os.path.join(resumes_dir, '*.pdf'))
        if not pdf_files:
            print(f"[WARNING] No PDF resumes found in {resumes_dir}")
            return

        print(f"[SCAN] Found {len(pdf_files)} resumes. Analyzing semantic match...")
        
        results = []
        for pdf_file in pdf_files:
            filename = os.path.basename(pdf_file)
            resume_text = self.extract_text_from_pdf(pdf_file)
            
            if not resume_text:
                results.append({"Candidate": filename, "Match Score (%)": 0.0, "Status": "Failed to read"})
                continue

            # Calculate semantic similarity
            resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
            cosine_score = util.cos_sim(jd_embedding, resume_embedding).item()
            match_percentage = round(cosine_score * 100, 2)
            
            results.append({
                "Candidate": filename,
                "Match Score (%)": match_percentage,
                "Status": "Analyzed"
            })

        # Sort and display results
        df = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        print("\n" + "="*50)
        print("[*] AI RESUME SCREENING RESULTS [*]")
        print("="*50)
        print(df.to_string(index=False))
        print("="*50)

        if output_csv:
            df.to_csv(output_csv, index=False)
            print(f"[SUCCESS] Results exported to {output_csv}")
            
        return df

if __name__ == "__main__":
    # Define paths relative to the script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resumes_folder = os.path.join(base_dir, "resumes")
    jd_file = os.path.join(base_dir, "job_description.txt")
    output_report = os.path.join(base_dir, "screening_report.csv")

    # Ensure directories exist
    os.makedirs(resumes_folder, exist_ok=True)

    if not os.path.exists(jd_file):
        with open(jd_file, 'w', encoding='utf-8') as f:
            f.write("We are looking for a Data Scientist with experience in Python, Machine Learning, Pandas, and Scikit-Learn. Must have strong analytical skills.")
        print(f"[INFO] Created dummy Job Description at {jd_file}")

    screener = AIResumeScreener()
    screener.screen_resumes(resumes_folder, jd_file, output_report)
