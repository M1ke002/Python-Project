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
-- Table `Furniture_store_management`.`Invoice_Detail`
-- -----------------------------------------------------

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


