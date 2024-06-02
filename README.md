<h1 align="center">SMTP USER RECON</h1>


<p align="center">
<img src='./Images/images.png' alt='logo' width='300'/>
</p>

SMTP User Recon is a Python tool that allows you to verify the existence of users on an SMTP server. It uses the SMTP VRFY protocol to check if a specific user is registered on the specified SMTP server.

## Features
- Verification of SMTP user existence using the VRFY protocol.
- Reading the list of users from a text file.
- Colorization of output for easy interpretation (green for existing users, red for non-existent users or errors).
- Automatic reconnection to the SMTP server in case of disconnection.

## Usage

1. Ensure you have Python installed on your system.
2. Install the `colorama` library if you haven't already:
```python
pip install colorama
```
3. Configure the details of the SMTP server and create a `users.txt` file with the list of users to verify.
4. Run the `smtp_user_recon.py` script:
```python
python3 smtp_users_recon.py
```
5. Observe the output to determine the existence of the users on the specified SMTP server.

## Contributions

Contributions are welcome! If you have any ideas to improve this tool or have found any bugs, feel free to open an issue or send a pull request.

