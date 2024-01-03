import smtplib
import time
import os
from email.message import EmailMessage

# STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
CURRENT_TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 1. SMTP 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

EMAIL_ADDR = os.environ['PC_ALARM_ID']
EMAIL_PASSWORD = os.environ['PC_ALARM_PW']

# 2. SMTP 서버에 로그인
smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

# 3. MIME 형태의 이메일 메세지 작성
message = EmailMessage()
message.set_content(CURRENT_TIME + ' PC ON')
message["Subject"] = CURRENT_TIME + ' PC ON'
message["From"] = EMAIL_ADDR
message["To"] = EMAIL_ADDR

# 4. 서버로 메일 보내기
smtp.send_message(message)

# 5. 메일을 보내면 서버와의 연결 끊기
smtp.quit()