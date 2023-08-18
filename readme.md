# Grailed Page Monitor Script

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This Python script monitors specified brand pages on Grailed and sends updates to a Discord webhook.

## Features

- Monitors Grailed brand pages for new items.
- Sends updates to a Discord webhook.
- Uses a configuration file (`config.json`) to specify brands and webhook settings.

## Prerequisites
- Python 3.8 or higher is required.

## Getting Started

1. Clone this repository:

    ```sh
    git clone https://github.com/NBAFrigge/GrailedMonitor
    cd grailed-page-monitor
    ```

2. Create a `config.json` file:

    ```json
    {
        "discord_webhook": "YOUR_DISCORD_WEBHOOK_URL",
        "brands": ["brand1", "brand2"]
    }
    ```

3. Run the script:

    ```sh
    python monitor.py
    ```

## Configuration

Edit the `config.json` file to customize the script's behavior:

- `discord_webhook`: Replace with your Discord webhook URL.
- `brands`: List of brand names to monitor.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.