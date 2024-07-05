import requests

def check_validator_status(validator_address):
    api_url = f"https://api.yourvalidatornode.com/v1/validators/{validator_address}/status"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        status = response.json().get('status', 'UNKNOWN')
        print(f"Validator {validator_address} is currently {status}.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
