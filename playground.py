from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
    Filter,
    ColumnValue,
    Include,
    Order,
)
from typing import Optional

sqlite_loom = Dataloom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    sql_logger="console",
)

pg_loom = Dataloom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    sql_logger="console",
)

mysql_loom = Dataloom(
    dialect="mysql",
    database="hi",
    password="root",
    user="root",
    host="localhost",
    logs_filename="logs.sql",
    port=3306,
    sql_logger="console",
)


class User(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)
    tokenVersion = Column(type="int", default=0)


class Profile(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="profiles")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    avatar = Column(type="text", nullable=False)
    userId = ForeignKeyColumn(
        User,
        maps_to="1-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User,
        maps_to="1-N",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


class Category(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="categories")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    type = Column(type="varchar", length=255, nullable=False)

    postId = ForeignKeyColumn(
        Post,
        maps_to="N-1",
        type="int",
        required=True,
        onDelete="CASCADE",
        onUpdate="CASCADE",
    )


conn, tables = mysql_loom.connect_and_sync(
    [User, Profile, Post, Category], drop=True, force=True
)


userId = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="@miller"),
)

userId2 = mysql_loom.insert_one(
    instance=User,
    values=ColumnValue(name="username", value="bob"),
)

profileId = mysql_loom.insert_one(
    instance=Profile,
    values=[
        ColumnValue(name="userId", value=userId),
        ColumnValue(name="avatar", value="hello.jpg"),
    ],
)
for title in ["Hey", "Hello", "What are you doing", "Coding"]:
    mysql_loom.insert_one(
        instance=Post,
        values=[
            ColumnValue(name="userId", value=userId),
            ColumnValue(name="title", value=title),
        ],
    )


for cat in ["general", "education", "tech", "sport"]:
    mysql_loom.insert_one(
        instance=Category,
        values=[
            ColumnValue(name="postId", value=1),
            ColumnValue(name="type", value=cat),
        ],
    )
    print()


profile = mysql_loom.find_one(
    instance=Profile,
    filters=[Filter(column="userId", value=1)],
    include=[Include(model=User, select=["id", "username", "tokenVersion"], has="one")],
)
print(profile)

user = mysql_loom.find_one(
    instance=User,
    filters=[Filter(column="id", value=userId)],
    include=[Include(model=Profile, select=["id", "avatar"], has="one")],
)
print(user)

user = mysql_loom.find_one(
    instance=User,
    filters=[Filter(column="id", value=userId)],
    include=[
        Include(
            model=Post,
            select=["id", "title"],
            has="many",
            offset=0,
            limit=2,
            order=[
                Order(column="createdAt", order="DESC"),
                Order(column="id", order="DESC"),
            ],
        ),
        Include(model=Profile, select=["id", "avatar"], has="one"),
    ],
)
print(user)

post = mysql_loom.find_one(
    instance=Post,
    filters=[Filter(column="userId", value=userId)],
    select=["title", "id"],
    include=[
        Include(
            model=User,
            select=["id", "username"],
            has="one",
            include=[Include(model=Profile, select=["avatar", "id"], has="one")],
        ),
        Include(
            model=Category,
            select=["id", "type"],
            has="many",
            order=[Order(column="id", order="DESC")],
            limit=2,
        ),
    ],
)

print(post)


user = mysql_loom.find_one(
    instance=User,
    filters=[Filter(column="id", value=userId2)],
    select=["username", "id"],
    include=[
        Include(
            model=Post,
            select=["id", "title"],
            has="many",
            include=[
                Include(
                    model=Category,
                    select=["type", "id"],
                    has="many",
                    order=[Order(column="id", order="DESC")],
                    limit=2,
                    offset=0,
                )
            ],
        ),
    ],
)

print(user)


posts = mysql_loom.find_one(Post, select=["id", "completed"])
print(posts)
