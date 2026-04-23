# 🚀 AWS S3 Static Website Deployment using Python (Boto3)

##  Project Overview

This project demonstrates how to **automate the deployment of a static website on AWS S3** using Python and Boto3.

Instead of manually configuring AWS resources, the entire infrastructure setup and deployment process is handled programmatically.

---

##  Objective

* Automate AWS resource creation
* Deploy a static website without manual steps
* Understand real-world cloud automation using Python

---

##  Tech Stack

* AWS S3
* Python
* Boto3 (AWS SDK)
* HTML, CSS
* Git & GitHub

---

##  Features

* Creates S3 bucket automatically
* Configures public access settings
* Uploads website files programmatically
* Applies bucket policy for public access
* Enables static website hosting
* Outputs live website URL

---

##  Project Structure

```
01-s3-static-website/
│
├── website/
│   ├── index.html
│   ├── projects.html
│   └── style.css
│
├── scripts/
│   └── upload.py
│
└── README
```

---

## 🚀 How It Works

1. Python script connects to AWS using configured credentials
2. Creates an S3 bucket
3. Uploads static website files
4. Sets permissions and bucket policy
5. Enables static website hosting
6. Returns public website URL

---

## ▶ How to Run

```bash
aws configure
python upload.py
```

---

##  Output

A live static website hosted on AWS S3.
live URL : http://patil-portfolio-site-2026.s3-website-ap-south-1.amazonaws.com
---

##  Sample Output

### Live Website
![Website](assets/website.png)

###  AWS S3 Bucket
![S3](assets/s3.png)

###  Deployment Output
![Terminal](assets/terminal.png)

---

##  Learning Outcomes

* Hands-on experience with AWS S3
* Automation using Boto3
* Understanding cloud deployment workflows
* Debugging real-world AWS issues

---

##  Security Note

AWS credentials are not included in this repository. Use your own IAM user credentials.

---

##  Future Improvements

* Add CI/CD pipeline using AWS CodePipeline
* Integrate CloudFront for CDN
* Add custom domain using Route 53

---

##  Author
Mrunali Patil
