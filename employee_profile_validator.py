# Gera e valida um perfil profissional simples.

employee_name = "  aNA sILVA  "

employee_role = "    data ANALYST"

department = " product engineering  "

employee_age = 28

clean_name = employee_name.strip()

formatted_name = clean_name.title()

clean_employee_role = employee_role.strip().title()
clean_department = department.strip().title()

profile_is_valid = True
if clean_name == "":
    profile_is_valid = False
    print("O nome do colaborador está vazio.")  
if clean_employee_role == "":
    profile_is_valid = False
    print("O cargo do colaborador está vazio.")
if clean_department == "":
    profile_is_valid = False
    print("O departamento está vazio.")
if employee_age <= 0:
    profile_is_valid = False
    print("A idade tem de ser positiva.")

bio = "  Analista de dados que transforma informação em decisões úteis para a equipa.  "
clean_bio = bio.strip()

employee_info = (f'---PERFIL PROFISSIONAL---\n'
                 f'Nome: {formatted_name}\n'
                 f'Cargo: {clean_employee_role}\n'
                 f'Departamento: {clean_department}\n'
                 f'Idade: {employee_age}\n'
                 f'Biografia: {clean_bio}')
                 
if len(clean_bio) < 20:
    profile_is_valid = False
    print("A bio é demasiado curta.")
if len(clean_bio) > 160:
    profile_is_valid = False
    print("A bio é demasiado grande.")  
if profile_is_valid:
    print(employee_info)








