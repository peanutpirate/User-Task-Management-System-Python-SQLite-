from database import *

create_tables()

while True:

    print("\n1 - Kullanıcı oluştur")
    print("2 - Görev ekle")
    print("3 - Görevleri listele")
    print("4 - Çıkış")

    secim = input("Seçim: ")

    if secim == "1":

        username = input("Kullanıcı adı: ")
        add_user(username)

        print("Kullanıcı oluşturuldu.")

    elif secim == "2":

        user_id = input("Kullanıcı ID: ")
        task = input("Görev: ")

        add_task(user_id,task)

        print("Görev eklendi.")

    elif secim == "3":

        user_id = input("Kullanıcı ID: ")

        tasks = get_tasks(user_id)

        for i,t in enumerate(tasks,1):
            print(i,".",t[0])

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")