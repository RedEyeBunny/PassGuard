# **PassGuard**

A secure, user-friendly, and efficient password management tool that stores and organizes your credentials locally on your machine, prioritizing privacy and security.

---

## **Features**

- **Secure Local Storage**: Passwords are stored locally on your machine with encryption for maximum security.
- **Strong Password Generator**: Generate complex and secure passwords tailored to your needs.
- **User-Friendly Interface**: Intuitive and easy-to-navigate interface for managing credentials.
- **Search Functionality**: Quickly search for stored credentials by account name or category.
- **Multi-Platform Support**: Works seamlessly on Windows, macOS, and Linux.

---

## **Technologies Used**

- **Programming Language**: Python
- **Libraries**:
  - `tkinter` (for GUI)
  - `bcrypt` (for encryption)
  - `mysql` (for secure local database storage)
- **Development Tools**:
  - IDE of your choice (e.g., PyCharm, VS Code)
  - Virtual environment for dependency management

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. **Set Up the Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

---

## **Usage**

1. **Add Password**: Use the "Add Password" feature to store a new password. It includes options to categorize and generate strong passwords.
2. **View Passwords**: Browse your saved passwords. Passwords are decrypted securely in-memory when viewed.
3. **Search Passwords**: Quickly locate a password using the search bar.
4. **Edit/Delete Passwords**: Update or remove stored credentials as needed.

---

## **Security Measures**

- **Encryption**: All passwords are encrypted.
- **Master Password**: Access the password manager with a secure master password.
- **Local Storage**: All data is stored locally, ensuring no information is shared online.

---

## **Contributing**

We welcome contributions to improve this password manager!  
To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## **Future Enhancements**

- **Cloud Backup (Optional)**: Encrypted backups to cloud storage.
- **Browser Integration**: Autofill passwords directly in the browser.
- **Two-Factor Authentication (2FA)**: Enhance security with 2FA support.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Acknowledgments**

- Inspired by the growing need for secure password management.
- Thanks to open-source libraries like `cryptography` for making encryption accessible.
