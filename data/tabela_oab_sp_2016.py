"""
Tabela de Honorários - OAB/SP 2016 (base) + serviços expandidos e referências 2025/2026.
Fator de correção aproximado 2016→2026: 1.75 (IPCA acumulado referência).
"""

FATOR_CORRECAO_2016_2026 = 1.75

TABELA = {
    "Parte Geral": [
        {"item": "1", "servico": "Ações de jurisdição contenciosa (geral)", "percentual": 20.0, "minimo": 3991.07, "observacao": "20% sobre valor econômico. Mínimo haja ou não benefício patrimonial."},
        {"item": "2a", "servico": "Recursos - Interposição", "percentual": None, "minimo": 1995.55, "observacao": "Mandatário constituído ou substabelecido"},
        {"item": "2b", "servico": "Recursos - Contra-razões", "percentual": None, "minimo": 1995.55, "observacao": ""},
        {"item": "2c", "servico": "Recursos - Memoriais", "percentual": None, "minimo": 1995.55, "observacao": ""},
        {"item": "2d", "servico": "Recursos - Sustentação oral", "percentual": None, "minimo": 3991.07, "observacao": "Outra cidade: mínimo dobrado + despesas"},
        {"item": "2e", "servico": "Recursos - Acompanhamento simples", "percentual": None, "minimo": 1197.33, "observacao": ""},
        {"item": "3", "servico": "Exame de processos em geral", "percentual": None, "minimo": 581.23, "observacao": ""},
        {"item": "4", "servico": "Prestação de serviços em audiência", "percentual": None, "minimo": 798.21, "observacao": ""},
        {"item": "5a", "servico": "Precatórias - Citação/intimação", "percentual": None, "minimo": 968.71, "observacao": ""},
        {"item": "5b", "servico": "Precatórias - Outros fins", "percentual": None, "minimo": 1356.19, "observacao": ""},
        {"item": "6", "servico": "Advocacia de partido (mensal)", "percentual": None, "minimo": 1995.55, "observacao": "Sem vínculo empregatício"},
    ],
    "Advocacia Cível": [
        {"item": "7", "servico": "Medidas cautelares / tutela de urgência", "percentual": None, "minimo": 2324.91, "observacao": ""},
        {"item": "8", "servico": "Ação de despejo (ordinária)", "percentual": 20.0, "minimo": 3991.07, "observacao": "20% sobre aluguel de 1 ano"},
        {"item": "9", "servico": "Despejo + cobrança de aluguéis", "percentual": 15.0, "minimo": 1995.55, "observacao": ""},
        {"item": "10", "servico": "Revisão / arbitramento de aluguel", "percentual": 20.0, "minimo": 3991.07, "observacao": ""},
        {"item": "12a", "servico": "Possessórias - Manutenção/reintegração", "percentual": 20.0, "minimo": 3991.07, "observacao": "20% sobre valor da coisa"},
        {"item": "12b", "servico": "Possessórias - Interdito proibitório", "percentual": 10.0, "minimo": 3991.07, "observacao": ""},
        {"item": "15", "servico": "Usucapião", "percentual": 20.0, "minimo": 3991.07, "observacao": "20% do valor do bem"},
        {"item": "18", "servico": "Desapropriação direta", "percentual": 10.0, "minimo": 4843.54, "observacao": "10% sobre diferença oferta x indenização"},
        {"item": "20", "servico": "Ação monitória", "percentual": 20.0, "minimo": 1937.42, "observacao": ""},
        {"item": "25", "servico": "Mandado de segurança", "percentual": 20.0, "minimo": 3991.07, "observacao": "10% a 20% sobre proveito"},
        {"item": "34", "servico": "Juizados Especiais Cíveis", "percentual": 20.0, "minimo": 1197.33, "observacao": ""},
        {"item": "C1", "servico": "Procedimento ordinário / comum", "percentual": 20.0, "minimo": 4060.80, "observacao": "Ref. tabelas recentes ~R$ 6.256 (2026)"},
        {"item": "C2", "servico": "Execução / cumprimento de sentença", "percentual": 20.0, "minimo": 2256.00, "observacao": ""},
        {"item": "C3", "servico": "Embargos à execução / impugnação", "percentual": 20.0, "minimo": 2256.00, "observacao": ""},
    ],
    "Família e Sucessões": [
        {"item": "35", "servico": "Inventário/arrolamento (todos herdeiros)", "percentual": 6.0, "minimo": 3991.07, "observacao": "6% sobre monte-mor"},
        {"item": "35b", "servico": "Inventário - meeiro/herdeiro/legatário", "percentual": 6.0, "minimo": 1995.55, "observacao": "6% sobre quinhão"},
        {"item": "36", "servico": "Habilitação de crédito em inventário", "percentual": 20.0, "minimo": 1995.55, "observacao": ""},
        {"item": "39", "servico": "Separação/divórcio consensual (sem bens)", "percentual": None, "minimo": 1995.55, "observacao": ""},
        {"item": "40", "servico": "Separação/divórcio judicial (com bens)", "percentual": 6.0, "minimo": 3991.07, "observacao": "Critério de inventário"},
        {"item": "44", "servico": "Investigação de paternidade", "percentual": 20.0, "minimo": 3991.07, "observacao": ""},
        {"item": "45", "servico": "Ação de alimentos", "percentual": 20.0, "minimo": 3991.07, "observacao": ""},
        {"item": "46", "servico": "Regulamentação de visitas / guarda", "percentual": None, "minimo": 2500.00, "observacao": "Referência de mercado"},
        {"item": "47", "servico": "União estável (reconhecimento/dissolução)", "percentual": 6.0, "minimo": 3991.07, "observacao": ""},
    ],
    "Trabalhista": [
        {"item": "T1", "servico": "Reclamação trabalhista (reclamante)", "percentual": 20.0, "minimo": 3000.00, "observacao": "Prática: 15% a 30% sobre proveito"},
        {"item": "T2", "servico": "Defesa trabalhista (reclamado)", "percentual": None, "minimo": 4000.00, "observacao": "Valor fixo de referência"},
        {"item": "T3", "servico": "Recurso ordinário trabalhista", "percentual": None, "minimo": 2500.00, "observacao": ""},
        {"item": "T4", "servico": "Execução trabalhista", "percentual": 15.0, "minimo": 2000.00, "observacao": ""},
        {"item": "T5", "servico": "Acordo trabalhista extrajudicial", "percentual": 10.0, "minimo": 1500.00, "observacao": ""},
    ],
    "Previdenciário": [
        {"item": "P1", "servico": "Benefício previdenciário (atrasados)", "percentual": 30.0, "minimo": 3500.00, "observacao": "Prática: 25% a 40% sobre atrasados"},
        {"item": "P2", "servico": "Aposentadoria / revisão de benefício", "percentual": 30.0, "minimo": 3500.00, "observacao": ""},
        {"item": "P3", "servico": "Auxílio-doença / BPC / LOAS", "percentual": 30.0, "minimo": 2500.00, "observacao": ""},
        {"item": "P4", "servico": "Recurso administrativo INSS", "percentual": None, "minimo": 1500.00, "observacao": ""},
    ],
    "Criminal": [
        {"item": "CR1", "servico": "Defesa criminal (rito ordinário)", "percentual": None, "minimo": 5000.00, "observacao": "Por fase ou global"},
        {"item": "CR2", "servico": "Tribunal do Júri (até pronúncia)", "percentual": None, "minimo": 4000.00, "observacao": ""},
        {"item": "CR3", "servico": "Tribunal do Júri (plenário)", "percentual": None, "minimo": 8000.00, "observacao": ""},
        {"item": "CR4", "servico": "Habeas corpus", "percentual": None, "minimo": 3500.00, "observacao": ""},
        {"item": "CR5", "servico": "Recurso criminal / apelação", "percentual": None, "minimo": 3000.00, "observacao": ""},
    ],
    "Atividades Avulsas / Consultoria": [
        {"item": "A1", "servico": "Consulta verbal (horário comercial)", "percentual": None, "minimo": 350.00, "observacao": "Atual mercado ~R$ 500-700"},
        {"item": "A2", "servico": "Consulta com exame de documentos", "percentual": None, "minimo": 750.00, "observacao": ""},
        {"item": "A3", "servico": "Hora técnica / intelectual", "percentual": None, "minimo": 564.00, "observacao": "Atual ~R$ 200-800/h"},
        {"item": "A4", "servico": "Parecer simples", "percentual": None, "minimo": 1113.00, "observacao": ""},
        {"item": "A5", "servico": "Parecer complexo", "percentual": 10.0, "minimo": 3339.00, "observacao": ""},
        {"item": "A6", "servico": "Elaboração de contrato / minuta", "percentual": 2.0, "minimo": 2000.00, "observacao": "Sobre valor do negócio"},
        {"item": "A7", "servico": "Notificação extrajudicial", "percentual": None, "minimo": 800.00, "observacao": ""},
        {"item": "A8", "servico": "Mediação / conciliação extrajudicial", "percentual": 10.0, "minimo": 2000.00, "observacao": ""},
    ],
    "Empresarial / Consumidor / Outros": [
        {"item": "E1", "servico": "Ação de direito do consumidor", "percentual": 20.0, "minimo": 2500.00, "observacao": ""},
        {"item": "E2", "servico": "Recuperação judicial / falência (devedor)", "percentual": 4.0, "minimo": 6780.95, "observacao": "2% a 6% do passivo"},
        {"item": "E3", "servico": "Habilitação de crédito em falência", "percentual": 10.0, "minimo": 968.71, "observacao": ""},
        {"item": "E4", "servico": "Assessoria societária", "percentual": None, "minimo": 3000.00, "observacao": ""},
        {"item": "E5", "servico": "Compliance / LGPD", "percentual": None, "minimo": 5000.00, "observacao": "Valor de mercado"},
        {"item": "E6", "servico": "Direito digital / proteção de dados", "percentual": None, "minimo": 4000.00, "observacao": ""},
    ],
}

