cuentas = [
    {"usuario": "laserking",  "cliente_id": 1, "saldo":  15000.0, "tipo": "personal", "activo": True },
    {"usuario": "shadowfox",  "cliente_id": 2, "saldo":   -500.0, "tipo": "personal", "activo": True },
    {"usuario": "neonbyte",   "cliente_id": 3, "saldo":  82000.0, "tipo": "empresa",  "activo": True },
    {"usuario": "pixelstorm", "cliente_id": 4, "saldo":      0.0, "tipo": "personal", "activo": False},
    {"usuario": "darkloop",   "cliente_id": 3, "saldo":   3200.0, "tipo": "empresa",  "activo": True },
    {"usuario": "codewolf",   "cliente_id": 5, "saldo":  -1200.0, "tipo": "personal", "activo": False},
]
clientes = [
    {"id": 1, "nombre": "Laura Sánchez",   "email": "laura@mail.com"},
    {"id": 2, "nombre": "Martín López",    "email": "martin@mail.com"},
    {"id": 3, "nombre": "Ana Rodríguez",   "email": "ana@mail.com"},
    {"id": 4, "nombre": "Pedro García",    "email": "pedro@mail.com"},
    {"id": 5, "nombre": "Sofía Martínez",  "email": "sofia@mail.com"},
]

def procesar_cuentas_en_riesgo(clientes, cuentas):
    reporte = []
    for cliente in clientes:
        tiene_saldo_negativo = False
        cuentas_negativas_lista = []
        cuentas_suspendidas_lista = []
        for cuenta_id in cliente.get("cuentas", []):
            cuenta = cuentas.get(cuenta_id)
            if not cuenta:
                continue
            saldo = cuenta.get("saldo", 0)
            if saldo < 0:
                tiene_saldo_negativo = True
                cuentas_negativas_lista.append(cuenta_id)
                if saldo < -1000 and cuenta.get("activo", True):
                    cuenta["activo"] = False
                    cuentas_suspendidas_lista.append(cuenta_id)
        if tiene_saldo_negativo:
            reporte.append({
                "cliente": cliente.get("id"),
                "motivo": "Saldo negativo detectado",
                "cuentas_negativas": cuentas_negativas_lista,
                "cuentas_suspendidas": cuentas_suspendidas_lista
            })
    return reporte
