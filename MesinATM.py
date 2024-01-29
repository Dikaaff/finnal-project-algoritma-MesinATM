import getpass
import json

class ATM:
    def __init__(self):
        self.accounts_file = 'accounts.json'
        self.load_accounts()
        self.current_account = None

    def load_accounts(self):
        try:
            with open(self.accounts_file, 'r') as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            self.accounts = {}
            self.save_accounts()

    def save_accounts(self):
        with open(self.accounts_file, 'w') as file:
            json.dump(self.accounts, file, indent=4)

    def display_menu(self):
        print("=== Aplikasi Mesin ATM ===")
        print("1. Masukkan PIN")
        print("2. Buat Rekening Baru")
        print("3. Keluar")

    def main_menu(self):
        while True:
            self.display_menu()
            choice = input("Pilih menu (1/2/3): ")

            if choice == '1':
                self.input_pin()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                print("Terima kasih! Sampai jumpa.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def input_pin(self):
        account_number = input("Masukkan nomor rekening: ")

        if account_number in self.accounts:
            pin = getpass.getpass("Masukkan PIN: ")
            masked_pin = '*' * len(pin)  # Membuat string bintang sepanjang PIN
            print(f"PIN: {masked_pin}")
            
            if pin == self.accounts[account_number]['pin']:
                self.current_account = account_number
                self.show_account_menu()
            else:
                print("PIN salah. Silakan coba lagi.")
        else:
            print("Nomor rekening tidak valid. Silakan coba lagi.")

    def create_account(self):
        name = input("Masukkan nama pengguna: ")
        pin = getpass.getpass("Buat PIN baru: ")

        # Membuat nomor rekening baru secara sederhana (harap diperhatikan bahwa ini hanya contoh sederhana)
        import random
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(10))

        self.accounts[account_number] = {'pin': pin, 'name': name, 'balance': 0.0}
        self.save_accounts()
        print(f"Rekening berhasil dibuat. Nomor rekening Anda adalah: {account_number}")

    def show_account_menu(self):
        while True:
            print(f"Selamat datang, {self.accounts[self.current_account]['name']}!")
            print("=== Menu Rekening ===")
            print("1. Transfer")
            print("2. Setor Uang")
            print("3. Tarik Uang")
            print("4. Periksa Saldo")
            print("5. Keluar")

            choice = input("Pilih menu (1/2/3/4/5): ")

            if choice == '1':
                self.transfer_money()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Terima kasih! Sampai jumpa.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def transfer_money(self):
        target_account = input("Masukkan nomor rekening tujuan: ")
        amount = float(input("Masukkan jumlah transfer: "))

        if target_account in self.accounts:
            if self.accounts[self.current_account]['balance'] >= amount:
                self.accounts[self.current_account]['balance'] -= amount
                self.accounts[target_account]['balance'] += amount
                self.save_accounts()
                print("Transfer berhasil!")
            else:
                print("Saldo tidak mencukupi untuk transfer.")
        else:
            print("Nomor rekening tujuan tidak valid.")

    def deposit_money(self):
        amount = float(input("Masukkan jumlah yang akan disetor: "))
        self.accounts[self.current_account]['balance'] += amount
        self.save_accounts()
        print("Setor uang berhasil!")

    def withdraw_money(self):
        amount = float(input("Masukkan jumlah yang akan ditarik: "))
        if self.accounts[self.current_account]['balance'] >= amount:
            self.accounts[self.current_account]['balance'] -= amount
            self.save_accounts()
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi untuk penarikan.")

    def check_balance(self):
        print(f"Saldo Anda saat ini adalah: {self.accounts[self.current_account]['balance']}")


# Main program
atm = ATM()
atm.main_menu()