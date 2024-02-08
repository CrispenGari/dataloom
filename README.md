### dataloom

**`dataloom`** is a lightweight and versatile Object-Relational Mapping (ORM) library for Python. With support for `PostgreSQL`, `MySQL`, and `SQLite3` databases, `dataloom` simplifies database interactions, providing a seamless experience for developers.

<p align="center">
<img src="/dataloom.png" alt="dataloom" width="200">
</p>

#### Why choose `dataloom`?

1. **Ease of Use**: `dataloom` offers a user-friendly interface, making it straightforward to work with.
2. **Flexible SQL Driver**: Write one codebase and seamlessly switch between `PostgreSQL`, `MySQL`, and `SQLite3` drivers as needed.
3. **Lightweight**: Despite its powerful features, `dataloom` remains lightweight, ensuring efficient performance.
4. **Comprehensive Documentation**: Benefit from extensive documentation that guides users through various functionalities and use cases.
5. **Active Maintenance**: `dataloom` is actively maintained, ensuring ongoing support and updates for a reliable development experience.
6. **Cross-platform Compatibility**: `dataloom` works seamlessly across different operating systems, including `Windows`, `macOS`, and `Linux`.
7. **Scalability**: Scale your application effortlessly with `dataloom`, whether it's a small project or a large-scale enterprise application.

### ⚠️ Warning

> **⚠️ Experimental Status of `dataloom`**: The `dataloom` module is currently in an experimental phase. As such, we strongly advise against using it in production environments until a major version is officially released and stability is ensured. During this experimental phase, the `dataloom` module may undergo significant changes, and its features are subject to refinement. We recommend monitoring the project updates and waiting for a stable release before incorporating it into production systems. Please exercise caution and consider alternative solutions for production use until the module reaches a stable release.\*\*

### Table of Contents

