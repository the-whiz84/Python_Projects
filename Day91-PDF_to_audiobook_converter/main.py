import boto3
import PyPDF2
import os

pdf_path = "./Privacy-Policy.pdf"

# Access AWS credentials from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_s3_bucket = os.getenv("AWS_S3_BUCKET")
region_name = os.getenv("AWS_REGION", "eu-central-1")


def pdf_to_text(pdf_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text


text = pdf_to_text(pdf_path)

# Initialize the Polly client
polly_client = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
).client("polly")

# Start the speech synthesis task and save it to S3 Bucket
response = polly_client.start_speech_synthesis_task(
    VoiceId="Joanna",
    OutputFormat="mp3",
    Text=text,
    Engine="neural",
    OutputS3BucketName=aws_s3_bucket,
)
