drop TABLE if exists login;

create table login(
    username text not null,
    password text not null
    
);

insert into login VALUES('admin','password');
