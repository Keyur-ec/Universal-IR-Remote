show databases;

create database irDB;

use irDB;

create table remote (button varchar(30), hex_data varchar(30));

insert into remote values ('power', '0x1FE48B7'),
						('mode', '0xAFE58A7'),
                        ('mute', '0x1FE7887'),
                        ('play/pause', '0x1FE807F'),
                        ('previous', '0x1FE40BF'),
                        ('next', '0x1FEC03F'),
                        ('eq', '0x1FE20DF'),
                        ('volume down', '0x1FEA05F'),
                        ('volume up', '0x1FE609F'),
                        ('rpt', '0x1FE10EF'),
                        ('u/sd', '0x1FE906F'),
                        ('0', '0x1FEE01F'),
                        ('1', '0x1FE50AF'),
                        ('2', '0x1FED827'),
                        ('3', '0x1FEF807'),
                        ('4', '0x1FE30CF'),
                        ('5', '0x1FEB04F'),
                        ('6', '0x1FE708F'),
                        ('7', '0x1FE00FF'),
                        ('8', '0x1FEF00F'),
                        ('9', '0x1FE9867');

select * from remote;

