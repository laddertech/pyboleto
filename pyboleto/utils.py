def doc_label(cpf_or_cnpj):
    # Apenas números, sem formatação, para a comparação
    doc_num = ''.join([n for n in cpf_or_cnpj if n.isnumeric()])
    return 'CNPJ' if len(doc_num) >= 14 else 'CPF'
