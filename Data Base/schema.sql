drop table if exists salle CASCADE ;
drop table if exists promo CASCADE ;
drop table if exists cours CASCADE ;
drop table if exists photo CASCADE ;
drop table if exists eleve CASCADE ;



create table eleve
     (ideleve char(30) PRIMARY KEY,
     nomeleve char(20),
     prenomeleve char(20));

Create table photo
     (idphoto integer PRIMARY KEY,
     ideleve char(30) REFERENCES eleve,
     photoname char(20));

Create table cours 
    (idcours char(20) PRIMARY KEY,
    nomcours char(20));

Create table promo
    (idpromo char(20) PRIMARY KEY,
    nompromo char(20));

Create table salle
    (idsalle char(20) PRIMARY KEY,
    idcours char(20) REFERENCES cours,
    idpromo char(20) REFERENCES promo);
