from typing import Literal, Annotated
from typing_extensions import TypedDict
from fastapi import Body

class InputPayload(TypedDict):
    pass

# ----------------------------
# Variables numericas
# ----------------------------
InputPayload.__annotations__["Edad_Al_Tx"] = Annotated[float, Body(ge=0, le=120, description="La edad debe estar entre 0 y 120")]
InputPayload.__annotations__["Tiempo_En_Lista_Días"] = Annotated[int, Body(ge=0, description="Número de días que lleva el paciente en lista de espera")]
InputPayload.__annotations__["Peso_Pre_Tx"] = Annotated[float, Body(ge=0, description="Peso antes de la cirugía en kilogramos")]
InputPayload.__annotations__["MELD_Score"] = Annotated[int, Body(ge=6, le=40, description="VALOR DEL MELD PRETRASPLANTE")]
InputPayload.__annotations__["Edad_Donante_Tx#1"] = Annotated[float, Body(ge=0, le=120, description="La edad debe estar entre 0 y 120")]
InputPayload.__annotations__["#_Unidades_Glóbulos_Rojos_Tx#1"] = Annotated[int, Body(ge=0, description="Unidades de glóbulos rojos usadas")]
InputPayload.__annotations__["#_Unidades_Plasma_Fresco_Congelado_Tx#1"] = Annotated[int, Body(ge=0, description="Unidades de plasma fresco congelado usadas")]
InputPayload.__annotations__["#_Unidades_Crioprecipitados_Tx#1"] = Annotated[int, Body(ge=0, description="Unidades de crioprecipitados usadas")]
InputPayload.__annotations__["#_Unidades_Plaquetas_Tx#1"] = Annotated[int, Body(ge=0, description="Unidades de plaquetas usadas")]
InputPayload.__annotations__["Tiempo_Quirúrgico_Tx#1"] = Annotated[float, Body(ge=0, description="Horas que tomó la cirugía")]
InputPayload.__annotations__["Días_En_UCI"] = Annotated[int, Body(ge=0, description="Días que duró un paciente en UCI")]
InputPayload.__annotations__["Días_En_Hospitalización_Piso"] = Annotated[int, Body(ge=0, description="Días que duró un paciente en una habitación")]
InputPayload.__annotations__["Días_Totales_Intrahospitalarios"] = Annotated[int, Body(ge=0, description="Días totales que duró hospitalizado")]
InputPayload.__annotations__["Tiempo_Isquemia_Fría_Tx#1"] = Annotated[float, Body(ge=0, description="Horas que duró el órgano sin sangre refrigerado")]
InputPayload.__annotations__["Composición_Corporal"] = Annotated[int, Body(ge=1, le=5, description="Categorías usadas para el BMI")]

# ----------------------------
# Variables binarias
# ----------------------------

bool_cols = [
    'Es_Mujer',
    'Donante_es_mujer',
    'Hepatocarcinoma',
    'Falla_Cardiaca_Pre_Tx',
    'Antecedente_De_Tabaquismo',
    'Antecedente_De_Alcoholismo',
    'Enfermedad_Coronaria_Pre_Tx',
    'Infarto_Cardiaco_Pre_Tx',
    'Diabetes_Mellitus_Pre_Tx',
    'Hipertensión_Arterial_Pre_Tx',
    'CMV_Receptor',
    'Trasplante_Combinado-Hígado-Riñón_Tx#1',
    'Soporte_Vasopresor_PeriTx',
    'Levosimendan_PeriTx',
    'Noradrenalina_PeriTx',
    'Adrenalina_PeriTx',
    'Vasopresina_PeriTx',
    'Dopamina_PeriTx',
    'Amiodarona_PeriTx',
    'Stent',
    'Requirió_Reconstrucción_Biliar',
    'Fast_Track',
    'Rechazo_Agudo',
    'Rechazo_Crónico',
    'Retrasplante',
    'PTLD',
    'Sobrevida_PeriQx_30_días_POP',
    ]
