
def T_RHSTU_PACIENTE(id_paciente,nm_paciente,nr_cpf,nm_rg,dt_nascimento,fl_sexo_biologico,
                     ds_escolaridade,ds_estado_civil,nm_grupo_sanguineo,nr_altura,nr_peso,
                     dt_cadastro,nm_usuario):
    paciente = {}
    paciente['ID_PACIENTE'] = id_paciente 
    paciente['NM_PACIENTE'] = nm_paciente
    paciente['NR_CPF'] = nr_cpf
    paciente['NM_RG'] = nm_rg
    paciente['DT_NASCIMENTO'] = dt_nascimento
    paciente['FL_SEXO_BIOLOGICO'] = fl_sexo_biologico
    paciente['DS_ESCOLARIDADE'] = ds_escolaridade
    paciente['DS_ESTADO_CIVIL'] = ds_estado_civil
    paciente['NM_GRUPO_SANGUINEO'] = nm_grupo_sanguineo
    paciente['NR_ALTURA'] = nr_altura
    paciente['NR_PESO'] = nr_peso
    paciente['DT_CADASTRO'] = dt_cadastro
    paciente['NM_USUARIO'] = nm_usuario
    return paciente  
    
