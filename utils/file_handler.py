def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues
    Supports multiple encoding formats for robust file reading
    Returns: list of raw lines (strings)
    """

    encodings = ["utf-8", "latin-1", "cp1252"]

    for enc in encodings:
        try:
            with open(filename, "r", encoding=enc) as file:
                lines = file.readlines()

            raw_lines = []
            for line in lines[1:]:   # skip header
                if line.strip():
                    raw_lines.append(line.strip())

            print(f"✔ File read successfully using {enc} encoding")
            return raw_lines

        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    print("Error: Unable to read file due to encoding issues.")
    return []