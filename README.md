# Downloads Folder Organizer

The Downloads Folder Formatter is a Python script that helps organize files in the downloads folder by moving them to their respective folders based on their file types. It provides a convenient way to keep your downloads folder tidy and well-organized.

## Features

- Moves files from the downloads folder to their respective folders based on file types.
- Supports customizable folder destinations for different file types.
- Utilizes a DownloadChecker to prevent moving files that are still being downloaded.
- Can be scheduled to run automatically at regular intervals using Windows Task Scheduler.

## Getting Started

### Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/) package manager

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/downloads-folder-formatter.git
   ```

2. Navigate to the project directory:

   ```shell
   cd downloads-folder-formatter
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Usage

1. Configure the folder destinations for different file types in the `constants.py` file.
2. Set up the desired schedule for running the script using Windows Task Scheduler.
   - Create a new task and specify the path to the Python executable (`python.exe`) and the path to the `main.py` script.
   - Configure the desired schedule (e.g., every hour, every day).
3. Run the script manually to test the functionality:

   ```shell
   python main.py
   ```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify the content according to your specific project requirements.
