# S3 Content Listing Service

This is an HTTP service built with **Flask** that lists the content of an **Amazon S3 bucket**. The service exposes an endpoint to retrieve the content of a specified path or the top-level content of the bucket.

## Features

- List the top-level content of an S3 bucket.
- List content for a specific path in the S3 bucket.

## Requirements

- Python 3.7 or higher
- **Flask** web framework
- **boto3** AWS SDK for Python
- **AWS account** with an S3 bucket and appropriate permissions for accessing the bucket

## Setup

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

`
git clone https://github.com/your-username/s3-listing-service.git
cd s3-listing-service
2. Install Dependencies
Install the required dependencies using pip:


Copy code
pip install -r requirements.txt
3. Set Environment Variables
Make sure to set the following environment variables for the AWS S3 bucket and region:

AWS_BUCKET: The name of your S3 bucket.
AWS_REGION: The region where your S3 bucket is located (e.g., us-east-1).
You can set them in your terminal:

Copy code
export AWS_BUCKET="your-bucket-name"
export AWS_REGION="us-east-1"
Or, you can use a .env file with a library like python-dotenv (you may need to install python-dotenv via pip).

4. Run the Service
Start the Flask web server with:

Copy code
python app.py
This will run the service locally at http://3.131.36.145:5000/list-bucket-content/
