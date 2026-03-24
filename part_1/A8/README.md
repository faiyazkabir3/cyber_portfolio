# A8 – Cryptography Used in Internet of Things (IoT) Devices

## Activity Description
This activity investigates how cryptography is used to secure Internet of Things (IoT) devices. The goal is to identify a cryptographic method used in IoT systems and explain how it protects communication between connected devices.

---

## Definition: Internet of Things (IoT)

The **Internet of Things (IoT)** refers to a network of interconnected physical devices—such as smart home appliances, sensors, wearable technology, and embedded systems—that communicate and exchange data through the Internet. 

Because IoT devices often operate with limited computing power and energy resources, they typically rely on **lightweight cryptographic techniques** to ensure secure communication and protect sensitive data (Whitman & Mattord, 2022).

---

## Discovery: AES-CCM Encryption in IoT Networks

A commonly used cryptographic method in IoT devices is **AES-CCM (Advanced Encryption Standard – Counter with CBC-MAC)**.

AES-CCM is widely implemented in IoT communication protocols such as:

- **Thread**
- **Matter**
- **IEEE 802.15.4 wireless networks**

These protocols are commonly used in **smart home devices**, including smart lights, sensors, and connected security systems.

---

## How AES-CCM Works

AES-CCM combines two cryptographic mechanisms:

1. **AES encryption** – protects the confidentiality of transmitted data.
2. **CBC-MAC authentication** – verifies the integrity and authenticity of messages.

This combination provides **authenticated encryption**, meaning that both the confidentiality and integrity of the communication are protected.

When an IoT device sends data:

1. The data is encrypted using the AES algorithm.
2. A cryptographic authentication tag is generated.
3. The receiving device verifies the tag before accepting the message.

If the authentication fails, the message is rejected, preventing tampering or unauthorized communication (Thread Group, 2016).

---

## Importance

Cryptography is essential in IoT environments because these devices often operate in large interconnected networks.

AES-CCM helps to:

- **Secure communication between smart devices**
- **Prevent unauthorized device control**
- **Protect sensitive user data collected by sensors and appliances**

Without cryptographic protection, attackers could intercept device communications, manipulate commands, or gain control of IoT systems.

---


## References

Thread Group. (2016). *Thread network security*. https://www.threadgroup.org/technology/security

Whitman, M. E., & Mattord, H. J. (2022). *Principles of information security* (7th ed.). Cengage Learning. https://unidel.edu.ng/focelibrary/books/Principles%20of%20Information%20Security%20by%20Whitman,%20Michael%20Mattord,%20Herbert%20(z-lib.org).pdf
Chaskar, H. (2017, December 27). IoT security using BLE encryption. Network Computing. https://www.networkcomputing.com/network-security/iot-security-using-ble-encryption
