# A5 – Cryptographic Implementation Used Online

## Activity Description
This activity investigates cryptographic techniques used to protect information transmitted over the Internet. The focus is on identifying a real-world cryptographic implementation used in online communication and explaining how it protects confidentiality, integrity, and authentication.

## Definition: Online Cryptography
Online cryptography refers to cryptographic mechanisms used to secure **data transmitted across networks such as the Internet**. These mechanisms ensure that communication between systems remains confidential, authentic, and protected from tampering. Online cryptography is essential for protecting sensitive information such as login credentials, financial transactions, and personal data (Stallings & Brown, 2018).

---

## Discovery: Transport Layer Security (TLS)

A widely used cryptographic implementation on the Internet is **Transport Layer Security (TLS)**. TLS is used in **HTTPS websites**, which secure communication between a user's web browser and a web server.

HTTPS can be identified in a browser through the **padlock icon** in the address bar, indicating that the connection is encrypted.

---

## How TLS Works

TLS establishes a secure communication channel through a process known as the **TLS handshake**.

During this process:

1. The client (web browser) connects to the server.
2. The server provides a **digital certificate** issued by a trusted Certificate Authority.
3. Both parties agree on encryption algorithms and generate shared cryptographic keys.
4. Once the handshake is complete, all communication is encrypted using symmetric encryption algorithms such as **AES-GCM**.

This ensures that the transmitted data cannot be intercepted or modified during transmission (Rescorla, 2018).

---

## Importance

TLS provides three important security protections:

- **Confidentiality** – encrypted communication prevents attackers from reading sensitive data.
- **Integrity** – cryptographic checks ensure that transmitted data has not been altered.
- **Authentication** – digital certificates verify the identity of the server.

These protections make TLS essential for secure services such as **online banking, e-commerce platforms, university login systems, and cloud services**.

---
## References

Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3 (RFC 8446).* RFC Editor. https://www.rfc-editor.org/rfc/rfc8446

Stallings, W., & Brown, L. (2018). *Computer security: Principles and practice* (4th ed.). Pearson.https://ebooks.karbust.me/Technology/Stallings,%20William_%20Brown,%20Lawrie%20-%20Computer%20Security_%20Principles%20and%20Practice-Pearson%20Education%20Limited%20(2018).pdf
