drop TABLE if exists orders;

create table orders(
    name text not null,
    mobile_num INTEGER not null,
    address text not null,
    dish_name text not NULL,
    price INTEGER not null
);


