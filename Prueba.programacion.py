"""1. Ingreso de datos del trabajador:
OK - El usuario ingresa el nombre del trabajador, su sueldo base y el número de horas extras trabajadas en el mes.
OK - Validar que el nombre del trabajador no esté vacío y que tenga una longitud máxima de 30 caracteres.
OK - Validar que el sueldo base y las horas extras sean valores numéricos positivo"""

sw=1
while sw==1:
     nombre_trabajador=input("Por favor ingrese su nombre del trabajador, tenga en cuenta que no puede superar los 30 carácteres:\n");
     if len(nombre_trabajador) <= 1:
        print("NOMBRE INVÁLIDO\n")

     elif len(nombre_trabajador)>30:
        print("EL NOMBRE NO PUEDE SUPERAR LOS 30 CARÁCTERES\n");
     else:
         break
     
 
while sw==1:
             sueldo_base=int(input("Ingrese el sueldo base del trabajador: "));
             if sueldo_base<=0:
                  print("ERROR: INGRESE UN SUELDO VÁLIDO\n");
             else:
                  break

while sw==1:
    try:
        horas_extras_del_mes=int(input("Ingrese las horas extras trabajadas durante el mes: "));
        #Horas extras puede ser cero porque el trabajador pudo no haber trabajado horas extras :)
        if horas_extras_del_mes<0:
            print("ERROR: INGRESE HORAS VÁLIDAS\n");
        else:
             break
    except ValueError:
         print("Ingrese un valor válido")

"""2. Cálculo de la liquidación:
OK Calcular el pago por horas extras, considerando que cada hora extra se paga un 50% más que una hora normal.
OK Calcular el total de ingresos, sumando el sueldo base y el pago por horas extras.
OK Calcular el descuento por fonasa, que corresponde al 7% del total de ingresos.
OK Calcular el descuento por AFP, que corresponde al 10% del total de ingresos.
OK Calcular el sueldo neto a pagar, restando el descuento por seguridad social al total de ingresos"""

#Inventamos que trabaja 160 horas al mes para poder saber cuanto le pagan normalmente por hora en base al sueldo base que el usuario va a poner y en base a eso poder calcular las horas extras. Considerando un mes de 4 semanas y 8 horas diarias de trabajo.

#Para calcular pago por hora
pago_hora_NORMAL=sueldo_base/160;

#Para calcular el pago de cada hora extra
pago_horas_EXTRAS=pago_hora_NORMAL*1.50*horas_extras_del_mes;

#Para calcular el total de ingreso mensual, considerando sueldo base y horas extras
total_ingresos_mensual=pago_horas_EXTRAS+sueldo_base;

#Para el DESCUENTO FONASA
descuento_FONASA=total_ingresos_mensual*0.07;

#Para el DESCUENTO AFP
descuento_AFP=total_ingresos_mensual*0.1;

#Para calcular el sueldo neto
seguridad_social_descuentos=descuento_FONASA+descuento_AFP
sueldo_neto_pagar=total_ingresos_mensual-seguridad_social_descuentos

"""Mostrar la liquidación:
OK   Mostrar un desglose de la liquidación, incluyendo el nombre del trabajador, su sueldo base, el pago por horas extras, el total de ingresos, el descuento por seguridad social y el sueldo neto a pagar, todo ordenado y bien presentado"""

print(f"Nombre del trabajador: {nombre_trabajador}");
print(f"Sueldo base: ${sueldo_base:}");
print(f"Pago por cada hora extra: ${pago_horas_EXTRAS}");
print(f"Total ingresos mensuales: ${total_ingresos_mensual}");
print(f"Descuentos por seguridad social: ${seguridad_social_descuentos}");
print(f"Sueldo neto a pagar: {sueldo_neto_pagar}");

"""Generar archivo de liquidación:
- Crear un archivo de texto (.txt) o un documento de Word (.docx) con los datos de la liquidación del trabajador.

- El archivo generado debe incluir el 
nombre del trabajador
su sueldo base
el pago por horas extras
el total de ingresos, los descuentos por FONASA y AFP, y el sueldo neto a pagar, todo de forma ordenada y bien presentada.
- El nombre del archivo generado debe seguir el formato "liquidacion_[nombre_trabajador].txt"""
      
with open("liquidacion_[nombre_trabajador].txt", "w") as documento:
    documento.write(f"DATOS DE LIQUIDACIÓN DE {nombre_trabajador}\n\n")
    documento.write(f"Nombre del trabajador: {nombre_trabajador}\n");
    documento.write(f"Sueldo base: ${sueldo_base:,.0f}\n");
    documento.write(f"Pago por cada hora extra: ${pago_horas_EXTRAS:,.0f}\n");
    documento.write(f"Total ingresos mensuales: ${total_ingresos_mensual:,.0f}\n");
    documento.write(f"Descuentos por seguridad social: ${seguridad_social_descuentos:,.0f}\n");
    documento.write(f"Sueldo neto a pagar: {sueldo_neto_pagar:,.0f}\n");