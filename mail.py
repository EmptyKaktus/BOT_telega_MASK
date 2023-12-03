import imaplib
import email
from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re

mail_pass = "1mo89OFgZ3-r8iO=C-=!"
username = ""
imap_server = "emptyilon3939@gmail.com"
imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, mail_pass)


