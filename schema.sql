DROP TABLE IF EXISTS dishes;
DROP TABLE IF EXISTS test;

CREATE TABLE dishes (
    id INTEGER,
    Name TEXT NOT NULL,
    Price INTEGER NOT NULL,
    dish_image IMAGE
);

INSERT INTO dishes (id, Name, Price,dish_image) VALUES
(1,"Chicken Biriyani",120.00,'static\chicken_biriyani.jpg'),
(2,"Chicken Curry",100.00,'static\chicken_curry.jpg'),
(3,"Chicken Kondattam",130.00,'static\Chicken Kondattam.webp'),
(4,"Mandi",150.00,'static\mandi.jpg'),
(5,"Al Faham(2 pieces)",130.00,'static\al faham 2 - Copy.jpg'),
(6,"Pasta",100.00,'static\pasta.jpg'),
(7,"Porotta",10.00,'static\porotta.jpg'),
(8,"Al Faham",200.00,'static\al faham.jpg'),
(9,"Vegetable Biriyani",100.00,'static\Vegetable Biriyani.webp'),
(10,"Shawaya",120.00,'static\shawaya.jpg'),
(11,"Crab Curry",150.00,'static\crab crry.jpg'),
(12,"Fish Curry",90.00,'static\fish 1.webp'),
(13,"Duck Curry",150.00,'static\Duck Curry.jpg'),
(14,"Mutton Biriyani",200.00,'static\mutton.jpg'),
(15,"Prawns Curry",150.00,'static\Prawns Curry.jpg');
