# ShortURL CLI

The **ShortURL CLI** is a command-line tool for interacting with a URL shortener service. It allows users to register, log in, shorten URLs, list stored URLs, look up original URLs, and manage their accounts.

---

## Features

- **User Registration**: Create a new user account.
- **User Login**: Log in and retrieve an authentication token.
- **Shorten URLs**: Generate a shortened URL with optional customizations.
- **List URLs**: View all stored URLs (admin) or only the URLs associated with your account.
- **Lookup URLs**: Retrieve the original URL associated with a short URL.
- **Change Password**: Update your account password securely.

---

## Installation

### 1. Clone the Repository
Clone the ShortURL repository to your local machine:

```bash
git clone https://github.com/squidurs/shorturl-cli.git
cd shorturl-cli
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
Set up a virtual environment to isolate dependencies:

For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Use the following commands to interact with the ShortURL CLI.

### Run the CLI
To access the CLI tool, execute:

```bash
python -m shorturl
```

This command will display the CLI's help menu with all available commands.

### Available Commands

#### 1. Register a New User
Register a new user by providing a username and password:

```bash
python -m shorturl register
```
You will be prompted to input a username and password interactively.

#### 2. Log In
Log in to your account to retrieve an authentication token:

```bash
python -m shorturl login
```
You will be prompted to input your username and password interactively. A successful login stores the authentication token in a local `token.txt` file.

#### 3. Shorten a URL
Create a short URL for any original URL:

```bash
python -m shorturl shorten --url <original_url> [--custom <custom_short_url>] [--length <length_of_short_url>]
```
- Replace `<original_url>` with the URL you want to shorten.
- Optionally specify:
  - `--custom` for a custom short URL slug.
  - `--length` for a randomly generated short URL of a specific length (default: 10).

Example:
```bash
python -m shorturl shorten --url https://example.com --custom mycustomurl
```

#### 4. List URLs
List stored URLs. Use either the `--all` or `--my` flag:

- **Admin:** View all stored URLs:
  ```bash
  python -m shorturl list --all
  ```

- **User:** View your URLs:
  ```bash
  python -m shorturl list --my
  ```

#### 5. Look Up a Short URL
Retrieve the original URL for a given short URL:

```bash
python -m shorturl lookup --short <short_url>
```
Replace `<short_url>` with the short URL you want to resolve.

Example:
```bash
python -m shorturl lookup --short mycustomurl
```

#### 6. Change Password
Change your account password:

```bash
python -m shorturl change-password
```
You will be prompted for your username and new password interactively.

### Example Workflow
Here’s an example workflow for using the ShortURL CLI:

1. Register a new user:
   ```bash
   python -m shorturl register
   ```
   Input the username and password when prompted.

2. Log in:
   ```bash
   python -m shorturl login
   ```
   Enter the credentials created during registration.

3. Shorten a URL:
   ```bash
   python -m shorturl shorten --url https://example.com 
   ```
   This will generate a random short URL for the given original URL.

4. List your URLs:
   ```bash
   python -m shorturl list --my
   ```

5. Look up a short URL:
   ```bash
   python -m shorturl lookup --short mycustomurl
   ```

---

Enjoy using the ShortURL CLI!   