---
title: "DNS Flushing"
categories: [college-notes]
tags: [ethical hacking]
---

DNS flushing is the process of clearing any IP addresses or other DNS records from the DNS cache. These are replaced with new ones.

## Importance

- Sometimes, it resolves error 404 in websites.
- Prevents DNS cache poisoning.
- Keeps search behaviour hidden from browsers.
- Improves network troubleshooting.

## How to do

### Windows

Use ``ipconfig /flushdns`` in the Command prompt

### Linux

Usually, Linux doesn't have any sort of DNS cache. If it does, use this command : ``sudo systemd-resolve --flush-caches``.

### Chrome

Chrome keeps a separate DNS cache which can be cleared by typing ``chrome://net-internals/#dns`` into the address bar and clicking on Clear host cache button.

## When to flush?

- After updating a website's IP address.
- If DNS spoofing is detecting.
- If experiencing website connectivity issues.
