USE [DB_OList];
GO 
    TRUNCATE TABLE tSimulacao_IA;

INSERT INTO tSimulacao_IA (Estado, Ticket_Medio, Frete_Medio)
VALUES -- São Paulo: Vai disparar ALERTA DE FRETE (5500 > 4500)
    ('SP', 250.00, 5500.00),
    -- Santa Catarina: Vai disparar ALERTA DE TICKET (75.00 < 100)
    ('SC', 75.00, 45.00);
GO