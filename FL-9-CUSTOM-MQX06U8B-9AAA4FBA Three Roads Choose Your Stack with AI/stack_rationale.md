# FL-9: Three Roads (Stack Rationale)

## The Constraints
- **Cost:** Must be 100% free forever.
- **Skill Level:** 7th-Semester IT student with AI/ML and Web Development experience, but I value speed and extreme low-maintenance.
- **Needs:** 4 static pages (Home, Work, About, Contact) mapping to case studies.
- **Display:** High-quality image galleries for UI/UX captures, text-heavy case studies, and external links to Scopus papers. No dynamic database needed yet.

## Three Stack Options (Simplest to Most Powerful)

### 1. Simplest: Markdown + GitHub Pages (Jekyll)
- **How to build:** Write pure Markdown files.
- **Hosting:** GitHub Pages (Free).
- **Backend:** None.
- **Trade-off:** Extremely fast to write, but very rigid to style. I wouldn't be able to implement my custom Identity Kit (Dark mode, specific fonts, custom layouts) easily without fighting the Jekyll templates.

### 2. The Middle Ground: Vanilla HTML + Tailwind CSS + Vanilla JS
- **How to build:** Write raw HTML files, use Tailwind CSS (via CDN or simple CLI) for rapid styling, and Vanilla JS for interactions.
- **Hosting:** GitHub Pages (Free).
- **Backend:** None (Static).
- **Trade-off:** Requires writing markup from scratch (unlike Markdown) and lacks component-based architecture (unlike React), but offers infinite styling flexibility with zero build-step overhead.

### 3. Most Powerful: Next.js + Vercel
- **How to build:** React components, App router, fully modular architecture.
- **Hosting:** Vercel (Free tier).
- **Backend:** Next.js API routes (Serverless).
- **Trade-off:** Overkill for a 4-page static portfolio. Introduces Node module dependency maintenance and a build process for a site that currently requires zero dynamic data fetching.

## My Decision: Vanilla HTML + Tailwind CSS + Vanilla JS
I am choosing the middle ground. 

**Why?**
1. **Maintenance ("Can I maintain this?"):** Yes. In two years, an NPM ecosystem for a React app will likely have deprecated packages. A Vanilla HTML file will still work perfectly in 2030 without requiring an `npm audit fix`. It is the ultimate low-maintenance stack.
2. **Displaying Work:** Tailwind gives me the exact granular control I need to implement my specific Identity Kit (Deep Navy, Electric Cyan) and arrange my image galleries perfectly, something Markdown cannot do.
3. **Pacing:** I can definitely finish this in two weeks because there is no boilerplate, no routing logic, and no state management to debug—just structural markup and utility classes.