binary_desc = "0 = No, 1 = Sí"
for key in bool_cols:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Causa: {key} ({binary_desc})")]
# ----------------------------
# Causa_Tx_*  (many binary cause indicators)
# ----------------------------
causas = [
    "Causa_Tx_ADENOMA GIGANTE", "Causa_Tx_ALCOHÓLICA", "Causa_Tx_ATRESIA VIAS BILIARES",
    "Causa_Tx_BUDDCHIARI", "Causa_Tx_CIRROSIS BILIAR SECUNDARIA", "Causa_Tx_CIRROSIS DEL INJERTO",
    "Causa_Tx_COLANGIOCARCINOMA", "Causa_Tx_COLANGIOPATÍA ISQUÉMICA", "Causa_Tx_COLANGITIS BILIAR PRIMARIA",
    "Causa_Tx_COLANGITIS ESCLEROSANTE PRIMARIA", "Causa_Tx_CRIPTOGENICA", "Causa_Tx_DEF ALFA 1 ANTITRIPSINA",
    "Causa_Tx_DEFECTO EN LA SÍNTESIS/SECRECIÓN DE ÁCIDOS BILIARES", "Causa_Tx_ENFERMEDAD POLIQUISTICA",
    "Causa_Tx_FHF", "Causa_Tx_FIBROSIS HEPATICA CONGENITA", "Causa_Tx_HBV", "Causa_Tx_HCV",
    "Causa_Tx_HEMOCROMATOSIS", "Causa_Tx_HEPATITIS AUTOINMUNE", "Causa_Tx_HEPATOBLASTOMA",
    "Causa_Tx_HIPERPLASIA NODULAR PROLIFERATIVA", "Causa_Tx_NASH", "Causa_Tx_OVERLAP (CBP + AIH)",
    "Causa_Tx_QUISTE HIATÍDICO", "Causa_Tx_TUMOR MIOFIBROBLASTICO", "Causa_Tx_WILSON",
    "Causa_Tx_Renal_HEPATORENAL TIPO I", "Causa_Tx_Renal_INSUFICIENCIA RENAL AGUDA",
    "Causa_Tx_Renal_INSUFICIENCIA RENAL CRÓNICA", "Causa_Tx_Renal_NEFROPATIA MEMBRANO PROLIFERATIVA",
    "Causa_Tx_Renal_NEFROPATIA POR IGA", "Causa_Tx_Renal_NEFROPATÍA DIABÉTICA"
]
for key in causas:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Causa: {key} ({binary_desc})")]


dislip = [
    "Dislipidemia_Pre_Tx_DÉFICIT DE HDL", "Dislipidemia_Pre_Tx_HIPERCOLESTEROLISMO",
    "Dislipidemia_Pre_Tx_HIPERLIPIDEMIA MIXTA", "Dislipidemia_Pre_Tx_HIPERTRIGLICERIDEMIA",
    "Dislipidemia_Pre_Tx_NO"
]
for key in dislip:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Dislipidemia flag: {key} ({binary_desc})")]

mdrd = [
    "MDRD_PreTx_ 15-29", "MDRD_PreTx_ 59-30", "MDRD_PreTx_ 90-60",
    "MDRD_PreTx_ > 90", "MDRD_PreTx_< 15"
]
for key in mdrd:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"MDRD group: {key} ({binary_desc})")]

ekg = [
    "EKG_PreQx_Bloqueo Rama Der", "EKG_PreQx_Bloqueo Rama Izq", "EKG_PreQx_Bradiarritmias",
    "EKG_PreQx_Extrasistoles", "EKG_PreQx_Mala prog Onda R", "EKG_PreQx_Normal",
    "EKG_PreQx_QTc prolongado ", "EKG_PreQx_Taquiarritmias supraventriculares",
    "EKG_PreQx_Taquiarritmias ventriculares", "EKG_PreQx_Trastornos de la repolarizacion"
]
for key in ekg:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"EKG flag: {key} ({binary_desc})")]

valv = [
    "Valvulopatía_Pre_Tx_NO", "Valvulopatía_Pre_Tx_AÓRTICA",
    "Valvulopatía_Pre_Tx_MITRAL", "Valvulopatía_Pre_Tx_PULMONAR",
    "Valvulopatía_Pre_Tx_TRICUSPÍDEA"
]
for key in valv:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Valvulopatia: {key} ({binary_desc})")]

