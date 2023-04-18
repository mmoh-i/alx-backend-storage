-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER itemcheck 
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN
  UPDATE items
  SET quantity = quantity - NEW.quantity
  WHERE id = NEW.items_id;
END;
