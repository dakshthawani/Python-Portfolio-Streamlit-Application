import ssl
import smtplib
import pandas as pd
import os


def send_mail(user_email, message):
    username = "dakshthawani70@gmail.com"
    password = os.getenv("PASSWORD")
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    # df = pd.read_csv("info.csv", sep=',')
    # print(df.columns)
    #
    # last_row = df.tail(1)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # for index, row in last_row.iterrows():
        #     receiver = row[user_email]
        server.sendmail(username, user_email, message)
    # """\
    # Subject: "class message Ritesh Sir"
    # Hi,
    # Class will be continue for this sunday also
    # message
    # """

# with smtplib.SMTP_SSL(host, port, context=context) as server:
#     server.login(username, password)
#     for index, row in df.iterrows():
#         receiver = row["email"]
#         message = f"Subject: Class message Ritesh Sir\n\nHi,\nClass will be continue for this sunday also\n{row['message']}"
#         server.sendmail(username, receiver, message)