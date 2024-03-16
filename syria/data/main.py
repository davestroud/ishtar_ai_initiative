import boto3
import requests
from datetime import datetime
import os


def download_latest_dataset(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)


def upload_to_s3(bucket_name, local_filename, s3_filename):
    s3 = boto3.client('s3')
    s3.upload_file(local_filename, bucket_name, s3_filename)


def main():
    url = "https://data.humdata.org/dataset/9d37a9b1-3df5-4bb5-afa8-a22d2ea0e27a/resource/19ec44dc-1e00-49aa-a203-fb0e0a454f3a/download/syria_hrp_political_violence_events_and_fatalities_by_month-year_as-of-29feb2024.xlsx"
    bucket_name = "syria-ishtar-ai"
    s3_filename = "syria_hrp_political_violence_events_and_fatalities_by_month-year_as-of-29feb2024.xlsx"
    local_filename = "latest_dataset.xlsx"

    # Download the latest dataset
    download_latest_dataset(url, local_filename)

    # Upload the dataset to S3
    upload_to_s3(bucket_name, local_filename, s3_filename)

    # Clean up: Delete local file
    os.remove(local_filename)


if __name__ == "__main__":
    main()
