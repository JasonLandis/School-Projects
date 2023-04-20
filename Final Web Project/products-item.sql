# Dump File
#
# Database is ported from MS Access
#--------------------------------------------------------
# Program Version 5.1.232

CREATE DATABASE IF NOT EXISTS `product`;
USE `product`;

#
# Table structure for table 'Item'
#

DROP TABLE IF EXISTS `Item`;

CREATE TABLE `Item` (
  `ItemID` INTEGER NOT NULL AUTO_INCREMENT, 
  `ItemName` VARCHAR(50), 
  `ItemPic` VARCHAR(50) NOT NULL, 
  `Description` VARCHAR(500), 
  `Price` INTEGER DEFAULT 0,
  `ItemLink` VARCHAR(255), 
  INDEX (`ItemID`), 
  INDEX (`ItemName`), 
  PRIMARY KEY (`ItemID`)
) ENGINE=innodb DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'Item'
#

INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (1, 'Developing Tank' , "images/devtank.jpg" , "The developing tank allows the user to pour liquids in and out without exposing the film to light. The film is placed into the canister while both are in the changing bag and the film remains there for the entire developing process. I use the Paterson Super System 4 developing tank." , 32.00 , "https://www.bhphotovideo.com/c/product/886586-REG/Paterson_Universal_Tank_with_Two.html");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (2, 'Changing Bag' , "images/changingbag.jpg" , "A changing bag allows you to transfer the film from its canister to the developing tank while keeping light out." , 33.00 , "https://www.bhphotovideo.com/c/product/253370-REG/Paterson_PTP125.html");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (3, 'Developer' , "images/developer.jpg" , "The developer reacts with the silver halide on the film, causing it to form metallic silver. There are a variety of developers, but I prefer to work with Rodinal" , 12.00 , "https://www.freestylephoto.biz/12054-Adox-Rodinal-Film-Developer-500-ml");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (4, 'Stop' , "images/stop.jpg" , "The developing tank allows the user to pour liquids in and out without exposing the film to light. The film is placed into the canister while both are in the changing bag and the film remains there for the entire developing process. I use the Paterson Super System 4 developing tank." , 10.00 , "https://www.bhphotovideo.com/c/product/886586-REG/Paterson_Universal_Tank_with_Two.html");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (5, 'Fixer' , "images/fixer.jpg" , "The fixer removes the undeveloped silver halide from the film. I use Ilford Rapid Fixer which can be used at dilutions of 1+4 or 1+9." , 9.00 , "https://www.ilfordphoto.com/rapid-fixer-product");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (6, 'Graduated Cylinder' , "images/measuring cup.jpg" , "Since developing film is a chemical process, you must pay attention to exactly how much you use of and dilute your chemicals. Therefore it is necessary to use a graduated cylinder to make sure your dilutions are correct." , 10.00 , "https://www.amazon.com/500mL-Graduated-Cylinder-Polypropylene-Graduation/dp/B00LV3ZFZ0/ref=sr_1_10?_encoding=UTF8&c=ts&dchild=1&keywords=Lab+Cylinders&qid=1633582903&s=industrial&sr=1-10&ts_id=393349011");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (7, '1000ml Amber Glass Bottles' , "images/amberglass.jpg" , "Amber glass bottles are resilient and offer protection against light, which extends the working life of the chemicals inside. Useful for storing the reusable chemicals." , 6.00 , "https://www.homesciencetools.com/product/bottle-1000ml-amber-glass-boston-round/");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (8, 'C-41 Chemical Kit' , "images/c41.jpg" , "This C-41 chemical kit contains powdered concentrates of all the chemicals you will need to develop color photos. I prefer using the unicolor kit, It can be purchased for $27 and can process 20 rolls of film (sometimes even more!), which means that it only costs $1.35 a roll to process! This is a far cry from the often exorbitant prices charged by film labs, which can charge up to $10 and sometimes more." , 27.00 , "https://www.freestylephoto.biz/10123-Unicolor-Powder-C-41-Film-Negative-Processing-Kit-1-Liter");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (9, 'Archival Sleeves' , "images/sleeve.jpg" , "Archival sleeves allow you to store your film safely and easily. If you want to look at your negatives or scan them, all you have to do is pull a strip out! I cut my rolls of 35mm film into 6 strips of 6 photos and sleeve them in archival sleeves." , 9.00 , "https://www.amazon.com/Archival-Storage-Sheets-35-7B25-Negatives/dp/B00009R90P");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (10, 'Can Opener' , "images/opener.jpg" , "A can opener is used insude the changing bag to pry open the canister of film and load it into the tank." , 10.00 , "https://www.amazon.com/OXO-Good-Grips-Can-Opener/dp/B00004OCJW/ref=sr_1_7?dchild=1&keywords=can+opener&qid=1633637361&sr=8-7");
INSERT INTO `Item` (`ItemID`, `ItemName`, `ItemPic`, `Description`, `Price`, `ItemLink`) VALUES (11, 'Sous Vide Cooker' , "images/sousvide.jpg" , "A sous vide cooker is absolutely essential when developing color photos. It is able to keep the chemcials and developing tank at exactly the temperature needed. As a bonus, you can cook great steaks with it!" , 45.00 , "https://www.ebay.com/itm/274772403056?hash=item3ff9b62370:g:ckgAAOSwAV1ghLeo");