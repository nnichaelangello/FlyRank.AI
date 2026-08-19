# Looking Back: The FlyRank Capstone Retrospective

If I could sit down with the version of Michael Angello from Week 1 of this internship, I think he’d be a little overwhelmed, but mostly incredibly proud of the velocity at which we just moved.

## What I Set Out to Do
When I started this track, my primary goal was simply to check the boxes: complete the ML assignments, build a passable website, and earn the certificate. I viewed the Machine Learning tasks and the Frontend Portfolio tasks as two completely separate silos. I wanted to prove that I could handle complex data pipelines (like my prior work on Federated Learning), while also having a place to host my resume. I didn't fully appreciate how intertwined the ability to *build* a model and the ability to *tell the story* of that model actually are.

## What Actually Changed
The biggest shift in my mindset occurred during the intersection of the ML validation audit (ML-09) and the portfolio design critiques (FL-12 & FL-18). 

On the ML side, hitting a 66% accuracy score early on felt like a massive win. But applying the diligence framework forced me to look closer, revealing a massive data leak because I was doing standard random splits instead of grouping by client ID. The real accuracy was 57%. Previously, I might have hidden that drop to look better. This track taught me that the honesty of the 57%—and the ability to explain *why* it dropped—is infinitely more valuable to an employer than a fake 66%. Honesty reads as credibility.

On the AI Fluency side, the biggest change was in how I view AI generation. In Week 1, I thought the magic of AI was in generating cool, complex graphics for my site. By Week 9 (FL-18), I realized that the real skill is *judgment*. I actively chose to reject AI-generated images for my main case studies, opting instead for real, slightly imperfect screenshots of the PRISMA and AKSARA dashboards. AI is a powerful tool for generating the code structure (like the Tailwind layouts and GSAP animations), but human judgment is required to curate the proof.

## What I'll Build Next
This momentum won't stop here. My next immediate project, detailed in FL-17, is an "AI Resume Screener & Skill Matcher." I plan to build a lightweight RAG pipeline using LangChain to semantically compare applicant PDFs against job descriptions. Because I preserved my Claude Project context, generating the frontend case study for this new project will take minutes, allowing me to focus entirely on the backend Python engineering. The habit is set.

## The Three Most Transferable Skills
If I have to distill the last several weeks into three core, highly employable skills that I am taking with me, they would be:

1. **Data Leakage Prevention & Honest Validation:** I now know exactly how to sniff out data leakage in standard datasets and implement `GroupShuffleSplit` or time-based splits. I know that a model's true value isn't its vanity accuracy, but its reliability in production.
2. **Translating Probabilities to Business Logic:** The ML-10 Action Playbook taught me that a stakeholder doesn't care about a "0.65 probability score." They care about a reason code like "Stale & Low CTR - Needs Content Update." I learned how to bridge the gap between Jupyter Notebook outputs and human workflows.
3. **AI-Native Frontend Assembly:** I don't need to be a senior UI/UX designer to build a premium, glassmorphism-styled website. By leveraging AI as a pair-programmer, I can rapidly assemble and deploy responsive, modern web applications that perfectly frame my backend engineering work.

This internship didn't just give me a certificate; it gave me an engine for my career. I now have the framework to build, the platform to showcase, and the fluency to articulate my value.
