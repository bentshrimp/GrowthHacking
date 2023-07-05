from faker import Faker
import random
import datetime
import mysql.connector
import os

# MySQL 연결 설정
cnx = mysql.connector.connect(
    host=os.environ.get('HOST'),
    user=os.environ.get('USER'),
    password=os.environ.get('PASSWORD'),
    database=os.environ.get('AD_DB')
)
cursor = cnx.cursor()

# Faker 객체 생성
fake = Faker()

# User 테이블에 더미 데이터 삽입
users = []
for _ in range(1000):
    ip = fake.ipv4()
    agent = fake.user_agent()
    location = fake.city()

    query = f"INSERT INTO User (ip, agent, location) VALUES ('{ip}', '{agent}', '{location}')"
    cursor.execute(query)
    users.append(ip)

# Event 테이블에 더미 데이터 삽입
for _ in range(1000):
    start_time = fake.date_time_between(start_date='-1y', end_date='now')
    user_ip = random.choice(users)
    type = random.choice(['click', 'hover', 'submit'])
    cursor_x_pos = random.randint(0, 100)
    cursor_y_pos = random.randint(0, 100)
    end_time = start_time + datetime.timedelta(minutes=random.randint(1, 30))

    query = f"INSERT INTO Event (start_time, user_ip, type, cursor_x_pos, cursor_y_pos, end_time) " \
            f"VALUES ('{start_time}', '{user_ip}', '{type}', {cursor_x_pos}, {cursor_y_pos}, '{end_time}')"
    cursor.execute(query)

# 변경 내용 커밋
cnx.commit()

# 연결 종료
cursor.close()
cnx.close()
