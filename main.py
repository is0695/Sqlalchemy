import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Books, Publisher, Stock, Shop, Sale

DSN = "postgresql://postgres:1@localhost:5432/base_alchemy"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(publisher_name='Вася')
book1 = Books(title="Python", publisher=pub1)
book2 = Books(title="C++", publisher=pub1)
book3 = Books(title="HTML", publisher=pub1)
book4 = Books(title="CSS", publisher=pub1)
shop1 = Shop(shop_name="IT")
stok1 = Stock(book=book1, shop=shop1, stock_count=10)
stok3 = Stock(book=book4, shop=shop1, stock_count=8)
sale1 = Sale(sale_price=300, sale_date="2023-01-17T07:10:24.552Z", sale_count=2, stock=stok1)
sale2 = Sale(sale_price=400, sale_date="2023-03-01T07:20:35.647Z", sale_count=4, stock=stok3)
pub2 = Publisher(publisher_name='Петя')
book5 = Books(title="Java", publisher=pub2)
book6 = Books(title="C++", publisher=pub2)
book7 = Books(title="JavaScript", publisher=pub2)
book8 = Books(title="PHP", publisher=pub2)
shop2 = Shop(shop_name="ZZZ")
stok2 = Stock(book=book3, shop=shop2, stock_count=5)
stok4 = Stock(book=book8, shop=shop2, stock_count=11)
sale3 = Sale(sale_price=500, sale_date="2023-06-28T07:15:47.552Z", sale_count=1, stock=stok3)
sale4 = Sale(sale_price=200, sale_date="2023-07-06T07:16:02.647Z", sale_count=6, stock=stok4)
session.add_all([pub1, book1, book2, book3, book4,
                 pub2, book5, book6, book7, book8,
                 shop1, stok1, stok2, stok3, stok4,
                 sale1, sale2, sale3, sale4])
session.commit()
session.close()


def search_publisher(i=input("Введите имя издателя: ")):
    if type(i) == str:
        for c in session.query(Sale.sale_date).join(Stock.shop).join(Stock.book).join(Books.publisher).filter(
                Publisher.publisher_name == i):
            print(c)
search_publisher()
