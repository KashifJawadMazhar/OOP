class FileHandler:
    def __init__(self, filepath):
        # File path where data will be saved or read from
        self.filepath = filepath

    def read(self):
        # Reads all rows from the CSV file
        rows = []
        try:
            file = open(self.filepath, "r", encoding="UTF-8")
            for line in file:
                rows.append(line.strip())  # remove newline
            file.close()
        except:
            print("Error reading file.")
        return rows

    def write(self, rows):
        # Writes a list of rows into the CSV file
        try:
            file = open(self.filepath, "w", encoding="UTF-8")
            for row in rows:
                file.write(row + "\n")
            file.close()
        except:
            print("Error writing file.")

    def encrypt(self):
        # Simple encryption: shift each character by +3 (Caesar cipher)
        rows = self.read()
        encrypted = []
        for row in rows:
            encrypted_row = ""
            for c in row:
                encrypted_row += chr(ord(c) + 3)
            encrypted.append(encrypted_row)
        self.write(encrypted)

    def decrypt(self):
        # Decryption: shift each character by -3
        rows = self.read()
        decrypted = []
        for row in rows:
            decrypted_row = ""
            for c in row:
                decrypted_row += chr(ord(c) - 3)
            decrypted.append(decrypted_row)
        self.write(decrypted)