import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(u.strip()) for u in os.getenv("ADMIN_IDS", "123456789").split(",") if u.strip()]

# Пути
DATA_PATH = 'data/'
FAQ_FILE = f"{DATA_PATH}faq.json"
HISTORY_FILE = f"{DATA_PATH}user_history.json"

# API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Webhook
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.getenv("PORT", "5000"))

# Email
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_USER = os.getenv("IMAP_USER")
IMAP_PASS = os.getenv("IMAP_PASS")
IMAP_FOLDER = os.getenv("IMAP_FOLDER", "INBOX")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

# Режим и лимиты
FREE_TEST_MODE = True  # True = все функции доступны всем

FEATURE_LIMITS = {
    'voice': 3,
    'pdf': 5,
    'llm': 2,
    'docx': 2,
    'cabinet': 0,
    'vip_notif': 0,
    'no_ads': 0,
    'support': 1,
}
