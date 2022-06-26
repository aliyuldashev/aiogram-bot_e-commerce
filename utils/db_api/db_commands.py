from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    #doyim in shudanish darkor chig`da gittinda
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    # async def add_user(self, full_name, username, telegram_id):
    #     sql = "INSERT INTO products_user (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
    #     return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM products_user"
        return await self.execute(sql, fetch=True)

    # async def select_user(self, **kwargs):
    #     sql = "SELECT * FROM products_user WHERE "
    #     sql, parameters = self.format_args(sql, parameters=kwargs)
    #     return await self.execute(sql, *parameters, fetchrow=True)

    # async def count_users(self):
    #     sql = "SELECT COUNT(*) FROM products_user"
    #     return await self.execute(sql, fetchval=True)

    # async def update_user_username(self, username, telegram_id):
    #     sql = "UPDATE products_user SET username=$1 WHERE telegram_id=$2"
    #     return await self.execute(sql, username, telegram_id, execute=True)

    # async def delete_users(self):
    #     await self.execute("DELETE FROM products_user WHERE TRUE", execute=True)

    # async def drop_users(self):
    #     await self.execute("DROP TABLE products_user", execute=True)


    async def add_product(
        self,
        category_code,
        category_name,
        subcategory_code,
        subcategory_name,
        productname,
        photo=None,
        price=None,
        description="",
    ):
        sql = "INSERT INTO products_product (category_code, category_name, subcategory_code, subcategory_name, productname, photo, price, description) VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"
        return await self.execute(
            sql,
            category_code,
            category_name,
            subcategory_code,
            subcategory_name,
            productname,
            photo,
            price,
            description,
            fetchrow=True,
        )

    # async def get_categories(self):
    #     sql = "SELECT DISTINCT category_name, category_code FROM products_product"
    #     return await self.execute(sql, fetch=True)

    # async def get_subcategories(self, category_code):
    #     sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM products_product WHERE category_code='{category_code}'"
    #     return await self.execute(sql, fetch=True)

    # async def count_products(self, category_code, subcategory_code=None):
    #     if subcategory_code:
    #         sql = f"SELECT COUNT(*) FROM products_product WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
    #     else:
    #         sql = f"SELECT COUNT(*) FROM products_product WHERE category_code='{category_code}'"
    #     return await self.execute(sql, fetchval=True)

    # async def get_products(self, category_code, subcategory_code):
    #     sql = f"SELECT * FROM products_product WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
    #     return await self.execute(sql, fetch=True)
    async def selcting_product(self):
        sql = f"SELECT * FROM products_product"
        return await self.execute(sql, fetch=True)
    async def get_product(self, product_id):
        sql = f"SELECT * FROM products_product WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    # async def get_users(self, telegram_id):
    #     try:
    #         sql = f"SELECT * FROM products_user WHERE telegram_id={telegram_id}"
    #         all = await self.execute(sql, fetch=True)
    #         if all ==[]:
    #             return False
    #         else:
    #             return True
    #     except:
    #         return False

    async def drop_products(self):
        await self.execute("DROP TABLE products_product", execute=True)


    async def buyurtma_add(self, zakaz_name, m_price, m_soni, s_price, m_name, m_tel, m_man, m_agent, m_time, agent_id, t_turi):
        sql = "INSERT INTO products_buyurtma (zakaz_name, m_price, m_soni, s_price, m_name, m_tel, m_man, m_agent, m_time, agent_id, t_turi) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11) returning *"
        return await self.execute(sql, zakaz_name, m_price, m_soni, s_price, m_name, m_tel, m_man, m_agent, m_time, agent_id, t_turi, fetchrow=True)


    async def first_catigory_selection(self):
        sql = f"SELECT * FROM products_first_tag"
        return await self.execute(sql, fetch=True)

    async def selecting_second_tag(self, second_id):
        sql = f"SELECT * FROM products_second_tag WHERE id={second_id}"
        return await self.execute(sql, fetch=True)

    async def getting_second_tegs(self, first_tags):
        sql = f"SELECT * FROM products_product WHERE first_tag_id={first_tags}"
        return await self.execute(sql, fetch=True)

    async def getting_third_tegs(self, first_tags, second_tags):
        sql = f"SELECT * FROM products_product WHERE first_tag_id={first_tags} AND second_tag_id={second_tags}"
        return await self.execute(sql, fetch=True)

    async def four_third_tegs(self, first_tags, second_tags, name):
        sql = f"SELECT * FROM products_product WHERE first_tag_id={first_tags} AND second_tag_id={second_tags} AND productname='{name}'"
        return await self.execute(sql, fetch=True)