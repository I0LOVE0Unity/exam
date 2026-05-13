import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

engine = sa.create_engine(
    "mssql+pymssql://ILABSQLW19S1:49172/shoe_shop",
    connect_args={"trusted": True}
)
SessionLocal = sessionmaker(engine)

Base = automap_base()
Base.prepare(autoload_with=engine)

session = SessionLocal()

Product = Base.classes.product
User = Base.classes.user
Supplier = Base.classes.supplier
Name = Base.classes.name
Category = Base.classes.category
Manufacturer = Base.classes.manufacturer
Unit = Base.classes.unit
Role = Base.classes.role
OrderItem = Base.classes.order_item


def _load_lookup(cls):
    return {r.id: r.title.strip() for r in session.query(cls).all()}
