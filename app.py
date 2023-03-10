from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
  acciones_unicas = [
    'ACCESIÓN', 'ACCIONES COLUSORIAS',
    'ACCIÓN DE ACCESO A LA INFORMACIÓN PÚBLICA', 'ACCIÓN DE HÁBEAS CORPUS',
    'ACCIÓN DE HÁBEAS DATA', 'ACCIÓN DE PROTECCIÓN',
    'ACCIÓN DE PROTECCIÓN CON MEDIDA CAUTELAR',
    'ACCIÓN DE RECUPERACIÓN DE LA POSESIÓN',
    'ACCIÓN EXTRAORDINARIA DE PROTECCIÓN', 'ACCIÓN PAULIANA',
    'AMPARO POSESORIO',
    'APELACION DECISIONES JUNTA GENERAL (ART. 249 LEY COMPAÑÍAS)',
    'APERTURA DE CAJA O CASILLEROS DE SEGURIDAD', 'ARRAIGO',
    'AUTORIZACIÓN JUDICIAL PARA VENTA DE MERCADERÍA EN NAVES',
    'AUTORIZACIÓN PARA CONTRAER SEGUNDAS NUPCIAS',
    'AUTORIZACIÓN PARA INSCRIPCIÓN DE ESCRITURA',
    'AUTORIZACIÓN PARA INSCRIPCIÓN DE ESCRITURA CON OPOSICIÓN',
    'CANCELACIÓN DE HIPOTECA',
    'CERTIFICACIÓN EXPEDIDA POR ADMINISTRADOR DE ASOCIACIÓN',
    'CERTIFICACIÓN EXPEDIDA POR ADMINISTRADOR DE CLUB',
    'CERTIFICACIÓN EXPEDIDA POR ADMINISTRADOR DEL CONDOMINIO',
    'CERTIFICACIÓN EXPEDIDA POR ADMINISTRADOR ESTABLECIMIENTO EDUCATIVO',
    'CERTIFICACIÓN EXPEDIDA POR ADMINISTRADOR OTRAS ORGANIZACIONES',
    'CERTIFICACIÓN EXPEDIDA POR ADMNISTRADOR DEL CONDOMINIO',
    'CERTIFICACIÓN EXPEDIDA POR ADMNISTRADOR OTRAS ORGANIZACIONES',
    'CHEQUE PRESENTADO AL COBRO FUERA DE PLAZO', 'COBRO DE CHEQUE',
    'COBRO DE CHEQUE PROTESTADO', 'COBRO DE DINERO', 'COBRO DE FACTURAS',
    'COBRO DE FACTURAS POR BIENES Y SERVICIOS, HONORARIOS PROFESIONALES CUANDO LA PRETENSIÓN NO SEA EXIGIBLE EN PROCEDIMIENTO MONITORIO O EN VIA EJECUTIVA',
    'COBRO DE HONORARIOS DE ABOGADO',
    'COBRO DE HONORARIOS PROFESIONALES CUANDO LA PRETENSIÓN NO SEA EXIGIBLE EN PROCEDIMIENTO MONITORIO O EN VIA EJECUTIVA',
    'COBRO DE LETRA DE CAMBIO', 'COBRO DE PAGARÉ A LA ORDEN',
    'COMPROBANTE DE PAGO PARCIAL CON EFECTOS DE CHEQUE PROTESTADO',
    'CONCURSO DE ACREEDORES', 'CONSIGNACIÓN DE LLAVES',
    'CONTRATO DE MUTUO O PRESTAMO',
    'CONTRATO O DECLARACIÓN JURADA POR MORA DEL PAGO DE PENSIONES DE ARRENDAMIENTO',
    'CONTRATOS DE PRENDA ESPECIAL DE COMERCIO',
    'CONTRATOS DE VENTA CON RESERVA DE DOMINIO', 'CONTRATOS PRENDARIOS',
    'COPIA Y LA COMPULSA AUTENTICAS DE LAS ESCRITURAS PÚBLICAS',
    'CUMPLIMIENTO DE CONTRATO', 'CUMPLIMIENTO DE CONTRATO PROMISORIO',
    'DACIÓN EN PAGO', 'DAÑO MORAL', 'DAÑOS Y PERJUICIOS',
    'DAÑOS Y PERJUICIOS (ART.34 COFJ)',
    'DECLARACIONES TESTIMONIALES URGENTES (ART. 122 NUM. 7 COGEP)',
    'DECLARACIÓN DE PARTE', 'DECLARACIÓN JURAMENTADA',
    'DECLARATORIA DE INSOLVENCIA', 'DECLARATORIA DE MUERTE PRESUNTA',
    'DEMARCACIÓN DE LINDEROS', 'DEPRECATORIO',
    'DEPÓSITO DE PENSIÓN DE ARRENDAMIENTO', 'DESAHUCIO', 'DESPOJO JUDICIAL',
    'DESPOJO VIOLENTO', 'DEVOLUCIÓN DE GARANTIA',
    'DEVOLUCIÓN DE LO COBRADO EN EXCESO', 'DOCUMENTOS',
    'DOCUMENTOS (ART. 356 NUM. 1)',
    'DOCUMENTOS PRIVADOS LEGALMENTE RECONOCIDOS O RECONOCIDOS POR DECISIÓN JUDICIAL',
    'EJECUCION DE AUTO QUE CONTIENE LA ORDEN DE PAGO EN PROCEDIMIENTO MONITORIO',
    'EJECUCION DE HIPOTECA', 'EJECUCION POR SILENCIO ADMINISTRATIVO',
    'EJECUCIÓN (ART. 363 NUM. 11)',
    'EJECUCIÓN DE ACTA DE MEDIACIÓN',
    'EJECUCIÓN DE ACTA DE MEDIACIÓN EXTRANJERA HOMOLOGADA',
    'EJECUCIÓN DE ACTA DE TRANSACCIÓN',
    'EJECUCIÓN DE CONTRATO PRENDARIO Y RESERVA DE DOMINIO',
    'EJECUCIÓN DE LAUDO ARBITRAL', 'EJECUCIÓN DE SENTENCIA EJECUTORIADA',
    'EMBARGO Y REMATE DE BIEN CON RESERVA DE DOMINIO',
    'EMBARGO Y REMATE DE PRENDA', 'EXCLUSIÓN DE SOCIO',
    'EXHIBICIÓN DE DOCUMENTOS',
    'EXHIBICIÓN DE LA COSA MUEBLE QUE SE PRETENDE REINVINDICAR',
    'EXHIBICIÓN DE TÍTULOS',
    'EXPROPIACIÓN (CONTROVERSIAS GENERADAS POR FALTA DE ACUERDO EN EL PRECIO A PAGAR)',
    'EXTINCIÓN DE DERECHO DE USO - HABITACIÓN', 'EXÁMEN GRAFOLÓGICO',
    'FACTURA O PRIMA DE SEGUROS', 'FACTURAS',
    'FACTURAS O DOCUMENTOS (ART. 356 NUM.2)', 'FALSEDAD DE INSTRUMENTO PÚBLICO',
    'IMPUGNACION DEL RECONOCIMIENTO VOLUNTARIO DE HIJO O HIJA',
    'INCUMPLIMIENTO DE CONTRATO', 'INSPECCIÓN PREPARATORIA', 'INTERDICCIÓN',
    'INVENTARIO', 'JUICIO DE PARTICIÓN CON OPOSICIÓN',
    'LANZAMIENTO (ART. 45 LEY DE INQUILINATO)',
    'LANZAMIENTO (ART. 46 LEY DE INQUILINATO)',
    'LAS ORDENADAS POR LEY (ART. 332  NUM. 1)',
    'LAS ORDENADAS POR LEY (ART. 347 NUM. 8)',
    'LEVANTAMIENTO DE PROHIBICIÓN DE ENAJENAR', 'MEDIDA CAUTELAR', 'MEJORAS',
    'NOTIFICACIÓN DE REVOCATORIA DE PODER', 'NULIDAD DE CONTRATO',
    'NULIDAD DE INSTRUMENTO PÚBLICO', 'NULIDAD DE SENTENCIA',
    'NULIDAD DEL ACTA DE MEDIACIÓN', 'OBRA NUEVA',
    'OPOSICIÓN A LA RENDICIÓN DE CUENTAS', 'OPOSICIÓN AL DESAHUCIO',
    'ORDINARIO', 'OTROS', 'PACTO DE RETROVENTA', 'PAGO DE DINERO',
    'PAGO DE LO NO DEBIDO', 'PAGO POR CONSIGNACIÓN', 'PARTICION NO VOLUNTARIA',
    'PARTICIÓN DE BIENES ENTRE COPROPIETARIOS',
    'PRESCRIPCIÓN ADQUISITIVA DE DOMINIO', 'PRESCRIPCIÓN DE HIPOTECA',
    'PRESCRIPCIÓN EXTINTIVA',
    'PRESCRIPCIÓN EXTRAORDINARIA ADQUISITIVA DE DOMINIO',
    'PROHIBICIÓN DE ENAJENAR', 'RECEPCIÓN DE PLENO DERECHO (ART. 122 RLOSNCP)',
    'RECEPCIÓN PRESUNTA DEFINITIVA',
    'RECLAMACION COOPROPIETARIOS (ART. 7 LEY DE PROPIEDAD HORIZONTAL)',
    'RECONOCIMIENTO DE DOCUMENTO PRIVADO',
    'RECONOCIMIENTO O DELCARATORIA DE UNIÓN DE HECHO',
    'RECONOCIMIENTO Y HOMOLOGACIÓN DE SENTENCIA EXTRANJERA',
    'RECTIFICACIÓN DE ESCRITURA', 'RECUSACIÓN', 'REINVINDICACIÓN',
    'RENDICIÓN DE CUENTAS', 'RENDICIÓN DE CUENTAS CON OPOSICIÓN',
    'REPETICIÓN POR PAGO DE SEGURO DE FIANZA', 'REQUERIMIENTO JUDICIAL',
    'RESCISIÓN DE CONTRATO', 'RESCISIÓN DE CONTRATO POR LESIÓN ENORME',
    'RESOLUCIÓN DE CONTRATO', 'RETENCIÓN', 'REVOCATORIA DE DONACIÓN',
    'SECUESTRO', 'SERVIDUMBRE',
    'SOLICITUD DE REBAJA DE PENSIÓN DE ARRENDAMIENTO',
    'SOLICITUD JUDICIAL EXCEPCIONAL DE CONCURSO PREVENTIVO',
    'SUSPENSIÓN DE OBRA', 'TERCERÍA EXCLUYENTE',
    'TERMINACIÓN DE CONTRATO', 'TERMINACIÓN DE CONTRATO DE PRESTAMO DE USO',
    'TRANSACCIÓN EXTRAJUDICIAL (ART. 347)', 'VICIOS REDHIBITORIOS'
  ] 
  cantones = ['ALAMOR', 'ALAUSÍ', 'ALFREDO BAQUERIZO MORENO (JUJAN)', 'AMALUZA', 'AMBATO', 'ARAJUNO', 'ARCHIDONA', 'ARENILLAS', 'ATACAMES', 'ATUNTAQUI', 'AZOGUES', 'BABA', 'BABAHOYO', 'BAEZA', 'BAHÍA DE CARÁQUEZ', 'BALAO', 'BALSAS', 'BALZAR', 'BAÑOS', 'BIBLIÁN', 'BOLÍVAR', 'CAJABAMBA', 'CALCETA', 'CALUMA', 'CAMILO PONCE ENRÍQUEZ', 'CARIAMANGA', 'CARLOS JULIO AROSEMENA TOLA', 'CATACOCHA', 'CATAMAYO', 'CATARAMA', 'CAYAMBE', 'CAÑAR', 'CELICA', 'CEVALLOS', 'CHAGUARPAMBA', 'CHAMBO', 'CHILLA', 'CHILLANES', 'CHONE', 'CHORDELEG', 'CHUNCHI', 'COLIMES', 'CORONEL MARCELINO MARIDUEÑA', 'COTACACHI', 'CUENCA', 'CUMANDÁ', 'DAULE', 'DÉLEG', 'ECHEANDÍA', 'EL CARMEN', 'EL CHACO', 'EL CORAZÓN', 'EL DORADO DE CASCALES', 'EL GUABO', 'EL PAN', 'EL PANGUI', 'EL TAMBO', 'EL TRIUNFO', 'EL ÁNGEL', 'ELOY ALFARO', 'ESMERALDAS', 'FLAVIO ALFARO', 'GENERAL ANTONIO ELIZALDE (BUCAY)', 'GENERAL LEONIDAS PLAZA GUTIÉRREZ', 'GENERAL VILLAMIL', 'GIRÓN', 'GONZANAMÁ', 'GUACHAPALA', 'GUALACEO', 'GUALAQUIZA', 'GUAMOTE', 'GUANO', 'GUARANDA', 'GUAYAQUIL', 'GUAYZIMI', 'HUACA', 'HUAMBOYA', 'HUAQUILLAS', 'IBARRA', 'ISIDRO AYORA', 'JAMA', 'JARAMIJÓ', 'JIPIJAPA', 'JUNÍN', 'LA BONITA', 'LA CONCORDIA', 'LA JOYA DE LOS SACHAS', 'LA LIBERTAD', 'LA MANÁ', 'LA TRONCAL', 'LA VICTORIA', 'LAS NAVES', 'LATACUNGA', 'LOGROÑO', 'LOJA', 'LOMAS DE SARGENTILLO', 'LORETO', 'LUMBAQUÍ', 'MACARÁ', 'MACAS', 'MACHACHI', 'MACHALA', 'MANTA', 'MARCABELÍ', 'MERA', 'MILAGRO', 'MIRA', 'MOCACHE', 'MOCHA', 'MONTALVO', 'MONTECRISTI', 'MUISNE', 'NABÓN', 'NARANJAL', 'NARANJITO', 'NARCISA DE JESÚS', 'NUEVA LOJA', 'NUEVO ROCAFUERTE', 'OLMEDO', 'OLMEDO', 'OTAVALO', 'OÑA', 'PABLO SEXTO', 'PACCHA', 'PAJAN', 'PALANDA', 'PALENQUE', 'PALESTINA', 'PALLATANGA', 'PALORA', 'PAQUISHA', 'PASAJE', 'PATATE', 'PAUTE', 'PEDERNALES', 'PEDRO CARBO', 'PEDRO VICENTE MALDONADO', 'PELILEO', 'PENIPE', 'PICHINCHA', 'PIMAMPIRO', 'PINDAL', 'PIÑAS', 'PORTOVELO', 'PORTOVIEJO', 'PUCARÁ', 'PUEBLOVIEJO', 'PUERTO AYORA', 'PUERTO BAQUERIZO MORENO', 'PUERTO EL CARMEN DE PUTUMAYO', 'PUERTO FRANCISCO DE ORELLANA', 'PUERTO LÓPEZ', 'PUERTO QUITO', 'PUERTO VILLAMIL', 'PUJILÍ', 'PUYO', 'PÍLLARO', 'QUERO', 'QUEVEDO', 'QUILANGA', 'QUINSALOMA', 'QUITO', 'RIOBAMBA', 'RIOVERDE', 'ROCAFUERTE', 'ROSA ZÁRATE', 'SALINAS', 'SALITRE', 'SAMBORONDÓN', 'SAN FERNANDO', 'SAN GABRIEL', 'SAN JACINTO DE BUENA FE', 'SAN JOSÉ DE CHIMBO', 'SAN JUAN BOSCO', 'SAN LORENZO', 'SAN MIGUEL', 'SAN MIGUEL', 'SAN MIGUEL DE LOS BANCOS', 'SAN VICENTE', 'SANGOLQUÍ', 'SANTA ANA', 'SANTA CLARA', 'SANTA ELENA', 'SANTA ISABEL', 'SANTA LUCÍA', 'SANTA ROSA', 'SANTIAGO', 'SANTIAGO DE MÉNDEZ', 'SANTO DOMINGO', 'SAQUISILÍ', 'SARAGURO', 'SEVILLA DE ORO', 'SHUSHUFINDI', 'SIGCHOS', 'SIMÓN BOLÍVAR', 'SOZORANGA', 'SUCRE', 'SUCÚA', 'SUSCAL', 'SÍGSIG', 'TABACUNDO', 'TAISHA', 'TARAPOA', 'TENA', 'TISALEO', 'TOSAGUA', 'TULCÁN', 'URCUQUÍ', 'VALDÉZ', 'VALENCIA', 'VELASCO IBARRA', 'VENTANAS', 'VINCES', 'YACUAMBI', 'YAGUACHI', 'YANTZAZA', 'ZAMORA', 'ZAPOTILLO', 'ZARUMA', 'ZUMBA', 'ZUMBI']
  return render_template("home.html", acciones_unicas=acciones_unicas,cantones=cantones)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
