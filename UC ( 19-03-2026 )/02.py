def saldo_final(saldo, saque):
   
    if saque > saldo:
        return "Saldo insuficiente"
    
    
    if saque > 1000:
        taxa = saque * 0.02
    else:
        taxa = 0
    
    saldo_restante = saldo - saque - taxa
    
    return saldo_restante