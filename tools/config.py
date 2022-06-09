import os
import yaml

CONFIG_FILE = os.environ.get('SCRAPER_CONFIG')

with open(CONFIG_FILE, 'r') as f:
    APP = yaml.safe_load(f)

SCRAPE_SCRIPT_PATH = APP['scrapeweb']['scrape_script_path']
SCRAPE_CACHE_PATH = APP['scrapeweb']['scrape_cache_path']
SCRAPEWEB_DB_PATH = APP['scrapeweb']['db_path']
TIMEZONE = APP['scrapeweb']['timezone']

MASTER_INTERNAL_HOST = APP['master_hosts']['internal']
MASTER_PUBLIC_HOST = APP['master_hosts']['public']

AWS_USER = APP['aws_resources']['aws_user']
S3_OUTPUT_BUCKET = APP['aws_resources']['s3_output_bucket']
S3_LANDING_DIR = APP['aws_resources']['s3_landing_dir']

ADMINS = (
    ( APP['admin']['name'], APP['admin']['email'] )
)

NOTIFY_LIST = APP['admin']['notify_list']
EMAIL_FROM_DOMAIN = APP['admin']['email_from_domain']