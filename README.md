# aiogram_bot_template

This is a boilerplate for a Telegram bot built with [aiogram](https://github.com/aiogram/aiogram).  
It includes SQLite for database storage, Poetry for dependency management, and Docker for easy deployment.

---

## Features
- Aiogram 3 – Fast and asynchronous Telegram bot framework  
- SQLite – Lightweight database storage  
- Poetry – Modern dependency management  
- Docker – Containerized deployment  
- Modular Structure – Organized handlers, middlewares, and keyboards  
- Logging Middleware – Logs every incoming update  
- Inline & Reply Keyboards – Pre-built keyboards for user interaction  

---

## Installation

### Clone the Repository
```sh
git clone https://github.com/OldXrist/aiogram_bot_template.git
cd aiogram_bot_template
```

### Install Dependencies with Poetry
```sh
pip install poetry
poetry install
```

### Create a .env File
```ini
BOT_TOKEN=<your_telegram_bot_token_here>
ADMINS=123456789,987654321
LOG_LEVEL=DEBUG
```

### Running the Bot Locally
```sh
python bot.py
```

---

## Running with Docker

### Build and Start the Container
```sh
docker-compose up --build -d
```

### View Logs
```sh
docker logs -f aiogram_bot_template
```

### Stop and Remove the Container
```sh
docker-compose down
```
