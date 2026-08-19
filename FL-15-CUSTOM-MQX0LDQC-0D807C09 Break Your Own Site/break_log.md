# Site Break & Hardening Log

## Triage: Fix-Now
These are critical breaks in the site's functionality that were addressed immediately.

1. **Empty Form Submission (Contact Page)**
   - **The Break:** When clicking "Send" on the contact page without filling out any fields, the form submitted successfully, sending a blank email to the backend.
   - **The Fix:** Added `required` attributes to the HTML `<input>` and `<textarea>` elements to enforce client-side validation before submission.

2. **Missing SEO and Findability**
   - **The Break:** Searching the site on Google would display a random snippet of text because there was no `<meta name="description">`. Sharing the link on WhatsApp/LinkedIn showed a broken preview card.
   - **The Fix:** Injected comprehensive SEO tags (Description, Author) and OpenGraph tags (`og:title`, `og:description`, `og:image`) across all 4 HTML files.

## Triage: Known Limitations
These are edge cases or structural limitations that are acknowledged but not prioritized for a hotfix.

1. **Excessively Long Names in Contact Form**
   - **The Break:** If a user types a 200-character name, it might break the email formatting on the Formspree side.
   - **Limitation:** Since this is a simple static portfolio, we do not have a custom backend to sanitize or enforce strict character limits gracefully. The basic HTML `maxlength` is used, but advanced validation is out of scope.

2. **Canvas Performance on Extremely Old Devices**
   - **The Break:** The interactive GSAP background (particles and blobs) drops frames on older mobile devices with weak GPUs.
   - **Limitation:** We accept this performance hit. The target audience (Tech Leads, Recruiters) typically uses modern devices, and the aesthetic WOW factor on desktop outweighs the need to support legacy mobile hardware.
