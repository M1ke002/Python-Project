SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';



-- Schema Furniture_store_management
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Furniture_store_management` ;
USE `Furniture_store_management` ;

-- -----------------------------------------------------
-- Table `Furniture_store_management`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Furniture_store_management`.`Product` (
  `idProduct` INT NOT NULL,
  `nameProduct` VARCHAR(50) NOT NULL,
  `Quantity` INT NOT NULL,
  `Price` INT NOT NULL,
  `Category` VARCHAR(45) NOT NULL,
  `Supplier` VARCHAR(45) NOT NULL,
  `Description` LONGTEXT NOT NULL,
  PRIMARY KEY (`idProduct`),
  UNIQUE INDEX `idProduct_UNIQUE` (`idProduct` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Furniture_store_management`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Furniture_store_management`.`Invoice` (
  `idInvoice` INT NOT NULL,
  `Date` VARCHAR(45) NOT NULL,
  `nameCustomer` VARCHAR(45) NOT NULL,
  `phoneNumberCustomer` VARCHAR(45) NOT NULL,
  `addressCustomer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idInvoice`),
  UNIQUE INDEX `idInvoice_UNIQUE` (`idInvoice` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Furniture_store_management`.`Customer`
-- -----------------------------------------------------
-- CREATE TABLE IF NOT EXISTS `Furniture_store_management`.`Customer` (
--   `idCustomer` INT NOT NULL,
--   `nameCustomer` INT NOT NULL,
--   `Address` VARCHAR(45) NOT NULL,
--   `PhoneNumber` VARCHAR(45) NOT NULL,
--   `Invoice_idInvoice` INT NOT NULL,
--   PRIMARY KEY (`idCustomer`, `Invoice_idInvoice`),
--   UNIQUE INDEX `idCustomer_UNIQUE` (`idCustomer` ASC),
--   UNIQUE INDEX `PhoneNumber_UNIQUE` (`PhoneNumber` ASC),
--   INDEX `fk_Customer_Invoice1_idx` (`Invoice_idInvoice` ASC),
--   CONSTRAINT `fk_Customer_Invoice1`
--     FOREIGN KEY (`Invoice_idInvoice`)
--     REFERENCES `Furniture_store_management`.`Invoice` (`idInvoice`)
--     ON DELETE NO ACTION
--     ON UPDATE NO ACTION)
-- ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Furniture_store_management`.`Invoice_Detail`
-- -----------------------------------------------------
-- CREATE TABLE IF NOT EXISTS `Furniture_store_management`.`Invoice_Detail` (
--   `Product_idProduct` INT NOT NULL,
--   `Invoice_idInvoice` INT NOT NULL,
--   `Price` INT NOT NULL,
--   `Quantity` INT NOT NULL,
--   PRIMARY KEY (`Product_idProduct`, `Invoice_idInvoice`),
--   INDEX `fk_Product_has_Invoice_Invoice1_idx` (`Invoice_idInvoice` ASC),
--   INDEX `fk_Product_has_Invoice_Product1_idx` (`Product_idProduct` ASC),
--   CONSTRAINT `fk_Product_has_Invoice_Product1`
--     FOREIGN KEY (`Product_idProduct`)
--     REFERENCES `Furniture_store_management`.`Product` (`idProduct`)
--     ON DELETE NO ACTION
--     ON UPDATE NO ACTION,
--   CONSTRAINT `fk_Product_has_Invoice_Invoice1`
--     FOREIGN KEY (`Invoice_idInvoice`)
--     REFERENCES `Furniture_store_management`.`Invoice` (`idInvoice`)
--     ON DELETE NO ACTION
--     ON UPDATE NO ACTION)
-- ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Furniture_store_management`.`Invoice_Detail` (
  `Invoice_idInvoice` INT NOT NULL,
  `Product_idProduct` INT NOT NULL,
  `Product_quantity` INT NOT NULL,
  PRIMARY KEY (`Invoice_idInvoice`,`Product_idProduct`),
  INDEX `fk_Product_has_Invoice_Invoice1_idx` (`Invoice_idInvoice` ASC),
  INDEX `fk_Product_has_Invoice_Product1_idx` (`Product_idProduct` ASC),
  CONSTRAINT `fk_Product_has_Invoice_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `Furniture_store_management`.`Product` (`idProduct`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Product_has_Invoice_Invoice1`
    FOREIGN KEY (`Invoice_idInvoice`)
    REFERENCES `Furniture_store_management`.`Invoice` (`idInvoice`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

SELECT * FROM  Product;
SELECT * FROM  Invoice;
SELECT * FROM  Invoice_Detail;

INSERT INTO `Product` VALUES (1, "Product 1", 4, 10000, "Category 1", "Supplier 1","Aaaa description");
INSERT INTO `Product` VALUES (2, "Product 2", 5, 20000, "Category 2", "Supplier 2","description");
INSERT INTO `Product` VALUES (3, "Product 3", 6, 30000, "Category 3", "Supplier 3","dsdadescription");

INSERT INTO `Invoice` VALUES (1,'2022-02-14','Mit','09142314','USA');
INSERT INTO `Invoice` VALUES (2,'2022-06-14','Buh','09142316','China');
INSERT INTO `Invoice` VALUES (3,'2022-07-14','Lmao','09144414','USA');

INSERT INTO `Invoice_Detail` VALUES (1,12,4);
INSERT INTO `Invoice_Detail` VALUES (1,6,3);
INSERT INTO `Invoice_Detail` VALUES (2,66,2);
INSERT INTO `Invoice_Detail` VALUES (2,6,1);
INSERT INTO `Invoice_Detail` VALUES (2,100,3);

DELETE FROM `Product` WHERE Product.idProduct = 79;
UPDATE `Product` SET idProduct = 100 WHERE idProduct = 90;

DROP TABLE Customer;
DROP TABLE Invoice;
DROP TABLE Invoice_Detail;
SHOW TABLES;

