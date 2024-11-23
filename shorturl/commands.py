import click
import requests
from shorturl.utils import *


#create user
@click.command()
@click.option('--username', prompt=True, help="Username for registration")
@click.password_option(help="Password for registration")
def register(username, password):
    """Create an account to use the URL shortener service"""
    response = requests.post('https://smollink.com/create-user', json={'username':username, 'password':password})
    
    if check_response_status(response):
        click.echo(f"User {username} created successfully.")


#login
@click.command()
@click.option('--username', prompt=True, help="Username for login")
@click.option('--password', prompt=True, hide_input=True, help="Password for login")
def login(username, password):
    """Login to gain access to the URL shortener service"""
    response = requests.post('https://smollink.com/login', data={"username": username, "password": password})
    if check_response_status(response, "Login successful."):
        token = response.json().get('access_token')
        if token:
            with open('token.txt', 'w') as token_file:
                token_file.write(token)
        else:
            click.echo("Failed to retrieve token.")
            

#shorten URL
@click.command()
@click.option('--url', prompt='Enter the URL', help='The URL you want to shorten')
@click.option('--custom', default=None, help='Custom short URL (optional)')
@click.option('--length', default=10, help='Length of the short URL (optional)')
def shorten(url, custom, length):
    """Shorten a given URL with optional custom short URL"""
    token = get_auth_token()
    if not token:
        click.echo("Failed to retrieve token.")
        return

    headers = {'Authorization': f'Bearer {token}'}
    
    response = requests.post('https://smollink.com/shorten', json={'url': url, 'custom_url': custom, 'length': length}, headers=headers)
    
    if check_response_status(response):
        result = response.json()
        click.echo(f"Short URL created: {result['short_url']}")

# list URLs (all: admin only. my: user specific)
@click.command()
@click.option('--all', is_flag=True, help='List all URLs (admin only)')
@click.option('--my', is_flag=True, help='List user URLs')
def list(all, my):
    """List all stored URLs (admin only)"""
    token = get_auth_token()
    if not token:
        click.echo("Failed to retrieve token.")
        return

    headers = {'Authorization': f'Bearer {token}'}
    
    if all and my:
        click.echo("Please use only one flag at a time: --all or --my.")
        return
    
    elif all:
        response = requests.get('https://smollink.com/list-urls', headers=headers)
        if check_response_status(response):
            url_list = response.json().get('url_pairs')
            click.echo(url_list)   
        
    elif my:
        response = requests.get('https://smollink.com/list-my-urls', headers=headers)
        if check_response_status(response):
            url_list = response.json().get('url_pairs')
            click.echo(url_list)
    else:
        click.echo('Specify a flag: --all or --my')

#lookup the original URL
@click.command()
@click.option('--short', prompt='Enter the short URL', help='The short URL to look up')
def lookup(short):
    """Look up the original URL from a short URL"""
    response = requests.get(f'https://smollink.com/lookup/{short}', json={'short_url': short})
    
    if check_response_status(response):
        original_url = response.json().get('original_url')
        click.echo(f"Original URL: {original_url}")

#change password
@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='New password.')
def change_password(username, password):
    """Change the password for your account"""
    token = get_auth_token()
    if not token:
        click.echo("Failed to retrieve token.")
        return

    headers = {'Authorization': f'Bearer {token}'}
    
    response = requests.post('https://smollink.com/change-password', json={'username': username, 'password': password},headers=headers)
    
    if check_response_status(response, 'Password changed successfully.'):
        return

