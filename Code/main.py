import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import warnings
warnings.filterwarnings("ignore") 
from data_cleaner import DataCleaner

class DatasetCleaningToolApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Main window
        self.title("Dataset Cleaning Tool")
        self.geometry("1200x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Application icon
        self.set_app_icon("assets")  # Keeping this as you have given

        self.cleaner = DataCleaner()

        # Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Creating frames
        self.create_frames()

    def set_app_icon(self, icon_path):
        try:
            self.iconbitmap(icon_path)  
        except Exception as e:
            print("Error loading icon:", e)

    def create_frames(self):
        # Left Frame for logo 
        self.left_frame = ctk.CTkFrame(self, width=200)
        self.left_frame.grid(row=0, column=0, sticky="ns")
        self.left_frame.grid_propagate(False)
        self.create_left_frame_content()

        # Right Frame for processing
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Input Frame
        self.input_frame = ctk.CTkFrame(self.right_frame)
        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.create_input_frame_content()

        # Output Frame
        self.output_frame = ctk.CTkFrame(self.right_frame)
        self.output_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.create_output_frame_content()

    def create_left_frame_content(self):
        # App logo 
        try:
            logo_image = Image.open("assets/logo.png")
            logo_image = logo_image.resize((180, 180), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = ctk.CTkLabel(self.left_frame, image=self.logo_photo, text="")
            logo_label.pack(pady=20)
        except Exception as e:
            print("Error loading logo:", e)
            logo_label = ctk.CTkLabel(self.left_frame, text="App logo", font=ctk.CTkFont(size=20, weight="bold"))
            logo_label.pack(pady=20)
        
        # Description
        description1 = ctk.CTkLabel(self.left_frame, text="Dataset", font=("Arial", 32, "bold"),  
            text_color="#FFD700", justify="left")
        description1.pack(pady=10)

        description2 = ctk.CTkLabel(self.left_frame, text="Cleaning", font=("Arial", 32, "bold"),  
            text_color="#FFD700", justify="left")
        description2.pack(pady=10)

        description3 = ctk.CTkLabel(self.left_frame, text="Tool", font=("Arial", 32, "bold"),  
            text_color="#FFD700", justify="left")
        description3.pack(pady=10)

        # GitHub Contact
        try:
            github_image = Image.open("assets/github_icon.png")
            github_image = github_image.resize((48, 48), Image.LANCZOS)
            self.github_photo = ImageTk.PhotoImage(github_image)
            
            github_button = ctk.CTkButton(
                self.left_frame,
                image=self.github_photo,
                text="BIKASH1002",
                command=lambda: self.open_link("https://github.com/BIKASH1002"),
                fg_color="transparent",
                hover_color="gray25",
                corner_radius=10
            )
            
            github_button.pack(side='bottom', pady=10)
        except Exception as e:
            print("Error loading GitHub icon:", e)
            contact = ctk.CTkLabel(self.left_frame, text="GitHub:\nBIKASH1002", justify="left")
            
            contact.pack(side='bottom', pady=10)

    def open_link(self, url):
        import webbrowser
        webbrowser.open_new_tab(url)

    def create_input_frame_content(self):
        # Title
        title = ctk.CTkLabel(self.input_frame, text="Dataset Input Analysis", font=ctk.CTkFont(size=16, weight="bold"))
        title.pack(pady=5)

        # Load Dataset Button
        load_button = ctk.CTkButton(
            self.input_frame,
            text="Load Dataset",
            command=self.load_dataset,
            corner_radius=10
        )
        load_button.pack(pady=5)

        # Frame for Cards
        self.cards_frame = ctk.CTkFrame(self.input_frame)
        self.cards_frame.pack(fill="both", expand=False, padx=10, pady=10)

    def create_output_frame_content(self):
        # Title
        title = ctk.CTkLabel(self.output_frame, text="Cleaned Dataset Analysis", font=ctk.CTkFont(size=16, weight="bold"))
        title.pack(pady=5)

        # Buttons and Dropdowns
        options_frame = ctk.CTkFrame(self.output_frame)
        options_frame.pack(pady=5)

        # Missing Values Handling
        self.missing_action = ctk.StringVar(value="impute")
        missing_label = ctk.CTkLabel(options_frame, text="Handle Missing Values:")
        missing_label.grid(row=0, column=0, padx=5, pady=5)
        missing_option_menu = ctk.CTkOptionMenu(
            options_frame,
            variable=self.missing_action,
            values=["impute", "remove"]
        )
        missing_option_menu.grid(row=0, column=1, padx=5, pady=5)

        self.impute_method = ctk.StringVar(value="mean")
        impute_label = ctk.CTkLabel(options_frame, text="Imputation Method:")
        impute_label.grid(row=0, column=2, padx=5, pady=5)
        impute_option_menu = ctk.CTkOptionMenu(
            options_frame,
            variable=self.impute_method,
            values=["mean", "median"]
        )
        impute_option_menu.grid(row=0, column=3, padx=5, pady=5)

        # Outlier Handling
        self.outlier_method = ctk.StringVar(value="IQR")
        outlier_label = ctk.CTkLabel(options_frame, text="Outlier Detection Method:")
        outlier_label.grid(row=1, column=0, padx=5, pady=5)
        outlier_option_menu = ctk.CTkOptionMenu(
            options_frame,
            variable=self.outlier_method,
            values=["IQR", "z-score"]
        )
        outlier_option_menu.grid(row=1, column=1, padx=5, pady=5)

        # Process Button
        process_button = ctk.CTkButton(
            options_frame,
            text="Process Data",
            command=self.process_data,
            corner_radius=10
        )
        process_button.grid(row=1, column=2, padx=5, pady=5)

        # Save Button
        save_button = ctk.CTkButton(
            options_frame,
            text="Save Cleaned Data",
            command=self.save_cleaned_data,
            corner_radius=10
        )
        save_button.grid(row=1, column=3, padx=5, pady=5)

        # Canvas for Matplotlib Figure
        self.output_canvas = tk.Canvas(self.output_frame, bg="#212020")
        self.output_canvas.pack(fill="both", expand=True, padx=10, pady=10)

    def load_dataset(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xls *.xlsx")]
        )
        if file_path:
            try:
                self.cleaner.load_dataset(file_path)
                counts = self.cleaner.get_initial_analysis()
                self.display_initial_analysis(counts)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def display_initial_analysis(self, counts):
        # Clear previous content
        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        # Cards for each count
        num_cards = len(counts)
        columns = num_cards  # Display cards in a single row
        self.cards_frame.grid_columnconfigure(tuple(range(columns)), weight=1)

        for idx, (key, value) in enumerate(counts.items()):
            card = ctk.CTkFrame(self.cards_frame, corner_radius=15, fg_color="gray25")
            card.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")

            self.cards_frame.grid_columnconfigure(idx, weight=1)

            label_key = ctk.CTkLabel(card, text=key, font=ctk.CTkFont(size=12, weight="bold"))
            label_key.pack(pady=(10, 5))

            label_value = ctk.CTkLabel(card, text=str(value), font=ctk.CTkFont(size=18, weight="bold"))
            label_value.pack(pady=(0, 10))

    def process_data(self):
        try:
            # Handle Missing Values
            action = self.missing_action.get()
            method = self.impute_method.get() if action == 'impute' else None
            self.cleaner.handle_missing_values(action, method)

            # Handle Outliers
            outlier_method = self.outlier_method.get()
            self.cleaner.handle_outliers(outlier_method)

            # Remove Duplicates
            self.cleaner.remove_duplicates()

            # Display the cleaned data
            self.display_cleaned_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_cleaned_data(self):
        # Visualizing the cleaned data
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import seaborn as sns

        self.output_canvas.delete("all")

        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Numerical Data excluding binary columns
        self.cleaner.identify_binary_columns()
        numerical_cols = self.cleaner.df.select_dtypes(include=[float, int]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in self.cleaner.binary_cols]

        if numerical_cols:
            self.cleaner.df[numerical_cols].hist(bins=30, ax=axes[0])
            axes[0].set_title('Numerical Data Distribution')
        else:
            axes[0].set_visible(False)

        # Categorical Data
        categorical_cols = self.cleaner.df.select_dtypes(include=['object', 'category']).columns.tolist()
        categorical_cols += self.cleaner.binary_cols  # Treat binary columns as categorical for plotting

        if categorical_cols:
            # For simplicity, plot the first categorical column
            sns.countplot(
                data=self.cleaner.df,
                x=categorical_cols[0],
                ax=axes[1]
            )
            axes[1].set_title(f'Distribution of {categorical_cols[0]}')
            plt.setp(axes[1].get_xticklabels(), rotation=45)
        else:
            axes[1].set_visible(False)

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.output_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)

    def save_cleaned_data(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xls *.xlsx")]
        )
        if file_path:
            try:
                self.cleaner.save_cleaned_data(file_path)
                messagebox.showinfo("Success", f"Cleaned data saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = DatasetCleaningToolApp()
    app.mainloop()
