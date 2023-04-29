delimiter //
-- Se encuentra en la tabla detalle
DROP TRIGGER if exists DescontarInventario //

CREATE TRIGGER DescontarInventario
AFTER INSERT ON detalle
FOR EACH ROW
BEGIN
	DECLARE cant INT DEFAULT 0;
    DECLARE invent INT DEFAULT 0;
    
    SELECT i.existencia INTO invent FROM inventario i WHERE id=new.Inventario_Id_inventario;
    SET cant = invent - new.cantidad;
    UPDATE inventario SET existencia = cant WHERE id=new.Inventario_Id_inventario;
END //

delimiter ;