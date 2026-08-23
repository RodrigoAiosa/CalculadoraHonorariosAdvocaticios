"""
Tabela de Honorários Advocatícios - OAB/SP 2016
Atualizada em 11/01/2016 | Publicada em 11/01/2016

Fonte: Tabela oficial da OAB São Paulo (valores de referência mínimos).
Observação: As tabelas de honorários são fixadas por cada Seccional da OAB.
Esta é baseada na OAB-SP 2016 e serve como referência orientativa.
"""

# Valores em R$ (mínimos da tabela 2016)

TABELA = {
    "Parte Geral": [
        {
            "item": "1",
            "servico": "Ações de jurisdição contenciosa ou que assumam este caráter",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "20% sobre o valor econômico da questão. Mínimo haja ou não benefício patrimonial."
        },
        {
            "item": "2a",
            "servico": "Recursos - Interposição de qualquer recurso",
            "percentual": None,
            "minimo": 1995.55,
            "observacao": "Mandatário expressamente constituído ou substabelecido"
        },
        {
            "item": "2b",
            "servico": "Recursos - Contra-razões de qualquer recurso",
            "percentual": None,
            "minimo": 1995.55,
            "observacao": ""
        },
        {
            "item": "2c",
            "servico": "Recursos - Elaboração de memoriais",
            "percentual": None,
            "minimo": 1995.55,
            "observacao": ""
        },
        {
            "item": "2d",
            "servico": "Recursos - Sustentação oral",
            "percentual": None,
            "minimo": 3991.07,
            "observacao": "Em outra cidade: mínimo R$ 7.982,15 + despesas de viagem"
        },
        {
            "item": "2e",
            "servico": "Recursos - Simples acompanhamento de recurso",
            "percentual": None,
            "minimo": 1197.33,
            "observacao": ""
        },
        {
            "item": "3",
            "servico": "Exame de processos em geral",
            "percentual": None,
            "minimo": 581.23,
            "observacao": ""
        },
        {
            "item": "4",
            "servico": "Prestação de serviços em audiência",
            "percentual": None,
            "minimo": 798.21,
            "observacao": ""
        },
        {
            "item": "5a",
            "servico": "Precatórias - Citação, intimação, notificação ou interpelação",
            "percentual": None,
            "minimo": 968.71,
            "observacao": ""
        },
        {
            "item": "5b",
            "servico": "Precatórias - Outros fins",
            "percentual": None,
            "minimo": 1356.19,
            "observacao": ""
        },
        {
            "item": "6",
            "servico": "Advocacia de partido (sem vínculo empregatício) - mensal",
            "percentual": None,
            "minimo": 1995.55,
            "observacao": "Valor mensal mínimo"
        },
    ],
    "Advocacia Cível - Procedimentos Especiais": [
        {
            "item": "7",
            "servico": "Medidas cautelares",
            "percentual": None,
            "minimo": 2324.91,
            "observacao": ""
        },
        {
            "item": "8",
            "servico": "Ordinária de despejo",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "20% sobre o valor do aluguel correspondente a um ano de locação"
        },
        {
            "item": "9a",
            "servico": "Despejo por falta de pagamento - com purgação de mora (autor)",
            "percentual": 10.0,
            "minimo": 1396.88,
            "observacao": "10% sobre o valor do débito"
        },
        {
            "item": "9b",
            "servico": "Despejo por falta de pagamento - com purgação de mora (réu)",
            "percentual": 5.0,
            "minimo": 1396.88,
            "observacao": "5% sobre o valor do débito"
        },
        {
            "item": "9e",
            "servico": "Despejo + cobrança de aluguéis",
            "percentual": 15.0,
            "minimo": 1995.55,
            "observacao": "15% sobre o valor da causa"
        },
        {
            "item": "10",
            "servico": "Revisão e arbitramento de aluguel",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "20% sobre a vantagem/diferença anual"
        },
        {
            "item": "11",
            "servico": "Renovatória de contrato de locação",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "Varia conforme resultado (ver tabela completa)"
        },
        {
            "item": "12a",
            "servico": "Possessórias - Manutenção e reintegração de posse",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "20% sobre o valor da coisa litigiosa"
        },
        {
            "item": "12b",
            "servico": "Possessórias - Interdito proibitório",
            "percentual": 10.0,
            "minimo": 3991.07,
            "observacao": "10% sobre o valor da coisa litigiosa"
        },
        {
            "item": "15",
            "servico": "Usucapião",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "20% do valor do bem"
        },
        {
            "item": "18a",
            "servico": "Desapropriação direta",
            "percentual": 10.0,
            "minimo": 4843.54,
            "observacao": "10% sobre a diferença entre a oferta e a indenização final"
        },
        {
            "item": "20",
            "servico": "Ação monitória",
            "percentual": 20.0,
            "minimo": 1937.42,
            "observacao": "Aplica-se item 1 da Parte Geral"
        },
        {
            "item": "25",
            "servico": "Mandado de segurança",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "10% a 20% sobre o valor econômico da questão"
        },
        {
            "item": "34",
            "servico": "Juizados Especiais Cíveis e Previdenciários",
            "percentual": 20.0,
            "minimo": 1197.33,
            "observacao": "Aplica-se item 1 da Parte Geral"
        },
    ],
    "Juízo de Família e Sucessões": [
        {
            "item": "35",
            "servico": "Inventários e arrolamentos (todos os herdeiros + inventariante)",
            "percentual": 6.0,
            "minimo": 3991.07,
            "observacao": "6% sobre o valor real do monte-mor"
        },
        {
            "item": "35b",
            "servico": "Inventários - apenas meeiro, herdeiro ou legatário",
            "percentual": 6.0,
            "minimo": 1995.55,
            "observacao": "6% sobre o valor da meação/quinhão/legado"
        },
        {
            "item": "36",
            "servico": "Habilitação de crédito em inventário/arrolamento",
            "percentual": 20.0,
            "minimo": 1995.55,
            "observacao": "20% sobre o valor do crédito"
        },
        {
            "item": "39c",
            "servico": "Separação consensual (sem bens a partilhar)",
            "percentual": None,
            "minimo": 1995.55,
            "observacao": ""
        },
        {
            "item": "40",
            "servico": "Separação judicial (com bens)",
            "percentual": 6.0,
            "minimo": 3991.07,
            "observacao": "Mesmo percentual de inventários"
        },
        {
            "item": "42",
            "servico": "Divórcio (fundado em separação de fato) com bens",
            "percentual": 6.0,
            "minimo": 3991.07,
            "observacao": "Percentual de inventários"
        },
        {
            "item": "44",
            "servico": "Investigação de paternidade",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "Aplica-se item 1 da Parte Geral"
        },
        {
            "item": "45",
            "servico": "Ação de alimentos",
            "percentual": 20.0,
            "minimo": 3991.07,
            "observacao": "Aplica-se item 1 da Parte Geral (valores aproximados da tabela)"
        },
    ],
    "Atividades Avulsas / Extrajudiciais (referência)": [
        {
            "item": "C1",
            "servico": "Consulta verbal (horário de expediente)",
            "percentual": None,
            "minimo": 350.00,
            "observacao": "Valor de referência comum em tabelas da época (ajustado)"
        },
        {
            "item": "C2",
            "servico": "Consulta com exame de documentos",
            "percentual": None,
            "minimo": 750.00,
            "observacao": "Valor de referência"
        },
        {
            "item": "C3",
            "servico": "Hora intelectual / técnica",
            "percentual": None,
            "minimo": 564.00,
            "observacao": "Valor de referência de tabelas contemporâneas"
        },
        {
            "item": "C4",
            "servico": "Parecer simples",
            "percentual": None,
            "minimo": 1113.00,
            "observacao": "Referência OAB-GO 2016 (similar)"
        },
        {
            "item": "C5",
            "servico": "Parecer complexo",
            "percentual": 10.0,
            "minimo": 3339.00,
            "observacao": "Referência"
        },
    ],
}

# Lista plana para selectbox
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
