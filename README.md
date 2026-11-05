**🔐 Password Generator**

A simple, secure, and customizable password generator written in Python. It uses Python's built-in secrets module, which is designed for cryptographically strong random values, so the passwords it creates are suitable for real accounts.

**Features**
- Generate random passwords of any length
- Choose which character types to include: lowercase, uppercase, digits, and symbols
- Guarantees at least one character from each selected type
- Option to exclude look-alike characters (e.g. O, 0, l, 1, I)
- Generate multiple passwords in one run
- Uses secrets instead of random for cryptographic security
- No external dependencies

**Security tips**
- Use passwords of at least 12 characters; longer is better.
- Use a unique password for every account.
- Store passwords in a reputable password manager rather than in plain text files.
- Never reuse generated passwords across sites.

**Contributing**

Contributions are welcome!

1.Fork the repository
2.Create a feature branch (git checkout -b feature/my-feature)
3.Commit your changes (git commit -m "Add my feature")
4.Push to the branch (git push origin feature/my-feature)
5.Open a Pull Request