SERVICOS_LISTA = []
for categoria, itens in TABELA.items():
    for item in itens:
        SERVICOS_LISTA.append({
            "categoria": categoria,
            "item": item["item"],
            "servico": item["servico"],
            "percentual": item["percentual"],
            "minimo": item["minimo"],
            "observacao": item["observacao"],
            "label": f"[{categoria}] {item['servico']}"
        })

CLAUSULAS_MODELO = """CLÁUSULA DE HONORÁRIOS (MODELO SUGESTIVO)

1. DOS HONORÁRIOS
O CONTRATANTE pagará ao CONTRATADO os honorários advocatícios no valor de R$ {valor:,.2f}, referentes aos serviços descritos neste contrato.

2. FORMA DE PAGAMENTO
Os honorários serão pagos da seguinte forma:
{parcelamento}

3. REAJUSTE
Os valores serão atualizados pelo IPCA ou índice oficial que o substitua, a partir do vencimento de cada parcela.

4. SUCUMBÊNCIA
Os honorários de sucumbência pertencem exclusivamente ao advogado (art. 23 da Lei 8.906/94) e não excluem nem compensam os honorários contratados.

5. DESPESAS
Custas processuais, emolumentos, deslocamentos, cópias e demais despesas necessárias correrão por conta do CONTRATANTE, mediante prestação de contas.

6. RESCISÃO
Em caso de rescisão antecipada por iniciativa do CONTRATANTE, serão devidos os honorários proporcionais aos serviços já prestados, observado o mínimo ético da tabela da OAB.

Observação: Modelo genérico. Adapte às particularidades do caso e da seccional da OAB.
"""
