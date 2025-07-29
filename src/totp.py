from base64 import b32encode
from hashlib import pbkdf2_hmac
from pyotp import TOTP
from qrcode import QRCode
from qrcode import constants as qrConsts
from secrets import token_bytes
from getpass import getpass


def get_secret() -> str:
    while True:
        secret_input: str = getpass("Secret: ").strip()
        if secret_input:
            return secret_input
        else:
            print("Secret cannot be empty. Please enter a valid secret.")


def generate_totp_secret(secret: str) -> str:
    derived_key: bytes = pbkdf2_hmac(
        hash_name="sha512",
        password=secret.encode("utf-8"),
        salt=token_bytes(16),
        iterations=100_000,
        dklen=32,
    )
    return b32encode(derived_key).decode("utf-8").rstrip("=")


def display_qr_code(otp_uri: str) -> None:
    qr: QRCode = QRCode(
        version=1,
        error_correction=qrConsts.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(otp_uri)
    qr.make(fit=True)
    qr.print_ascii(tty=True)


def verify(totp: TOTP) -> None:
    while True:
        user_code: str = input(f"Enter the 6-digit code: ").strip()

        if len(user_code) == 6 and user_code.isdecimal():
            if totp.verify(user_code):
                return

            print("Invalid code. Please enter a 6-digit numeric code.")

        else:
            print("Incorrect code. Please try again.")


def totp_simulator() -> None:
    secret: str = get_secret()
    base32_secret: str = generate_totp_secret(secret)

    totp: TOTP = TOTP(base32_secret)
    otp_uri: str = totp.provisioning_uri(name="Barakadax", issuer_name="2FA demo")

    display_qr_code(otp_uri)

    verify(totp)
    print("--- Verification Successful! ---")
    print(f"Your original secret input was: '{secret}'")
    print("--- Program Finished ---")


if __name__ == "__main__":
    totp_simulator()
