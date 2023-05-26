import pytest
import smtplib


@pytest.fixture()
def smtp_connection_yield():
    with smtplib.SMTP("smtp.163.com", 25, timeout=5) as smtp_connection:
        print("------start connection-------")
        yield smtp_connection
        print("-------end connection--------")


def test_send_mail(smtp_connection_yield):
    print("发邮件")

