# Day 91 - PDF Parsing and Text-to-Speech Automation

This project is a short automation pipeline: read a PDF, extract its text, then hand that text to AWS Polly so it can generate speech. The code is compact, but it touches a few real production concerns at once: file parsing, cloud credentials, and asynchronous media generation.

That makes it a good lesson in stitching services together with minimal code.

## 1. Extract Text from the PDF Safely

The PDF step is isolated in its own function:

```python
def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text
```

That separation is important. PDF parsing is its own concern, and keeping it outside the AWS setup makes the script easier to understand and extend.

The function iterates page by page instead of assuming the whole document can be treated as one chunk immediately. That is a sensible pattern for document-processing workflows.

## 2. Keep Secrets Out of the Source Code

The script reads AWS configuration from environment variables:

```python
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_s3_bucket = os.getenv("AWS_S3_BUCKET")
region_name = os.getenv("AWS_REGION", "eu-central-1")
```

This is the right habit for any project that touches a cloud API. Secrets should not be hardcoded into scripts, especially for something like Polly where the output is also tied to a storage bucket.

The day is also a good reminder that "automation" often means coordinating local files with remote infrastructure.

## 3. Hand the Text to Polly as a Speech Task

Once the text is extracted, the script creates a Polly client:

```python
polly_client = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name,
).client("polly")
```

And then starts the speech synthesis task:

```python
response = polly_client.start_speech_synthesis_task(
    VoiceId="Joanna",
    OutputFormat="mp3",
    Text=text,
    Engine="neural",
    OutputS3BucketName=aws_s3_bucket,
)
```

This is a strong example of service composition:

- `pypdf` extracts content
- `boto3` sends it to Polly
- S3 stores the generated audio

The script does not try to play the audio locally. It delegates output delivery to AWS storage, which is often the right choice for long-running or cloud-based workflows.

## How to Run the PDF-to-Audiobook Script

1. Set the required environment variables:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_S3_BUCKET`
   - optionally `AWS_REGION`
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Verify that the PDF text is extracted and the speech synthesis task is created in Polly with output written to the configured S3 bucket.

## Summary

Today, you connected document parsing to cloud text-to-speech. The project reads a PDF page by page, keeps AWS credentials in the environment, and hands the extracted text to Polly as an MP3 synthesis task. The larger lesson is how small Python scripts can act as glue between local artifacts and managed cloud services.
