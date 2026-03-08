# A7 – Cryptography Used in Modern Networks

## Activity Description
This activity investigates cryptographic techniques used to secure communication within modern network infrastructures. The focus is on identifying a cryptographic mechanism that protects the integrity and authenticity of network services.

## Definition: Cryptography in Modern Networks

Cryptography in modern networks refers to the use of encryption algorithms and cryptographic protocols to secure communication across network infrastructures. These mechanisms protect data exchanged between systems and ensure that network services remain trustworthy and resistant to manipulation (Stallings & Brown, 2018).

Cryptographic technologies are used in many network services, including:

- Secure web communication (TLS)
- Wireless network security (WPA3)
- Domain name systems
- Network authentication protocols

---

## Discovery: Domain Name System Security Extensions (DNSSEC)

An important cryptographic technology used in modern networks is **Domain Name System Security Extensions (DNSSEC)**.

DNSSEC enhances the traditional Domain Name System (DNS) by adding **cryptographic digital signatures** to DNS records. These signatures allow systems to verify that DNS responses originate from legitimate sources.

DNSSEC helps protect users from malicious attacks that attempt to redirect traffic to fraudulent websites.

---

## How DNSSEC Works

DNSSEC works by adding **digital signatures** to DNS records using **public key cryptography**.

The process works as follows:

1. The DNS server signs DNS records using a **private key**.
2. These signatures are published along with the DNS records.
3. DNS resolvers retrieve the corresponding **public key**.
4. The resolver verifies the digital signature to ensure the DNS data has not been altered.

If the signature validation fails, the DNS response is rejected (Arends et al., 2005).

---
## Importance

DNSSEC improves network security by preventing attacks that manipulate DNS responses.

It helps protect against:

- **DNS spoofing**
- **DNS cache poisoning**
- **Redirection to malicious websites**

By ensuring that DNS responses are authentic and unmodified, DNSSEC strengthens the reliability and security of Internet infrastructure.

---

## References

Arends, R., Austein, R., Larson, M., Massey, D., & Rose, S. (2005). *DNS Security Introduction and Requirements (RFC 4033).* RFC Editor. https://www.rfc-editor.org/rfc/rfc4033

Stallings, W., & Brown, L. (2018). *Computer security: Principles and practice* (4th ed.). Pearson. https://ebooks.karbust.me/Technology/Stallings,%20William_%20Brown,%20Lawrie%20-%20Computer%20Security_%20Principles%20and%20Practice-Pearson%20Education%20Limited%20(2018).pdf
