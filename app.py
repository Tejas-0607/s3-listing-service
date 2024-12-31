import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# AWS S3 client
s3 = boto3.client('s3')

# Replace with your bucket name
BUCKET_NAME = 'projectbkt2024'

@app.route('/list-bucket-content/', defaults={'path': ''}, methods=['GET'])
@app.route('/list-bucket-content/<path:path>', methods=['GET'])
def list_bucket_content(path):
    try:
        # List objects from the bucket
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=path)
        contents = []
        
        for obj in response.get('Contents', []):
            contents.append({
                'Key': obj['Key'],
                'Size': obj['Size'],
                'LastModified': obj['LastModified'].isoformat()
            })
        
        return jsonify({'Contents': contents})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

