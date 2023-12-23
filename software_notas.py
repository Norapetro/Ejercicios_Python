def nota_final(nota, recuperacion=None):
    if nota >= 0.0 and nota <= 0.9:
        return f"Definitivamente perdió sin derecho a recuperar ({nota})"
    elif nota >= 1.0 and nota <= 2.5:
        if recuperacion is not None:
            if recuperacion == 5.0:
                return f"Nota final: 3.0 ({nota} original + {recuperacion} recuperación) - Aceptable para recuperación"
            else:
                return f"Perdió, pero puede recuperar ({nota})"
        else:
            return "La nota de recuperación es necesaria para este rango"
    elif nota >= 2.6 and nota <= 2.9:
        if recuperacion is not None:
            if recuperacion == 5.0:
                return f"Nota final: 3.5 ({nota} original + {recuperacion} recuperación) - Aceptable para recuperación"
            else:
                return f"Puedes recuperar ({nota})"
        else:
            return "La nota de recuperación es necesaria para la nota final."
    elif nota >= 3.0 and nota <= 3.5:
        if recuperacion is not None:
            return f"Nota: ({nota}) - Aceptable para recuperación"
        else:
            return f"Nota final aceptable ({nota})"
    elif nota >= 3.6 and nota <= 3.9:
        return f"Nota ACEPTABLE, ({nota}) sigue mejorando "
    elif nota >= 4.0 and nota <= 4.5:
        return f"Nota EXCELENTE, ({nota}) vas por buen camino "
    elif nota >= 4.6 and nota <= 5.0:
        return f"Nota CIENTIFICO, ({nota}) tienes un gran futuro por delante "
    else:
        return "La nota ingresada no es válida"

nota_original = float(input("Ingrese la nota: "))

if 1.0 <= nota_original <= 3.5:
    recuperacion = float(input("Ingrese la nota de recuperación: "))
else:
    recuperacion = None

resultado = nota_final(nota_original, recuperacion)
print(resultado)



# software de notas del 0 al 5.0
# si la nota es 0 hasta 0.9 definitivamente perdió sin derecho a recuperar
# si la nota es 1.0 hasta 2.5 perdió pero puede recuperar, si en la recuperación saca 5.0 la nota final queda en 3.0
# si la nota es 2.6 hasta 2.9 puede recuperar  si en la recuperación saca 5.0 la nota final queda en 3.5
# si la nota es 3.0 hasta 3.5 pero es de recuperación la nota es aceptable
# si la nota es 3.0 hasta 3.9 la nota final es aceptable sigue mejorando
# si la nota es 4.0 hasta 4.5 excelente vas por buen camino
# si la nota es 4.5 hasta 5.0 científico tienes un gran futuro por delante 
