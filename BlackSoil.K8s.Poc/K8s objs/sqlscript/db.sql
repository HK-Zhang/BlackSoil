GO
IF(db_id(N'snoopyshoppingcart') IS NULL)
BEGIN
	CREATE DATABASE snoopyshoppingcart
END;

GO
USE snoopyshoppingcart

GO
IF NOT EXISTS (SELECT * FROM sysobjects WHERE NAME='shopping' AND XTYPE='U')
BEGIN
	CREATE TABLE shopping
	(
		AddedOn datetime,
		ConnectionID nvarchar(100),
		IP nvarchar(20),
		CartItem nvarchar(100)
	)
END

GO
INSERT INTO [dbo].[shopping]
           ([AddedOn]
           ,[ConnectionID]
           ,[IP]
           ,[CartItem])
     VALUES
           ('2018-07-09 00:00:00.000'
           ,'122'
           ,'127.0.0.1'
           ,'Grape')
GO
