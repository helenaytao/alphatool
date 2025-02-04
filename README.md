# AlphaTool

AlphaTool is a Python-based program designed to protect sensitive information on Windows systems through advanced data encryption and security measures. It uses the `cryptography` library to provide robust encryption for files and directories, ensuring that your sensitive data remains secure.

## Features

- **Generate Encryption Key**: Generates a new encryption key and saves it to a file.
- **Encrypt Files**: Encrypts individual files using the loaded encryption key.
- **Decrypt Files**: Decrypts individual files using the loaded encryption key.
- **Protect Directory**: Encrypts all files in a specified directory.
- **Unprotect Directory**: Decrypts all files in a specified directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alphatool.git
   cd alphatool
   ```

2. Install the required Python package:
   ```bash
   pip install cryptography
   ```

## Usage

1. Run the program:
   ```bash
   python alpha_tool.py
   ```

2. Follow the prompts to enter the directory path you wish to protect.

## Important Notes

- Make sure to keep the `secret.key` file safe as it is required for decrypting your files.
- Loss of the encryption key will result in permanent data loss.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any feature improvements or bug fixes.

## Disclaimer

This tool is intended for educational purposes only. Use it at your own risk. The authors are not responsible for any data loss or damage.