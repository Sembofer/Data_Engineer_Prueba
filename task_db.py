from cfg import SQL_DIR
from cfg import DB_CONNSTR
from conn_db import DB_connection


def query(number, data):
    df_rs = DB_connection(DB_CONNSTR, SQL_DIR).db_query(f"query_{number}", data)
    return df_rs

