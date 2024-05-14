from fastapi import FastAPI
import psycopg2
import datetime

app = FastAPI()

@app.get("/")
def insert_diary():
    
    diary_id = 1
    title = "タイトル"
    content = "内容"
    user_id = 2

    # データベースとのコネクションを確立
    connection = psycopg2.connect("host=dpg-cp10olvjbltc73e5dh9g-a.singapore-postgres.render.com dbname=diary_db_dl9t user=konomi password=Hdy3LHk3jDgyQM45S2gXifyNepDt9HoI")

    # カーソルをオープン
    cursor = connection.cursor()

    cursor.execute("select max(diary_id) as diary_id from t_diary where user_id = %s", (user_id))
    print(cursor.fetchall())
    # diary_id = int(cursor.fetchone()) + 1

    # now = datetime.datetime.now
    sql = "INSERT INTO t_diary (diary_id, title, content, registered_date, update_date, user_id) VALUES (%s, %s, %s, current_timestamp, current_timestamp, %s)"
    cursor.execute(sql, (diary_id, title, content, user_id))

    cursor.execute("SELECT * FROM t_diary")
    query_result = cursor.fetchall()

    connection.commit()    
    
    return query_result


