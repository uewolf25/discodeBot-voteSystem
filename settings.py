# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env-python3.6')
load_dotenv(dotenv_path)

AP= os.environ.get("YOUR_TOKEN")
