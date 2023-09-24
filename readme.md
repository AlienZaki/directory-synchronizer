# Directory Synchronization Tool

This is a Python script for synchronizing directories periodically. It allows you to keep two directories in sync by copying updated and new files from a source directory to a replica directory while also removing files and directories from the replica that no longer exist in the source directory.

## Table of Contents

- [Features](#features)
- [Synchronization Strategy](#synchronization-strategy)
- [Logging](#logging)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Command-line Arguments](#command-line-arguments)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Periodically synchronizes directories.
- Copies updated and new files from the source to the replica directory.
- Removes files and directories from the replica that do not exist in the source directory.
- Utilizes the `filecmp` module for directory comparison.
- Employs hashing (MD5) to compare file content for accuracy.
- Supports specifying the synchronization interval.
- Provides logging to both a log file and the console.

## Synchronization Strategy

This script combines the powerful features of both the `filecmp` module and hashing (MD5) to ensure a robust synchronization process. It uses `filecmp` to perform directory comparison, identifying common files, files only present in the source, and files only present in the replica. For ensuring file content accuracy, MD5 hashing is used to compare the contents of common files, guaranteeing that only changed files are copied.

## Logging

The script provides detailed logging, both to a log file and the console. You can monitor the synchronization process in real-time by checking the log file and the console output.


## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed on your system.

## Usage

1. Clone this repository or download the script file to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script with the following command:

   ```shell
   python synchronizer.py <source_path> <replica_path> <interval> <log_file>
   ```

   Replace `<source_path>`, `<replica_path>`, `<interval>`, and `<log_file>` with the appropriate values:

   - `<source_path>`: The path to the source directory you want to synchronize.
   - `<replica_path>`: The path to the replica directory that will be synchronized with the source.
   - `<interval>`: The synchronization interval in seconds. The script will run periodically with this interval.
   - `<log_file>`: The path to the log file where synchronization logs will be stored.

4. The script will start synchronizing the directories based on the specified interval.

## Command-line Arguments

The script accepts the following command-line arguments:

- `source_path`: The path to the source directory you want to synchronize.
- `replica_path`: The path to the replica directory that will be synchronized with the source.
- `interval`: The synchronization interval in seconds.
- `log_file`: The path to the log file where synchronization logs will be stored.

## Example

Here's an example of how to use the script:

```shell
python synchronizer.py /path/to/source /path/to/replica 3600 /path/to/sync.log
```

In this example:

- `source_path` is set to `/path/to/source`.
- `replica_path` is set to `/path/to/replica`.
- `interval` is set to `3600` seconds (1 hour).
- `log_file` is set to `/path/to/sync.log`.


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This script is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.