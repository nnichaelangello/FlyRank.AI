# Demo Video Script (FL-09)

*Petunjuk: Buka terminal Anda, bersiaplah untuk mengeksekusi `python research_scout.py`. Buka kode `research_scout.py` di editor Anda agar bisa ditunjukkan di layar. Jalankan rekaman (Loom/OBS) dan bacakan naskah di bawah ini dengan suara natural.*

---

**[0:00 - Intro & The "Why"]**
"Hi, I'm Michael Angello. Today I'm going to demonstrate my Research Scout Agent, built in Python. The purpose of this agent is to help content strategists and researchers gather raw textual intelligence automatically. Instead of manually Googling a topic and clicking through articles, this agent does it for you and packages the text into a clean JSON file."

**[0:20 - Running the Code]**
"Let's run it live. I have my terminal open, and the current query is set to 'how to train a federated learning model'. I'll type `python research_scout.py` and hit enter."
*(Tekan enter di terminal)*
"As you can see, it's querying Google for the top 3 URLs. Now it's visiting each URL, sending an HTTP request, and parsing the HTML."

**[0:45 - Explaining a Design Decision]**
*(Buka kode `research_scout.py` di layar, sorot bagian BeautifulSoup)*
"While it runs, I want to point out a specific design decision here. I chose to use the `BeautifulSoup` library and specifically target paragraph tags `<p>`. This ensures we extract the actual readable body content of the article, filtering out most of the messy navigation bars, footers, and raw HTML tags."

**[1:10 - Showing the Output]**
*(Buka file `research_results.json` di editor)*
"The run just finished. It generated this `research_results.json` file. Let's open it. Here we can see the URL it visited, and a massive string of clean text extracted from the page. This is now ready to be fed into an LLM or an NLP pipeline for summarization."

**[1:30 - Explaining a Limitation]**
"However, it's important to be honest about limitations. Because this agent uses the `requests` library, it does not execute JavaScript. If it hits a modern React or Vue application that relies entirely on client-side rendering, or a site heavily protected by Cloudflare, it won't be able to scrape the content. For those edge cases, I would need to upgrade the architecture to use Playwright or Selenium."

**[1:55 - Outro]**
"And that's the Research Scout Agent. It's fast, lightweight, and gets the job done for standard web content. The full code and documentation are available on my GitHub. Thanks for watching." 

*(Hentikan Rekaman)*
