When prompted for an API token, you need to use your PyPI API token instead of your username and password. Here’s how you can generate and use an API token:

### Steps to Generate and Use a PyPI API Token

1. **Generate an API Token:**
   - Log in to your PyPI account at [PyPI](https://pypi.org/).
   - Go to your account settings by clicking on your username in the top right corner and selecting "Your projects".
   - Click on "Add API token".
   - Give your token a name (e.g., "colort-upload-token") and scope (usually "Entire account" is fine).
   - Click "Add token" and copy the generated token. **Make sure to copy it now, as you won't be able to see it again.**

2. **Upload Your Package Using the API Token:**
   - When prompted for your API token during the `twine upload` process, paste the token you copied.

### Example

1. **Generate the API Token:**
   - Follow the steps above to generate and copy your API token.

2. **Upload the Package:**
   - Run the upload command:
     ```sh
     twine upload dist/*
     ```
   - When prompted, paste your API token:
     ```sh
     Enter your API token: pypi-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
     ```

### Explanation

- **Generate an API Token:** This token is a secure way to authenticate your uploads to PyPI without using your username and password.
- **Upload the Package:** Use `twine upload dist/*` and provide the API token when prompted.

By using an API token, you ensure a more secure and streamlined process for uploading your package to PyPI. Once uploaded, anyone can install your package using:

```sh
pip install colort
```