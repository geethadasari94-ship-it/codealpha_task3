# 📧 Email Extractor using Python

A simple Python automation script that extracts email addresses from a `.txt` file and saves them into a separate output file.

## 🎯 Task Objective

The goal of this project is to automate the repetitive task of finding email addresses from a text file.

Instead of manually searching for email addresses, the Python script automatically identifies them and saves the results into another file.

## ✨ Features

* 📄 Reads text from a `.txt` file
* 🔍 Finds email addresses automatically
* 🚫 Removes duplicate email addresses
* 💾 Saves extracted emails into a separate file
* ⚡ Simple and fast automation

## 🛠️ Technologies Used

* **Python**
* **Regular Expressions (`re`)**
* **File Handling**

## 📂 Project Structure

```text
codealpha_task3/
│
├── email_extractor.py
├── emails.txt
├── extracted_emails.txt
└── README.md
```

## 🚀 How to Run

```bash
python email_extractor.py
```

After running the script, the extracted email addresses are saved in `extracted_emails.txt`.

## 🧪 Example

### Input — `emails.txt`

```text
Hello Geetha,

For support, contact support@example.com.

You can also contact admin@example.org
or sales@example.net.

Thank you.
```

### Output — `extracted_emails.txt`

```text
support@example.com
admin@example.org
sales@example.net
```

## 🌐 Demo / Output

**Live Demo:** Not applicable — this is a Python automation script that runs locally.

### Sample Output

```text
Email addresses extracted successfully!
Total emails found: 3
```

## 🔑 Key Concepts

* Regular Expressions using `re`
* File handling using `open()`
* Reading and writing text files
* Automation using Python

## 🎓 Internship Task

**Task:** Task Automation with Python Scripts

**Internship:** CodeAlpha Python Programming Internship

## 👩‍💻 Author

**D. Geeta Dasari**

B.Tech CSE (AI & ML)

## 🙏 Acknowledgement

Thanks to **CodeAlpha** for providing this internship opportunity and project task.

## 📄 License

This project is created for educational and internship purposes.
