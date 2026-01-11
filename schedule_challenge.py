def add_contact(schedule, contact_name, contact_phone, contact_email):
    contact = { "name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": False }
    schedule.append(contact)
    print(f"Contato {contact_name} foi adicionado com sucesso!")
    return

def show_schedule(schedule):
    for idx, contact in enumerate(schedule, start=1):
        favorite = "✓" if contact["favorite"] else " "

        contact_name = contact["name"]
        contact_phone = contact["phone"]
        contact_email = contact["email"]

        print(f"{idx}. Favorito [{favorite}] | {contact_name} | {contact_phone} | {contact_email}")
    return

def update_field(label, current_value):
    new_value = input(f"{label} atual [{current_value}]: ").strip()
    return new_value if new_value != "" else current_value


def edit_contat(schedule):
    show_schedule(schedule)

    idx_contact = int(input("Digite o numero do contato que deseja atualizar!: ")) -1

    contact = schedule[idx_contact]
    contact_name = update_field("nome", contact["name"])
    contact_phone = update_field("telefone", contact["phone"])
    contact_email = update_field("e-mail", contact["email"])
    contact_favorite = contact["favorite"]

    schedule[idx_contact] = { "name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": contact_favorite }

    print(f"Contato {contact_name} atualizado com sucesso!")

    show_schedule(schedule)
    
    return

def favorite_contact(schedule):
    show_schedule(schedule)

    idx_contact = int(input("Digite o numero do contato que deseja favoritar ou remover do favoritos!: ")) -1

    contact = schedule[idx_contact]
    is_favorite = contact["favorite"]
    schedule[idx_contact]["favorite"] = False if schedule[idx_contact]["favorite"] else True
    
    text_action = "Desfavoritar" if is_favorite else "Favoritar"
    print(f"Contato {text_action} com sucesso!")
    
    show_schedule(schedule)
    
    return

def delete_contact(schedule):
    show_schedule(schedule)

    idx_contact = int(input("Digite o numero do contato que deseja favoritar ou remover do favoritos!: ")) -1

    schedule.pop(idx_contact)

    print(f"Contato {idx_contact + 1} removido com sucesso com sucesso!")

    show_schedule(schedule)

    return

schedule = []

while True:
    print("\nMenu do Gerenciado de agenda:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Deletar contato")
    print("6. Sair")

    choice = input("Digite a sua escoolha: ")

    if choice == "1":
        contact_name = input("Digite o nome do contato que deseja adicionar: ")
        contact_phone = input("Digite o telefone do contato que deseja adicionar: ")
        contact_email = input("Digite o e-mail do contato que deseja adicionar: ")
        add_contact(schedule, contact_name, contact_phone, contact_email)

    elif choice == "2":
        show_schedule(schedule)

    elif choice == "3":
        edit_contat(schedule)

    elif choice == "4":
        favorite_contact(schedule)

    elif choice == "5":
        delete_contact(schedule)

    elif choice == "6":
        print("Programa finalizado")
        break