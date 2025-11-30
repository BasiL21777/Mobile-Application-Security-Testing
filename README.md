<div align="center">

# **DepiApk**

</div>

**DepiApk** is a powerful Python-based security scanner for Android applications. It is designed to detect vulnerabilities within APK files and provide developers, penetration testers, and security professionals with actionable insights into potential risks.

---

## **Features**

DepiApk provides a comprehensive set of security assessment capabilities for Android applications, including:

### **• APK Inspection**

Analyzes APK files to identify potential security weaknesses.

### **• Deep Analysis**

Utilizes custom Python routines to inspect code, application structure, and internal resources.

### **• Sensitive Data Detection**

Finds exposed credentials, API keys, tokens, and other sensitive information.

### **• Detailed Reporting**

Generates clear and well-structured **PDF** and **HTML** reports outlining vulnerabilities and remediation steps.

### **• CI/CD Integration**

Supports automation pipelines, allowing seamless integration into **CI/CD workflows** for continuous security monitoring.

### **• Intuitive Output**

Uses color-coded terminal messages to simplify the interpretation of findings.

---

## **Installation**

Before installation, ensure the following are installed:

* **Python 3.10+**
* **Java / OpenJDK**

### **Linux**

```bash
git clone https://github.com/BasiL21777/Mobile-Application-Security-Testing
cd Mobile-Application-Security-Testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Windows**

```bash
git clone https://github.com/BasiL21777/Mobile-Application-Security-Testing
cd Mobile-Application-Security-Testing
python3 -m venv venv
.\venv\Scripts\activate
pip install -r .\requirements.txt
```

---

## **Usage**

### **Scan an APK**

```bash
python DepiApk.py -apk file.apk
```

### **Scan Using Extracted Source Code (Faster)**

```bash
python DepiApk.py -apk file.apk -source <source-code-path>
```

### **Generate PDF and HTML Reports**

```bash
python DepiApk.py -apk file.apk -report
```

