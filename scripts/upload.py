import boto3
import os
import mimetypes
import json

BUCKET_NAME = "patil-portfolio-site-2026"   # 🔁 change if needed (must be unique)
REGION = "ap-south-1"

s3 = boto3.client("s3")

# 1. Create bucket
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            "LocationConstraint": REGION
        }
    )
    print("✅ Bucket created")
except Exception as e:
    print("⚠️ Bucket may already exist:", e)

# 2. Disable block public access
s3.put_public_access_block(
    Bucket=BUCKET_NAME,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False
    }
)

print("✅ Public access enabled")

# 3. Upload files
folder_path ="C:/Users/patil/OneDrive/Desktop/AWS Projects/01-s3-static-website/website"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        content_type, _ = mimetypes.guess_type(file_path)

        if content_type is None:
            content_type = "binary/octet-stream"

        s3.upload_file(
            file_path,
            BUCKET_NAME,
            file,
            ExtraArgs={
                "ContentType": content_type
            }
        )

        print(f"📤 Uploaded {file}")

# 4. Add bucket policy (FIXED VERSION)
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }
    ]
}

s3.put_bucket_policy(
    Bucket=BUCKET_NAME,
    Policy=json.dumps(policy)
)

print("✅ Bucket policy added")

# 5. Enable static website hosting
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration={
        "IndexDocument": {"Suffix": "index.html"}
    }
)

print("🚀 Website deployed successfully!")

print(f"🌍 URL: http://{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com")