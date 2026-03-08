# A6 – Cryptographic Implementation Used Offline

## Activity Description
This activity investigates cryptographic techniques used to protect data stored on physical devices. The focus is on identifying an example of offline cryptography that secures stored data from unauthorized access.

## Definition: Offline Cryptography

Offline cryptography refers to cryptographic techniques used to protect **data stored on physical devices**, also known as **data at rest**. These techniques ensure that stored information remains secure even if a device is lost, stolen, or accessed by unauthorized individuals (Whitman & Mattord, 2022).

Offline encryption is commonly used on personal computers, smartphones, and external storage devices to protect sensitive files.

---

## Discovery: Full Disk Encryption (AES)

A widely used offline cryptographic implementation is **Full Disk Encryption (FDE)** using the **Advanced Encryption Standard (AES)**.

Examples of technologies that use AES encryption include:

- **BitLocker** on Microsoft Windows
- **FileVault** on macOS
- **Android and iOS device encryption**

These technologies encrypt the entire storage drive so that all stored files are protected.

---

## How It Works

AES is a **symmetric encryption algorithm** that encrypts data in **128-bit blocks** using cryptographic keys of **128, 192, or 256 bits** (NIST, 2001).

When full disk encryption is enabled:

1. Data written to the disk is automatically encrypted.
2. When the system starts, the user must authenticate using a password, PIN, or biometric authentication.
3. Once authenticated, the system decrypts the disk so the operating system can access files normally.

Without the correct authentication credentials, the encrypted data remains unreadable.

---

## Importance

Offline cryptography protects stored data in several scenarios:

- **Lost or stolen laptops**
- **Unauthorized physical access to storage devices**
- **Compliance with data protection regulations**

Even if attackers gain physical access to the device, the encrypted data cannot be accessed without the correct encryption key.

---
## References

National Institute of Standards and Technology. (2001). *Announcing the Advanced Encryption Standard (AES) (FIPS PUB 197).* https://doi.org/10.6028/NIST.FIPS.197

Whitman, M. E., & Mattord, H. J. (2022). *Principles of information security* (7th ed.). Cengage Learning.https://unidel.edu.ng/focelibrary/books/Principles%20of%20Information%20Security%20by%20Whitman,%20Michael%20Mattord,%20Herbert%20(z-lib.org).pdf
