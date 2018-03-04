#!/usr/bin/env python3

"""Create and print out reports based on the data in database.

    Functions:
        get_data() - fetch data from database and print it out.
        make_report() - generate report.
"""

import psycopg2

DB_NAME = "news"

# This object contains titles, output strings, sql queries used to make report.
reports = {
    "articles": {
        "title": "\n The most popular three articles: \n",
        "output": "\t'{}' - {} views \n",
        "sql": """select title, log_data.num
    from articles,
    (select substring(path from '\w+-.+') as slug, count(*) as num
    from log where not status like '4%' group by path) as log_data
    where articles.slug = log_data.slug
    order by log_data.num desc limit 3"""
        },
    "authors": {
        "title": "\n The three most popular article authors: \n",
        "output": "\t{} - {} views \n",
        "sql": """select name, sum(article_views_num) as author_views
    from authors,
    (select title, author, article_views_num
    from articles,
    (select substring(path from '\w+-.+') as slug, count(*)as article_views_num
    from log
    where not status like '4%'group by path)
    as log_data
    where articles.slug = log_data.slug)
    as articles_views_report
    where authors.id=articles_views_report.author
    group by authors.name order by author_views desc limit 3"""
        },
    "errors": {
        "title": "\n More than 1% requests lead to errors on: \n",
        "output": "\t{} - {}% \n",
        "sql": """select to_char(c.days, 'FMMonth DD, YYYY'), c.err_rate
    from (select a.days, a.num, b.num,
    (round(((b.num::float / a.num::float)*10000))/100.00) as err_rate from
    (select date(time) as days, count(*) as num from log group by days) as a,
    (select date(time) as days, count(*) as num from log where status like '4%'
    group by days) as b
    where a.days = b.days) as c
    where c.err_rate > 1"""
        }}


def get_data(conn, title, output, sql):
    """Fetch data using given conn (connection object),
    sql (SQL statement - string) and print it out
    using given title (string) , output (string)"""
    with conn:
        with conn.cursor() as curs:
            curs.execute(sql)
            data = curs.fetchall()
            print(title)
            for row in data:
                print(output.format(row[0], row[1]))
            print("------------------------------------------------------")


def make_report(*args):
    """Make report using data from reports object and get_data() function."""
    conn = psycopg2.connect(database=DB_NAME)

    for report in args:
        get_data(conn, report["title"], report["output"], report["sql"])

    conn.close()


if __name__ == "__main__":
    make_report(reports["articles"], reports["authors"], reports["errors"])
