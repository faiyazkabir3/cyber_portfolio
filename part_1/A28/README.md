# A28 – Password Security System Using bcrypt

## Definition

A security solution is a system designed to protect data from unauthorized access or misuse. In this project, the security solution focuses on secure password handling through password strength checking and password hashing using **bcrypt**. Bcrypt is specifically designed for password storage and provides stronger protection than general-purpose hashing methods (Whitman & Mattord, 2022).

---

## Project Description

This project implements a password security system that:

- checks password strength
- rejects weak passwords
- hashes passwords using **bcrypt**
- stores hashed passwords securely
- avoids storing passwords in plain text

---

## How It Works

1. The user enters a username and password  
2. The system checks password strength  
3. Weak passwords are rejected  
4. Stronger passwords are hashed using bcrypt  
5. The username and hashed password are stored in a file  

---

## Features

### 1. Password Strength Checker
The system checks for:

- minimum length of 8 characters
- uppercase letters
- lowercase letters
- numbers
- special characters

### 2. Secure Hashing with bcrypt
The password is hashed using **bcrypt** before storage.

This means:

- the real password is not stored
- the password is harder to crack
- the system is more secure than plain-text storage

### 3. Automatic Salting
Bcrypt automatically includes a unique salt in each password hash.

This means:

- identical passwords produce different hashes
- rainbow table attacks are less effective

### 4. Secure Storage
Stored format:

`username:hashed_password`

Only the hashed password is stored in the file.

---

## Security Benefits

- protects stored passwords from direct exposure
- reduces the risk of brute-force attacks
- prevents plain-text password storage
- improves password security using industry-standard hashing

---

## Why bcrypt Was Used

Bcrypt was chosen because it is specifically designed for password hashing. Unlike simple hashing algorithms, bcrypt automatically handles salting and is intentionally slower, making password cracking more difficult.

---

## Evidence

•	secure_1.py file (source code)
•	password.txt (bcrypt hashed password output in text file)
•	screenshot of outputs

---

