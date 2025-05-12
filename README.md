# PomoDorito - Discord Pomodoro Bot 🍅⏰

PomoDorito is a Discord bot designed to help users manage their time using the Pomodoro technique. It provides timers and notifications to improve productivity and focus during work sessions.

## Features ✨

- Pomodoro timer with customizable work and break intervals ⏳
- Discord commands to start, pause, and reset timers 🎮
- Notifications and reminders in Discord channels 🔔
- Modular design using Discord Cogs for easy extension 🧩

## Installation 🛠️

1. Clone the repository:

   ```
   git clone https://your-repo-url.git
   cd discord-bot
   ```

2. Create and activate a Python virtual environment:

   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Discord bot token:
   ```
   BOT_TOKEN=your_discord_bot_token_here
   ```

## Running the Bot Locally ▶️

Run the bot using:

```
python -m pomobot
```

The bot will load the token from the `BOT_TOKEN` environment variable.

## Deploying as a Windows Service with NSSM 🖥️

To run Pomobot as a Windows service using NSSM:

1. Download and place `nssm.exe` in your deployment folder alongside the `pomobot` module.

2. Open Command Prompt as Administrator and navigate to the deployment folder.

3. Install the service:

   ```
   nssm install PomobotService
   ```

4. In the NSSM GUI:

   - Set **Path** to your Python executable (e.g., `C:\Users\YourName\.venv\Scripts\python.exe`).
   - Set **Startup directory** to the deployment folder path.
   - Set **Arguments** to `-m pomobot`.
   - Under the **Environment** tab, add a new variable:
     - Name: `BOT_TOKEN`
     - Value: your Discord bot token

5. Click **Install service**.

6. Start the service:
   ```
   nssm start PomobotService
   ```

## Testing 🧪

Unit tests are located in the `tests` directory. Run tests with:

```
pytest
```

## Contributing 🤝

Contributions are welcome! Please open issues or pull requests for improvements or bug fixes.

## License 📄

This project is licensed under the MIT License.
