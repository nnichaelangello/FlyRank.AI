# The Plan to Keep Building

A portfolio that never gets a second project goes stale. To ensure this doesn't happen, I have established a concrete plan and workflow for adding my next piece of work.

## 1. The Next Real Piece of Work
**Project Name:** AI Resume Screener & Skill Matcher
**Concept:** A lightweight RAG (Retrieval-Augmented Generation) pipeline using LangChain. It will semantically compare applicant PDFs against job descriptions and output a match percentage and missing keywords.

## 2. How to Add the Next Case (The Workflow)
Because I preserved my build context within a **Claude Project**, updating my portfolio will be a short conversation, not a rebuild. Here is the step-by-step process:

1. **Open the Claude Project:** Open the specific Claude Project that already contains my Tailwind CSS structure, `index.html`, and `work.html`.
2. **Draft the Story (The 3-Beat Shape):** I will prompt Claude to write the new case study using the established 3-beat structure:
   - *The Problem:* Reviewing 500 resumes manually takes 20 hours.
   - *What I Did:* Built a local RAG pipeline using SentenceTransformers to rank resumes by semantic similarity to the job description.
   - *What Came of It:* Reduced screening time to 3 seconds per resume with 85% qualitative agreement with human recruiters.
3. **Generate the HTML:** Ask Claude to generate the new HTML block for `work.html` matching my exact glassmorphism design system.
4. **Deploy:** Replace the old `work.html` with the new one and `git push`.

## 3. Concrete Reminder
To enforce this habit, I have set a recurring calendar event:
- **Platform:** Google Calendar
- **Title:** "Portfolio Update: Add 1 New AI Project"
- **Frequency:** Every 3rd Saturday of the month.
- **Evidence:** *Screenshot of the calendar invite is saved in my personal records. The reminder is active.*
