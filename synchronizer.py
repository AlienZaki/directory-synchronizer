import os
import sys
import hashlib
import filecmp
import shutil
import argparse
import time
import logging


class Synchronizer:

    def __init__(self, source_path, replica_path, interval, log_file):
        self.source_path = source_path
        self.replica_path = replica_path
        self.interval = interval

        self.setup_logging(log_file)

    def setup_logging(self, log_file):
        """Configure logging to both console and file."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(),
            ]
        )

    def calculate_md5(self, file_path):
        """Calculate MD5 hash for a file."""
        md5 = hashlib.md5()
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(4096)  # Read in chunks
                if not data:
                    break
                md5.update(data)
        return md5.hexdigest()

    def sync(self, source, replica):
        """Synchronize files from source to replica."""

        # Compare directories using filecmp
        comparison = filecmp.dircmp(source, replica)

        # Copy updated files from source to replica
        for common_file in comparison.common_files:
            source_file_path = os.path.join(source, common_file)
            replica_file_path = os.path.join(replica, common_file)

            if self.calculate_md5(source_file_path) != self.calculate_md5(replica_file_path):
                logging.info(f'Updating file: {replica_file_path}')
                shutil.copy2(source_file_path, replica_file_path)

        # Copy new files and folders from source to replica
        for item in comparison.left_only:
            left_path = os.path.join(source, item)
            right_path = os.path.join(replica, item)

            if os.path.isdir(left_path):
                os.makedirs(right_path, exist_ok=True)
                logging.info(f'Created directory: {right_path}')
                self.sync(left_path, right_path)
            else:
                logging.info(f'Copying new file: {left_path}')
                shutil.copy2(left_path, right_path)

        # Remove files from replica that are not in source
        for item in comparison.right_only:
            right_path = os.path.join(replica, item)

            if os.path.isfile(right_path):
                logging.info(f'Removing file: {right_path}')
                os.remove(right_path)
            elif os.path.isdir(right_path):
                logging.info(f'Removing directory: {right_path}')
                shutil.rmtree(right_path)

        # Recursively sync subdirectories - this is where the magic happens :)
        for subdir in comparison.subdirs.keys():
            self.sync(
                os.path.join(source, subdir),
                os.path.join(replica, subdir)
            )

    def run(self):
        """Run the synchronization process periodically."""
        logging.info(f'Synchronization started - Source: {self.source_path}, Replica: {self.replica_path} Interval: {self.interval}')
        while True:
            try:
                self.sync(self.source_path, self.replica_path)
                time.sleep(self.interval)
            except KeyboardInterrupt:
                logging.info('Synchronization stopped by user.')
                sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Periodically synchronize directories.')
    parser.add_argument('source_path', help='Source directory path')
    parser.add_argument('replica_path', help='Replica directory path')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    parser.add_argument('log_file', help='Log file path')

    args = parser.parse_args()

    source_path = args.source_path
    replica_path = args.replica_path
    interval = args.interval
    log_file_path = args.log_file

    synchronizer = Synchronizer(source_path, replica_path, interval, log_file_path)
    synchronizer.run()
