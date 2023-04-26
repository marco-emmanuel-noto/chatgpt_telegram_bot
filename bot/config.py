import yaml
import os
from pathlib import Path
import ast

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
telegram_token = os.environ["TELEGRAM_TOKEN"]
openai_api_key = os.environ["OPENAI_API_KEY"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
env_allowed_users = os.environ.get('ALLOWED_TELEGRAM_USERNAMES', '')
allowed_telegram_usernames = (lambda s: s.split(',') if s else [])(env_allowed_users)
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = os.environ["MONGODB_URI"]

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"

split_string = lambda s: s.split(',') if s else []