eco = [
    "Ecocardiograma_PreQx-FE_Cod_40-60%", "Ecocardiograma_PreQx-FE_Cod_< 40%",
    "Ecocardiograma_PreQx-FE_Cod_>60%"
]
for key in eco:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Ecocardiograma code: {key} ({binary_desc})")]

donante_causes = [
    "Causa_Muerte_Donante_Tx#1_ACV", "Causa_Muerte_Donante_Tx#1_ADENOMA DE HIPOFISIS",
    "Causa_Muerte_Donante_Tx#1_HEMORRAGIA SUBARACNOIDEA", "Causa_Muerte_Donante_Tx#1_HERIDA CUELLO",
    "Causa_Muerte_Donante_Tx#1_HERIDA X ARMA  DE FUEGO", "Causa_Muerte_Donante_Tx#1_HIPERTENSION ENDOCRANEANA",
    "Causa_Muerte_Donante_Tx#1_HIPÓXICA", "Causa_Muerte_Donante_Tx#1_OTRO TUMOR CEREBRAL",
    "Causa_Muerte_Donante_Tx#1_PARO CARDIORESPIRATORIO DE ORIGEN NO CLARO",
    "Causa_Muerte_Donante_Tx#1_POST-CLIPAJE ANEURISMA", "Causa_Muerte_Donante_Tx#1_RESECCION DE MENINGIOMA",
    "Causa_Muerte_Donante_Tx#1_RUPTURA ANEURISMA", "Causa_Muerte_Donante_Tx#1_STATUS CONVULSIVO",
    "Causa_Muerte_Donante_Tx#1_TCE", "Causa_Muerte_Donante_Tx#1_TRAUMA RAQUIMEDULAR"
]
for key in donante_causes:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Donor death cause: {key} ({binary_desc})")]

tipo_cx = [
    "Tipo_de_Cx-Trasplante_Tx#1_BYPASS", "Tipo_de_Cx-Trasplante_Tx#1_CROSS-CLAMPING",
    "Tipo_de_Cx-Trasplante_Tx#1_PIGGY-BACK", "Tipo_de_Cx-Trasplante_Tx#1_SPLIT"
]
for key in tipo_cx:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Tipo Cx: {key} ({binary_desc})")]

sev_rechazo = [
    "Severidad_Rechazo_Agudo_BORDERLINE", "Severidad_Rechazo_Agudo_LEVE",
    "Severidad_Rechazo_Agudo_MODERADO", "Severidad_Rechazo_Agudo_NO",
    "Severidad_Rechazo_Agudo_SEVERO"
]
for key in sev_rechazo:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Severidad rechazo: {key} ({binary_desc})")]

ind_retra = [
    "Indicación_Retrasplante_BUDD CHIARI", "Indicación_Retrasplante_COLANGIOPATIA ISQUEMICA",
    "Indicación_Retrasplante_DISFUNCIÓN PRIMARIA DEL INJERTO ", "Indicación_Retrasplante_HELLP",
    "Indicación_Retrasplante_TROMBOSIS ARTERIA HEPÁTICA", "Indicación_Retrasplante_TROMBOSIS PORTAL"
]
for key in ind_retra:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Indicación retransplante: {key} ({binary_desc})")]

neoplasias = [
    "Neoplasia_PostTx_CA PIEL", "Neoplasia_PostTx_CA PULMON", "Neoplasia_PostTx_CA RENAL",
    "Neoplasia_PostTx_CA SENO", "Neoplasia_PostTx_CA UTERO", "Neoplasia_PostTx_NO",
    "Neoplasia_PostTx_PTLD", "Neoplasia_PostTx_SARCOMA DE KAPOSI"
]
for key in neoplasias:
    InputPayload.__annotations__[key] = Annotated[int, Body(ge=0, le=1, description=f"Neoplasia postTx: {key} ({binary_desc})")]

# Child_Pugh_Letra: we keep as string (A/B/C) — adjust if you want numeric codes
InputPayload.__annotations__["Child_Pugh_Letra"] = Literal['A','B','C']