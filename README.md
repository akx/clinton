# Clinton: Smart Invoice Renamer 📄✨

Clinton automatically renames PDF invoices and bills according to their contents, such as dates, sums, and other relevant information.

I got frustrated with certain SaaS vendors naming their invoices with e.g. just an opaque number,
making it impossible to easily identify them for correlating with expense management systems.

This is obviously rough around the edges.

## Features

- Extract dates, sums, and other key information from PDF files using `pdfminer` and custom rules.
- Copy-rename files based on extracted information

## Why "Clinton"?

Bill. Bill Clinton.

## Getting Started

To start using Clinton:

1. Clone this repository.
2. Install the required dependencies; `pip install -e .` should do. (Remember to use a virtualenv!)
3. Unless you happen to use the exact same cloud services I do, you may need to augment the files in `clinton/maps`.
   Contributions are welcome!
4. Run `python -m clinton *.pdf` to see what it'd extract from the files; run with the `-d DIR` parameter to have it copy-rename them to `DIR`.

## License

Clinton is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code in accordance with its terms.
