import tkinter as tk
from tkinter import ttk

class SalesDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Dashboard")
        self.root.geometry("900x550")  # Initial size
        self.root.configure(bg="#F5F5DC")  # Background color

        # Configure grid for responsiveness
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=3)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=5)
        self.root.grid_columnconfigure(0, weight=1)

        # Main Frame (Centering All Elements)
        self.main_frame = tk.Frame(self.root, bg="#F5F5DC")
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Header Frame
        self.header_frame = tk.Frame(self.main_frame, bg="#002147")
        self.header_frame.pack(fill="x", pady=10)
        self.header_label = tk.Label(self.header_frame, text="Manage Sales Details", fg="white", bg="#002147", font=("Arial", 14, "bold"))
        self.header_label.pack(pady=10)

        # Input Fields Frame (Centered & Responsive)
        self.input_frame = tk.Frame(self.main_frame, bg="#F5F5DC")
        self.input_frame.pack(pady=10)

        for i in range(4):
            self.input_frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.input_frame.grid_columnconfigure(j, weight=1)

        tk.Label(self.input_frame, text="Invoice No.", bg="#F5F5DC", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.invoice_entry = tk.Entry(self.input_frame)
        self.invoice_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.input_frame, text="Customer Name", bg="#F5F5DC", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.customer_entry = tk.Entry(self.input_frame)
        self.customer_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.input_frame, text="Contact", bg="#F5F5DC", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.contact_entry = tk.Entry(self.input_frame)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.input_frame, text="Description", bg="#F5F5DC", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.description_entry = tk.Text(self.input_frame, height=4, width=30)
        self.description_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Button Frame (Centered & Responsive)
        self.button_frame = tk.Frame(self.main_frame, bg="#F5F5DC")
        self.button_frame.pack(pady=10)

        for btn_text, btn_color in zip(["Save", "Update", "Delete", "Clear"], ["#007BFF", "#28A745", "#DC3545", "#6C757D"]):
            btn = tk.Button(self.button_frame, text=btn_text, bg=btn_color, fg="white")
            btn.pack(side="left", padx=5)

        # Table Frame (Expands with Window)
        self.table_frame = tk.Frame(self.root, bg="#F5F5DC")
        self.table_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=10)
        
        self.tree = ttk.Treeview(self.table_frame, columns=("ID", "Invoice No.", "Name", "Contact"), show="headings")
        self.tree.heading("ID", text="Sale ID")
        self.tree.heading("Invoice No.", text="Invoice No.")
        self.tree.heading("Name", text="Customer Name")
        self.tree.heading("Contact", text="Contact")
        
        self.tree.column("ID", width=50)
        self.tree.column("Invoice No.", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Contact", width=100)
        
        self.tree.pack(fill="both", expand=True)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SalesDashboard(root)
    root.mainloop()
