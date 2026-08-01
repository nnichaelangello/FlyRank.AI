# PF-04: DNS Walkthrough

## What happens when someone types my URL?
When a user types `michaelangello.flyrank.ai` into their browser, a multi-step process happens in the background to connect them to my Netlify-hosted portfolio.

1. **The Resolver:** The user's browser doesn't know where `michaelangello.flyrank.ai` is. It asks their internet service provider's "Resolver" (like a digital phonebook operator) to find it.
2. **The Nameserver:** The resolver searches the global internet directory and eventually reaches the Nameserver that controls the `flyrank.ai` domain. 
3. **The Record:** The nameserver looks at its internal ledger. It sees a specific rule (a record) that says: "If someone asks for the `michaelangello` subdomain, don't give them an IP address directly. Instead, point them to `michaelangello.netlify.app`." This type of "alias" rule is called a **CNAME record**.
4. **The Response:** The nameserver tells the resolver this alias. The resolver then looks up Netlify's actual IP address, hands it back to the user's browser, and the browser loads my portfolio securely over HTTPS!

## Why CNAME?
A CNAME (Canonical Name) record is essentially a forwarding address. It is crucial because Netlify's server IP addresses can change dynamically for load balancing. If I used an A Record (which points to a hardcoded IP address), my site would break if Netlify updated their servers. By using a CNAME pointing to my Netlify domain, Netlify handles the complex IP routing automatically.

## Capstone Checklist
Once my capstone is approved and Ops provisions my subdomain:
1. Wait for Ops to confirm they have added the `CNAME` record pointing `michaelangello.flyrank.ai` to my free Netlify URL.
2. Log into Netlify -> Site Configuration -> Domain Management.
3. Click "Add Custom Domain" and type `michaelangello.flyrank.ai`.
4. Wait a few minutes for the DNS propagation to clear globally.
5. Check the "HTTPS/SSL" section in Netlify to ensure it says "Let's Encrypt certificate provisioned" so the site has the secure padlock.
6. Open a private browsing window, type `michaelangello.flyrank.ai`, and verify it loads correctly.
