# 🎬 Video Script: AI Resume Screener & Automation Agent

**Target Duration:** 3 - 5 Minutes
**Objective:** Fulfill the FL-09 graduation evaluation criteria (End-to-End Live Run, 1 Design Decision, 1 Limitation).

---

## 🕒 [0:00 - 0:45] Introduction & Problem Context
**On-Screen Visuals (What to show):** 
- Open the terminal / Command Prompt (leave it idle for now).
- Open File Explorer, displaying a folder containing dummy/fake PDF CVs that will be tested.

**🗣️ Voice Narration (What you should say):**
> "Hello everyone, my name is Michael. Today I will be demonstrating the AI Agent I built during my FlyRank.AI internship.
> 
> The problem I set out to solve is very straightforward: HR teams waste too much time manually reading through hundreds of resumes just to find a few relevant candidates. To solve this, I built an automated *AI Resume Screener*. This agent 'listens' to a specific folder, and whenever a new PDF resume arrives, it instantly reads the content, extracts the text, and measures the candidate's fit against the job criteria using Machine Learning Semantic Search. Let's see it in action!"

---

## 🕒 [0:45 - 2:30] Live End-to-End Run
**On-Screen Visuals (What to show):** 
1. In the Terminal, type and execute the command: `python "FL-04 Ship an Automation Workflow v2/automation_watcher.py"` (or wherever your watcher script is located).
2. Split your screen: Terminal on the left, File Explorer on the right.
3. Copy a dummy PDF CV file and Paste it into the folder monitored by the bot (e.g., an `Incoming_CVs` folder).
4. Show the terminal immediately reacting, processing the PDF, and outputting the match score!

**🗣️ Voice Narration (What you should say):**
> "Now, I am going to run my *Automation Watcher* script in the background... [press Enter in terminal].
> Okay, the bot is now active and listening. 
> 
> On the right side here is the HR folder. Now, imagine a new applicant submits their resume. I am going to drop this PDF file into the folder... [Paste the PDF file].
> 
> [Wait for the terminal to react]... There we go! As you can see in the terminal, my AI agent immediately detected the file. It instantly extracted the PDF text and sent it to the Machine Learning model for scoring. And here are the results! The AI gave a high relevance score because this candidate has Machine Learning experience that perfectly matches the open position. HR can now instantly identify top candidates in a matter of seconds!"

---

## 🕒 [2:30 - 3:30] Design Decision
**On-Screen Visuals (What to show):** 
- Open your text editor (VS Code or Cursor), and display the source code of `FL-17-CUSTOM-MQX0Q5QE-6FE1938E The Plan to Keep Building Details\resume_screener.py`
- Highlight or point your mouse at the line of code that imports `sentence-transformers` or initializes the AI algorithm.

**🗣️ Voice Narration (What you should say):**
> "So, how does this agent work under the hood? I want to highlight one crucial design decision I made.
> 
> Instead of just using basic keyword matching algorithms, I decided to use a *HuggingFace Sentence-Transformers* AI model (as you can see on this line of code). I made this decision because keyword matching is incredibly rigid. If HR is looking for a 'Software Engineer' but the applicant wrote 'Python Developer' on their CV, a legacy system would reject them. But by using *Sentence-Transformers*, my AI understands the **semantic meaning** and context of the words, so relevant applicants are still detected even if they use different synonyms."

---

## 🕒 [3:30 - 4:30] Limitation & Conclusion
**On-Screen Visuals (What to show):** 
- Open your FlyRank.AI GitHub Repository or show your face on camera (if using a small webcam bubble in the corner).

**🗣️ Voice Narration (What you should say):**
> "While this agent massively accelerates the workflow, it does have a limitation that I discovered during testing.
> 
> Its biggest limitation right now relates to language and PDF structure. Because the machine learning language model I'm using is predominantly trained on English data, its semantic accuracy will drop significantly if an applicant uploads a resume written in a regional language or a non-standard mixed language format. Furthermore, scanned image PDFs (without an OCR text layer) cannot be read by my current text extractor bot. Addressing these issues will be my primary focus for future work.
> 
> That concludes my *AI Resume Screener* demo for FlyRank.AI. This system is now ready to be scaled to the cloud. Thank you for watching!"

---
*(Stop screen recording)*
