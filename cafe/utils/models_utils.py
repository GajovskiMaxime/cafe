
def table_name(table):
    return table.__tablename__.lower()


def column_name(table, key):
    return table.properties.get(key)['name'].lower()
