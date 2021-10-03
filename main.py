#1. 이메일 보내기 기본 예제

import smtplib
from email.mime.text import MIMEText

sendEmail = "se072@naver.com"
recvEmail = "nangpae2001@hanmail.net"
password = "C$j9223096"

smtpName = "smtp.naver.com" #smtp 서버 주소
smtpPort = 587 #smtp 포트 번호

text = "메일 보내기 테스트입니다."
msg = MIMEText(text) #MIMEText(text , _charset = "utf8")

msg['Subject'] ="Mail 전송 테스트"
msg['From'] = sendEmail
msg['To'] = recvEmail
print(msg.as_string())

s=smtplib.SMTP( smtpName , smtpPort ) #메일 서버 연결
s.starttls() #TLS 보안 처리
s.login( sendEmail , password ) #로그인
s.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
s.close() #smtp 서버 연결을 종료합니다.