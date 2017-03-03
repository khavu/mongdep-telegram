import pymysql


def connect_db():
    database = pymysql.connect(host="127.0.0.1", user="root", passwd="123.abc", db="mongdep")
    cur = database.cursor()
    return cur, database


def select_db(table_name):
    cur, database = connect_db()
    cur.execute('DESCRIBE %s;' % table_name)
    fields_table = [i[0] for i in cur.fetchall()]
    cur.execute('select * from %s order by weigh_crawl desc;' % table_name)
    rows_table = cur.fetchall()
    cur.close()
    database.close()
    return fields_table, rows_table


def insert_db(table_name, values):
    cur, database = connect_db()
    fields = "(mong_link)"
    query = """INSERT INTO {table_name} {fields} VALUES (%s)""".format(table_name=table_name, fields=fields)
    #values = tuple(values)
    print(fields)
    print(values)
    cur.execute(query, values)
    database.commit()
    cur.close()
    database.close()
    return None


def find_value_db(table_name, field, value):
    cur, database = connect_db()
    query = """SELECT * FROM {table_name} WHERE {field} = '{value}'""".format(table_name=table_name, field=field,
                                                                              value=value)
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    database.close()
    return result


def select_db_option(table_name, field_selected, condition):
    cur, database = connect_db()
    query = """SELECT {field_selected} FROM {table_name} WHERE {condition}""".format(table_name=table_name,
                                                                                     field_selected=field_selected,
                                                                                     condition=condition)
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    database.close()
    return result


def update_db(table_name, field_updated, condition):
    cur, database = connect_db()
    query = """update {table_name} set {field_updated} where {condition}""".format(table_name=table_name,
                                                                                   field_updated=field_updated,
                                                                                   condition=condition)
    cur.execute(query)
    database.commit()
    cur.close()
    database.close()
    return None