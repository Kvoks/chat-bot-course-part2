python3 -m venv .venv
source .venv/bin/activate
python -m bot

# python -m bot.recreate_database
# watch -n 1 'sqlite3 bot.sqlite -cmd ".mode box" "SELECT * FROM telegram_updates ORDER BY id DESC LIMIT 1"'
# watch -n 1 'sqlite3 bot.sqlite -cmd ".mode box" "SELECT * FROM users"'
