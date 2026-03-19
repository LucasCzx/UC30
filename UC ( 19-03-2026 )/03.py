def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    elif fogo:
        return "Fogo"
    elif agua:
        return "Água"
    else:
        return "Sem magia"