# Design Critique: Feedback and Fixes

**Proof Statement:** "I build robust, privacy-preserving Machine Learning and AI Computer Vision systems that solve real-world problems."

## The Feedback

I reached out to a fellow Computer Science student to review my live portfolio. I asked them to evaluate the site based on two specific questions:
1. *In ten seconds, what do I do?*
2. *Would you believe I'm good at it?*

**Reviewer's Response:**
> "The site looks incredible. The dark-mode, futuristic design gives off a very strong tech vibe, so I instantly believe you have the technical skills to back it up. However, regarding the first question: in the first 10 seconds, all I see on the home page is your name 'Michael Angello Q.R.' and a 'See The Proof' button. I know you're in tech, but I don't immediately know if you're a Web Developer, a Blockchain developer, or an AI engineer until I scroll down to read the smaller paragraph or navigate to the Work page. Also, as a minor note, the project cards look nice but they could use a slightly stronger shadow on hover to make them pop out more from the dark background."

## Sorting the Feedback

### Must-Fix (Critical for the 10-Second Test)
- **The Profession Subtitle:** The lack of a clear, bold title directly under my name in the Hero Section. If visitors don't instantly know what my exact specialization is within the first 10 seconds, the portfolio fails its primary job of immediate communication.

### Nice-to-Have (Later)
- **Stronger Hover Shadows:** The project cards already have a scaling hover animation (`hover:scale-[1.05]`), so adding an extra drop-shadow is a minor visual enhancement that can be addressed later. It doesn't break the core user journey.

## The Fixes Implemented

I tackled the **Must-Fix** issue immediately to ensure the site passes the 10-second test. 
I edited `index.html` and added a bold, bright accent subtitle directly beneath the main heading in the hero section:
`<h2 class="text-xl md:text-2xl text-accent font-mono mb-6">AI Researcher & ML Engineer</h2>`

**Result:**
Now, within one second of the page loading, a recruiter or visitor instantly reads:
**Michael Angello Q.R.**
*AI Researcher & ML Engineer*

This perfectly anchors my proof statement before they even have to scroll down to the "About" or "Work" sections.
