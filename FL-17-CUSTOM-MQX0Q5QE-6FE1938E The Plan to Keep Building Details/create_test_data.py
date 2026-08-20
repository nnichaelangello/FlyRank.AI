import os
from fpdf import FPDF

def create_resume(filename, name, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Resume: {name}", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=content)
    pdf.output(filename)
    print(f"Created: {filename}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resumes_dir = os.path.join(base_dir, "resumes")
    os.makedirs(resumes_dir, exist_ok=True)

    # Resume 1: Perfect Match
    content_1 = """Experience: 5 years as a Machine Learning Engineer.
    Skills: Python, Data Science, Pandas, Scikit-learn, HuggingFace, LLMs, NLP.
    I build scalable models and deploy them. I write clean maintainable code."""
    create_resume(os.path.join(resumes_dir, "Alice_Smith_ML.pdf"), "Alice Smith", content_1)

    # Resume 2: Partial Match
    content_2 = """Experience: 3 years as a Backend Developer.
    Skills: Python, Django, SQL, APIs.
    I can write clean code and deploy servers. I am interested in learning Machine Learning."""
    create_resume(os.path.join(resumes_dir, "Bob_Jones_Backend.pdf"), "Bob Jones", content_2)

    # Resume 3: No Match
    content_3 = """Experience: 4 years as a Graphic Designer.
    Skills: Adobe Photoshop, Illustrator, UI/UX Design, Figma.
    I create beautiful user interfaces and branding materials."""
    create_resume(os.path.join(resumes_dir, "Charlie_Brown_Design.pdf"), "Charlie Brown", content_3)

    print("Test resumes generated successfully.")