- [dataloom](#dataloom)
  - [Why choose `dataloom`?](#why-choose-dataloom)
- [⚠️ Warning](#️-warning)
- [Table of Contents](#table-of-contents)
- [Key Features:](#key-features)
- [Installation](#installation)
- [Python Version Compatibility](#python-version-compatibility)
- [Usage](#usage)
- [Connection](#connection)
- [Dataloom Classes](#dataloom-classes)
  - [`Model` Class](#model-class)
  - [`Column` Class](#column-class)
  - [`PrimaryKeyColumn` Class](#primarykeycolumn-class)
  - [`ForeignKeyColumn` Class](#foreignkeycolumn-class)
  - [`CreatedAtColumn` Class](#createdatcolumn-class)
  - [`UpdatedAtColumn` Class](#updatedatcolumn-class)
  - [`Filter` Class](#filter-class)
  - [`ColumnValue` Class](#columnvalue-class)
  - [`Order` Class](#order-class)
  - [`Include`](#include)
- [Syncing Tables](#syncing-tables)
  - [1. The `sync` method.](#1-the-sync-method)
  - [2. The `connect_and_sync` method.](#2-the-connect_and_sync-method)
- [CRUD Operations with Dataloom](#crud-operations-with-dataloom)
  - [1. Creating a Record](#1-creating-a-record)
    - [1. `insert_one()`](#1-insert_one)
    - [2. `insert_bulk()`.](#2-insert_bulk)
  - [2. Getting records](#2-getting-records)
    - [1. `find_all()`](#1-find_all)
    - [2. `find_many()`](#2-find_many)
    - [3. `find_one()`](#3-find_one)
    - [4. `find_by_pk()`](#4-find_by_pk)
  - [3. Deleting a record](#3-deleting-a-record)
    - [1. `delete_by_pk()`](#1-delete_by_pk)
    - [2. `delete_one()`](#2-delete_one)
    - [3. `delete_bulk()`](#3-delete_bulk)
      - [Warning: Potential Risk with `delete_bulk()`](#warning-potential-risk-with-delete_bulk)
      - [Guidelines for Safe Usage](#guidelines-for-safe-usage)
  - [4. Updating a record](#4-updating-a-record)
    - [1. `update_by_pk()`](#1-update_by_pk)
    - [2. `update_one()`](#2-update_one)
    - [3. `update_bulk()`](#3-update_bulk)
- [Ordering](#ordering)
- [Filters](#filters)
- [What is coming next?](#what-is-coming-next)

### Key Features:

- **Lightweight**: `dataloom` is designed to be minimalistic and easy to use, ensuring a streamlined `ORM` experience without unnecessary complexities.

- **Database Support**: `dataloom` supports popular relational databases such as `PostgreSQL`, `MySQL`, and `SQLite3`, making it suitable for a variety of projects.

- **Simplified Querying**: The `ORM` simplifies the process of database querying, allowing developers to interact with the database using Python classes and methods rather than raw SQL queries.

- **Intuitive Syntax**: `dataloom`'s syntax is intuitive and `Pythonic`, making it accessible for developers familiar with the Python language.

- **Flexible Data Types**: The `ORM` seamlessly handles various data types, offering flexibility in designing database schemas.

### Installation

To install `dataloom`, you just need to run the following command using `pip`:

```bash
pip install dataloom
```

### Python Version Compatibility

`dataloom` supports **`Python`** version **`3.12`** and above. Ensure that you are using a compatible version of **`Python`** before installing or using `dataloom`.

You can check your **`Python`** version by running:

```bash
python --version
```

### Usage

In this section we are going to go through how you can use our `orm` package in your project.

### Connection

To use Dataloom, you need to establish a connection with a specific database dialect. The available dialect options are `mysql`, `postgres`, and `sqlite`. In this example, we'll demonstrate how to set up a connection to a PostgreSQL database named "hi" using the `postgres` dialect. The following is an example of how you can establish a connection with postgres database.

```python
from dataloom import Dataloom

# Create a Dataloom instance with PostgreSQL configuration
pg_loom = Dataloom(
    dialect="postgres",
    database="hi",
    password="root",
    user="postgres",
    host="localhost",
    sql_logger="console",
    logs_filename="logs.sql",
    port=5432,
)

# Connect to the PostgreSQL database
conn = pg_loom.connect()


# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

To establish a connection with a `MySQL` database using Dataloom, you can use the following example:

```python
from dataloom import Dataloom

# Create a Dataloom instance with MySQL configuration
mysql_loom = Dataloom(
    dialect="mysql",
    database="hi",
    password="root",
    user="root",
    host="localhost",
    sql_logger="console",
    logs_filename="logs.sql",
    port=3306,
)

# Connect to the MySQL database
conn = mysql_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()

```

To establish a connection with an `SQLite` database using Dataloom, you can use the following example:

```python
from dataloom import Dataloom

# Create a Dataloom instance with SQLite configuration
sqlite_loom = Dataloom(
    dialect="sqlite",
    database="hi.db",
    logs_filename="sqlite-logs.sql",
    logging=True,
    sql_logger="console",
)

# Connect to the SQLite database
conn = sqlite_loom.connect()

# Close the connection when the script completes
if __name__ == "__main__":
    conn.close()
```

The `Dataloom` class takes in the following options:
| Parameter | Description | Value Type | Default Value | Required |
| --------------- | --------------------------------------------------------------------------------- | --------------- | -------------- | -------- |
| `dialect` | Dialect for the database connection. Options are `mysql`, `postgres`, or `sqlite` | `str` or `None` | `None` | `Yes` |
| `database` | Name of the database for `mysql` and `postgres`, filename for `sqlite` | `str` or `None` | `None` | `Yes` |
| `password` | Password for the database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `user` | Database user (only for `mysql` and `postgres`) | `str` or `None` | `None` | `No` |
| `host` | Database host (only for `mysql` and `postgres`) | `str` or `None` | `localhost` | `No` |
| `sql_logger` | Enable logging for the database queries. If you don't want to see the sql logs you can set this option to `None` which is the default value. If you set it to `file` then you will see the logs in the default `dataloom.sql` file, you can overide this by passing a `logs_filename` option. Setting this option to `console`, then sql statements will be printed on the console. | `console`or `file` or `None`| `True` | `No` |
| `logs_filename` | Filename for the query logs | `str` or `None` | `dataloom.sql` | `No` |
| `port` | Port number for the database connection (only for `mysql` and `postgres`) | `int` or `None` | `None` | `No` |

### Dataloom Classes

#### `Model` Class

A model in Dataloom is a top-level class that facilitates the creation of complex SQL tables using regular Python classes. This example demonstrates how to define two tables, `User` and `Post`, by creating classes that inherit from the `Model` class.

```py
from dataloom import (
    Dataloom,
    Model,
    PrimaryKeyColumn,
    Column,
    CreatedAtColumn,
    UpdatedAtColumn,
    TableColumn,
    ForeignKeyColumn,
)

class User(Model):
    __tablename__:TableColumn = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    name = Column(type="text", nullable=False, default="Bob")
    username = Column(type="varchar", unique=True, length=255)

    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()


class Post(Model):
    __tablename__: TableColumn = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(
        type="varchar",
        length=255,
        nullable=False,
    )
    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()

    # relations
    userId = ForeignKeyColumn(
        User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
    )
```

- Within the `User` model definition, the table name is explicitly specified using the `__tablename__` property, set to `"users"`. This informs `dataloom` to use the provided name instead of automatically deriving it from the class name. If `TableColumn` is not specified, the class name becomes the default table name during the synchronization of tables. To achieve this, the `TableColumn` class is used, accepting the specified table name as an argument.

> 👉:**Note:** When defining a table name, it's not necessary to specify the property as `__tablename__`. However, it's considered good practice to name your table column like that to avoid potential clashes with other columns in the table.

- Every table must include exactly one primary key column. To define this, the `PrimaryKeyColumn` class is employed, signaling to `dataloom` that the specified field is a primary key.
- The `Column` class represents a regular column, allowing the inclusion of various options such as type and whether it is required.
- The `CreatedAtColumn` and `UpdatedAt` column types are automatically generated by the database as timestamps. If timestamps are unnecessary or only one of them is needed, they can be omitted.
- The `ForeignKeyColumn` establishes a relationship between the current (child) table and a referenced (parent) table.

#### `Column` Class

In the context of a database table, each property marked as a column in a model is treated as an individual attribute. Here's an example of how to define a column in a table using the `Column` class:

```python
username = Column(type="text", nullable=False, default="Hello there!!")
```

Here are some other options that you can pass to the `Column`:
| Argument | Description | Type | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------- | ------- |
| `type` | Required datatype of a column | any `datatype` | |
| `nullable` | Optional to specify if the column will allow null values or not. | `bool` | `False` |
| `length` | Optional to specify the length of the type. If passed as `N` with type `T`, it yields an SQL statement with type `T(N)`. | `int` \| `None` | `None` |
| `auto_increment` | Optional to specify if the column will automatically increment or not. | `bool` | `False` |
| `default` | Optional to specify the default value in a column. | `any` | `None` |
| `unique` | Optional to specify if the column will contain unique values or not. | `bool` | `False` |

> Talking about data types, each `dialect` has its own accepted values. Here is a list of types supported by each and every `dialect`:

1. `mysql`

   - `"int"` - Integer data type.
   - `"smallint"` - Small integer data type.
   - `"bigint"` - Big integer data type.
   - `"float"` - Floating-point number data type.
   - `"double"` - Double-precision floating-point number data type.
   - `"numeric"` - Numeric or decimal data type.
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"blob"` - Binary Large Object (BLOB) data type.

2. `postgres`

   - `"int"` - Integer data type (Alias: `"INTEGER"`).
   - `"smallint"` - Small integer data type (Alias: `"SMALLINT"`).
   - `"bigint"` - Big integer data type (Alias: `"BIGINT"`).
   - `"serial"` - Auto-incrementing integer data type (Alias: `"SERIAL"`).
   - `"bigserial"` - Auto-incrementing big integer data type (Alias: `"BIGSERIAL"`).
   - `"smallserial"` - Auto-incrementing small integer data type (Alias: `"SMALLSERIAL"`).
   - `"float"` - Real number data type (Alias: `"REAL"`).
   - `"double precision"` - Double-precision floating-point number data type (Alias: `"DOUBLE PRECISION"`).
   - `"numeric"` - Numeric data type (Alias: `"NUMERIC"`).
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"interval"` - Time interval data type.
   - `"uuid"` - UUID (Universally Unique Identifier) data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"jsonb"` - Binary JSON (JavaScript Object Notation) data type.
   - `"bytea"` - Binary data type (Array of bytes).
   - `"array"` - Array data type.
   - `"inet"` - IP network address data type.
   - `"cidr"` - Classless Inter-Domain Routing (CIDR) address data type.
   - `"macaddr"` - MAC (Media Access Control) address data type.
   - `"tsvector"` - Text search vector data type.
   - `"point"` - Geometric point data type.
   - `"line"` - Geometric line data type.
   - `"lseg"` - Geometric line segment data type.
   - `"box"` - Geometric box data type.
   - `"path"` - Geometric path data type.
   - `"polygon"` - Geometric polygon data type.
   - `"circle"` - Geometric circle data type.
   - `"hstore"` - Key-value pair store data type.

3. `sqlite`
   - `"int"` - Integer data type (Alias: `"INTEGER"`).
   - `"smallint"` - Small integer data type (Alias: `"SMALLINT"`).
   - `"bigint"` - Big integer data type (Alias: `"BIGINT"`).
   - `"float"` - Real number data type (Alias: `"REAL"`).
   - `"double precision"` - Double-precision floating-point number data type (Alias: `"DOUBLE"`).
   - `"numeric"` - Numeric data type (Alias: `"NUMERIC"`).
   - `"text"` - Text data type.
   - `"varchar"` - Variable-length character data type.
   - `"char"` - Fixed-length character data type.
   - `"boolean"` - Boolean data type.
   - `"date"` - Date data type.
   - `"time"` - Time data type.
   - `"timestamp"` - Timestamp data type.
   - `"json"` - JSON (JavaScript Object Notation) data type.
   - `"blob"` - Binary Large Object (BLOB) data type.

> Note: Every table is required to have a primary key column and this column should be 1. Let's talk about the `PrimaryKeyColumn`

#### `PrimaryKeyColumn` Class

This class is used to create a unique index in every table you create. In the context of a table that inherits from the `Model` class, exactly one `PrimaryKeyColumn` is required. Below is an example of creating an `id` column as a primary key in a table named `Post`:

```python
class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="users")
    id = PrimaryKeyColumn(type="int", auto_increment=True)
    #...rest of your columns

```

The following are the arguments that the `PrimaryKeyColumn` class accepts.
| Argument | Description | Type | Default |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------- | ------------- |
| `type` | The datatype of your primary key. | `str` | `"bigserial`" |
| `length` | Optional to specify the length of the type. If passed as `N` with type `T`, it yields an SQL statement with type `T(N)`. | `int` \| `None` | `None` |
| `auto_increment`| Optional to specify if the column will automatically increment or not. |`bool` |`False` |
|`default` | Optional to specify the default value in a column. |`any` |`None` |
|`nullable` | Optional to specify if the column will allow null values or not. |`bool` |`False` |
|`unique` | Optional to specify if the column will contain unique values or not. |`bool` |`True` |

#### `ForeignKeyColumn` Class

This class is utilized when informing `dataloom` that a column has a relationship with a primary key in another table. Consider the following model definition of a `Post`:

```py
class Post(Model):
    __tablename__: Optional[TableColumn] = TableColumn(name="posts")
    id = PrimaryKeyColumn(type="int", auto_increment=True, nullable=False, unique=True)
    completed = Column(type="boolean", default=False)
    title = Column(type="varchar", length=255, nullable=False)
    # timestamps
    createdAt = CreatedAtColumn()
    updatedAt = UpdatedAtColumn()
    # relations
    userId = ForeignKeyColumn(
        User, type="int", required=True, onDelete="CASCADE", onUpdate="CASCADE"
    )

```

- `userId` is a foreign key in the table `posts`, indicating it has a relationship with a primary key in the `users` table.

This column accepts the following arguments:
| Argument | Description | Type | Default |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------- |
| `table` | Required. This is the parent table that the current model references. In our example, this is referred to as `User`. | `Model` | |
| `type` | Optional. Specifies the data type of the foreign key. If not provided, dataloom can infer it from the parent table. | `str` \| `None` | `None` |
| `required` | Optional. Indicates whether the foreign key is required or not. | `bool` | `False` |
| `onDelete` | Optional. Specifies the action to be taken when the associated record in the parent table is deleted. | `str` [`"NO ACTION"`, `"SET NULL"`, `"CASCADE"`] | `"NO ACTION"` |
| `onUpdate` | Optional. Specifies the action to be taken when the associated record in the parent table is updated. | str [`"NO ACTION"`, `"SET NULL"`, `"CASCADE"`] | `"NO ACTION"` |

It is crucial to specify the actions for `onDelete` and `onUpdate` to ensure that `dataloom` manages your model's relationship actions appropriately. The available actions are:

1. `"NO ACTION"` - If you delete or update the parent table, no changes will occur in the child table.
2. `"SET NULL"` - If you delete or update the parent table, the corresponding value in the child table will be set to `null`.
3. `"CASCADE"` - If you delete or update the table, the same action will also be applied to the child table.

#### `CreatedAtColumn` Class

When a column is designated as `CreatedAtColumn`, its value will be automatically generated each time you create a new record in a database, serving as a timestamp.

#### `UpdatedAtColumn` Class

When a column is designated as `UpdatedAtColumn`, its value will be automatically generated each time you create a new record or update an existing record in a database table, acting as a timestamp.

#### `Filter` Class

This `Filter` class in `dataloom` is designed to facilitate the application of filters when executing queries and mutations. It allows users to specify conditions that must be met for the operation to affect certain rows in a database table. Below is an example demonstrating how this class can be used:

```python
affected_rows = pg_loom.update_one(
    Post,
    values=[
        ColumnValue(name="title", value="Hey"),
        ColumnValue(name="completed", value=True),
    ],
    filters=[
        Filter(column="id", value=1, join_next_filter_with="AND"),
        Filter(column="userId", value=1, join_next_filter_with="AND"),
    ],
)
```

So from the above example we are applying filters while updating a `Post` here are the options that you can pass on that filter class:
| Argument | Description | Type | Default |
|-------------------------|------------------------------------------------------------|-------------------------------------------|------------------------|
| `column` | The name of the column to apply the filter on | `String` | - |
| `value` | The value to filter against | `Any` | - |
| `operator` | The comparison operator to use for the filter | `'eq'`, `'lt'`, `'gt'`, `'leq'`, `'geq'`, `'in'`, `'notIn'`, `'like'` | `'eq'` |
| `join_next_filter_with` | The logical operator to join this filter with the next one | `'AND'`, `'OR'` | `'AND'` |

> 👉 : **Note:** You can apply either a list of filters or a single filter when filtering records.

#### `ColumnValue` Class

Just like the `Filter` class, `dataloom` also provides a `ColumnValue` class. This class acts as a setter to update the values of columns in your database table.

The following code snippet demonstrates how the `ColumnValue` class is used to update records in the database:

```py
re = pg_loom.update_one(
    Post,
    values=[
        ColumnValue(name="title", value="Hey"),
        ColumnValue(name="completed", value=True),
    ],
    filters=[
        Filter(column="id",  value=1, join_next_filter_with="AND"),
        Filter(column="userId", value=1, join_next_filter_with="AND"),
    ],
)
```

It accepts two arguments: `name` and `value`. name represents the column name, while value corresponds to the new value to be assigned to that column.

| Argument | Description                                                | Type  | Default |
| -------- | ---------------------------------------------------------- | ----- | ------- |
| `name`   | The name of the column to be updated or inserted.          | `str` | -       |
| `value`  | The value to assign to the column during update or insert. | `Any` | -       |

#### `Order` Class

The `Order` class enables us to specify the desired order in which documents should be returned. Below is an example illustrating its usage:

```py
posts = pg_loom.find_all(
    Post,
    select=["id", "completed", "title", "createdAt"],
    limit=3,
    offset=0,
    order=[
        Order(column="createdAt", order="ASC"),
        Order(column="id", order="DESC"),
    ]
)
```

> 👉 **Note:** When utilizing a list of orders, they are applied sequentially, one after the other:

| Argument | Description                                                               | Type                | Default |
| -------- | ------------------------------------------------------------------------- | ------------------- | ------- |
| `column` | The name of the column to order by.                                       | `str`               | -       |
| `order`  | The order direction, either `"ASC"` (ascending) or `"DESC"` (descending). | `"ASC"` or `"DESC"` | `"ASC"` |

#### `Include`

### Syncing Tables

Syncing tables involves the process of creating tables from models and saving them to a database. After defining your tables, you will need to synchronize your database tables using the `sync` method.

#### 1. The `sync` method.

This method enables you to create and save tables into the database. For instance, if you have two models, `User` and `Post`, and you want to synchronize them with the database, you can achieve it as follows:

```py
tables = sqlite_loom.sync([Post, User], drop=True, force=True)
print(tables)
```

The method returns a list of table names that have been created or that exist in your database. The `sync` method accepts the following arguments:

| Argument | Description                                                     | Type   | Default |
| -------- | --------------------------------------------------------------- | ------ | ------- |
| `models` | A list of your table classes that inherit from the Model class. | `list` | `[]`    |
| `drop`   | Whether to drop tables during syncing or not.                   | `bool` | `False` |
| `force`  | Forcefully drop tables during syncing or not.                   | `bool` | `False` |
| `alter`  | Alter tables instead of dropping them during syncing or not.    | `bool` | `False` |

> We've noticed two steps involved in starting to work with our `orm`. Initially, you need to create a connection and then synchronize the tables in another step.

#### 2. The `connect_and_sync` method.

The `connect_and_sync` function proves to be very handy as it handles both the database connection and table synchronization. Here is an example demonstrating its usage:

```py
# ....

sqlite_loom = Dataloom(
    dialect="sqlite", database="hi.db", logs_filename="sqlite-logs.sql", logging=True
)
conn, tables = sqlite_loom.connect_and_sync([Post, User], drop=True, force=True)
print(tables)

if __name__ == "__main__":
    conn.close()
```

Returns a `conn` and the list of `tablenames` that exist in the database. The method accepts the same arguments as the `sync` method.

### CRUD Operations with Dataloom

In this section of the documentation, we will illustrate how to perform basic `CRUD` operations using `dataloom` on simple `Models`. Please note that in the following code snippets, I will be utilizing `sqlite_loom`. However, it's important to highlight that you can use any `loom` of your choice to follow along.

#### 1. Creating a Record

To insert a single or multiple records in a database you make use of the following functions:

1. `insert_one()`
2. `insert_bulk()`

##### 1. `insert_one()`

The `insert_one` method allows you to save a single row in a specific table. Upon saving, it will return the primary key (`pk`) value of the inserted document. The following example shows how the `insert_one()` method works.

```python
# Example: Creating a user record
userId = pg_loom.insert_one(
    instance=User, values=ColumnValue(name="username", value="@miller")
)

userId = pg_loom.insert_one(
    instance=User,
    values=[
        ColumnValue(name="username", value="@miller"),
        ColumnValue(name="name", value="Jonh"),
    ],
)
```

This function takes in two arguments which are `instance` and `values`. Where values are the column values that you are inserting in a user table or a single column value.

| Argument   | Description                                                                                                  | `Type`                               | `Required` | `Default` |
| ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------ | ---------- | --------- |
| `instance` | The instance of the table where the row will be inserted.                                                    | `Model`                              | `Yes`      | `None`    |
| `values`   | The column values to be inserted into the table. It can be a single column value or a list of column values. | `list[ColumnValue]` or `ColumnValue` | `Yes`      | `None`    |

##### 2. `insert_bulk()`.

The `insert_bulk` method facilitates the bulk insertion of records, as its name suggests. The following example illustrates how you can add `3` posts to the database table simultaneously.

```python
# Example: Inserting multiple posts
rows = pg_loom.insert_bulk(
    User,
    values=[
        [
            ColumnValue(name="username", value="@miller"),
            ColumnValue(name="name", value="Jonh"),
        ],
        [
            ColumnValue(name="username", value="@brown"),
            ColumnValue(name="name", value="Jonh"),
        ],
        [
            ColumnValue(name="username", value="@blue"),
            ColumnValue(name="name", value="Jonh"),
        ],
    ],
)
```

The argument parameters for the `insert_bulk` methods are as follows.

| Argument   | Description                                                                                                                                                                                                 | `Type`                                     | `Required` | `Default` |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------- | --------- |
| `instance` | The instance of the table where the row will be inserted.                                                                                                                                                   | `Model`                                    | `Yes`      | `None`    |
| `values`   | The column values to be inserted into the table. **It must be a list of list of column values with the same length, otherwise dataloom will fail to map the values correctly during the insert operation.** | `list[list[ColumnValue]]` or `ColumnValue` | `Yes`      | `None`    |

> In contrast to the `insert_one` method, the `insert_bulk` method returns the row count of the inserted documents rather than the individual primary keys (`pks`) of those documents.

#### 2. Getting records

To retrieve documents or a document from the database, you can make use of the following functions:

1. `find_all()`: This function is used to retrieve all documents from the database.
2. `find_by_pk()`: This function is used to retrieve a document by its primary key (or ID).
3. `find_one()`: This function is used to retrieve a single document based on a specific condition.
4. `find_many()`: This function is used to retrieve multiple documents based on a specific condition.

##### 1. `find_all()`

This method is used to retrieve all the records that are in the database table. Below are examples demonstrating how to do it:

```py
users = pg_loom.find_all(
    instance=User,
    select=["id", "username"],
    limit=3,
    offset=0,
    order=[Order(column="id", order="DESC")],
)
print(users) # ? [{'id': 1, 'username': '@miller'}]
```

The `find_all()` method takes in the following arguments:

| Argument   | Description                                    | Type          | Default | Required |
| ---------- | ---------------------------------------------- | ------------- | ------- | -------- |
| `instance` | The model class to retrieve documents from.    | `Model`       | `None`  | `Yes`    |
| `select`   | List of fields to select from the documents.   | `list[str]`   | `None`  | `No`     |
| `limit`    | Maximum number of documents to retrieve.       | `int`         | `None`  | `No`     |
| `offset`   | Number of documents to skip before retrieving. | `int`         | `0`     | `No`     |
| `order`    | List of columns to order the documents by.     | `list[Order]` | `None`  | `No`     |
| `include`  | List of related models to eagerly load.        | `list[Model]` | `None`  | `No`     |

> 👉 **Note:** Note that the `include` argument is not working at the moment. This argument allows us to eagerly load child relationships from the parent model.

##### 2. `find_many()`

Here is an example demonstrating the usage of the `find_many()` function with specific filters.

```py
users = mysql_loom.find_many(
    User,
    filters=[Filter(column="username", value="@miller")],
    select=["id", "username"],
    offset=0,
    limit=10,
)

print(users) # ? [{'id': 1, 'username': '@miller'}]
```

The `find_many()` method takes in the following arguments:

| Argument   | Description                                    | Type                     | Default | Required |
| ---------- | ---------------------------------------------- | ------------------------ | ------- | -------- |
| `instance` | The model class to retrieve documents from.    | `Model`                  | `None`  | `Yes`    |
| `filters`  | List of filters to apply to the query.         | `list[Filter] \| Filter` | `None`  | `No`     |
| `select`   | List of fields to select from the documents.   | `list[str]`              | `None`  | `No`     |
| `limit`    | Maximum number of documents to retrieve.       | `int`                    | `None`  | `No`     |
| `offset`   | Number of documents to skip before retrieving. | `int`                    | `0`     | `No`     |
| `order`    | List of columns to order the documents by.     | `list[Order]`            | `None`  | `No`     |
| `include`  | List of related models to eagerly load.        | `list[Model]`            | `None`  | `No`     |

> The distinction between the `find_all()` and `find_many()` methods lies in the fact that `find_many()` enables you to apply specific filters, whereas `find_all()` retrieves all the documents within the specified model.

##### 3. `find_one()`

Here is an example showing you how you can use `find_by_pk()` locate a single record in the database.

```py
user = mysql_loom.find_one(
    User,
    filters=[Filter(column="username", value="@miller")],
    select=["id", "username"],
)
print(user) # ? {'id': 1, 'username': '@miller'}
```

This method take the following as arguments

| Argument      | Description                                                          | Type                             | Default | Required |
| ------------- | -------------------------------------------------------------------- | -------------------------------- | ------- | -------- |
| `instance`    | The model class to retrieve instances from.                          | `Model`                          |         | `Yes`    |
| `filters`     | Filter or list of filters to apply to the query.                     | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `select`      | List of fields to select from the instances.                         | `list[str]`                      | `[]`    | `No`     |
| `include`     | List of related models to eagerly load.                              | `list[Include]`                  | `[]`    | `No`     |
| `return_dict` | Flag indicating whether to return the result as a dictionary or not. | `bool`                           | `True`  | `No`     |
| `offset`      | Number of instances to skip before retrieving.                       | `int \| None`                    | `None`  | `No`     |

##### 4. `find_by_pk()`

Here is an example showing how you can use the `find_by_pk()` to locate a single record in the database.

```py
user = mysql_loom.find_by_pk(User, pk=userId, select=["id", "username"])
print(user) # ? {'id': 1, 'username': '@miller'}
```

The method takes the following as arguments:

| Argument      | Description                                                          | Type            | Default | Required |
| ------------- | -------------------------------------------------------------------- | --------------- | ------- | -------- |
| `instance`    | The model class to retrieve instances from.                          | `Model`         |         | `Yes`    |
| `pk`          | The primary key value to use for retrieval.                          | `Any`           |         | `Yes`    |
| `select`      | List of fields to select from the instances.                         | `list[str]`     | `[]`    | `No`     |
| `include`     | List of related models to eagerly load.                              | `list[Include]` | `[]`    | `No`     |
| `return_dict` | Flag indicating whether to return the result as a dictionary or not. | `bool`          | `True`  | `No`     |

#### 3. Deleting a record

To delete a record or records in a database table you make use of the following functions:

1. `delete_by_pk()`
2. `delete_one()`
3. `delete_bulk()`

##### 1. `delete_by_pk()`

Using the `delete_by_pk()` method, you can delete a record in a database based on the primary-key value.

```py
affected_rows = mysql_loom.delete_by_pk(instance=User, pk=1)
```

The above take the following as arguments:

| Argument   | Description                                        | Type    | Default | Required |
| ---------- | -------------------------------------------------- | ------- | ------- | -------- |
| `instance` | The model class from which to delete the instance. | `Model` |         | `Yes`    |
| `pk`       | The primary key value of the instance to delete.   | `Any`   |         | `Yes`    |

##### 2. `delete_one()`

You can also use `filters` to delete a record in a database. The `delete_one()` function enables you to delete a single record in a database that matches a filter.

```py
affected_rows = mysql_loom.delete_one(
    instance=User, filters=[Filter(column="username", value="@miller")]
)
```

The method takes in the following arguments:

| Argument   | Description                                                | Type                             | Default | Required |
| ---------- | ---------------------------------------------------------- | -------------------------------- | ------- | -------- |
| `instance` | The model class from which to delete the instance(s).      | `Model`                          |         | `Yes`    |
| `filters`  | Filter or list of filters to apply to the deletion query.  | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `offset`   | Number of instances to skip before deleting.               | `int \| None`                    | `None`  | `No`     |
| `order`    | List of columns to order the instances by before deletion. | `list[Order] \| None`            | `[]`    | `No`     |

##### 3. `delete_bulk()`

You can also use the `delete_bulk()` method to delete a multitude of records that match a given filter:

```py
affected_rows = mysql_loom.delete_bulk(
    instance=User, filters=[Filter(column="username", value="@miller")]
)
```

The method takes the following as arguments:

| Argument   | Description                                                | Type                             | Default | Required |
| ---------- | ---------------------------------------------------------- | -------------------------------- | ------- | -------- |
| `instance` | The model class from which to delete instances.            | `Model`                          |         | `Yes`    |
| `filters`  | Filter or list of filters to apply to the deletion query.  | `Filter \| list[Filter] \| None` | `None`  | `No`     |
| `limit`    | Maximum number of instances to delete.                     | `int \| None`                    | `None`  | `No`     |
| `offset`   | Number of instances to skip before deleting.               | `int \| None`                    | `None`  | `No`     |
| `order`    | List of columns to order the instances by before deletion. | `list[Order] \| None`            | `[]`    | `No`     |

###### Warning: Potential Risk with `delete_bulk()`

⚠️ **Warning:** When using the `delete_bulk()` function, exercise caution as it can be aggressive. If the filter is not explicitly provided, there is a risk of mistakenly deleting all records in the table.

###### Guidelines for Safe Usage

To mitigate the potential risks associated with `delete_bulk()`, follow these guidelines:

1. **Always Provide a Filter:**

   - When calling `delete_bulk()`, make sure to provide a filter to specify the subset of records to be deleted. This helps prevent unintentional deletions.

   ```python
   # Example: Delete records where 'status' is 'inactive'
   sqlite_loom.delete_bulk(filter={'status': 'inactive'})
   ```

2. **Consider Usage When Necessary:**

- When contemplating data deletion, it is advisable to consider more targeted methods before resorting to `delete_bulk()`. Prioritize the use of `delete_one()` or `delete_by_pk()` methods to remove specific records based on your needs. This ensures a more precise and controlled approach to data deletion.

3. **Use limit and offsets options**

- You can consider using the `limit` and offset options during invocation of `delete_bulk`

```py
affected_rows = mysql_loom.delete_bulk(
    instance=Post,
    order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
    filters=[Filter(column="id", operator="gt", value=0)],
    offset=0,
    limit=10,
)
```

By following these guidelines, you can use the `delete_bulk()` function safely and minimize the risk of unintended data loss. Always exercise caution and adhere to best practices when performing bulk deletion operations.

#### 4. Updating a record

To update records in your database table you make use of the following functions:

1. `update_by_pk()`
2. `update_one()`
3. `update_bulk()`

##### 1. `update_by_pk()`

The `update_pk()` method can be used as follows:

```py
affected_rows = mysql_loom.update_by_pk(
    instance=Post,
    pk=1,
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The above method takes in the following as arguments:

| Argument   | Description                                                     | Type                               | Default | Required |
| ---------- | --------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update the instance.               | `Model`                            |         | `Yes`    |
| `pk`       | The primary key value of the instance to update.                | `Any`                              |         | `Yes`    |
| `values`   | Single or list of column-value pairs to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

##### 2. `update_one()`

Here is an example illustrating how to use the `update_one()` method:

```py
affected_rows = mysql_loom.update_one(
    instance=Post,
    filters=[
        Filter(column="id", value=8, join_next_filter_with="OR"),
        Filter(column="userId", value=1, join_next_filter_with="OR"),
    ],
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The method takes the following as arguments:

| Argument   | Description                                                     | Type                               | Default | Required |
| ---------- | --------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update the instance(s).            | `Model`                            |         | `Yes`    |
| `filters`  | Filter or list of filters to apply to the update query.         | `Filter \| list[Filter] \| None`   |         | `Yes`    |
| `values`   | Single or list of column-value pairs to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

##### 3. `update_bulk()`

The `update_bulk()` method updates all records that match a filter in a database table.

```py
affected_rows = mysql_loom.update_bulk(
    instance=Post,
    filters=[
        Filter(column="id", value=8, join_next_filter_with="OR"),
        Filter(column="userId", value=1, join_next_filter_with="OR"),
    ],
    values=[
        ColumnValue(name="title", value="Updated?"),
    ],
)
```

The above method takes in the following as argument:

| Argument   | Description                                                     | Type                               | Default | Required |
| ---------- | --------------------------------------------------------------- | ---------------------------------- | ------- | -------- |
| `instance` | The model class for which to update instances.                  | `Model`                            |         | `Yes`    |
| `filters`  | Filter or list of filters to apply to the update query.         | `Filter \| list[Filter] \| None`   |         | `Yes`    |
| `values`   | Single or list of column-value pairs to update in the instance. | `ColumnValue \| list[ColumnValue]` |         | `Yes`    |

### Ordering

In dataloom you can order documents in either `DESC` (descending) or `ASC` (ascending) order using the helper class `Order`.

```py
posts = mysql_loom.find_all(
    instance=Post,
    order=[Order(column="id", order="DESC")],
)
```

You can apply multiple and these orders will ba applied in sequence of application here is an example:

```py
posts = mysql_loom.find_all(
    instance=Post,
    order=[Order(column="id", order="DESC"), Order(column="createdAt", order="ASC")],
)
```

### Filters

There are different find of filters that you can use when filtering documents for mutations and queries.

### What is coming next?

1. Associations
2. Pagination
