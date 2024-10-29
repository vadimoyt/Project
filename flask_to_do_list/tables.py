
from db import Database
from db_connection import DB_CONNECTION

db = Database(**DB_CONNECTION)

db.get_cursor().execute(
    "create table if not exists tasks ("
    "id serial primary key,"
    "category varchar(50),"
    "title varchar(250) not null,"
    "description text,"
    "status varchar(50) default 'todo',"
    "created_at timestamp default current_timestamp,"
    "dead_line timestamp,"
    "file_path varchar(255))"
)
db.get_cursor().execute(
    "insert into tasks (title, category, description, dead_line) values ('Running', 'Health', 'Run 5 km', '2024-12-25')"
)
db.get_cursor().close()