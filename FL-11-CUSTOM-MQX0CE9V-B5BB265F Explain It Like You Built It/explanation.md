# How I Built the Fade-In Animations (GSAP)

One of the parts I found most interesting while building this portfolio was figuring out how to make elements appear on the screen smoothly and professionally, rather than having them just pop up abruptly when the page loads. To achieve this, I used an animation library called **GSAP (GreenSock Animation Platform)**.

Imagine you're watching a theater play. When the curtains open, the actors aren't just standing stiffly in the middle of the stage. Instead, they walk in smoothly from the shadows (opacity: 0) until they are fully visible under the spotlight (opacity: 1), moving slightly into position to make the entrance feel dynamic.

This is exactly the concept I applied to the case study cards and text sections in my portfolio.

## How does it actually work?

First, in my HTML, I assign a specific class name—like `fade-in` or `glass-card`—to any text or image container that I want to animate.

Then, on the Javascript side (`main.js`), I use a GSAP command called `gsap.fromTo()`. The logic behind this command is incredibly straightforward:

1. **The Starting Point (From):** I tell GSAP, "Hey, when the page first loads, force all elements with the `fade-in` class to be completely transparent (`opacity: 0`) and push them down 30 pixels from their original position."
2. **The Ending Point (To):** Next, I give it the final instruction, "Over the course of 1 second, smoothly transition their color back to 100% visible (`opacity: 1`) and slide them up to their true, original position (`y: 0`)."

To make it feel less rigid (so the elements don't just appear all at exactly the same time), I added a property called `stagger: 0.2`. This means if there are four project cards in a row, the first card will appear, the second card will follow 0.2 seconds later, and so on. This creates a beautiful, cascading waterfall effect, like a row of dominoes falling gracefully.

By doing this, I ensure that my portfolio feels premium, responsive, and "alive" every time someone visits it, preventing any awkward, unstyled content from flashing on the screen during the initial browser render.
