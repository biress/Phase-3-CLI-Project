from app.models import Customer, Reservation, Table
from app.database import SessionLocal
from datetime import datetime

def main_menu():
    session = SessionLocal()
    while True:
        print("\n1. Register Customer\n2. Make Reservation\n3. View Reservations\n4. Exit")
        choice = input("> ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            session.add(Customer(name=name, phone_number=phone))
            session.commit()
            print("Customer added.")

        elif choice == "2":
            customer_id = int(input("Customer ID: "))
            table_id = int(input("Table ID: "))
            date_str = input("Reservation Time (YYYY-MM-DD HH:MM): ")
            guest_count = int(input("Guests: "))
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            reservation = Reservation(
                customer_id=customer_id,
                table_id=table_id,
                reservation_time=date_obj,
                guest_count=guest_count
            )
            session.add(reservation)
            session.commit()
            print("Reservation added.")

        elif choice == "3":
            reservations = session.query(Reservation).all()
            for r in reservations:
                print(f"ID {r.id} | Customer {r.customer.name} | Table {r.table.table_number} | Time {r.reservation_time}")

        elif choice == "4":
            break
