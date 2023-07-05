from faker import Faker
import random
import mysql.connector
import os

# MySQL 연결 설정
cnx = mysql.connector.connect(
    host=os.environ.get('HOST'),
    user=os.environ.get('USER'),
    password=os.environ.get('PWD'),
    database=os.environ.get('AD_DB')
)
cursor = cnx.cursor()

# Faker 객체 생성
fake = Faker()

# Slot 테이블에 더미 데이터 삽입
for i in range(11, 21):
    ad_num = random.randint(1, 5)
    query = f"INSERT INTO Slot (id, ad_num) VALUES ({i}, {ad_num})"
    cursor.execute(query)

# # AD 테이블에 더미 데이터 삽입
# for i in range(301, 1001):
#     uri = fake.url()
#     size = random.randint(100, 1000)
#     target_link = fake.url()
#     content_type = random.choice(["image/jpeg", "image/png", "video/mp4"])
#     slot_id = random.randint(1, 10)
#     query = f"INSERT INTO AD (id, uri, size, target_link, content_type, slot_id) " \
#             f"VALUES ({i}, '{uri}', {size}, '{target_link}', '{content_type}', {slot_id})"
#     cursor.execute(query)

# # # Advertiser 테이블에 더미 데이터 삽입
# # for i in range(1, 100):
# #     name = fake.company()
# #     phone = fake.phone_number()
# #     query = f"INSERT INTO Advertiser (id, name, phone) VALUES ({i}, '{name}', '{phone}')"
# #     cursor.execute(query)

# # # AD_contract 테이블에 더미 데이터 삽입
# # for i in range(1, 1000):
# #     ad_id = i
# #     advertiser_id = random.randint(1, 5)
# #     price = random.randint(1000, 5000)
# #     start_date = fake.past_datetime(start_date="-30d", tzinfo=None)
# #     end_date = fake.future_datetime(end_date="+30d", tzinfo=None)
# #     query = f"INSERT INTO AD_contract (ad_id, advertiser_id, price, start_date, end_date) " \
# #             f"VALUES ({ad_id}, {advertiser_id}, {price}, '{start_date}', '{end_date}')"
# #     cursor.execute(query)

# # 변경 내용 커밋
# cnx.commit()

# # 연결 종료
# cursor.close()
# cnx.close()
