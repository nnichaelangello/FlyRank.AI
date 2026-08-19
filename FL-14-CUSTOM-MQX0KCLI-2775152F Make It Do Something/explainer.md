# Formspree Backend Explainer

## What is a Backend?
A backend is the "server-side" of a website. While the frontend (HTML/CSS) dictates how a website looks, the backend is responsible for processing data, talking to databases, sending emails, and handling logic that shouldn't happen directly in the user's browser.

## What My Feature Does
My feature is a working contact form on my portfolio. Instead of forcing users to click a `mailto:` link that opens their email client (which is often annoying or broken), they can type their message directly on my website and click "Send".

## How the Data Flows
1. **The User Submits:** A visitor fills out their Name, Email, and Message on my `contact.html` page and clicks the submit button.
2. **The Frontend Action:** The HTML `<form>` tag is configured with `action="https://formspree.io/f/YOUR_FORMSPREE_ID"` and `method="POST"`. This tells the browser to take the form data, package it up, and send an HTTP POST request to Formspree's servers.
3. **The Backend Processing (Formspree):** Formspree acts as my "Backend as a Service". Their servers receive the POST request, validate the data, and format it into a readable email.
4. **The Final Delivery:** Formspree's email servers send that formatted message directly to my personal Gmail inbox.

*(Note for testing: Since this uses Formspree's free tier, no backend coding was required on my part, saving infrastructure costs while providing a fully functional dynamic feature).*
