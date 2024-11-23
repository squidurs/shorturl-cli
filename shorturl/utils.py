import click
import json

def check_response_status(response, message=None):
    try:
        error_message = json.loads(response.text).get("detail", response.text)
    except json.JSONDecodeError:
        error_message = response.text
    if response.status_code == 200:
        if message:
            click.echo(message)
        return True
    elif 400 <= response.status_code < 500:
        click.echo(f"Client error: {response.status_code} - {error_message}")
    elif 500 <= response.status_code < 600:
        click.echo(f"Server error: {response.status_code} - {error_message}")
    else:
        click.echo(f"Unexpected error: {response.status_code} - {error_message}")
    return False

def get_auth_token():
    try:
        with open('token.txt', 'r') as token_file:
            return token_file.read().strip()
    except FileNotFoundError:
        click.echo("Authentication token not found. Please log in first.")
        return None