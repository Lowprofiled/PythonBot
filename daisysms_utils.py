import requests
import time


def daisysms_get_number(service: str = 'ub') -> tuple[str, str] | None:

    # Make the request
    r = requests.get(f'https://daisysms.com/stubs/handler_api.php?api_key=5okAduLi3uSg6six6IItiIcIEAPgKe&action=getNumber&service={service}&max_price=5.5')
    if r.status_code > 200:
        return none

    print(f"Response: {r.status_code}")
    print(f"Response: {r.text}")

    # Split the response text by colon to extract the ID and phone number
    parts = r.text.split(':')
    if len(parts) >= 3:
        id_number = parts[1]  # Extract ID
        phone_number = parts[2]  # Extract phone number

    if phone_number.startswith("1"):
        phone_number = phone_number[1:]



    # Now you can use the ID in another line of code
    print("ID:", id_number)
    print("Phone Number:", phone_number)

    return id_number, phone_number

def daisysms_poll_status(id_number: str) -> str | None:

    count = 0
    while True:

        if count == 15:
            return None

        status_url = f'https://daisysms.com/stubs/handler_api.php?api_key=5okAduLi3uSg6six6IItiIcIEAPgKe&action=getStatus&id={id_number}'
        r = requests.get(status_url)
        print(r.status_code)
        print(r.text)

        #condition to check for the otp
        # if otp:
        # return otp

        time.sleep(3)

        count += 1
