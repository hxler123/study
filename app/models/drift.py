from sqlalchemy import Column, String, Integer, SmallInteger
from .base import Base


class Drift(Base):
    """
    请求赠送的字段信息
    gift wish 的数据需要同步
    """

    # 赠送人信息
    # 赠送人姓名/id
    giver_name = Column(String(20), nullable=False)
    giver_id = Column(Integer(), nullable=False)

    # 请求者信息
    # 请求者姓名/id
    supplicant_name = Column(String(20), nullable=False)
    supplicant_id = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)
    mobile = Column(String(20), nullable=False)
    recipient_name = Column(String(20), nullable=False)
    message = Column(String())

    # 书籍信息
    # isbn title
    isbn = Column(String(50), nullable=False)
    book_title = Column(String(20))
    book_author = Column(String(20))
    book_img = Column(String(20))

    # 交易的状态
    pending = Column(SmallInteger, default=1)

    # wish gift id
    gift_id = Column(Integer, nullable=False)
    wish_id = Column(Integer, nullable=False)







